#  leep year
def isleapyear(year): 
  if(year%4==0andyear%100!=0)oryear%400==0:
    return True
  else:
    return False

year=2012

if lisleapyear(year):
  print('{} is a leap year.'. format(year))
else:
  print('{} is not a leap year.'.format( year)

