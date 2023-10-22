#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

from xml.dom import minidom, Node
  
doc = minidom.Document() 
  
doc.appendChild(doc.createComment("Simple xml document__chapter 8")) 
  
#generate the book 
book = doc.createElement('book') 
doc.appendChild(book) 
  
#the title 
title = doc.createElement('title') 
title.appendChild(doc.createTextNode("sample xml thing")) 
book.appendChild(title) 
  
#the author section 
author = doc.createElement("author") 
book.appendChild(author) 
name = doc.createElement('name') 
author.appendChild(name) 
firstname = doc.createElement('first') 
firstname.appendChild(doc.createTextNode("ma")) 
name.appendChild(firstname) 
lastname = doc.createElement('last') 
name.appendChild(lastname) 
lastname.appendChild(doc.createTextNode("xiaoju")) 
  
affiliation = doc.createElement("affiliation") 
affiliation.appendChild(doc.createTextNode("Springs Widgets, Inc.")) 
author.appendChild(affiliation) 
  
#The chapter 
chapter = doc.createElement('chapter') 
chapter.setAttribute('number', '1') 
title = doc.createElement('title') 
title.appendChild(doc.createTextNode("First")) 
chapter.appendChild(title) 
book.appendChild(chapter) 
  
para = doc.createElement('para') 
para.appendChild(doc.createTextNode("I think widgets are greate.You should buy lots of them forom")) 
company = doc.createElement('company') 
company.appendChild(doc.createTextNode("Spirngy Widgts, Inc")) 
para.appendChild(company) 
chapter.appendChild(para) 
  
print doc.toprettyxml() 

# write to xml file
f = open("test1.xml", "w")
f.write(doc.toprettyxml())
f.close()

