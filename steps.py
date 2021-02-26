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

csv_heads = ["ID", "Time", "Steps"]

with open("steps-data.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(csv_heads)

ID = 0

while True:
    data = auth2_client.activities()
    print(data)
    sleep(5)
    # time = datetime.datetime.now()
    # steps = data["activities"]["steps"]
    # data_list = [ID, time, steps]
    # print(datetime.datetime.now())
    # print(data)
    # with open("steps-data.csv", "a") as file:
    #     writer = csv.writer(file)
    #     writer.writerow(data_list)
    # sleep(30.0)
    # ID += 1