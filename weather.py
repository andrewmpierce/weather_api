from key import *

import urllib
import json
import requests


class WeatherUnderground():
    pass

def current():
    zip = input('For which ZIP code would you like to see the weather? ')
    r = requests.get('http://api.wunderground.com/api/{}/geolookup/conditions/q/{}.json'.format(key, zip))
    parsed_json = r.json()
    city = parsed_json['location']['city']
    state = parsed_json['location']['state']
    weather = parsed_json['current_observation']['weather']
    temperature_string = parsed_json['current_observation']['temperature_string']
    feelslike_string = parsed_json['current_observation']['feelslike_string']
    return print('Weather in ' + city + ', ' + state + ': ' + weather.lower() + '. The temperature is ' + temperature_string + ' but it feels like ' + feelslike_string + '.')



def ten_day():
    zip = input('For which ZIP code would you like to see the weather? ')
    r = requests.get('http://api.wunderground.com/api/{}/forecast10day/q/{}.json'.format(key, zip))
    parsed_json = r.json()
    print(json.dumps(parsed_json, indent=4, sort_keys=True))
    # city = parsed_json['location']['city']
    # state = parsed_json['location']['state']
    # weather = parsed_json['current_observation']['weather']
    # temperature_string = parsed_json['current_observation']['temperature_string']
    # feelslike_string = parsed_json['current_observation']['feelslike_string']
    # return print('Weather in ' + city + ', ' + state + ': ' + weather.lower() + '. The temperature is ' + temperature_string + ' but it feels like ' + feelslike_string + '.')
def sunrise():
    zip = input('For which ZIP code would you like to see the weather? ')
    r = requests.get('http://api.wunderground.com/api/{}/astronomy/q/{}.json'.format(key, zip))
    parsed_json = r.json()
    sunrise = parsed_json['sun_phase']['sunrise']['hour']+':'+parsed_json['sun_phase']['sunrise']['minute']
    sunset = parsed_json['sun_phase']['sunset']['hour']+':'+parsed_json['sun_phase']['sunset']['minute']
    print("Sunrise is at: " + sunrise + ", sunset is at: " + sunset)
    #print(json.dumps(parsed_json, indent=4, sort_keys=True))

def alerts():
    zip = input('For which ZIP code would you like to see the weather? ')
    r = requests.get('http://api.wunderground.com/api/{}/alerts/q/{}.json'.format(key, zip))
    parsed_json = r.json()
    alert = parsed_json['alerts']
    alert_type = parsed_json['alerts']['message']
    if alert == []:
        print("There are no alerts for your area! Probably a good thing...")
    else:
        print("Oh no! The Weather Service says "+alert_type)
    #print(json.dumps(parsed_json, indent=4, sort_keys=True))
