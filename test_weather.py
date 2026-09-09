from unittest.mock import Mock, patch
import pytest
from weather import get_tokyo_weather

@pytest.fixture
def mock_weather_responce():
    mock_responce = Mock()
    mock_responce.status_code = 200
    mock_responce.json.return_value = [
        {
            "timeSeries": [
                {
                    "areas": [
                        {"weathers": ["晴れ"]}
                        ]
                },
                {
                    "areas": [
                        {"unknown": ["unknown"]}
                        ]
                },
                {
                    "areas": [
                        {"temps": ["25"]}
                        ]
                }
                ]
        }
    ]

    return mock_responce
    


@patch('weather.requests.get')
def test_get_tokyo_weather(mock_get, mock_weather_responce):
    # mock_responce = Mock()
    # mock_responce.status_code = 200
    # mock_responce.json.return_value = [
    # {
    #     "timeSeries": [
    #     {
    #         "areas": [
    #         {
    #             "weathers": ["晴れ"]
    #         }
    #         ]
    #     },
    #     {
    #         "areas": [
    #         {
    #             "unknown": ["unknown"]         
    #         }
    #         ]
    #     },
    #     {
    #         "areas": [
    #         {
    #             "temps": ["25"]
    #         }
    #         ]
    #     }
    #     ]
    # }
    # ]

    mock_get.return_value = mock_weather_responce

    weather, temp = get_tokyo_weather()

    assert weather == "晴れ"
    assert temp == "25"