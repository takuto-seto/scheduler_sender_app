import requests
import sys
import logging

logging.basicConfig(
    filename='log/get_tokyo_weather.log',
    format='%(asctime)s %(levelname)s %(message)s ',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:M:S'
)

def get_tokyo_weather():


    region_code = "130000"
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{region_code}.json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        tokyo_areas = data[0]['timeSeries'][0]['areas'][0]
        tokyo_weather = tokyo_areas['weathers'][0]

        tokyo_area_temp = data[0]['timeSeries'][2]['areas'][0]
        tokyo_temp = tokyo_area_temp['temps']

        return f"{tokyo_weather}", f"{tokyo_temp}"

    else:
        logging.error("dataの取得に失敗しました")
        sys.exit()