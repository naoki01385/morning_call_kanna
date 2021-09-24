import json
file=open('info.json','r')
info=json.load(file)
from linebot import LineBotApi
from linebot.models import TextSendMessage
CHANNEL_ACCESS_TOKEN=info['CHANNEL_ACCESS_TOKEN']
line_bot_api=LineBotApi(CHANNEL_ACCESS_TOKEN)
import time


def main():
        USER_ID = info['USER_ID']
        messages= TextSendMessage(text="おはよう〜 \n 朝だよ!!起きて❤️")
        line_bot_api.push_message(USER_ID, messages=messages)
    
def main2():
        USER_ID = info['USER_ID']
        messages= TextSendMessage(text="おきてよ〜☹️")
        line_bot_api.push_message(USER_ID, messages=messages)
def main3():
        USER_ID = info['USER_ID']
        messages= TextSendMessage(text="も〜！！")
        line_bot_api.push_message(USER_ID, messages=messages)
        
def main4():
        USER_ID = info['USER_ID']
        messages= TextSendMessage(text="おこったかんな〜")
        line_bot_api.push_message(USER_ID, messages=messages)
        
def main5():
        USER_ID = info['USER_ID']
        messages= TextSendMessage(text="ゆるさないかんな〜")
        line_bot_api.push_message(USER_ID, messages=messages)
def main6():
        USER_ID = info['USER_ID']
        messages= TextSendMessage(text="おまえがだ〜んな❤️")
        line_bot_api.push_message(USER_ID, messages=messages)
        
if __name__ == "__main__":
        main()
        time.sleep(2)
        main2()
        time.sleep(2)
        main3()
        time.sleep(2)
        main4()
        time.sleep(2)
        main5()
        time.sleep(2)
        main6()    