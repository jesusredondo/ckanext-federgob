#!/usr/bin/python
# -*- coding: utf-8 -*-

#Script by: Jesús Redondo García
#Date: 28-10-2014

#Script to process the user metadata about the catalog.

#Get all the fields from fields.conf
fields_conf_file = open('fields.conf','r')
fields_lines = fields_conf_file.readlines()
fields_conf_file.close()

for line in fields_lines :
	if '{-URL-CATALOG-} : ' in line : url_catalog = line.replace('{-URL-CATALOG-} : ','').replace('\n','')
	elif '{-URL-DATASET-} : ' in line : url_dataset = line.replace('{-URL-DATASET-} : ','').replace('\n','')
	elif '{-LANGUAGE-} : ' in line : language = line.replace('{-LANGUAGE-} : ','').replace('\n','')
	elif '{-TITLE-} : ' in line : title = line.replace('{-TITLE-} : ','').replace('\n','')
	elif '{-DESCRIPTION-} : ' in line : description = line.replace('{-DESCRIPTION-} : ','').replace('\n','')
	elif '{-ISSUED-} : ' in line : issued = line.replace('{-ISSUED-} : ','').replace('\n','')
	elif '{-URL-PUBLISHER-} : ' in line : url_publisher = line.replace('{-URL-PUBLISHER-} : ','').replace('\n','')
	elif '{-URL-LICENSE-} : ' in line : url_license = line.replace('{-URL-LICENSE-} : ','').replace('\n','')



#Save the metadata in the base catalog.
fIn = open('base_catalog_template.rdf','r')
filedata = fIn.read()
fIn.close()

newdata = filedata.replace('{-URL-CATALOG-}',url_catalog)
newdata = newdata.replace('{-URL-DATASET-}',url_dataset)
newdata = newdata.replace('{-LANGUAGE-}',language)
newdata = newdata.replace('{-TITLE-}',title)
newdata = newdata.replace('{-DESCRIPTION-}',description)
newdata = newdata.replace('{-ISSUED-}',issued)
newdata = newdata.replace('{-URL-PUBLISHER-}',url_publisher)
newdata = newdata.replace('{-URL-LICENSE-}',url_license)

fOut = open('base_catalog.rdf','w')
fOut.write(newdata)
fOut.close()
