from twilio.rest import Client
import get_temp
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)
# Your Account SID from twilio.com/console
account_sid = os.getenv('ACCOUNT_SID')
# Your Auth Token from twilio.com/console
auth_token  = os.getenv("AUTH_TOKEN")

client = Client(account_sid, auth_token)
temp_data = get_temp.Get_Temp().start()
print(temp_data)
json_to_string = " 현재 온도 : {}\n\n{}\n\n 강수확률 : {} \n\n 바람 : {}\n\n 미세먼지 : {} \n\n 초미세먼지 : {}\n\n 습도 : {} ".format(temp_data['현재 온도'],temp_data["최저최고"],temp_data['강수확률'],temp_data['바람'],temp_data['미세먼지'],temp_data['초미세먼지'],temp_data['습도'])
message = client.messages.create(
    to="+8201091486129", 
    from_="+19706950752",
    body=json_to_string)

print(message.sid)
