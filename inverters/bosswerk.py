#!/usr/bin/env python3

# the logic to get the data from the webinterface: https://forum.fhem.de/index.php?topic=123506.0

import requests
from .inverter import Inverter


def get_data(url, user, password) -> dict:
    data = requests.get(url, verify=False, auth=(user, password))

    for zeile in data.text.split('\n'):

        if 'var webdata_now_p' in zeile:
            watt_now = zeile
            left_texter = watt_now.find('"', 0, len(watt_now)) + 1
            right_texter = watt_now.find('"', left_texter, len(watt_now))
            watt_now = watt_now[left_texter:right_texter]

        elif 'var webdata_today_e' in zeile:
            watt_today = zeile
            left_texter = watt_today.find('"', 0, len(watt_today)) + 1
            right_texter = watt_today.find('"', left_texter, len(watt_today))
            watt_today = watt_today[left_texter:right_texter]

        elif 'var webdata_total_e' in zeile:
            watt_overall = zeile
            left_texter = watt_overall.find('"', 0, len(watt_overall)) + 1
            right_texter = watt_overall.find('"', left_texter, len(watt_overall))
            watt_overall = watt_overall[left_texter:right_texter]

    return {'watt_now': watt_now, 'watt_today': watt_today, 'watt_overall': watt_overall}


class BosswerkMi300(Inverter):
    def __init__(self, url: str, user='admin', password='admin', name='Bosswerk MI300'):
        """
        Class to Manage the Bosswerk MI300 Inverter
        https://www.bosswerk.de/wp-content/uploads/2021/07/Datenblatt_Bosswerk_MI300.pdf
        
        Params:
        url: the url to reach the webinterface of the inverter
        user: the user (htaccess) of the webinterface -> this can be changed in the inverters webinterface
        password: the password (htaccess) of the webinterface -> this can be changed in the inverters webinterface
        name: this name can be anything
        """

        super().__init__(name, typ='Bosswerk MI300', get_data_func=self._get_data)
        self.url = url
        self.user = user
        self.password = password

    def _get_data(self):
        get_data(self.url, self.user, self.password)
