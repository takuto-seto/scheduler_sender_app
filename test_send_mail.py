import pytest
from unittest.mock import Mock, patch
from send_mail import send_weather_mail, MailSendError

@pytest.fixture
def mock_weather_data():
    """正常系の天気データ"""
    return "晴れ", "25℃"

@patch('send_mail.get_tokyo_weather')
def test_send_weather_mail_success(mock_get_weather, mock_weather_data):
    mock_get_weather.return_value = mock_weather_data

    send_weather_mail()

    mock_get_weather.assert_called_once()

    
