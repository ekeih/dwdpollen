# DWD Pollen API Client

[![PyPI version](https://badge.fury.io/py/dwdpollen.svg)](https://badge.fury.io/py/dwdpollen)

The DWD (Deutscher Wetterdienst) publishes information about the current and future pollen load in Germany.
The data is published as an [JSON endpoint](https://opendata.dwd.de/climate_environment/health/alerts/s31fg.json) and documented in this [German PDF](https://opendata.dwd.de/climate_environment/health/alerts/Beschreibung_pollen_s31fg.pdf).

## Install
```angular2html
pip install dwdpollen
```

## `region_id` and `partregion_id`
The API uses the `region_id` and `partregion_id` to identify the different regions in Germany. The following regions are available:

| Region                         | `region_id` | Partregion                                         | `partregion_id` |
| ------------------------------ | ----------- | -------------------------------------------------- | --------------- |
| Schleswig-Holstein und Hamburg | 10          | Inseln und Marschen                                | 11              |
|                                |             | Geest, Schleswig-Holstein und Hamburg              | 12              |
| Mecklenburg-Vorpommern         | 20          |                                                    | -1              |
| Niedersachsen und Bremen       | 30          | Westl. Niedersachsen/Bremen                        | 31              |
|                                |             | Östl. Niedersachsen                                | 32              |
| Nordrhein-Westfalen            | 40          | Rhein.-Westfäl. Tiefland                           | 41              |
|                                |             | Ostwestfalen                                       | 42              |
|                                |             | Mittelgebirge NRW                                  | 43              |
| Brandenburg und Berlin         | 50          |                                                    | -1              |
| Sachsen-Anhalt                 | 60          | Tiefland Sachsen-Anhalt                            | 61              |
|                                |             | Harz                                               | 62              |
| Thüringen                      | 70          | Tiefland Thüringen                                 | 71              |
|                                |             | Mittelgebirge Thüringen                            | 72              |
| Sachsen                        | 80          | Tiefland Sachsen                                   | 81              |
|                                |             | Mittelgebirge Sachsen                              | 82              |
| Hessen                         | 90          | Nordhessen und hess. Mittelgebirge                 | 91              |
|                                |             | Rhein-Main                                         | 92              |
| Rheinland-Pfalz und Saarland   | 100         | Saarland                                           | 103             |
|                                |             | Rhein, Pfalz, Nahe und Mosel                       | 101             |
|                                |             | Mittelgebirgsbereich Rheinland-Pfalz               | 102             |
| Baden-Württemberg              | 110         | Oberrhein und unteres Neckartal                    | 111             |
|                                |             | Hohenlohe/mittlerer Neckar/Oberschwaben            | 112             |
|                                |             | Mittelgebirge Baden-Württemberg                    | 113             |
| Bayern                         | 120         | Allgäu/Oberbayern/Bay. Wald                        | 121             |
|                                |             | Donauniederungen                                   | 122             |
|                                |             | Bayern n. der Donau, o. Bayr. Wald, o. Mainfranken | 123             |
|                                |             | Mainfranken                                        | 124             |

## Usage

The API will return the data on a best effort basis. There is no guarantee which dates exist in the result. Mostly the current and the next day are available and on Friday after 11 AM the data for Sunday should be available. But there is no guarantee, so the caller has to check the result itself.
**What?** Yes... it sounds strange... but usually the DWD updates the API result everyday at 11 AM and on Friday the forecast for Sunday is included.

```
import dwdpollen
api = dwdpollen.DwdPollenApi()
api.get_pollen(50, -1)
```

```
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
