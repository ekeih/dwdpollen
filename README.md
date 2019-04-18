# DWD Pollen API Client

The DWD (Deutscher Wetterdienst) publishes information about the current and future pollen load in Germany.
The data is published as an [JSON endpoint](https://opendata.dwd.de/climate_environment/health/alerts/s31fg.json) and documented in this [German PDF](https://opendata.dwd.de/climate_environment/health/alerts/Beschreibung_pollen_s31fg.pdf).

## Install
```angular2html
pip install dwdpollen
```

## `region_id` and `partregion_id`
The API uses the `region_id` and `partregion_id` to identify the different regions in Germany. The following regions are available:

```
Schleswig-Holstein und Hamburg (region_id: 10): Inseln und Marschen (partregion_id: 11)
Schleswig-Holstein und Hamburg (region_id: 10): Geest, Schleswig-Holstein und Hamburg (partregion_id: 12)

Mecklenburg-Vorpommern  (region_id: 20, partregion_id: -1)

Niedersachsen und Bremen (region_id: 30): Westl. Niedersachsen/Bremen (partregion_id: 31)
Niedersachsen und Bremen (region_id: 30): Östl. Niedersachsen (partregion_id: 32)

Nordrhein-Westfalen (region_id: 40): Rhein.-Westfäl. Tiefland (partregion_id: 41)
Nordrhein-Westfalen (region_id: 40): Ostwestfalen (partregion_id: 42)
Nordrhein-Westfalen (region_id: 40): Mittelgebirge NRW (partregion_id: 43)

Brandenburg und Berlin  (region_id: 50, partregion_id: -1)

Sachsen-Anhalt (region_id: 60): Tiefland Sachsen-Anhalt (partregion_id: 61)
Sachsen-Anhalt (region_id: 60): Harz (partregion_id: 62)

Thüringen (region_id: 70): Tiefland Thüringen (partregion_id: 71)
Thüringen (region_id: 70): Mittelgebirge Thüringen (partregion_id: 72)

Sachsen (region_id: 80): Tiefland Sachsen (partregion_id: 81)
Sachsen (region_id: 80): Mittelgebirge Sachsen (partregion_id: 82)

Hessen (region_id: 90): Nordhessen und hess. Mittelgebirge (partregion_id: 91)
Hessen (region_id: 90): Rhein-Main (partregion_id: 92)

Rheinland-Pfalz und Saarland (region_id: 100): Saarland (partregion_id: 103)
Rheinland-Pfalz und Saarland (region_id: 100): Rhein, Pfalz, Nahe und Mosel (partregion_id: 101)
Rheinland-Pfalz und Saarland (region_id: 100): Mittelgebirgsbereich Rheinland-Pfalz (partregion_id: 102)

Baden-Württemberg (region_id: 110): Oberrhein und unteres Neckartal (partregion_id: 111)
Baden-Württemberg (region_id: 110): Hohenlohe/mittlerer Neckar/Oberschwaben (partregion_id: 112)
Baden-Württemberg (region_id: 110): Mittelgebirge Baden-Württemberg (partregion_id: 113)

Bayern (region_id: 120): Allgäu/Oberbayern/Bay. Wald (partregion_id: 121)
Bayern (region_id: 120): Donauniederungen (partregion_id: 122)
Bayern (region_id: 120): Bayern n. der Donau, o. Bayr. Wald, o. Mainfranken (partregion_id: 123)
Bayern (region_id: 120): Mainfranken (partregion_id: 124)

```

## Usage

The API will return the data on a best effort basis. There is no guarantee which dates exist in the result. Mostly the current and the next day are available and on Friday after 11 AM the data for Sunday should be available. But there is no guarantee, so the caller has to check the result itself.

```
import dwdpollen
api = dwdpollen.DwdPollenApi()
api.get_pollen(50, -1)

{'region_id': 50,
 'region_name': 'Brandenburg und Berlin ',
 'partregion_id': -1,
 'partregion_name': '',
 'last_update': datetime.datetime(2019, 4, 18, 11, 0),
 'next_update': datetime.datetime(2019, 4, 19, 11, 0),
 'pollen': {'Graeser': {'2019-04-19': {'value': 0.0,
    'raw': '0',
    'human': 'keine Belastung'},
   '2019-04-20': {'value': 0.0, 'raw': '0', 'human': 'keine Belastung'}},
  'Roggen': {'2019-04-19': {'value': 0.0,
    'raw': '0',
    'human': 'keine Belastung'},
   '2019-04-20': {'value': 0.0, 'raw': '0', 'human': 'keine Belastung'}},
  'Hasel': {'2019-04-19': {'value': 0.0,
    'raw': '0',
    'human': 'keine Belastung'},
   '2019-04-20': {'value': 0.0, 'raw': '0', 'human': 'keine Belastung'}},
  'Beifuss': {'2019-04-19': {'value': 0.0,
    'raw': '0',
    'human': 'keine Belastung'},
   '2019-04-20': {'value': 0.0, 'raw': '0', 'human': 'keine Belastung'}},
  'Esche': {'2019-04-19': {'value': 2.0,
    'raw': '2',
    'human': 'mittlere Belastung'},
   '2019-04-20': {'value': 2.0, 'raw': '2', 'human': 'mittlere Belastung'}},
  'Birke': {'2019-04-19': {'value': 3.0,
    'raw': '3',
    'human': 'hohe Belastung'},
   '2019-04-20': {'value': 3.0, 'raw': '3', 'human': 'hohe Belastung'}},
  'Erle': {'2019-04-19': {'value': 0.0,
    'raw': '0',
    'human': 'keine Belastung'},
   '2019-04-20': {'value': 0.0, 'raw': '0', 'human': 'keine Belastung'}},
  'Ambrosia': {'2019-04-19': {'value': 0.0,
    'raw': '0',
    'human': 'keine Belastung'},
   '2019-04-20': {'value': 0.0, 'raw': '0', 'human': 'keine Belastung'}}}}

```

## License
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
