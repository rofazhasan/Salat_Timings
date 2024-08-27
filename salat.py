import requests
from datetime import datetime
api_endpoint="http://api.aladhan.com/v1/timingsByCity/:date"
def get_salat_timings(day,country,city):
  parameters={
    "date" : day,
    "country" : country,
    "city":city,
    "school":1
  }
  request_a=requests.get(url=api_endpoint,params=parameters)
  if request_a.json()["code"]==200:
    reqD=request_a.json()["data"]["timings"]
    dat=[]
    sala=["Fajr","Dhuhr","Asr","Maghrib","Isha"]
    for i in range(0,5):
      dat.append(reqD[sala[i]])
      dat[i] = datetime.strptime(dat[i], '%H:%M').strftime('%I:%M %p')
      if i==4:
       dat.append(request_a.json()["data"]["date"]["readable"])
      i+=1
    return dat
  else:
    return 201
