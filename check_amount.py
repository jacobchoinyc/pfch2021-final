import json

with open('movie_list_final.json', 'r') as datafile:

    data = json.load(datafile)

    num = 0

    for movie_id in data:
        num += 1
        print(num)
        # 645006