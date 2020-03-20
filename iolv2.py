import requests
import json
import pandas
import math

class IOL:

    def __init__(self,usuario,contrasena):
        self.user=usuario
        self.__passw=contrasena
        self.__access=json.loads(requests.post(
            "https://api.invertironline.com/token",
            data={
                "username":self.user,
                "password":self.__pass,
                "grant_type":"password"}).text)
        self.__bearer=self.__access["access_token"]
        self.__refresh=self.__access["refresh_token"]
        
    def estado(self):
        
