from key.key import *

import urllib
import json
import requests


class CurrentWeather:
    def __init__(self, r, zip):
        self.zip = zip
        self.r = requests.get('http://api.wunderground.com/api/{}/geolookup/conditions/q/{}.json'.format(key, self.zip))

    def get(self):
        parsed_json = self.r.json()
        city = parsed_json['location']['city']
        state = parsed_json['location']['state']
        weather = parsed_json['current_observation']['weather']
        temperature_string = parsed_json['current_observation']['temperature_string']
        feelslike_string = parsed_json['current_observation']['feelslike_string']
        return print('Weather in ' + city + ', ' + state + ': ' + weather.lower() + '. The temperature is ' + temperature_string + ' but it feels like ' + feelslike_string + '.')


class TenDayWeather:
    def __init__(self, r, zip):
        self.zip = zip
        self.r = requests.get('http://api.wunderground.com/api/{}/geolookup/forecast10day/q/{}.json'.format(key, self.zip))

    def get(self):
        parsed_json = self.r.json()



class SunRiseWeather:
    def __init__(self, r, zip):
        self.zip = zip
        self.r = requests.get('http://api.wunderground.com/api/{}/geolookup/astronomy/q/{}.json'.format(key, self.zip))

    def get(self):
        parsed_json = self.r.json()
        sunrise = parsed_json['sun_phase']['sunrise']['hour']+':'+parsed_json['sun_phase']['sunrise']['minute']
        sunset = parsed_json['sun_phase']['sunset']['hour']+':'+parsed_json['sun_phase']['sunset']['minute']
        print("Sunrise is at: " + sunrise + ", sunset is at: " + sunset)


class AlertsWeather:
    def __init__(self, r, zip):
        self.zip = zip
        self.r = requests.get('http://api.wunderground.com/api/{}/alerts/q/{}.json'.format(key, self.zip))

    def get(self):
        parsed_json = self.r.json()
        #print(json.dumps(parsed_json, indent=4, sort_keys=True))
        alert = parsed_json['alerts']
        if alert == []:
            print("There are no alerts for your area! Probably a good thing...")
        else:
            alert_type = parsed_json['alerts']['message']
            print("Oh no! The Weather Service says "+alert_type)


def hurricanes():
    zip = input('For which ZIP code would you like to see the weather? ')
    r = requests.get('http://api.wunderground.com/api/{}/currenthurricane/view.format'.format(key, zip))
    parsed_json = r.json()
    print(json.dumps(parsed_json, indent=4, sort_keys=True))
