#!/usr/bin/python

import xml.sax

class TallyHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.GUID = ""
      self.MAILINGNAME = ""
      self.PARENT = ""
      self.TAXUNITNAME = ""
      self.ORIGINALNAME = ""
      self.EXPANDEDSYMBOL = ""
      self.DECIMALSYMBOL = ""
      self.ISUPDATINGTARGETID = ""
      self.ASORIGINAL = ""
      self.ISSUFFIX = ""
      self.HASSPACE = ""
      self.INMILLIONS = ""
      self.ALTERID = ""
      #self. = ""
      
      self.NUMBERINGMETHOD = ""
      self.HASSPACE = ""
      self.INMILLIONS = ""
      self.ALTERID = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "CURRENCY":
         print "*****CURRENCY*****"
         name = attributes["NAME"]
         reserved = attributes["RESERVEDNAME"]
         print "Name:", name, "Reserved Name:",  reserved
      elif tag == "VOUCHERTYPE":
         print "*****VOUCHERTYPE*****"
         name = attributes["NAME"]
         reserved = attributes["RESERVEDNAME"]
         print "Name:", name, "Reserved Name:",  reserved

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "GUID":
         print "GUID:", self.GUID
      elif self.CurrentData == "PARENT":
         print "PARENT:", self.PARENT
      elif self.CurrentData == "MAILINGNAME":
         print "MAILINGNAME:", self.MAILINGNAME
      elif self.CurrentData == "TAXUNITNAME":
         print "TAXUNITNAME:", self.TAXUNITNAME
      elif self.CurrentData == "NUMBERINGMETHOD":
         print "NUMBERINGMETHOD:", self.NUMBERINGMETHOD




         
      elif self.CurrentData == "ORIGINALNAME":
         print "ORIGINALNAME:", self.ORIGINALNAME
      elif self.CurrentData == "EXPANDEDSYMBOL":
         print "EXPANDEDSYMBOL:", self.EXPANDEDSYMBOL
      elif self.CurrentData == "DECIMALSYMBOL":
         print "DECIMALSYMBOL:", self.DECIMALSYMBOL
      elif self.CurrentData == "ISUPDATINGTARGETID":
         print "ISUPDATINGTARGETID:", self.ISUPDATINGTARGETID
      elif self.CurrentData == "ASORIGINAL":
         print "ASORIGINAL:", self.ASORIGINAL
      elif self.CurrentData == "ISSUFFIX":
         print "ISSUFFIX:", self.ISSUFFIX
      elif self.CurrentData == "HASSPACE":
         print "HASSPACE:", self.HASSPACE
      elif self.CurrentData == "INMILLIONS":
         print "INMILLIONS:", self.INMILLIONS
      elif self.CurrentData == "ALTERID":
         print "ALTERID:", self.ALTERID
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "GUID":
         self.GUID = content
      elif self.CurrentData == "MAILINGNAME":
         self.MAILINGNAME = content
      elif self.CurrentData == "ORIGINALNAME":
         self.ORIGINALNAME = content
      elif self.CurrentData == "EXPANDEDSYMBOL":
         self.EXPANDEDSYMBOL = content
      elif self.CurrentData == "DECIMALSYMBOL":
         self.DECIMALSYMBOL = content
      elif self.CurrentData == "ISUPDATINGTARGETID":
         self.ISUPDATINGTARGETID = content
      elif self.CurrentData == "ASORIGINAL":
         self.ASORIGINAL = content
      elif self.CurrentData == "ISSUFFIX":
         self.ISSUFFIX = content
      elif self.CurrentData == "HASSPACE":
         self.HASSPACE = content
      elif self.CurrentData == "INMILLIONS":
         self.INMILLIONS = content
      elif self.CurrentData == "ALTERID":
         self.ALTERID = content
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = TallyHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("voucher_type.xml")
