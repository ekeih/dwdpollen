"""
dwdpollen - API client for the "Deutscher Wetterdienst" to get the current pollen load in Germany
Copyright (C) 2019  Max Rosin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import datetime
import logging
import pytz
import requests

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

DWD_URL = 'https://opendata.dwd.de/climate_environment/health/alerts/s31fg.json'


def get_data(url):
    """
    Fetch the data via http and return it as a dictionary.
    :param url: The API URL.
    :return: The API response as a dictionary.
    """
    request = requests.get(url)
    request.raise_for_status()
    return request.json()


def build_legend(legend):
    """
    The API returns a strange legend. So the this legend

    {'id3': '1',
     'id4_desc': 'geringe bis mittlere Belastung',
     'id7_desc': 'hohe Belastung',
     'id6_desc': 'mittlere bis hohe Belastung',
     'id2': '0-1',
     'id3_desc': 'geringe Belastung',
     'id1': '0',
     'id1_desc': 'keine Belastung',
     'id7': '3',
     'id5_desc': 'mittlere Belastung',
     'id6': '2-3',
     'id5': '2',
     'id2_desc': 'keine bis geringe Belastung',
     'id4': '1-2'
    }

    gets converted to the following

    {'1': 'geringe Belastung',
     '0-1': 'keine bis geringe Belastung',
     '0': 'keine Belastung',
     '3': 'hohe Belastung',
     '2-3': 'mittlere bis hohe Belastung',
     '2': 'mittlere Belastung',
     '1-2': 'geringe bis mittlere Belastung'
    }
    """
    new_legend = {}
    for key, value in legend.items():
        if '_desc' not in key:
            new_legend[value] = legend['{}_desc'.format(key)]
    return new_legend


class DwdPollenApi:
    """API client object to get the current pollen load in Germany."""

    def __init__(self):
        """Create the client and update it once."""
        self.last_update = None
        self.next_update = None
        self.content = None
        self.data = {}
        self.legend = None
        self.update()

    def build_pollen(self, allergen):
        """
        Transform the pollen load of one allergen into something useful.

        When the API returns

        {
          'tomorrow': '3',
          'dayafter_t': '-1',
          'toda': '3'
        }

        this function will return

        {
          '2019-04-18': {
            'value': 3.0,
            'raw': '3',
            'human': 'hohe Belastung'},
          '2019-04-19': {
            'value': 3.0,
            'raw': '3',
            'human': 'hohe Belastung'
          }
        }

        :param allergen: One allergen dictionary as it is returned by the API. Check the example.
        :return: A dictionary of dictionaries with dates as a keys and allergen values as values.
        """

        def build_values(value):
            return {
                'value': calculate_value(value),
                'raw': value,
                'human': self.legend[value]
            }

        def calculate_value(value):
            items = value.split('-')
            result = 0
            for item in items:
                result += int(item)
            return result / len(items)

        new_pollen = {}
        today = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        tomorrow = today + datetime.timedelta(days=1)
        day_after_tomorrow = today + datetime.timedelta(days=2)

        if today.weekday() < 4: # Monday - Thursday
            new_pollen = {
                today.strftime('%Y-%m-%d'): build_values(allergen['today']),
                tomorrow.strftime('%Y-%m-%d'): build_values(allergen['tomorrow'])
            }
        elif today.weekday() == 4: # Friday
            new_pollen = {
                today.strftime('%Y-%m-%d'): build_values(allergen['today']),
                tomorrow.strftime('%Y-%m-%d'): build_values(allergen['tomorrow'])
            }
            if allergen['dayafter_to'] != '-1':
                new_pollen[day_after_tomorrow.strftime('%Y-%m-%d')] = \
                    build_values(allergen['dayafter_to'])
        elif today.weekday() == 5: # Saturday
            new_pollen = {
                today.strftime('%Y-%m-%d'): build_values(allergen['tomorrow']),
                tomorrow.strftime('%Y-%m-%d'): build_values(allergen['dayafter_to'])
            }
        elif today.weekday() == 6: # Sunday
            new_pollen = {
                today.strftime('%Y-%m-%d'): build_values(allergen['dayafter_to'])
            }
        return new_pollen

    def update(self):
        """Update all pollen data."""
        data = get_data(DWD_URL)
        self.last_update = datetime.datetime.strptime(data['last_update'], '%Y-%m-%d %H:%M Uhr')
        self.next_update = datetime.datetime.strptime(data['next_update'], '%Y-%m-%d %H:%M Uhr')
        self.legend = build_legend(data['legend'])

        for region in data['content']:
            new_region = {
                'region_id': region['region_id'],
                'region_name': region['region_name'],
                'partregion_id': region['partregion_id'],
                'partregion_name': region['partregion_name'],
                'last_update': self.last_update,
                'next_update': self.next_update,
                'pollen': {}
            }
            for allergen, pollen in region['Pollen'].items():
                new_pollen = self.build_pollen(pollen)
                new_region['pollen'][allergen] = new_pollen
            self.data['{}-{}'.format(region['region_id'], region['partregion_id'])] = new_region

    def get_pollen(self, region_id, partregion_id):
        """
        Get the pollen load of the requested region and partregion.
        :param region_id: API ID of the region.
        :param partregion_id: API ID of the partregion.
        :return: A dictionary with all pollen information of the requested (part)region.
        """
        return self.data['{}-{}'.format(region_id, partregion_id)]
