from config import OPENWEATHERMAP_API_KEY
import requests
from urllib.parse import urlencode
from datetime import datetime, timedelta
import json


class Weather_API_Engine():
    def __init__(self):
        params = dict(
            q='Sankt-Peterburg',
            appid=OPENWEATHERMAP_API_KEY
        )

        url = 'http://api.openweathermap.org/data/2.5/weather?%s&units=metric' % urlencode(params)
        rw = requests.get(url)

        weather = json.loads(rw.text)
        coord = weather["coord"]

        ###############
        nparams = dict(
            lat=weather["coord"]["lat"],
            lon=weather["coord"]["lon"],
            appid=OPENWEATHERMAP_API_KEY
        )
        url = "https://api.openweathermap.org/data/2.5/onecall?%s&units=metric" % urlencode(nparams)
        self.response = requests.get(url)

    def from_deg_to_direction(self, deg):
        if deg < 22.5 or deg >= 337.5:
            return "N"
        elif 22.5 <= deg < 67.5:
            return "NE"
        elif 67.5 <= deg < 112.5:
            return "E"
        elif 112.5 <= deg < 157.5:
            return "SE"
        elif 157.5 <= deg < 202.5:
            return "S"
        elif 202.5 <= deg < 247.5:
            return "SW"
        elif 247.5 <= deg < 292.5:
            return "W"
        elif 292.5 <= deg < 337.5:
            return "NW"

    def from_dt_txt_to_time_of_day(self, dt_txt):
        return dt_txt.split()[1][:-3]

    def from_ts_to_time_of_day(self, ts):
        dt = datetime.fromtimestamp(ts)
        return dt.strftime("%H:%M")#.lstrip("0")


    def what_day_is_tomorrow(self):
        if datetime.today().hour < 13:
            return 1
        else:
            return 0


    def weekday_and_date(self, n):
        now_day = datetime.today()
        delta = timedelta(n)
        new_day = now_day + delta
        day = new_day.date().strftime('%d')#.%m')
        weekday = new_day.strftime('%A')
        return f"{weekday},{day}"

    def get_weather_data(self):
        onecall = json.loads(self.response.text)
        #time_now = datetime.now().strftime('%H:%M')
        temp_now = str(int(onecall["current"]["temp"])) + "°"
        icon_now = onecall["current"]["weather"][0]["icon"]
        description_now = onecall["current"]["weather"][0]["description"].capitalize()
        wind_speed_now = str(onecall["current"]["wind_speed"]) + "m/s " + self.from_deg_to_direction(onecall["current"]["wind_deg"])
        humidity_now = str(onecall["current"]["humidity"]) + "%"
        pressure_now = str(onecall["current"]["pressure"] * 0.75) + "mmHg"

        ##############################################


        time1 = self.from_ts_to_time_of_day(onecall["hourly"][3]["dt"])
        temp1 = str(onecall["hourly"][3]["temp"]) + "°"
        icon1 = str(onecall["hourly"][3]["weather"][0]["icon"])

        time2 = self.from_ts_to_time_of_day(onecall["hourly"][6]["dt"])
        temp2 = str((onecall["hourly"][6]["temp"])) + "°"
        icon2 = onecall["hourly"][6]["weather"][0]["icon"]

        time3 = self.from_ts_to_time_of_day(onecall["hourly"][9]["dt"])
        temp3 = str(onecall["hourly"][9]["temp"]) + "°"
        icon3 = onecall["hourly"][9]["weather"][0]["icon"]

        time4 = self.from_ts_to_time_of_day(onecall["hourly"][12]["dt"])
        temp4 = str(onecall["hourly"][12]["temp"]) + "°"
        icon4 = onecall["hourly"][12]["weather"][0]["icon"]
        #######################################################################

        tomorrow1_temp = str(onecall["current"]["temp"]) + "°"
        tomorrow1_temp_icon = onecall["current"]["weather"][0]["icon"]
        tomorrow2_temp = str(onecall["daily"][self.what_day_is_tomorrow()]["temp"]["day"]) + "°"
        tomorrow2_temp_icon = onecall["daily"][self.what_day_is_tomorrow()]["weather"][0]["icon"]
        tomorrow3_temp = str(onecall["daily"][self.what_day_is_tomorrow() + 1]["temp"]["day"]) + "°"
        tomorrow3_temp_icon = onecall["daily"][self.what_day_is_tomorrow() + 1]["weather"][0]["icon"]
        tomorrow4_temp = str(onecall["daily"][self.what_day_is_tomorrow() + 2]["temp"]["day"]) + "°"
        tomorrow4_temp_icon = onecall["daily"][self.what_day_is_tomorrow() + 2]["weather"][0]["icon"]
        tomorrow5_temp = str(onecall["daily"][self.what_day_is_tomorrow() + 3]["temp"]["day"]) + "°"
        tomorrow5_temp_icon = onecall["daily"][self.what_day_is_tomorrow() + 3]["weather"][0]["icon"]
        tomorrow6_temp = str(onecall["daily"][self.what_day_is_tomorrow() + 4]["temp"]["day"]) + "°"
        tomorrow6_temp_icon = onecall["daily"][self.what_day_is_tomorrow() + 4]["weather"][0]["icon"]
        tomorrow7_temp = str(onecall["daily"][self.what_day_is_tomorrow() + 5]["temp"]["day"]) + "°"
        tomorrow7_temp_icon = onecall["daily"][self.what_day_is_tomorrow() + 5]["weather"][0]["icon"]
        tomorrow8_temp = str(onecall["daily"][self.what_day_is_tomorrow() + 6]["temp"]["day"]) + "°"
        tomorrow8_temp_icon = onecall["daily"][self.what_day_is_tomorrow() + 6]["weather"][0]["icon"]
        ######################################################################

        data = {
            'current':{
                #'time': time_now,
                'temp':temp_now,
                'icon':icon_now,
                'desc':description_now,
                'wind':wind_speed_now,
                'humidity':humidity_now,
                'pressure':pressure_now
            },
            'hourly':[
                {
                    'time':time1,
                    'temp':temp1,
                    'icon':icon1
                },
                {
                    'time': time2,
                    'temp': temp2,
                    'icon': icon2
                },
                {
                    'time': time3,
                    'temp': temp3,
                    'icon': icon3
                },
                {
                    'time': time4,
                    'temp': temp4,
                    'icon': icon4
                },
            ],
            'daily':
            [
                {
                    'day': "Today",
                    'temp': tomorrow1_temp,
                    'icon': tomorrow1_temp_icon
                },
                {
                    'day': "Tomorrow",
                    'temp': tomorrow2_temp,
                    'icon': tomorrow2_temp_icon
                },
                {
                    'day': self.weekday_and_date(2),
                    'temp': tomorrow3_temp,
                    'icon': tomorrow3_temp_icon
                },
                {
                    'day': self.weekday_and_date(3),
                    'temp': tomorrow4_temp,
                    'icon': tomorrow4_temp_icon
                },
                {
                    'day': self.weekday_and_date(4),
                    'temp': tomorrow5_temp,
                    'icon': tomorrow5_temp_icon
                },
                {
                    'day': self.weekday_and_date(5),
                    'temp': tomorrow6_temp,
                    'icon': tomorrow6_temp_icon
                },
                {
                    'day': self.weekday_and_date(6),
                    'temp': tomorrow7_temp,
                    'icon': tomorrow7_temp_icon
                },
                {
                    'day': self.weekday_and_date(7),
                    'temp': tomorrow8_temp,
                    'icon': tomorrow8_temp_icon
                }
            ]
        }


        print(onecall["daily"])
        return data

api_engine = Weather_API_Engine()

api_engine.get_weather_data()