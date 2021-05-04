# TASK:
# A list of lecture times is given in case1. Our task is to find out the maximum Time gap between two lectures that a student may get.\
# Start Time of the first lecture is the  time when college opens and the end time of the last class is when the college closes
# Given case1 below has 4 lectuers starting from 5:00 am in morning till 4:30pm in evening.


import string
import datetime

case1 = ["9:30 AM-10:30 AM", "5:00 AM-9:00 AM", "12:10 PM-2:30 PM", "3:45 PM-4:30 PM"]
timeList = []
TIME_DIFFERENCE = 0

def getSeconds(timeStrings):
    if(timeStrings.split()[-1] == "AM"):
        hh,mm = timeStrings.split()[-2].split(":")
        totalSeconds = int(hh)*3600 + int(mm)*60   
    elif(timeStrings.split()[-1] == "PM"):
        hh,mm = timeStrings.split()[-2].split(":")
        if(int(hh) == 12):
            totalSeconds = int(hh)*3600 + int(mm)*60
        else: 
            hh = int(hh)+12
            totalSeconds = (int(hh) + 12) * 3600 + int(mm)*60
    return(totalSeconds)

def sortTimeList(case1):
    for i in case1:
        t1,t2 = i.split("-")
        startTime = getSeconds(t1)
        endTime = getSeconds(t2)
        timeList.append(startTime)
        timeList.append(endTime)
    timeList.sort()
    return timeList


def getDiff(case1,TIME_DIFFERENCE):
    timeList = sortTimeList(case1)
    for i in range(1,len(case1)):
        # print(timeList[i*2])
        if(timeList[i*2] - timeList[(i*2) - 1] > TIME_DIFFERENCE):
            TIME_DIFFERENCE = timeList[i*2] - timeList[(i*2) - 1] 
    return TIME_DIFFERENCE

maxGap = getDiff(case1,TIME_DIFFERENCE)
# time = maxGap/3600
# # hours = int(time)
# minutes = (time*60)%60
print("Maximum time-gap Between Two Lectures:","%d:%02d" % (int(maxGap/3600), ((maxGap/3600)*60)%60))
