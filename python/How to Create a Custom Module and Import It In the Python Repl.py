import requests
import pprint

r = requests.get('https://api.dailysmarty.com/posts')
r.json()
pprint.pprint(r.json()['posts'][0])
pprint.pprint(r.json()['posts'][0]['url_for_post'])
