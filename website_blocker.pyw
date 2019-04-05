import time
from datetime import datetime as dt

file_path=r"C:\Windows\System32\drivers\etc\hosts"
host_file="127.0.0.1"
website_list=["store.steampowered.com","www.youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,12) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        with open(file_path,"r+") as file:
            content=file.read()
            print("Working hours")
            for websites in website_list:
                if websites in content:
                    pass
                else:
                    file.write(host_file +"  "+ websites + "\n")
        
    else:
        with open(file_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for lines in content:
                if not any(website in lines for website in website_list):
                    file.write(lines)
            file.truncate()
            print("fun time")
    time.sleep(5)