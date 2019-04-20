import os
from sightengine.client import SightengineClient

api_user = os.environ['SE_API_USER']
api_secret = os.environ['SE_API_SECRET']

print("API user:", api_user)
print("API secret:", api_secret)

client = SightengineClient(api_user, api_secret)
output = client.check('celebrities').set_url(image_url)

i = 1
for face in output['faces']:
    if 'celebrity' in face:
        if face['celebrity'][0]['prob'] > 0.85:
            print(Celeface['celebrity'][0]['name']) # the name of the celebrity on the image