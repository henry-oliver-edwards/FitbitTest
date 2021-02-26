import gather_keys_oauth2 as Oauth2
import fitbit
import pandas as pd
import datetime
from time import sleep
import csv

OAuthCID = "22C8DC"
CSecret = "967eacb87b08aee6a31f041958781eb5"

server = Oauth2.OAuth2Server(OAuthCID, CSecret)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token["access_token"])
refresh_token = str(server.fitbit.client.session.token["refresh_token"])

auth2_client = fitbit.Fitbit(OAuthCID, CSecret, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=refresh_token)

startTime = pd.datetime(year=2021, month=2, day=16)

csv_heads = ["ID", "Time", "Sleep List", "Total Time Asleep", "Total Sleep Records", "Total Time In Bed"]

with open("sleep-data.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(csv_heads)

ID = 0

while True:
    data = auth2_client.get_sleep(startTime)
    time = datetime.datetime.now()
    sleepList = str(data["sleep"])
    totalAsleep = str(data["summary"]["totalMinutesAsleep"])
    totalSleepRecs = str(data["summary"]["totalSleepRecords"])
    totalTimeInBed = str(data["summary"]["totalTimeInBed"])
    data_list = [ID, time, sleepList, totalAsleep, totalSleepRecs, totalTimeInBed]
    print(datetime.datetime.now())
    print(data)
    with open("sleep-data.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(data_list)
    sleep(60.0)
    ID += 1