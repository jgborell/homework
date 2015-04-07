int_1 = int(raw_input("Please enter the first integer: "))
int_2 = int(raw_input("Please enter the second integer: "))
addition = int_1 + int_2
diff = int_1 - int_2
prod = int_1 * int_2
quot = int_1 / int_2
mod = int_1 % int_2

print "The sum of %i and %i is: %i" % (int_1, int_2, addition)
print "The difference of %i and %i is: %i" % (int_1, int_2, diff)
print "The product of %i and %i is: %i" % (int_1, int_2, prod)
print "The quotient of %i and %i is: %i with remainder %i" %(int_1, int_2, quot, mod)