import datetime, requests, json, pprint
res = MY_API

for i in range(6):
  daily = weather['daily']
  date = daily[i]['dt']
  date_time = datetime.datetime.fromtimestamp( date ) 
  best = date_time.strftime( "%h %d") 
  temp = int(daily[i]['temp']['day'])
  description = daily[i]['weather'][0]['main']
  print(best, "-", temp, "°C,", description)
