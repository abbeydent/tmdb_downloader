import json


f = open("json_files/tmdb602561.json", "r")
json_data = json.load(f)
print(json_data['adult'])
print(json_data['backdrop_path'])
print(json_data['belongs_to_collection'])
print(json_data['budget'])
print(json_data['genres'])
print(json_data['homepage'])
print(json_data['id'])
print(json_data['imdb_id'])
print(json_data['original_language'])
print(json_data['original_title'])
print(json_data['overview'])
print(json_data['popularity'])
print(json_data['poster_path'])
print(json_data['production_companies'])
print(json_data['production_countries'])
print(json_data['release_date'])
print(json_data['revenue'])
print(json_data['runtime'])
print(json_data['spoken_languages'])
print(json_data['status'])
print(json_data['tagline'])
print(json_data['title'])
print(json_data['video'])
print(json_data['vote_average'])
print(json_data['vote_count'])



