import random as rnd
days_of_the_week=["sunday","monday","tuesday","wedenesday","thursday","friday","saturday"]
temperature=[]
above_avarage=[]
avarage=0
good_days_count_for_shelly=0
highest_temperature=26
highest_temperature_day=days_of_the_week[0]
lowest_temperature=40
lowest_temperatureday=days_of_the_week[0]
sum_temprature=0

for i in range (7):
    temperature.append(rnd.randint(26,40))

for i in range (7):
	sum_temprature+=temperature[i]
	if temperature[i] % 2 == 0:
		good_days_count_for_shelly+=1
	if temperature[i] > highest_temperature:
		highest_temperature = temperature[i]
		highest_temperature_day = days_of_the_week[i]
	if temperature[i] < lowest_temperature:
		lowest_temperature = temperature[i]
	lowest_temperaureday = days_of_the_week[i]

	print(days_of_the_week[i],temperature[i])

avg_temperature = sum_temprature/7
 
for b in range(7):
 	if temperature[b] > avg_temperature:
 		above_avarage.append(days_of_the_week[b])
print ("the average temp is"+str(avg_temperature))
print ("the days that it was above average"+str(above_avarage))

good_days_shelly_had = "good_days_count_for_shelly"
print("good_days_shelly_had",good_days_count_for_shelly)

