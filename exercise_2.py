gallons = float(raw_input("How many gallons do you require? "))
liters = gallons * 3.7854
barrel = 19.5 / gallons
co2 = gallons * 20
e_energy = 115 / 75.7 * gallons
cost = gallons * 4

print "You asked for %.2f gallons of gasoline." %(gallons)
print "That is %.2f liters." %(liters)
print "Which is %.2f barrels of oil." %(barrel)
print "This will release %.2f pounds of CO2" %(co2)
print "You will output the equivalent energy of %.2f ethanol gallons" %(e_energy)
print "This will cost you $%.2f " %(cost)