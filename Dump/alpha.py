from urllib.request import urlopen
import datetime

"""To get the date in the format YYY-MM-DD"""

i=datetime.datetime.now()
y=int("  %d"%i.year)
m=int("  %d"%i.month)
d=int("  %d"%i.day)
date=str(datetime.date(y,m,d))

"""To get an input of the date from the user"""

time=int(input('enter the time  (choose from 0 , 3 , 6 , 9 , 12 , 15 , 18 , 21) :'))
if (time==3 or time==6 or time==9 or time==12 or time==15 or time==18 or time==21):
	t=(time-3)
elif time==0:
	t=(21)
else:
	print("invalid time")
	exit()
if (t==0 or t==3 or t==6 or t==9):
	t='0'+str(t)+':00:00'
elif (t==12 or t==15 or t==18 or t==21):
	t=str(t)+':00:00'	
dt='"dt_txt":'+'"'+date+' '+t+'"'

"""Input the location of the place from the user"""

q=input('Enter the location :')

"""Input the API_key from the user"""

APPID=input('Enter your API key :')
time=str(time)+':00:00'
url='http://api.openweathermap.org/data/2.5/forecast?q='+q+'&APPID='+APPID
f=urlopen(url)
u=str(f.read())
z=((u.find(dt))-1)
g1=u.find("temp",z)
g2=u.find("temp_min",z)
g3=u.find("temp_max",z)
g4=u.find("pressure",z)
g5=u.find("sea_level",z)
g6=u.find("grnd_level",z)
g7=u.find("humidity",z)
g8=u.find("temp_kf",z)
g9=u.find("Rain",z)
g10=u.find("speed",z)
g11=u.find("deg",z)
p1=float(float(u[g1+6:g1+12])-float(273))
p2=float(u[g2+10:g2+16])
p3=float(u[g3+10:g3+16])
p4=float(u[g4+10:g4+16])
p5=float(u[g5+11:g5+17])
p6=float(u[g6+12:g6+18])
p7=float(u[g7+10:g7+13])
p8=float(u[g8+9:g8+13])
p9=u[g9+21:g9+34]
p10=float(u[g10+7:g10+11])
p11=float(u[g11+5:g11+8])
print('')
print("The weather report for date("+date+") and time("+str(time)+") is as follows")
print('')
print("temp="+p1)
print("temp_min="+(p2-273))
print("temp_max="+(p3-273))
print("pressure="+p4)
print("sea_level="+p5)
print("grnd_level="+p6)
print("humidity="+p7)
print("temp_kf="+p8)
print("Rain="+p9)
print("wind speed="+p10)
print("wind degree="+p11)
print("")