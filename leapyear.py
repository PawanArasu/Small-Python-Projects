import calendar

year = int(input('Year: '))
leap_year = calendar.isleap(year)

if leap_year:
    print('Its a Leap Year!!')
else:
    print('its not a leap Year')    

