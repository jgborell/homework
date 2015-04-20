import re
from temp_conv import cel_to_feh, feh_to_cel

city_temperature = {"Boston" : "0 C", "Boise" : "48 F", "Phoenix" : "85 F",
                    "Miami" : "40 C", "Riverside" : "30 C", "Baltimore" : "32 F"}

def conv_temps(list_name):
    for item in city_temperature.items():
        if 'C' in item[1]:
            temp = cel_to_feh(int(''.join(re.findall("[-+]?\d+[\.]?\d*", item[1]))))
            print "In %s it is %s Celsius, \n\t which is equivalent to %s degrees Fahrenheit" % (item[0], item[1], temp)
        else:
            temp = feh_to_cel(int(''.join(re.findall("[-+]?\d+[\.]?\d*", item[1]))))
            print "In %s it is %s Celsius, \n\t which is equivalent to %s degrees Fahrenheit" % (item[0], item[1], temp)


conv_temps(city_temperature)