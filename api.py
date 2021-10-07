import pprint
import requests
from requests.structures import CaseInsensitiveDict
from CONF import COORDS_KEY, COORDS_KEY_WEATHER
# from utilis import Weather


class API(object):
    """
    management class for the API functionality of the app
    """
    def __init__(self):
        self.loc_list = []
        self.max_temp = {}
        self.min_temp = {}
        self.humidity = {}
        self.status = {}

    def get_loc(self, location):
        """
        get coords for the provided location
        :param location: a string describing the searched location
        :return:
        """
        # api url
        url = "https://www.mapquestapi.com/geocoding/v1/" \
              "address?key=%s"% COORDS_KEY

        # setting up headers
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"

        # setting up requested data for the program
        data = '{"location": "%s","options": {"thumbMaps": true}}' % location

        # request
        resp = requests.post(url, headers=headers, data=data)
        resp_dict = resp.json()
        # filtering out the important data
        # pprint.pprint(resp_dict["results"][0])
        self.loc_list = [[loc["adminArea5"], loc["adminArea1"],
                          loc["adminArea3"], loc["adminArea4"], loc["displayLatLng"]]
                         for loc in resp_dict["results"][0]["locations"]]
        # print(self.loc_list)
        return self.loc_list

    def choose_city(self, index):
        lat = self.loc_list[index][4]["lat"]
        lon = self.loc_list[index][4]["lng"]
        url = "https://api.openweathermap.org/data/2.5/" \
              "onecall?lat=%s&lon=%s&appid=" \
              "%s" % (lat, lon, COORDS_KEY_WEATHER)

        resp = requests.get(url)
        data_dict = resp.json()

        pprint.pprint(data_dict["daily"])
        self.max_temp = {day: data["temp"]["max"]-273.1 for
                         day, data in enumerate(data_dict["daily"])}
        self.min_temp = {day: data["temp"]["min"]-273.1 for
                         day, data in enumerate(data_dict["daily"])}
        self.humidity = {day: data["humidity"] for
                         day, data in enumerate(data_dict["daily"])}
        self.status = {day: data["weather"][0]["main"] for
                       day, data in enumerate(data_dict["daily"])}
        return self


if __name__ == "__main__":
    api = API()
    api.get_loc("Israel")
    api.choose_city(1)
