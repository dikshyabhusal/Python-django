import requests
from datetime import datetime
import threading

def download(image_url, index):
    data = requests.get(image_url)
    with open(f"{index}.png", "wb") as f:
        f.write(data.content)


image_data = [
    "https://cnex.com.np/images/Pioneering-Female-Img7.png",
    "https://cnex.com.np/images/Our-Story.png",
    "https://cnex.com.np/images/Our-Story.png",
    "https://cnex.com.np/images/Pioneering-Female-Img7.png",
    "https://cnex.com.np/images/disk-image-rotate.png"
]

threads = []  
t1 = datetime.now()
print("***WITH THREADING***")

for index, image_url in enumerate(image_data):
    thread = threading.Thread(target=download, args=(image_url, index))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

t2 = datetime.now()
total_time = t2 - t1
total_seconds = total_time.total_seconds()
print(f"Execution time: {total_seconds} seconds")
