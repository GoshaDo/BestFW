

class Weather:
    """Weather object:
    country : string
    city : string
    district: string
    max_temp : {0: int, 1: int, 2: int, 3: int, 4: int, 5: int , 6: int}
    min_temp : {0: int, 1: int, 2: int, 3: int, 4: int, 5: int , 6: int}
    humidity :  {0: int, 1: int, 2: int, 3: int, 4: int, 5: int , 6: int}"""
    def __init__(self, country, city, district, max_temp, min_temp, humidity, status):
        self.country = country
        self.district = district
        self.city = city
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.humidity = humidity
        self.status = status
