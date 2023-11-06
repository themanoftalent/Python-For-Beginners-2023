from xml.dom import minidom, Node 
  
doc = minidom.Document() 
 
#generate the book 
book = doc.createElement('annotation') 
doc.appendChild(book) 
  
#the folder 
folder = doc.createElement('folder') 
folder.appendChild(doc.createTextNode("PFID2009")) 
book.appendChild(folder) 
 
#filename
filename = doc.createElement('filename')
filename.appendChild(doc.createTextNode("000001.jpg"))
book.appendChild(filename)

# image size
size = doc.createElement('size')
width = doc.createElement('width')
height = doc.createElement('height')
depth = doc.createElement('depth')
width.appendChild(doc.createTextNode("353"))
height.appendChild(doc.createTextNode("500"))
depth.appendChild(doc.createTextNode("3"))
size.appendChild(width)
size.appendChild(height)
size.appendChild(depth)
book.appendChild(size)
 
#The chapter 
obj = doc.createElement('object') 
title = doc.createElement('title') 
title.appendChild(doc.createTextNode("First")) 
obj.appendChild(title) 
book.appendChild(obj) 
  
para = doc.createElement('para') 
para.appendChild(doc.createTextNode("I think widgets are greate.You should buy lots of them forom")) 
company = doc.createElement('company') 
company.appendChild(doc.createTextNode("Spirngy Widgts, Inc")) 
para.appendChild(company) 
obj.appendChild(para) 
  
print doc.toprettyxml() 

# write to xml file
f = open("test1.xml", "w")
f.write(doc.toprettyxml())
f.close()

