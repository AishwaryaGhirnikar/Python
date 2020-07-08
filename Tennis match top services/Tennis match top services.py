import os
import numpy as np
import pandas as pd
import sys
from moviepy import video
from moviepy.editor import *
import soundfile as sf
import pyloudnorm as pyln
from heapq import nlargest
from multiprocessing import Process, Semaphore
from moviepy.editor import VideoFileClip, concatenate_videoclips

def break_files():
    df = pd.read_csv(r"C:\Users\HP\Project 1\project.csv")
    num = 0
    
    for index in df.index:
        broken_video = VideoFileClip(r"C:\Users\HP\Project 1\Tennis match.mp4").subclip(df['service start time in sec'][index], 
                                                                                        df['service end time in sec'][index])
        broken_video.write_videofile(r"C:\Users\HP\Project 1 New\service_%s.mp4" % num)
        
        broken_video.audio.write_audiofile(r"C:\Users\HP\Project 1 New\service_%s.wav" % num)
        num+=1
        
        
        
directory = r"C:\Users\HP\Project 1 New"
service = {}

def top_service():

    for filename in os.listdir(directory):
        
        if filename.endswith(".wav"):
            filepath = os.path.join(directory,filename)  #Joins paths of directory & filename in directory
            data, rate = sf.read(filepath)  # o mload audio (with shape (samples, channels))
            meter = pyln.Meter(rate)  # create BS.1770 meter
            loudness = meter.integrated_loudness(data)  # measure loudness
            key=filename.split(".")[0] + ".mp4"
            service[key] = loudness
        #print(loudness)
    #print(service)
        
    '''
    #Getting loudess of top services in list form
    
    keys, values = zip(*service.items())
    values = list(values)
    #print(list(values))
    values.sort()
    n=int(input("Give the number of top services from tennis match: "))
    top_services = values[-n:]
    top_services.sort(reverse=True)
    print(top_services)
    '''
    
    #Getting top services having top loudness
    while True:
        
        n = input("\nHow many top services you want see? ")
        
        if n <= '0':
            print("0 or negative number is not accepted. Please enter non zero positive number")
        elif n > str(len(service)):
            print("Enter the number less than total number of services and it should not be float or character")
        else:
            try: 
                n = int(n)
                top_services = nlargest(n, service, key = service.get)
                print(top_services)
                break
            except ValueError:
                print("Unvalid Input. Please try again ...")

    top_services_clip=[]
    
    for i in top_services:
        top_services_clip.append(VideoFileClip(os.path.join(directory,i)))

    final_clip = concatenate_videoclips(top_services_clip)
    final_clip.write_videofile(os.path.join(directory,"tennis_match_top_services.mp4"))
    
    
