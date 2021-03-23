# word ='# Ani # Gago'
# res = word.replace('#','Hi') # vandakanishi texy dnuma erkrord argumenty('Hi')
# print(res)
# x = -7
# print(abs(x)) #abc-n misht sarquma drakan(+)
# print('Hi',end=' ')
# print('Bye')
# import json 
# file_name = 'about_users.json'
# player1 = {
# 	'name': 'Aram',
# 	'age': 18,
# 	'height':180,
# 	'awards':['master',3,2,1]
# }
# player2 = {
# 	'name': 'Ani',
# 	'age': 14,
# 	'height':178,
# 	'awards':[3,2,1]
# }
# myplayers = [player1,player2]
# for data in myplayers:
# 	if data['name'] == 'Ani':
# 		data['name'] = 'Razos'
# 		print('Player name is', data['name'])

# with open(file_name, 'w') as file:
# 	json.dump(myplayers, file)
# file = open(file_name)
# json_data = json.load(file)
# for data in json_data:
# 	print('\nPlayer name is', data['name'])
# 	print('Player age is', data['age'])
# 	print('Player height is', data['height'])
# 	print('Player awards is', data['awards'])
# file_name = 'about_users.txt'

# try:
# 	with open(file_name) as file:
# 		user = json.load(file)
# 		pint('Hello', user)
# except FileNotFoundError:
# 	username = input('what is your name? ')
# 	with open(file_name, 'w') as file:
# 		user = json.dump(username, file)
# 		print('Hello', username) 
import json
import os
import requests
import time

image_urls = {}
my_list = []

with open('task_urls.json', 'rb') as data_file:
	image_urls = json.load(data_file)

for i in image_urls['items']:
	my_list.append(i['url'])

def download_image(my_list):
	for i in my_list:
		img_bytes = requests.get(i).content
		img_name = i.split('/')[3]
		img_name = f'{img_name}.jpg'
	with open( img_name, 'wb') as img_file:
		img_file.write(img_bytes)
		print(f'{img_name} was downloaded...')

path = f'{os.getcwd()}/web_images'

try:
	os.mkdir(path)
	os.chdir(path)
	download_image(my_list)

except OSError:
	print('Creation of the directory %s failed' % path)
else:
	print('Succesfully created directory %s ' % path)