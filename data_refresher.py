count=0
import pandas as pd
import numpy as np
import schedule
import time

def job():
    global count
    count+=1
    print(f"Refreshing data every 5 minutes,data refresh count --> {count}")  # Replace this with your actual code/task
    
    #retrieves air pollution from government data API 
    wd = pd.read_csv("https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001b9dcfea930f84fbc4526756ab3d1b502&format=csv&limit=1000")
    wd.dropna(inplace=True)      #drops all empty rows
    wd.reset_index(inplace=True) #resets the current index
    wd.drop(columns=['index'],inplace=True)

    #saves the csv processed csv file
    wd.to_csv('live_data.csv',index_label='index',index=True)
    return()

schedule.every(300).seconds.do(job)  #schedules the called fucntion to run every five minutes


while True:
    schedule.run_pending()
    time.sleep(1)  # Check every second
    