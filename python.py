simport random 

temperatures = []
for i in range(7):
    temperatures.append(random.randint(26, 41))
weekdays=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Sautday"]
good_days_count=0
lowest_temp=41
highest_temp=25
highest_temp_day=""
lowest_temp_day=""
for i in range(len(temperatures)):
    if temperatures[i] % 2 == 0:
        print(weekdays[i])
        good_days_count += 1
    if temperatures[i] < lowest_temp:
        lowest_temp = temperatures[i]
        lowest_temp_day = weekdays[i]
    
    if temperatures[i] > highest_temp:
        highest_temp = temperatures[i]
        highest_temp_day = weekdays[i]
average=0
tempsum=0
for i in range(len(temperatures)):
	tempsum+=temperatures[i]
average=tempsum/7
above_avg=[]
for i in range(len(temperatures)):
	if temperatures[i]>average:
		above_avg.append(temperatures[i])
print("the weather report:")
for i in range(7):
	print(weekdays[i],":",temperatures[i])
print("*")
print("*")
print("shelly had",good_days_count,"good days")
print("*")
print("*")
print("the hottset temperature was:",highest_temp,"on",highest_temp_day)
print("the lowest was:",lowest_temp,"on",lowest_temp_day)
print("*")
print("*")
print("the average temperature was:",average)
print("the days with above average temperature were:",above_avg)