from datetime import datetime
from time import sleep

znak1 = chr(16)
znak2 = chr(17)

while True:
    sleep(0.5)
    date = datetime.now()
    time = '%d:%d:%02d' % (date.hour, date.minute, date.second)
    print("► " + time + " ◄", end="\r")

