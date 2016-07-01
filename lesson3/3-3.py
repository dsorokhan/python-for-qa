import datetime


print (datetime.datetime.strptime('11 Jan 2016', '%d %b %Y').date())
print (datetime.datetime.strptime('4 April 2011', '%d %B %Y').date())
print (datetime.datetime.strptime('11.03.2014', '%d.%m.%Y').date())
print (datetime.datetime.strptime('03/24/91', '%m/%d/%y').date())


