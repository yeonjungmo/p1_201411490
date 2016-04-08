"""
@author:YJM
@Date:20160408
"""

def FindingLeapYear():
    print "DO you want Leapyear, Please input year"
    year=raw_input("Input the year:")
    year=int(year)
    
    if(year%4 == 0) and (year % 100 !=0 or year % 400==0):
        res="LeapYear"
    else:
        res="NormalYear"
    print res



def SumOfMultiplesOf3_5():
    print "sumOfMultiplesOf3_5"
    
    Start=raw_input("Start your value")
    Finish=raw_input("Finish your value")
    Start=int(start)
    Finish=int(Finish)
    sum=0
    for i in range(Start,Finish):
       if i%3==0:
        sum+=i
       elif i%5==0:
        sum+=i
       elif i%15==0:
        sum-=i
    print sum



def Updown():
    print "Game start value up and down"
    while True:
       val = raw_input("check your value:")
       value = int(val)
       num = 80
       if(num<value):
           print "down"
       elif(num>value):
           print "up"
       else:
           print "bingo"
           break;
    

   
 

def lab6():
    FindingLeapYear()
    SumOfMultiplesOf3_5()
    Updown()

def main():
	lab6()

if __name__=="__main__":
	main()