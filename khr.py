#!/usr/bin/python3
import argparse
import inspect
import json

import requests


class KodiHttpRemote():
    def __init__(self, url):
        self.url = url + '/jsonrpc'
        self.playerid = self.get_player_id()

    def send_post(self, data):
        res = requests.post(
            self.url,
            data=json.dumps(data),
            headers={'Content-Type': 'application/json'},
        )
        print(res)
        print(res.text)

    def base_req(self, method, params=None):
        r = {}
        r['id'] = 1
        r['jsonrpc'] = '2.0'
        r['method'] = method
        if params is not None:
            r['params'] = params
        return r

    def get_player_id(self):
        r = self.base_req(
            'Player.GetPlayers'
        )
        return r['id']

    def k_increment_volume(self):
        return self.base_req(
            'Application.SetVolume', {'volume': 'increment'}
        )

    def k_decrement_volume(self):
        return self.base_req(
            'Application.SetVolume', {'volume': 'decrement'}
        )

    def k_mute(self):
        return self.base_req(
            'Application.SetMute', {'mute': 'toggle'}
        )

    def k_playpause(self):
        return self.base_req(
            'Player.PlayPause', {'playerid': self.playerid}
        )

    def k_next_audiostream(self):
        return self.base_req(
            'Player.SetAudioStream',
            {'playerid': self.playerid, 'stream': 'next'}
        )


def list_actions():
    all_functions = inspect.getmembers(KodiHttpRemote, inspect.isfunction)
    arr = []
    for f in all_functions:
        if f[0].startswith('k_') is True:
            arr.append(f[0][2:100])
    return sorted(arr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        'arg', nargs='?', default=None, choices=list_actions(),
        help='kodi action to take'
    )
    parser.add_argument(
        '-u', '--url', default='http://192.168.0.13:8080',
        help='kodi\'s url')
    args = parser.parse_args()

    khr = KodiHttpRemote(args.url)

    payload = getattr(khr, 'k_' + args.arg)()
    khr.send_post(payload)
