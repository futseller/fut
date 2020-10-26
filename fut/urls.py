import requests

from .exceptions import FutError

# config
rc = requests.get(
    'https://www.ea.com/fifa/ultimate-team/web-app/config/config.json').json()
auth_url = rc['authURL']
pin_url = rc['pinURL']  # TODO: urls in dict?
client_id = rc['eadpClientId']
release_type = rc['releaseType']
fun_captcha_public_key = rc['funCaptchaPublicKey']


# remote config - should be refresh every x seconds
rc = requests.get(
    'https://www.ea.com/fifa/ultimate-team/web-app/content/21D4F1AC-91A3-458D-A64E-895AA6D871D1/2021/fut/config/companion/remoteConfig.json').json()

if rc['pin'] != {"b": True, "bf": 500, "bs": 10, "e": True, "r": 3, "rf": 300}:
    print('>>> WARNING: ping variables changed: %s' % rc['pin'])

if rc['futweb_maintenance']:
    raise FutError('Futweb maintenance, please retry in few minutes.')

itemsPerPage = dict()
itemsPerPage = rc['itemsPerPage']
# nasty hack but it's better than parsing big js file
itemsPerPage['transferMarket'] += 1
itemsPerPage['club'] = 91  # ea, please don't troll us :-)

# TODO: read sku's from https://utas.mob.v1.fut.ea.com/ut/shards/v2

# TODO: card info url not found yet
# TODO: get hash from somewhere, dynamic year
card_info_url = 'https://fifa21.content.easports.com/fifa/fltOnlineAssets/21D4F1AC-91A3-458D-A64E-895AA6D871D1/2021/fut/items/web/'
# TODO: could be nice to add locals on startup
# TODO: needs to base64 decoded.
messages_url = 'https://www.ea.com/fifa/ultimate-team/web-app/loc/en_US.json'
