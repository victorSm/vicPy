Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import wdaysched
>>> w = wdaysched.WeekDay()
>>> win = w.strInput()
start time: 2:00 pm
end time: 11:00 pm
>>> w.boolEvent(win[0],win[1])
True
>>> 
