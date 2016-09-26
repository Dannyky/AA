#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("Master-sample.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print "Root element : %s" % collection.getAttribute("shelf")

# Get all the movies in the collection
movies = collection.getElementsByTagName("movie")
tvseries = collection.getElementsByTagName("tvseries")
CURRENCY = collection.getElementsByTagName("CURRENCY")


# Print detail of each movie.
for curr in CURRENCY:
   print "*****CURRENCY*****"
   if curr.hasAttribute("NAME"):
      print "Name: %s" % curr.getAttribute("NAME")

   GUID = curr.getElementsByTagName('GUID')[0]
   print "GUID: %s" % GUID.childNodes[0].data
   format = movie.getElementsByTagName('format')[0]
   print "Format: %s" % format.childNodes[0].data
   
   rating = movie.getElementsByTagName('rating')[0]
   print "Rating: %s" % rating.childNodes[0].data
   description = movie.getElementsByTagName('description')[0]
   print "Description: %s" % description.childNodes[0].data



# Print detail of each movie.
for movie in movies:
   print "*****Movie*****"
   if movie.hasAttribute("title"):
      print "Title: %s" % movie.getAttribute("title")

   type = movie.getElementsByTagName('type')[0]
   print "Type: %s" % type.childNodes[0].data
   format = movie.getElementsByTagName('format')[0]
   print "Format: %s" % format.childNodes[0].data
   
   rating = movie.getElementsByTagName('rating')[0]
   print "Rating: %s" % rating.childNodes[0].data
   description = movie.getElementsByTagName('description')[0]
   print "Description: %s" % description.childNodes[0].data


# Print detail of each movie.
for tv in tvseries:
   print "*****TV Series*****"
   if tv.hasAttribute("title"):
      print "Title: %s" % movie.getAttribute("title")

   type = tv.getElementsByTagName('type')[0]
   print "Type: %s" % type.childNodes[0].data
   
   format1 = tv.getElementsByTagName('format1')[0]
   print "Format1: %s" % format1.childNodes[0].data
   rating = tv.getElementsByTagName('rating')[0]
   print "Rating: %s" % rating.childNodes[0].data
   description = tv.getElementsByTagName('description')[0]
   print "Description: %s" % description.childNodes[0].data
