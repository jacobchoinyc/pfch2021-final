# found api
import requests
import json
from urllib.parse import urljoin

base_url = "https://api.themoviedb.org/3/movie/"

movie_list = []

for movie_id in range(0, 850000):
    from urllib.parse import urljoin
    new_url = urljoin(base_url, str(movie_id))
    payload = {
        'api_key': 'ba6dd31ab750db2b746258f3a48de552',
        'language': 'en-US'
    }
    r = requests.get(new_url, params=payload)
    objects = json.loads(r.text)
    if objects.get('success') is not None:
        continue

    movie = {
            'id': objects['id'],
            'release_date': objects['release_date'],
            'genres': [],
        }  
    for genres in objects['genres']:
        movie['genres'].append(genres['name'])
    
    movie_list.append(movie)
    print(objects['id'])

with open('movie_list9.json', 'w') as outfile:
    json.dump(movie_list,outfile,indent=2)