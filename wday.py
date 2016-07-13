#only for python34

from datetime import datetime

def str_Input():
        startstring=str(input("start time: "))
        endstring=str(input("end time: "))
        starttime = datetime.strptime(startstring,"%I:%M %p")
        endtime = datetime.strptime(endstring,"%I:%M %p")
        wdaytimes=[starttime,endtime]
        return wdaytimes
def bool_Event (eventstart = datetime, eventend = datetime):
        eventout = False
        rtime = datetime.now()
        efinish = eventend.time()
        estart = eventstart.time()
        rt = rtime.time()
        if (rt > estart) and (rt < efinish):
                 eventout = True
        else:
                 eventout = False

        return eventout
