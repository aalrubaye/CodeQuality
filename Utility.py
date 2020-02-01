import sys
import datetime
import time

__author__ = 'Abdul Rubaye'


# show or hide print repo progress
def show_progress_message(do_print, message):
    if do_print:
        sys.stdout.write("\r" + message)
        sys.stdout.flush()


# convert date/time stamp to a regular string
def change_date_to_string(date):
    dt = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    return str(dt.year) + str(dt.month) + str(dt.day) + str(dt.hour) + str(dt.minute) + str(dt.second)


# return the time elapsed for each process of a repository
def time_elapsed(start):
    elapsed_time = time.time() - start
    return str(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


