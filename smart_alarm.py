import requests                 # for making HTTP requests
import json                     # library for handling JSON data
import time                     # module for sleep operation
import datetime
import pytz
from boltiot import Bolt        # importing Bolt from boltiot module
import config                     # config file

mybolt = Bolt(config.bolt_api_key, config.device_id)

def send_telegram_message(message):
        url="https://api.telegram.org/"+ config.telegram_bot_id +"/sendMessage"
        data =  {
                  "chat_id": config.telegram_chat_id,
                  "text" : message
                }
        try:
             response=requests.request("POST",url,params=data)
             print("This is  the  Telegram URL")
             print(url)
             print("This is  the  Telegram response")
             print(response.text)
             telegram_data=json.loads(response.text)
             return telegram_data["ok"]
        except Exception as e:
             print("An error occured in sending the alert message via Telegram")
             print(e)
             return False
while True:
# Get the current time in UTC
          current_time_utc = datetime.datetime.utcnow()

# Define the time zone for India (IST)
          india_timezone = pytz.timezone('Asia/Kolkata')

          current_time_india = current_time_utc.astimezone(india_timezone)
          current_time_str = current_time_india.strftime("%H:%M:%S")
          print("The Current Time in India (IST) is: " + current_time_str)
          current_time_hrs=current_time_india.strftime("%H")
          current_time_mins=current_time_india.strftime("%M")
          if(current_time_hrs=="17" and current_time_mins=="46"):
             print("It is time to wake up Sir")
             message="Sir,  The  time is " +current_time_str+ " Wake up "
             telegram_status=send_telegram_message(message)
             print("This is the Telegram status : ", telegram_status)
             response = mybolt.digitalWrite('1','HIGH')
             print(response)
             response=mybolt.digitalWrite('1','LOW')
             print(response)
          time.sleep(5)
