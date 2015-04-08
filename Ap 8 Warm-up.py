""" def sleep_in(weekday, vacation):
    if weekday == True and vacation == False:
        print False
        return False
    else:
        print True
        return True
sleep_in(False, False)
sleep_in(True, False)
sleep_in(False, True) """

def sleep_in(weekday, vacation):
    return vacation or not weekday
print sleep_in(False, False)
print sleep_in(True, False)
print sleep_in(False, True)