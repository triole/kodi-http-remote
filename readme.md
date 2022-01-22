# Kodi Http Remote

<!--- mdtoc: toc begin -->

1. [Synopsis](#synopsis)
2. [Help](#help)<!--- mdtoc: toc end -->

## Synopsis

A very basic [Kodi](https://kodi.tv/) remote written in Python using http post requests. Currently doesn't support auth but shouldn't be a problem to add it if required.

The api specifications can be found on the [wiki page](https://kodi.wiki/view/JSON-RPC_API/v12).

## Help

```text mdox-exec="python3 khr.py -h"
usage: khr.py [-h] [-u URL]
              [{decrement_volume,increment_volume,mute,next_audiostream,playpause}]

positional arguments:
  {decrement_volume,increment_volume,mute,next_audiostream,playpause}
                        kodi action to take (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     kodi's url (default: http://192.168.0.13:8080)
```
