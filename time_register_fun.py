import datetime
import time 

def time_register():
    current_time = time.time()
    time_object = datetime.datetime.fromtimestamp(current_time)
    formatted_time = time_object.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time