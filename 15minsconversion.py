#!/usr/bin/python

import pandas as pd
import os
import time

def fetch(pathdir, now, new_pathdir):
    for root, dirs, files in os.walk(pathdir, topdown=False):
        print 'found directory:', root
        for file in files:
            print 'filename: \t', file
            filestamp = os.path.getmtime(os.path.join(root,file))
            filecmp = now - 900
            if filestamp > filecmp:
                print 'file updated within 15 mins', os.path.join(root,file)
                # code to convert xlsx to csv using pandas
                read_file = pd.read_excel(os.path.join(root,file))
                # save at new path with same directory name and file
                # print type(file)
                z = file.split('.')
                x = root.split('/')
                f = new_pathdir + x[-1] + '/' + z[0] + '.csv'
                read_file.to_csv(f, index=None)
                print 'converted to csv, saving at: \t', f
            else:
                print 'file update older than 15 mins'



pathdir = '/root/exportpath/'
now = time.time()
new_pathdir = '/root/output/'
fetch(pathdir, now, new_pathdir)


