import matplotlib.pyplot as mp


mp.figure(figsize=(10,5))
mp.title('Активность компьютера.')

day0 = open('monday.txt','r+')
day0 = round(float(day0.read()))


day1 = open('tuesday.txt','r+')
day1 = round(float(day1.read()))


day2 = open('wednesday.txt','r+')
day2 = round(float(day2.read()))


day3 = open('thursday.txt','r+')
day3 = round(float(day3.read()))


day4 = open('friday.txt','r+')
day4 = round(float(day4.read()))


day5 = open('saturday.txt','r+')
day5 = round(float(day5.read()))


day6 = open('sunday.txt','r+')
day6 = round(float(day6.read()))
print(type(day6))




x = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
y = [round((day0/60)/60),round((day1/60)/60),round((day2//60)/60),round((day3/60)/60),round((day4/60)/60),round((day5/60)/60),round((day6/60)/60)]


mp.bar(x,y,label = 'Активность ПК')
#mp.plot(x,y,color = 'red',marker = 'o',markersize = 7)

mp.xlabel('Дни недели')
mp.ylabel('Кол-во часов')
mp.savefig('MonitorCheck.png')









