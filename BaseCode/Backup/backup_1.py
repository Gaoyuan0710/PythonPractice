#! /usr/bin/python
#Filename:backup 1.0

import os
import time

source = ['~/Downloads', '~/Document'];
target_dir = '~/test/'

target = target_dir + time.strftime('%Y%M%d%H%M%S') + '.zip'
zip_command = "zip -qr %s %s"%(target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'You successed backup to', target
else:
	print 'Backup Failed'
