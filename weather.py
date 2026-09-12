import requests
import sys
import logging


class WeatherAPIError(Exception):
    """APIへのアクセス失敗"""
    pass

class WeatherDataError(Exception):
    """データ構造が異常"""
    pass



def get_tokyo_weather():

    region_code = "999999"
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
        raise WeatherAPIError("APIがエラーを返しました")