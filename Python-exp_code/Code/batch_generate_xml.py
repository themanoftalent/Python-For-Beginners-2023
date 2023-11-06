#!/usr/bin/python
from test import write_to_file

fileHandler = open('PFID.txt')
fileList = fileHandler.readlines()

for i in range(0, len(fileList)):
	# get the food type 
	if fileList[i].find('Food:') != -1:
		index = fileList[i].find(":")
		food_line = fileList[i]
		food_type = food_line[index+3 : len(food_line)]
		print food_type	

	# write to file system of the xml with parameters
	if fileList[i].find('image:') != -1:
		index = fileList[i].find("\\")
		img_line = fileList[i]
		img_name_with_suffix = img_line[index+9 : len(img_line)]
	  	index = img_name_with_suffix.find(".jpg")	
		img_name = img_name_with_suffix[0: index]
		print img_name
		write_to_file(img_name_with_suffix, food_type, img_name+".xml")

fileHandler.close()
