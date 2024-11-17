def calculate_area_of_rectangle():
    length = int(input('value of length'))
    breadth = int(input('value of breadth'))
    area_of_rectangle = length * breadth

    print('area_of_rectangle', area_of_rectangle)
calculate_area_of_rectangle()

def calculate_workdone():
    force = int(input('value of force'))
    distance = int(input('value of distance'))
    workdone = force * distance


    print('workdone',workdone)
calculate_workdone()

def calculate_pressure():
    force=int(input('value of force'))
    area=int(input('value of area'))
    pressure=force/area

    print('pressure',pressure)
calculate_pressure()


def calculate_resistance():
    potentialdifference=int(input('value of potentialdifference'))
    current = int(input('value of current'))
    resistance = potentialdifference/current

    print('resistance',resistance)
calculate_resistance()

def calculate_impulse():
    force = int(input('value of force'))
    time = int(input('value of time'))
    impulse = force*time

    print('impulse',impulse)
calculate_impulse()
