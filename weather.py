import requests
import sys
import logging


def get_tokyo_weather():

    region_code = "130000"
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{region_code}.json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        tokyo_areas = data[0]['timeSeries'][0]['areas'][0]
        tokyo_weather = tokyo_areas['weathers'][0]

        tokyo_area_temp = data[0]['timeSeries'][2]['areas'][0]
        tokyo_temp = tokyo_area_temp['temps'][0]

        return f"{tokyo_weather}", f"{tokyo_temp}"

    else:
        logging.error("dataの取得に失敗しました")
        sys.exit()