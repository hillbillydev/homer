import requests

def lambda_handler(event, context):
    url = 'https://api.geonet.org.nz/quake?MMI=3'  # TODO Make MMI an variable coming from AWS
    res = requests.get(url)

    return res.json()
