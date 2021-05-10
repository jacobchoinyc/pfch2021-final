import json
import math

with open('movie_list_final.json', 'r') as datafile:

    data = json.load(datafile)

    jan = []

    for movie_num in data:

        if movie_num['release_date'].find('-10-') != -1 or movie_num['release_date'].find('-11-') != -1 or movie_num['release_date'].find('-12-') != -1:
            
            if movie_num['genres'] != []:
                date = movie_num['release_date'].split("-", 1)
                year = math.floor(int(date[0]) / 10) * 10
                year_key = str(year) + "s"

                for genre in movie_num['genres']:

                    genre_exist = False
                    for new_data in jan:

                        if new_data['name'] == genre:
                            
                            year_exist = False
                            for year_data in new_data['children']:
                                if year_data['name'] in year_key:
                                    year_data['value'] += 1
                                    year_exist = True

                            if year_exist is False:
                                new_year = {
                                    'name': year_key,
                                    'value': 1
                                }
                                new_data['children'].append(new_year)
                            genre_exist = True

                    if genre_exist is False:
                        genres = {
                            'name': genre,
                            'children': [{
                                'name': year_key,
                                'value': 1
                            }]
                        }
                        jan.append(genres)


with open('q4.json', 'w') as outfile:
    json.dump(jan,outfile,indent=2)