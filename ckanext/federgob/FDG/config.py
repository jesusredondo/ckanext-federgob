#!/usr/bin/python
# -*- coding: utf-8 -*-

#Script by: Jesús Redondo García
#Date: 28-10-2014

#Script to get the needed metadata.

import sys
import codecs

print '\nFill the following fields about the catalog.'
print 'If you need info about each field please visit: https://github.com/jesusredondo/ckanext-federatedatosgob.\n'

# Ask for parameters 
while True :
	print ' URL OF THE CATALOG : ',
	url_catalog = sys.stdin.readline().replace('\n','')
	if url_catalog != '' : break

while True :
	print 'URL DATASET : ',
	url_dataset = sys.stdin.readline().replace('\n','')
	if url_dataset != '' : break

while True :
	print 'LANGUAGE IN RFC 1766 STANDARD : ',
	language = sys.stdin.readline().replace('\n','')
	if language != '' : break

while True :
	print 'TITLE : ',
	title = sys.stdin.readline().replace('\n','')
	if title != '' : break

while True :
	print 'DESCRIPTION : ',
	description = sys.stdin.readline().replace('\n','')
	if description != '' : break

while True :
	print 'ISSUED IN ISO-8601 STANDARD : ',
	issued = sys.stdin.readline().replace('\n','')
	if issued != '' : break

while True :
	print 'URL OF THE PUBLISHER USING NTI FORMAT : ',
	url_publisher = sys.stdin.readline().replace('\n','')
	if url_publisher != '' : break

while True :
	print 'URL OF THE LICENSE : ',
	url_license = sys.stdin.readline().replace('\n','')
	if url_license != '' : break


#Save the info in fields.conf:
fields_conf_file = open('fields.conf','r')
fields_lines = fields_conf_file.readlines()
fields_conf_file.close()

output = ''
for line in fields_lines :
	if '{-URL-CATALOG-}' in line : output = output + '{-URL-CATALOG-} : '+url_catalog+ '\n'
	elif '{-URL-DATASET-}' in line : output = output + '{-URL-DATASET-} : '+url_dataset+ '\n'
	elif '{-LANGUAGE-}' in line : output = output + '{-LANGUAGE-} : '+language+ '\n'
	elif '{-TITLE-}' in line : output = output + '{-TITLE-} : '+title+ '\n'
	elif '{-DESCRIPTION-}' in line : output = output + '{-DESCRIPTION-} : '+description+ '\n'
	elif '{-ISSUED-}' in line : output = output + '{-ISSUED-} : '+issued+ '\n'
	elif '{-URL-PUBLISHER-}' in line : output = output + '{-URL-PUBLISHER-} : '+url_publisher+ '\n'
	elif '{-URL-LICENSE-}' in line : output = output + '{-URL-LICENSE-} : '+url_license+ '\n'

fOut = open('fields.conf','w')
fOut.write(output)
fOut.close()


execfile('merge_metadata.py')