def isFloat(string): #needed ability to accept floats as speed see line 11
    try:
        float(string)
        return True
    except ValueError:
        return False
def fact_check():
    speed = raw_input("Enter a speed in miles per hour: ")
    if speed.isdigit() and speed is not "0":
        return speed
    elif isFloat(speed) and speed is not "0":
        return speed
    else:
        print "Reenter speed, it must be a number > 0: "
    return fact_check()
speed = float(fact_check())
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