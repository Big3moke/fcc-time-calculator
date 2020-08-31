
def add_time(start, duration):
##convert to decimal
    if start.find('PM') != -1:
        locationIndic = start.find('PM')
        locationComma = start.find(':')
        numberWhole = float(start[:locationComma].replace(':','.'))
        numberDecim = float(start[locationComma:locationIndic].replace(':','.'))
        decimToB10 = numberDecim / 0.6
        number = decimToB10 + numberWhole
        # print(number)

    elif start.find('AM') != -1:
        locationIndic = start.find('AM')
        locationComma = start.find(':')
        numberWhole = float(start[:locationComma].replace(':','.'))
        numberDecim = float(start[locationComma:locationIndic].replace(':','.'))
        decimToB10 = numberDecim / 0.6
        number = decimToB10 + numberWhole
        # print(number)

    durLocIndic = duration.find(':')
    durWhole = float(duration[:durLocIndic].replace(':', '.'))
    durDecim = float(duration[durLocIndic:].replace(':', '.'))/0.6
    dur = durWhole + durDecim
    # print(durDecim)


    add = number + dur
    print(add)
    # print(add)

    if add < 12.00:
        whole = str(add).find('.')
        wholeDecim = str(add)[whole:]
        wholeNummy = str(add)[:whole]
        # print(wholeNummy)
        convToHr = (float(wholeDecim) * 0.6) + float(wholeNummy)
        convToHr = str(convToHr).replace('.',':')
        new_time = (convToHr + ' AM')

    elif add < 24.00:
        whole = str(add).find('.')
        wholeDecim = str(add)[whole:]
        wholeNummy = str(add-12)[:whole]
        # print(wholeNummy)
        convToHr = round((float(wholeDecim) * 0.6) + float(wholeNummy), 2)
        convToHr = str(convToHr).replace('.',':')
        new_time = (convToHr + ' PM')

    elif add > 24.00:
        dayz = round(add/24)
        hourz= add%24
        print(dayz)
        print(hourz)

        if hourz < 12.00:
            str(hourz).
        # elif hourz < 24.00:


    # return new_time
