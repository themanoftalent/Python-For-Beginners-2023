from xml.dom import minidom, Node 

def write_to_file(img_name,food_type, file_name):
  
	doc = minidom.Document() 
	 
	# generate the annotation 
	annotation = doc.createElement('annotation') 
	doc.appendChild(annotation) 
	 
	# the folder 
	folder = doc.createElement('folder') 
	folder.appendChild(doc.createTextNode("PFID2009")) 
	annotation.appendChild(folder) 
	  
	# the filename 
	filename = doc.createElement("filename") 
	filename.appendChild(doc.createTextNode(img_name))
	annotation.appendChild(filename) 

	# size
	size = doc.createElement('size')
	width = doc.createElement('width')
	height = doc.createElement('height')
	depth = doc.createElement('depth')

	width.appendChild(doc.createTextNode('1944'))
	height.appendChild(doc.createTextNode('2592'))
	depth.appendChild(doc.createTextNode('3'))

	size.appendChild(width)
	size.appendChild(height)
	size.appendChild(depth)
	annotation.appendChild(size)
	 
	# segmented
	segmented = doc.createElement('segmented')
	segmented.appendChild(doc.createTextNode("0"))
	annotation.appendChild(segmented) 

	# object 
	object = doc.createElement('object')
	name = doc.createElement('name')
	pose = doc.createElement('pose')
	truncated = doc.createElement('truncated')
	difficult = doc.createElement('difficult')
	bndbox = doc.createElement('bndbox')
	xmin = doc.createElement('xmin')
	ymin = doc.createElement('ymin')
	xmax = doc.createElement('xmax')
	ymax = doc.createElement('ymax')

	name.appendChild(doc.createTextNode(food_type))
	pose.appendChild(doc.createTextNode('Unspecified'))
	truncated.appendChild(doc.createTextNode('0'))
	difficult.appendChild(doc.createTextNode('0'))
	xmin.appendChild(doc.createTextNode('0'))
	ymin.appendChild(doc.createTextNode('0'))
	xmax.appendChild(doc.createTextNode('1944'))
	ymax.appendChild(doc.createTextNode('2592'))
	 
	bndbox.appendChild(xmin)
	bndbox.appendChild(ymin)
	bndbox.appendChild(xmax)
	bndbox.appendChild(ymax)

	object.appendChild(name)
	object.appendChild(pose)
	object.appendChild(truncated)
	object.appendChild(difficult)
	object.appendChild(bndbox)
	annotation.appendChild(object)
	 
	print doc.toprettyxml() 

	# write to xml file
	f = open(file_name, "w")
	f.write(doc.toprettyxml())
	f.close()
  
