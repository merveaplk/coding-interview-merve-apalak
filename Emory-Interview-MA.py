#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 01:39:06 2022

@author: merve
"""


import hashlib
import os
import datetime
import pandas as pd 
import wfdb as W
from scipy.signal import iirnotch,filtfilt
import heartpy as hp
import matplotlib.pyplot as plt
from scipy.signal import resample,iirnotch,medfilt
import csv

path='/home/merve/Desktop/A00'

######## File handling #########
data_csv=[]
def convert_datime(time):
    return datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d-%H:%M:%S')

for root, dirs, files in os.walk(path):
    for name in files:
        r_name,ext=os.path.splitext(name)
        if ext=='.mat':
            root_recording=os.path.join(root, name)
            MD5=hashlib.md5(open(root_recording, 'rb').read()).hexdigest()
            creation_date=convert_datime(os.path.getctime(root_recording))
            modification_date=convert_datime(os.path.getmtime(root_recording))
            sizes=os.path.getsize(root_recording)
            fs = W.rdrecord(root_recording[:-4]).fs
            data_csv.append([root_recording,name[:-4], MD5,creation_date,modification_date,sizes,fs])
            
final_frame=pd.DataFrame(data_csv, columns=['roots','file_name','MD5','creation_date','modification_date','size','fs'])        
final_frame.to_csv('A00_dic',index=False) 

#3.c It should not change by changing the filenames. Filename does not have ab affect.
#3.d In general, metadata should not have effect md5sum
3.e when you compress a file, the compression takes filenames and dates into account. In this case, md5sum should change      

####### Peak detection ############

path='/home/merve/Desktop/Emory_interview/A00'

indexes=[]
for root, dirs, files in os.walk(path):
    for name in files:
        r_name,ext=os.path.splitext(name)
        if ext=='.hea':
            path=os.path.join(root, name)    
            [channel,dics] = W.rdsamp(path[:-4])
            fs=dics['fs']
            filtered = hp.filter_signal(channel[:,0], cutoff = 0.05, sample_rate = fs, filtertype='notch')
            resampled_data = resample(filtered, len(filtered) * 2)
            wd, m = hp.process(hp.scale_data(resampled_data), fs * 2)
            RR_location=pd.Series(list(wd['RR_indices']))
            RR_location.to_csv('/home/merve/Desktop/Emory_interview/RR_indices/'+r_name)



###Notch filter for ECG signal
def baseline_wanderer(data):
    fs = 300 
    f0 = 60
    Q = 30.0 
    
    
    b, a =iirnotch(f0, Q, fs)    
    filtered_data = filtfilt(b, a, data)
    
    return filtered_data


  
