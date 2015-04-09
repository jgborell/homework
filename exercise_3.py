def get_input(message):
    user_input = str(input(message))
    if user_input.isdigit() and not 0:
        return user_input
    elif user_input == 0:
        print("Do not use 0")
    return None

speed = None

while speed is None:
    speed = float(get_input("Please enter a speed in miles/hour: "))

meters_mile = 1609.34
meters_hour = speed * meters_mile
barleycorns_day = meters_hour * 117.647 * 24
furlongs = meters_hour / 201.168
fortnight = furlongs * 24 * 14
mach = meters_hour / ((1130 * 60 * 60) / 3.28084)
speed_light = meters_hour/(299792458 * 60 * 60)




print "Original speed in mph is: {}" .format(speed)
print "Converted to barleycorn/day is: {}" .format(barleycorns_day)
print "Converted to furlong/fortnights is: {}" .format(fortnight)
print "Converted to Mach number is: {}" .format(mach)
print "Converted to the percentage of the speed of light is: {}" .format(speed_light)
print "Thanks for playing"