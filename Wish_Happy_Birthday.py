import datetime


while True:
    x = datetime.datetime.now()

    y = x.strftime("%d/%m/%Y %H:%M:%S")
    if(y == "23/07/2020 00:16:00"):
        print("Happy Birthday")