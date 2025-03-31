### Module used for getting data from Twitch: https://github.com/mark-rez/Twitch-Chat-Reader?tab=readme-ov-file


from twitchchatreader import TwitchChatReader
from twitchchatreaderevents import CommentEvent, ConnectEvent
import os
import csv
from datetime import datetime



#insert the name of the streamer to collect logs from
streamer_handle = "ironmouse"

#establish connection to stream
reader: TwitchChatReader = TwitchChatReader(streamer_handle) 

#groundwork for folder that will be filled with the chat logs
script_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(script_dir, "chat_logs_" + streamer_handle)
#to help differentiate text files, will also add the date and time to them
now = datetime.now()
today = now.strftime("%Y%m%d_%H%M")


if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' created.")
    
else:
    print("exists already bozo")
file_path = os.path.join(folder_path, streamer_handle + "_" + today + ".txt") 

#If connection good print
@reader.on("connect")
def on_connect(event: ConnectEvent):
    print("Connection established!")

#If read chat message, print and add into .txt file

@reader.on("comment")

def on_connect(event: CommentEvent):
    chat_message = ("\""+ event.comment+ "\"")
    print(chat_message)
    with open(file_path, "a") as file:
        file.write(chat_message + "\n")

## Those who know :skull: ##

