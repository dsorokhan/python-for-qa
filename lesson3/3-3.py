import datetime


s = '11.03.2014'

#print (datetime.datetime.strptime('11 Jan 2016',  '%d %b %Y').date())
#print (datetime.datetime.strptime('4 April 2011', '%d %B %Y').date())
#print (datetime.datetime.strptime('11.03.2014',   '%d.%m.%Y').date())
#print (datetime.datetime.strptime('03/24/91',     '%m/%d/%y').date())

for item in ('%d %b %Y', '%d %B %Y', '%d.%m.%Y', '%m/%d/%y'):
    try:
        d = datetime.datetime.strptime(s, item).date()
    except ValueError:
        d = None
    if d != None:
        break

if d == None:
    print ('Incorrect input date format')
else:
    print (d)


