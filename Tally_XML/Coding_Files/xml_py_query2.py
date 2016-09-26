#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
print "one"
DOMTree = xml.dom.minidom.parse("voucher_type.xml")
print "two"
TALLYMESSAGE = DOMTree.documentElement
print "three"


# Get all the movies in the collection
movies = TALLYMESSAGE.getElementsByTagName("CURRENCY")
tvseries = TALLYMESSAGE.getElementsByTagName("VOUCHERTYPE")

# Print detail of each movie.
for movie in movies:
   print "*****CURRENCY*****"
   if movie.hasAttribute("NAME"):
      print "NAME: %s" % movie.getAttribute("NAME")
   if movie.hasAttribute("RESERVEDNAME"):
      print "RESERVEDNAME: %s" % movie.getAttribute("RESERVEDNAME")

   GUID = movie.getElementsByTagName('GUID')[0]
   print "GUID: %s" % GUID.childNodes[0].data
   MAILINGNAME = movie.getElementsByTagName('MAILINGNAME')[0]
   print "MAILINGNAME: %s" % MAILINGNAME.childNodes[0].data
   ORIGINALNAME = movie.getElementsByTagName('ORIGINALNAME')[0]
   print "ORIGINALNAME: %s" % ORIGINALNAME.childNodes[0].data
   EXPANDEDSYMBOL = movie.getElementsByTagName('EXPANDEDSYMBOL')[0]
   print "EXPANDEDSYMBOL: %s" % EXPANDEDSYMBOL.childNodes[0].data
   DECIMALSYMBOL = movie.getElementsByTagName('DECIMALSYMBOL')[0]
   print "DECIMALSYMBOL: %s" % DECIMALSYMBOL.childNodes[0].data
   ISUPDATINGTARGETID = movie.getElementsByTagName('ISUPDATINGTARGETID')[0]
   print "ISUPDATINGTARGETID: %s" % ISUPDATINGTARGETID.childNodes[0].data
   ASORIGINAL = movie.getElementsByTagName('ASORIGINAL')[0]
   print "ASORIGINAL: %s" % ASORIGINAL.childNodes[0].data
   ISSUFFIX = movie.getElementsByTagName('ISSUFFIX')[0]
   print "ISSUFFIX: %s" % ISSUFFIX.childNodes[0].data
   HASSPACE = movie.getElementsByTagName('HASSPACE')[0]
   print "HASSPACE: %s" % HASSPACE.childNodes[0].data
   INMILLIONS = movie.getElementsByTagName('INMILLIONS')[0]
   print "INMILLIONS: %s" % INMILLIONS.childNodes[0].data
   ALTERID = movie.getElementsByTagName('ALTERID')[0]
   print "ALTERID: %s" % ALTERID.childNodes[0].data

# Print Vocher Types
for movie in tvseries:
   print "*****VOUCHER TYPES*****"
   if movie.hasAttribute("NAME"):
      print "NAME: %s" % movie.getAttribute("NAME")
   if movie.hasAttribute("RESERVEDNAME"):
      print "RESERVEDNAME: %s" % movie.getAttribute("RESERVEDNAME")

   GUID = movie.getElementsByTagName('GUID')[0]
   print "GUID: %s" % GUID.childNodes[0].data
   PARENT = movie.getElementsByTagName('PARENT')[0]
   print "PARENT: %s" % PARENT.childNodes[0].data
   MAILINGNAME = movie.getElementsByTagName('MAILINGNAME')[0]
   print "MAILINGNAME: %s" % MAILINGNAME.childNodes[0].data
   TAXUNITNAME = movie.getElementsByTagName('TAXUNITNAME')[0]
   print "TAXUNITNAME: %s" % TAXUNITNAME.childNodes[0].data
   EXPANDEDSYMBOL = movie.getElementsByTagName('EXPANDEDSYMBOL')[0]
   print "EXPANDEDSYMBOL: %s" % EXPANDEDSYMBOL.childNodes[0].data
   DECIMALSYMBOL = movie.getElementsByTagName('DECIMALSYMBOL')[0]
   print "DECIMALSYMBOL: %s" % DECIMALSYMBOL.childNodes[0].data
   ISUPDATINGTARGETID = movie.getElementsByTagName('ISUPDATINGTARGETID')[0]
   print "ISUPDATINGTARGETID: %s" % ISUPDATINGTARGETID.childNodes[0].data
   ASORIGINAL = movie.getElementsByTagName('ASORIGINAL')[0]
   print "ASORIGINAL: %s" % ASORIGINAL.childNodes[0].data
   ISSUFFIX = movie.getElementsByTagName('ISSUFFIX')[0]
   print "ISSUFFIX: %s" % ISSUFFIX.childNodes[0].data
   HASSPACE = movie.getElementsByTagName('HASSPACE')[0]
   print "HASSPACE: %s" % HASSPACE.childNodes[0].data
   INMILLIONS = movie.getElementsByTagName('INMILLIONS')[0]
   print "INMILLIONS: %s" % INMILLIONS.childNodes[0].data
   ALTERID = movie.getElementsByTagName('ALTERID')[0]
   print "ALTERID: %s" % ALTERID.childNodes[0].data
   GUID = movie.getElementsByTagName('GUID')[0]
   print "GUID: %s" % GUID.childNodes[0].data
   MAILINGNAME = movie.getElementsByTagName('MAILINGNAME')[0]
   print "MAILINGNAME: %s" % MAILINGNAME.childNodes[0].data
   ORIGINALNAME = movie.getElementsByTagName('ORIGINALNAME')[0]
   print "ORIGINALNAME: %s" % ORIGINALNAME.childNodes[0].data
   EXPANDEDSYMBOL = movie.getElementsByTagName('EXPANDEDSYMBOL')[0]
   print "EXPANDEDSYMBOL: %s" % EXPANDEDSYMBOL.childNodes[0].data
   DECIMALSYMBOL = movie.getElementsByTagName('DECIMALSYMBOL')[0]
   print "DECIMALSYMBOL: %s" % DECIMALSYMBOL.childNodes[0].data
   ISUPDATINGTARGETID = movie.getElementsByTagName('ISUPDATINGTARGETID')[0]
   print "ISUPDATINGTARGETID: %s" % ISUPDATINGTARGETID.childNodes[0].data
   ASORIGINAL = movie.getElementsByTagName('ASORIGINAL')[0]
   print "ASORIGINAL: %s" % ASORIGINAL.childNodes[0].data
   ISSUFFIX = movie.getElementsByTagName('ISSUFFIX')[0]
   print "ISSUFFIX: %s" % ISSUFFIX.childNodes[0].data
   HASSPACE = movie.getElementsByTagName('HASSPACE')[0]
   print "HASSPACE: %s" % HASSPACE.childNodes[0].data
   INMILLIONS = movie.getElementsByTagName('INMILLIONS')[0]
   print "INMILLIONS: %s" % INMILLIONS.childNodes[0].data
   ALTERID = movie.getElementsByTagName('ALTERID')[0]
   print "ALTERID: %s" % ALTERID.childNodes[0].data
