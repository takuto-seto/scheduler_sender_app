import pytest
from unittest.mock import Mock, patch
from send_mail import send_weather_mail, MailSendError

@pytest.fixture
def mock_weather_data():
    """正常系の天気データ"""
    return "晴れ", "25℃"

@patch('send_mail.get_tokyo_weather')
@patch('send_mail.smtplib.SMTP_SSL')
def test_send_weather_mail_success(mock_smtp, mock_get_weather, mock_weather_data):
    mock_get_weather.return_value = mock_weather_data

    # SMTP_SSLのモック設定
    mock_server = Mock()
    mock_smtp.return_value.__enter__.return_value = mock_server

    send_weather_mail()

    mock_get_weather.assert_called_once()
    mock_server.sendmail.assert_called_once()


@patch('send_mail.get_tokyo_weather')
def test_send_weather_mail_error(mock_get_weather):
    """WeatherAPIを発生させる """

    from weather import WeatherAPIError
    mock_get_weather.side_effect = WeatherAPIError("APIエラー")

    with pytest.raises(SystemExit):
        send_weather_mail()