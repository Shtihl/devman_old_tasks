# Prettify JSON

Script for prettify raw JSON data

# Quickstart

For running this script you should have installed Python 3.x [Python.org](https://python.org/)

Example of script launch on Linux, Python 3.5:

working in terminal 

```bash

$ python pprint_json.py <path to file>
{
    "geometry": {
        "coordinates":[
            37.39703804817934,55.740999719549094
        ],
        "type":"Point"
    },
    "properties": {
        "DatasetId":1854,
        "VersionNumber":1,
        "ReleaseNumber":2,
        "RowId":"79742784-9ef3-4543-bc98-a219a8903c18",
        "Attributes": {
            "global_id":14371450,
            "Name":"Ароматный Мир",
            "IsNetObject":"да",
            "OperatingCompany":"Ароматный Мир",
            "TypeService":"реализация продовольственных товаров",
            "AdmArea":"Западный административный округ",
            "District":"район Кунцево",
            "Address":"улица Академика Павлова, дом 10",
            "PublicPhone": [
                {
                    "PublicPhone":"(495) 777-51-95"
                }
            ],
            "WorkingHours":[
                {
                    "Hours":"09:30-22:30",
                    "DayOfWeek":"понедельник"
                },
                ....
            ],
            "ClarificationOfWorkingHours":null
        }
    },
    "type":"Feature"
}

```

Data from [data.mos.ru](https://data.mos.ru/)

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
