import time 
from plyer import notification 
if __name__=='__main__':
    while True:
        notification.notify(
            title = "All Day Reminder!!",
            message = "Today you have to submit your assignment!!",
            timeout = 2 
        )
    time.sleep(10) 