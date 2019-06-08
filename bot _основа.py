import datetime
import random
import vk_api
import requests 
from vk_api.longpoll import VkLongPoll, VkEventType 
with open('C:/Users/Vova/Desktop/secret.txt','r') as file:
    t=file.read()
vk_session = vk_api.VkApi(token=t)
vk = vk_session.get_api()
check=set()
def send_to_all(text):
    members=vk.groups.getMembers(group_id='183149235')['items']
    for person in members:
        try:
            vk.messages.send(user_id=person,
                        random_id=random.randint(0,10**9),
                        message=text)
        except:
            continue
while True:
    date=datetime.datetime.today()
    day=date.weekday()
    date=datetime.date.today()
    if day==0 and flag:
        flag=False
        #отправляем расписание на неделю
        #send_to_all()
    else:
        flag=True
    if date not in check:
        check.add(date)
        #отправляем расписание на день
        #send_to_all()
