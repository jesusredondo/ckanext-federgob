#!/usr/bin/python
# -*- coding: utf-8 -*-

#Script by: Jesús Redondo García
#Date: 28-10-2014

import os
from subprocess import call


#Modify default_crontab
path_base = os.path.dirname( os.path.realpath( __file__ ) )
path_crontab_default = os.path.join(path_base,'Ctab','default_crontab')
path_crontab = os.path.join(path_base,'Ctab','Cron_auto')

crontab_file_default = open(path_crontab_default,'r')
filedata = crontab_file_default.read()
crontab_file_default.close()

newdata = filedata.replace('@@-PATH-PLUGIN-@@',path_base)


crontab_file = open(path_crontab,'w')
crontab_file.write(newdata)
crontab_file.close()


#Include the crontab file to the system
#print param
call(["crontab", "-u", "root",path_crontab])
print "Federatedatosgob will be updated each day at 00:00 a.m."
