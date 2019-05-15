import requests
import sys
import os
import json
import time

api_key = sys.argv[1]

if not os.path.exists("json_files"):
	os.mkdir("json_files")

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

response = requests.get('https://api.themoviedb.org/3/movie/latest?api_key=' + api_key)
json_response = response.json()
movie_count = int(json_response['id'])

movie_start = movie_count-5

for i in range(movie_start, movie_count):
	print("downloading: " + str(i))
	response = requests.get('https://api.themoviedb.org/3/movie/' + str(i) + '?api_key=' + api_key)
	#print(response.read())
	json_response = response.json()
	f = open("json_files/tmdb" + str(i) + ".json", "w")
	f.write(json.dumps(json_response, indent=4))
	f.close()
	time.sleep(15)



#print(response.read())
