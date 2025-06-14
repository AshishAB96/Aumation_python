import schedule 
import time
from datetime import datetime

def MySchedule():

    print("Inside the my schedule function at :",datetime.now())
    
def main():
    print("Current time is : ",datetime.now())
    schedule.every(20).seconds.do(MySchedule)
    print("Application is in wating state .....")

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("End of Automation script : ")


if __name__ == "__main__":
    main()


