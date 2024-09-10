import time
from datetime import datetime


def task1():
    print("task 1 started")
    time.sleep(2)
def task2():
    print("task 2 started")
    time.sleep(2)

t1= datetime.now()
task1()
task2()
t2 =datetime.now()
execution_time = t2 -t1
print(f"Execution time is {execution_time}")