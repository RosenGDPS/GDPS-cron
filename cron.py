import requests
import time
import enum 
import config


def cronOnce():
    requests.get(config.GDPS_DB_URL + "tools/cron/cron.php")
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
def buildTime(t : time.struct_time) -> str:
    def fixLen(str_to_fix):
        return str_to_fix if str(str_to_fix).__len__() > 1 else ("0" + str(str_to_fix))
    return fixLen(str(t.tm_hour)) + ":" + fixLen(str(t.tm_min)) + ":" + fixLen(str(t.tm_sec))
def mainLoop():
    try:
        config.DEBUG
    except AttributeError:
        config.DEBUG = False
    if not config.DEBUG:
            if config.GDPS_DB_URL == "http://exampleGDPS.7m.pl/database/":
                cronNotify(cronNotification.ERROR, f"Please modify the 'GDPS_DB_URL' variable in the 'config.py' file.")
                exit()
    while True:
        
        


        try:
            t = time.localtime(time.time())
            cronOnce()
            cronNotify(cronNotification.SUCCESS, f"{buildTime(t)} => Ran a CRON procedure successfully!")
        except:
            cronNotify(cronNotification.ERROR, f"{buildTime(t)} => Failed to run the CRON procedure.")
        try:
            time.sleep(config.CRON_SECONDS)
        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    mainLoop()
