timee = int(input("Enter second: "))

#convert second to hour , minute and second
second_to_hour = round(timee / 3600,3)              
hour = int(second_to_hour)                          
minute = (second_to_hour - int(hour))* 60             
second = (minute - int(minute)) * 60                  

#convert time to "hh:mm:ss" format
if hour<10:
    saat = "0" + str(hour)
else:
    saat = str(hour)

if int(minute)<10:
    daghighe = "0" + str(int(minute))
else:
    daghighe = str(int(minute))

if int(second)<10:
    saniye = "0" + str(int(second))
else:
    saniye = str(int(second))


#print converted time to H:m:s
print("seconds to clock : ",saat,":",daghighe,":",saniye)