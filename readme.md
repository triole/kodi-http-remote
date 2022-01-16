# Kodi Http Remote

<!--- mdtoc: toc begin -->
<!--- mdtoc: toc end -->

A very basic [kodi](https://kodi.tv/) remote written in Python using http post requests. Currently doesn't support auth but shouldn't be a problem to add it if required.

```text mdox-exec="python3 khr.py -h"
usage: khr.py [-h] [-u URL]
              [{decrement_volume,increment_volume,mute,playpause}]

positional arguments:
  {decrement_volume,increment_volume,mute,playpause}
                        kodi action to take (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     kodi's url (default: http://192.168.0.13:8080)
```
