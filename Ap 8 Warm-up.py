def sleep_in(weekday, vacation):
    if weekday == True and vacation == False:
        print False
        return False
    else:
        print True
        return True
sleep_in(False, False)
sleep_in(True, False)
sleep_in(False, True)