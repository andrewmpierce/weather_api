import requests_mock
import requests
from weather import *
from key.key import *


@requests_mock.Mocker()
def test_currentweather(m):
    with open('json/current.json') as current_conditions:
        m.get('http://api.wunderground.com/api/{}/geolookup/conditions/q/94101.json'.format(key), text=current_conditions.read())

    current_conditions = CurrentWeather(key, '94101')
    ans = current_conditions.get()

    assert ans == ('Weather in San Francisco, CA: clear. The temperature is 61.9 F (16.6 C) but it feels like 61.9 F (16.6 C).')


@requests_mock.Mocker()
def test_tendayweather(m):
    with open('json/tenday.json') as tenday:
        m.get('http://api.wunderground.com/api/{}/forecast10day/q/94101.json'.format(key), text=tenday.read())

    ten_day = TenDayWeather(key, '94101')
    ans = ten_day.get()




@requests_mock.Mocker()
def test_sunriseweather(m):
    with open('json/sunrise.json') as sunrise:
        m.get('http://api.wunderground.com/api/{}/astronomy/q/94101.json'.format(key), text=sunrise.read())

    sunrise = SunRiseWeather(key, '94101')
    ans = sunrise.get()

    assert ans['sun_phase']['sunrise']['hour'] == "7"
    assert ans['sun_phase']['sunrise']['minute'] == "01"
    assert ans['sun_phase']['sunset']['hour'] == "16"
    assert ans['sun_phase']['sunset']['minute'] == "56"


@requests_mock.Mocker()
def test_alertsweather(m):
    with open('json/alerts.json') as heat:
        m.get('http://api.wunderground.com/api/{}/alerts/q/94101.json'.format(key), text=heat.read())

    alerts = AlertsWeather(key, '94101')
    ans = heat.get()

    assert ans =='\u000A...Heat advisory remains in effect until 7 am CDT Saturday...\u000A\u000A* temperature...heat indices of 100 to 105 are expected each \u000A afternoon...as Max temperatures climb into the mid to upper \u000A 90s...combined with dewpoints in the mid 60s to around 70. \u000A Heat indices will remain in the 75 to 80 degree range at \u000A night. \u000A\u000A* Impacts...the hot and humid weather will lead to an increased \u000A risk of heat related stress and illnesses. \u000A\u000APrecautionary/preparedness actions...\u000A\u000AA heat advisory means that a period of hot temperatures is\u000Aexpected. The combination of hot temperatures and high humidity\u000Awill combine to create a situation in which heat illnesses are\u000Apossible. Drink plenty of fluids...stay in an air-conditioned\u000Aroom...stay out of the sun...and check up on relatives...pets...\u000Aneighbors...and livestock.\u000A\u000ATake extra precautions if you work or spend time outside. Know\u000Athe signs and symptoms of heat exhaustion and heat stroke. Anyone\u000Aovercome by heat should be moved to a cool and shaded location.\u000AHeat stroke is an emergency...call 9 1 1.'



@requests_mock.Mocker()
def test_hurricanesweather(m):
    with open('json/hurricanes.json') as hurricane:
        m.get('http://api.wunderground.com/api/{}/currenthurricane/view.json'.format(key), text=hurricane.read())

    hurricanes = HurricanesWeather(key)
    ans = hurricanes.get()

    assert ans == "There is currently 1 hurricane: Daniel"
