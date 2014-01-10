from datetime import time
from time import gmtime
import calendar

def uIntToString(uintTime):
    timeStruct = gmtime(float(uintTime))
    year = str(timeStruct.tm_year)
    month = calendar.month_name[timeStruct.tm_mon]
    day = str(timeStruct.tm_mday)
    return day + " " + month + " " + year
