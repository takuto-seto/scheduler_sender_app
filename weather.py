import requests

region_code = "130000"
url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{region_code}.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print("dataの取得に失敗しました")