import csv

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
Months = [1,2,3,4,5,6,7,8,9,10,11,12]
Years = [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]


def date():
    while True:
            user_inputDD = int(input ( " Please enter the day of the survey in the format DD : "))
        
            if user_inputDD in days:
                print()
                print("baba yaga")
                return user_inputDD
            else:
                print()
                print("Out of range")

def month(user_inputDD):
     while True:
         

        user_inputMM = int(input ( " Please enter the month of the survey in the format MM : "))
            
        if user_inputMM in Months:
            print()
            print("month")
            return user_inputMM
                
        else:
            print()
            print("Out of range")

    
def year (user_inputMM):
    while True:
        
        user_inputYYYY = int(input ( " Please enter the year of the survey in the format YYYY : "))
        if user_inputYYYY in Years:    
            if (user_inputYYYY % 4 == 0 and user_inputYYYY % 100 != 0) or (user_inputYYYY % 400 == 0):
                    
                print()
                print("leap year")
                return user_inputYYYY
            
            else:
                print()
                print("not a leap year")
                return user_inputYYYY
                    
        
        else:
            print()
            print("Out of range")

          
user_inputDD = date()
user_inputMM = month(user_inputDD)        
user_inputYYYY= year(user_inputMM)
        
