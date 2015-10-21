#from key.key import *

import urllib
import json
import requests
import os

key = os.environ['WUNDERGROUND_KEY']

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
        #print(json.dumps(parsed_json, indent=4, sort_keys=True))
        for day in parsed_json['forecast']['txt_forecast']['forecastday']:
            print("On "+day['title']+ " the forecast is "+day['fcttext'])


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


class HurricanesWeather:
    def __init__(self, r):
        self.r = requests.get('http://api.wunderground.com/api/{}/currenthurricane/view.json'.format(key))

    def get(self):
        parsed_json = self.r.json()
        print("There are currently "+str(len(parsed_json['currenthurricane']))+ " hurricanes: ")
        for hurricane in parsed_json['currenthurricane']:
        #print(json.dumps(hurricane, indent=4, sort_keys=True))
            name = hurricane['stormInfo']['stormName']
            print(name)


def get_zip():
    zip = input("What is your five digit zip code?\n")
    return zip

def main():
    option = input("""So what do you want to know?
    Enter 1 for current conditions;
    Enter 2 for ten day forecast;
    Enter 3 for sunrise and sunset times;
    Enter 4 for all current weather alerts;
    Enter 5 for all current tracked hurricanes.\n""" )
    if option == '1':
        new = CurrentWeather(key, get_zip())
        new.get()
    elif option == '2':
        new = TenDayWeather(key, get_zip())
        new.get()
    elif option == '3':
        new = SunRiseWeather(key, get_zip())
        new.get()
    elif option == '4':
        new = AlertsWeather(key, get_zip())
        new.get()
    else:
        new = HurricanesWeather(key)
        new.get()
main()
