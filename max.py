"""
Main engine of project
"""
import json
from time import sleep


from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


from mapcreator import create
import twitter


geolocator = Nominatim(user_agent="specify_your_app_name_here")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=3)


def as_user(dct):
    """

    :param dct: dict()


    :return: dict()
    Shape JSON in an appropriate way
    --------------------------------
    >>> as_user({"users": [{"name": "Kate", "age": 3}, {"name": "Joe", "age": 5}]})
    {'users': {'Kate': {'age': 3}, 'Joe': {'age': 5}}}
    >>> as_user({"users": [{"name": "Kate", "age": 3}]})
    {'users': {'Kate': {'age': 3}}}
    >>> as_user({"users": [{"name": "Kate"}]})
    {'users': {'Kate': {}}}
    """
    if "users" in dct:
        length = len(dct["users"])
        dct = [(dct["users"][elm]["screen_name"], \
               dct["users"][elm]["location"]) for elm in range(length)]
    return dct


def js_reader(fl_name, func):
    """

    :param fl_name: str()
    :param func: function()


    :return: dict()
    ---------------
    Read JSON file
    """
    with open(fl_name, mode="r", encoding="utf-8") as file:
        loaded = json.load(file, object_hook=func)
    return loaded


def main(name, i_p):
    """
    :param name: name of file
    :param i_p: unique i_p
    :return:
    --------
    Information processing module
    """
    twitter.start(name)
    data = {}
    lst = js_reader("file.json", as_user)
    while True:
        try:
            for point in lst:
                sleep(0.5)
                place = point[1].split(",")[0] if point[1] else "USA"
                location = geolocator.geocode(place)
                if not location:
                    continue
                place = (location.address, (location.latitude, location.longitude))
                if place not in data:
                    data[place] = {point[0]}
                else:
                    data[place].add(point[0])
            create(data, name=name+i_p)
            break
        except Exception:
            sleep(1)
            data.clear()
            print(1)
            continue
