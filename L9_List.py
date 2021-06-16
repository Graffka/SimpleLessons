#-------------------------------------------------------------------
# Program by Vycheslav.H.
#
#
# Version   Date    Info
# 1.0       2021    Lesson
#
#------------------------------------------------------------------

cars = ['Audi', 'BMW', 'Mercedes', 'VW']
cars.append('Volvo')
cars.insert(1, 'Scania')
cars.insert(0, 'TEST')

for car in cars:
    car.upper()

#create new list
number_list = list(range(0,17))

for i in number_list:
    i+=1

#changed each other
new_cars = cars

#not changed
indep_cars = cars[:]
