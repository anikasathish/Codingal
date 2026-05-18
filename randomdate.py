import random
import time

def getRandomDate(startDate, endDate):
    """
    Return a random date string between startDate and endDate.
    Dates must be in 'M/D/YYYY' or 'MM/DD/YYYY' format.
    """
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    if endTime < startTime:
        raise ValueError("endDate must be after startDate")
   
    randomTime = startTime + random.random() * (endTime - startTime)
    
    return time.strftime(dateFormat, time.localtime(randomTime))

print("Random Date =", getRandomDate("1/1/2016", "12/12/2018"))
