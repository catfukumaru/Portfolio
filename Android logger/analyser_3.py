

import re
from datetime import datetime
import threading
import time
import pandas as pd

class LogEntry:    
    def __init__(self, pid='', tid='', level='', tag='', message='', line ='', time=''):
        self.pid = pid
        self.tid = tid 
        self.level = level 
        self.tag = tag 
        self.message = message
        self.time = time
        self.raw_line = line
    
    def to_integer(self, not_int=""):
        return int(not_int)

    def remove_extra_spaces(self, unformatted_string):
        return str(unformatted_string).strip()

    def parse_timestamp(self, unformatted_time):
        #print(unformatted_time)
        dt = datetime.strptime(unformatted_time, "%m-%d %H:%M:%S.%f")
        new_dt = dt.replace(year=2024)
        timestamp = new_dt.timestamp()
        return timestamp





def parse_log_file(file_path):
    entries = []

    with open(file_path, mode='r', encoding='utf-8') as file:
        log_file_lines = file.readlines()
    
    for line in log_file_lines:
        parsed_entry = parse_log_line(line)

        if parsed_entry is not None:
            entries.append(parsed_entry)
    
    
    print("Finished processing files!")
    return entries


def reminder_loop(stop_event, interval=5):
    """
    Prints reminders while the task is still running.
    """
    start = time.time() # start measuring the time 

    while not stop_event.wait(interval): # while the long task has not stopped
        elapsed = int(time.time() - start) # measure the time passed
        print(f"[INFO] Still running... ({elapsed}s elapsed)") # print the update



#not_matched = []

def parse_log_line(line): 

    regex =r"([-+])*(\d{2}-\d{2})*\s+(\d{2}:\d{2}:\d{2}\.\d{3})\s+(\d{3,5})\s+(\d{3,5})\s+(\bWTF|ALL|V|D|I|W|E|F|O\b)\s+([^:]+):{1,}\s+(.+)" # i am  going to stop here cause i don't want to spend more time trying to fix the rege i am sure its enough 
    match = re.search(regex, line, re.I)
    
    # if not match: 
    #     not_matched.append(line)
    #     return None
    #print(match.group(8))
    entry = LogEntry()
    #print( match.group(1))
    if match: 
              

        time = match.group(2) +' '+ match.group(3) 
        entry.timestamp = entry.parse_timestamp(time)

        entry.pid = entry.to_integer(match.group(4))

        entry.tid = entry.to_integer(match.group(5))

        entry.level = entry.remove_extra_spaces(match.group(6))

        entry.tag = entry.remove_extra_spaces(match.group(7))

        entry.message = match.group(8)

        entry.raw_line = line

    return  entry

            

def show_errors(logs):
    total = 0
    satisfies_condition = []
    for log in logs:
        if log.level == 'E'or log.level == "F":
            satisfies_condition.append(log)
            total+=1
    
    if total ==0:
        return {'empty': 'yeah i guess the logs are wrong'}
    # just want to see the first one though   
    return satisfies_condition



def search_logs(logs, keyword):
    total = 0
    satisfies_condition = []
    for log in logs:
        if keyword in log.message:
            satisfies_condition = log
            total+=1
    
    if total ==0:
        return {'empty': 'yeah i guess the keyword is wrong'}
    
    return satisfies_condition

    




def filter_by_tag(logs, tag):
    total = 0
    satisfies_condition = []
    for log in logs:
        if log.tag == tag:
            satisfies_condition.append(log)
            total+=1

    if total ==0:
        return {'empty': 'yeah i guess the tag is wrong'}
    # just want to see the first one though
    return satisfies_condition




def count_levels(logs):

    verbose = 0
    debug = 0
    info = 0
    warning = 0
    error = 0
    fatal = 0
    show_no_logs = 0
    show_all_logs = 0
    should_not_happen = 0

    for log in logs:
        match log.level:
            case 'WTF':
                should_not_happen +=1
            case 'ALL':
                show_all_logs+=1
            case 'V':
                verbose+=1
            case 'D':
                debug+=1
            case 'I':
                info+=1
            case 'W':
                warning +=1
            case 'E':
                error+=1
            case 'F':
                fatal+=1
            case 'O':
                show_no_logs +=1

    all_levels = {
    "verbose": verbose,
    "debug": debug,
    "info": info,
    "warning": warning,
    "error": error,
    "fatal": fatal,
    "show_no_logs": show_no_logs,
    "show_all_logs": show_all_logs,
    "should_not_happen": should_not_happen
    }

    return all_levels




def detect_crashes(logs):
    matched_logs = []
    for log in logs:
        if 'F' in log.level:
            #print("crashed")
            matched_logs.append(log)
    return matched_logs




def filter_by_pid(logs, pid):
    total = 0
    satisfies_condition = []
    for log in logs:
        if log.pid == pid:
            satisfies_condition.append(log)
            total+=1

    if total ==0:
        return {'empty': 'yeah i guess the tag is wrong'}
    # just want to see the first one though
    return satisfies_condition



def make_dataframe():

    stop_event = threading.Event() # what tell the program tha the long running task has ended 

    # Start reminder thread 
    reminder_thread = threading.Thread(
        target=reminder_loop, # the function that needs to be rerun to show me updates
        args=(stop_event,), # the arguments of the update function
        daemon=True # so that the function works 
    )
    reminder_thread.start() # start the main thread

    print("[INFO] Task started...")

    # Run your actual task
    result =  parse_log_file('Android.log')

    # Stop reminders
    stop_event.set() # update what tell the program that the task is done

    print(f"[DONE]") # letting me know that the function i need an update on is done

    df = pd.DataFrame([vars(s) for s in result]) 

    return df


