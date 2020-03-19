x=0
print('Enter ur current attendance in round figure.Example if ur attendance is 78.19 or 78.9 then enter 78')
res=int(input())
print('Enter total no. of classes attended and total no. of classes held ')
classes_attended=int(input())
classes_held=int(input())
print('Enter how much percentage you want to achieve ')
percentage=int(input())
while int(res)<percentage:
    x=x+1
    res=100*((classes_attended+x)/(classes_held+x))
print('No. of classes to attend to get',percentage,'%','attendance is ',x)
