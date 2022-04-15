#!/usr/bin/python3
import argparse
import json
from inspect import getmembers, isfunction

import requests

from lib.endpoints import Endpoints


class KodiHttpRemote(Endpoints):
    def __init__(self, url):
        self.url = url + '/jsonrpc'
        self.playerid = self.get_player_id()

    def get_player_id(self):
        req = self._req(
            'Player.GetPlayers'
        )
        res = self.send_post(req)
        id = None
        try:
            id = res['id']
        except (KeyError, TypeError):
            pass
        return id

    def send_post(self, req):
        res = requests.post(
            req['url'],
            data=json.dumps(req['obj']),
            headers={'Content-Type': 'application/json'},
        )
        if req['obj']['method'] != 'Player.GetPlayers':
            self.print_response(req['obj']['method'], res)
        return res.json()

    def print_response(self, method, res):
        print(method + ' ' + str(res))
        print(json.dumps(res.json(), indent=4))


def list_actions():
    arr = []
    for el in [o[0] for o in getmembers(Endpoints) if isfunction(o[1])]:
        if el.startswith('_') is False:
            arr.append(el)
    return arr


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        'arg', nargs='?', default='get_item', choices=list_actions(),
        help='kodi action to take'
    )
    parser.add_argument(
        '-u', '--url', default='http://192.168.0.7:8080',
        help='kodi\'s url')
    args = parser.parse_args()

    khr = KodiHttpRemote(args.url)
    payload = getattr(khr, args.arg)()
    payload_arr = payload
    if isinstance(payload, list) is False:
        payload_arr = [payload]
    for pl in payload_arr:
        khr.send_post(pl)
