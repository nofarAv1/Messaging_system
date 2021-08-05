import time
import datetime

def convert_time_human_readable():
    timestamp = time.time()
    value = datetime.datetime.fromtimestamp(timestamp)
    return value.strftime('%Y-%m-%d %H:%M:%S')