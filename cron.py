import requests
import time
import enum 
from config import *

def cronOnce():
    requests.get(GDPS_DB_URL + "tools/cron/cron.php")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class cronNotification(enum.Enum):
    SUCCESS = 1
    ERROR = 2
def cronNotify(NotificationType : cronNotification, message):
    if NotificationType == cronNotification.SUCCESS:
        print(f"{bcolors.OKGREEN}[SUCCESS] {message}{bcolors.ENDC}")
    elif NotificationType == cronNotification.ERROR:
        print(f"{bcolors.FAIL}[FAIL] {message}{bcolors.ENDC}")

if __name__ == '__main__':
    while True:
        try:
            cronOnce()
            cronNotify(cronNotification.SUCCESS, "Ran a CRON procedure successfully!")
        except:
            cronNotify(cronNotification.ERROR, "Failed to run the CRON procedure.")
        try:
            time.sleep(3600)
        except KeyboardInterrupt:
            exit()
