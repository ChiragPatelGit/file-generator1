import string
import sys

#Open and Read the Template File
filein = open("TestConfigTemplate.txt")
src = string.Template(filein.read())

hostname = "Shiloh"
addr1 = "2.2"
mask1 = "255.240"

#Substitute and store in th variable "result"
d={'hostname':hostname, 'addr1':addr1, 'mask1':mask1}

result = src.substitute(d)

#Create an output file based on provided hostname
fileout = open(hostname + '.cfg', 'w')
fileout.write(result)
fileout.close()
