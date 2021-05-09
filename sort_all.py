import json
import math

with open('movie_list.json', 'r') as datafile:

    data = json.load(datafile)

    jan = []

    for movie_num in data:
        if movie_num['genres'] != []:
            date = movie_num['release_date'].split("-", 1)
            if len(date) > 1:
                year = date[0]
                year = math.floor(int(year) / 10) * 10
                for genre in movie_num['genres']:

                    genre_exist = False
                    for new_data in jan:

                        if new_data['name'] == genre:
                            
                            year_exist = False
                            for year_data in new_data['children']:
                                if int(year_data['name']) == int(year):
                                    year_data['value'] += 1
                                    year_exist = True

                            if year_exist is False:
                                new_year = {
                                    'name': str(year),
                                    'value': 1
                                }
                                new_data['children'].append(new_year)

                            genre_exist = True

                    if genre_exist is False:
                        genres = {
                            'name': genre,
                            'children': [{
                                'name': year,
                                'value': 1
                            }]
                        }
                        jan.append(genres)



with open('all.json', 'w') as outfile:
    json.dump(jan,outfile,indent=2)