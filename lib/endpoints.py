class Endpoints():
    def __init__(self):
        self.playerid = None
        self.url = None

    def _req(self, method, params=None):
        r = {}
        r['url'] = self.url
        r['obj'] = {}
        r['obj']['id'] = 1
        r['obj']['jsonrpc'] = '2.0'
        r['obj']['method'] = method
        if params is not None:
            r['obj']['params'] = params
        return r

    def get_item(self):
        return self._req(
            'Player.GetItem',
            {
                "properties":
                    [
                        "title", "file", "showtitle", "streamdetails",
                        "season", "episode", "tvshowid"
                    ],
                    "playerid": self.playerid
            }
        )

    def increment_volume(self):
        return self._req(
            'Application.SetVolume', {'volume': 'increment'}
        )

    def decrement_volume(self):
        return self._req(
            'Application.SetVolume', {'volume': 'decrement'}
        )

    def mute(self):
        return self._req(
            'Application.SetMute', {'mute': 'toggle'}
        )

    def playpause(self):
        return self._req(
            'Player.PlayPause', {'playerid': self.playerid}
        )

    def next_audiostream(self):
        return self._req(
            'Player.SetAudioStream',
            {'playerid': self.playerid, 'stream': 'next'}
        )
