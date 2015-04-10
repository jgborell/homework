def isFloat(string): #needed ability to accept floats as speed see line 11
    try:
        float(string)
        return True
    except ValueError:
        return False
def fact_check():
    gallons = raw_input("How many gallons do you want?: ")
    if gallons.isdigit() and gallons is not "0":
        return gallons
    elif isFloat(gallons) and gallons is not "0":
        return gallons
    else:
        print "Reenter number of gallons, it must be a number > 0: "
    return fact_check()
gallons = fact_check()
gallons = str(gallons)
gallons = float(gallons)
liters = gallons * 3.7854
barrel = round(gallons / 19.5, 2)
co2 = gallons * 20
e_energy = 115 / 75.7 * gallons
cost = gallons * 4

print "You asked for %.2f gallons of gasoline." %(gallons)
print "That is %.2f liters." %(liters)
print "Which is %.2f barrels of oil." %(barrel)
print "This will release %.2f pounds of CO2" %(co2)
print "You will output the equivalent energy of %.2f ethanol gallons" %(e_energy)
print "This will cost you $%.2f " %(cost)