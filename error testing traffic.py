import csv

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

Years = [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]

dictionary = { 1: 31, 2:28, 3:31,4:30 ,5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}    
            
    
while True:
    
    try:
        user_inputYYYY = int(input ( " Please enter the year of the survey in the format YYYY : "))
        
        if 2002 <= user_inputYYYY <= 2024:
            
            if (user_inputYYYY % 4 == 0 and user_inputYYYY % 100 != 0) or (user_inputYYYY % 400 == 0):
                    
                print()
                print("leap year")
                
                break            
            else:
                print()
                print("not a leap year")
                break
                
                    
        
        else:
            print()
            print("Out of range")
                
    except ValueError:
             
            print("Invalid input! Please enter an integer.")
            
while True:
    
         
    try:
        
        
        user_inputMM = int(input ( " Please enter the month of the survey in the format MM : "))
            
        if 1 <= user_inputMM <= 12:
            
            print()
            print("month")
            
            if (user_inputYYYY % 4 == 0 and user_inputYYYY % 100 != 0) or (user_inputYYYY % 400 == 0):
                dictionary.update({2:29})
                break
            
            break    
        else:
            print()
            print("Out of range")
                
    except ValueError:
             
        print("Invalid input! Please enter an integer.")
        
while True:    
    try:
        
            
        user_inputDD = int(input ( " Please enter the day of the survey in the format DD : "))
        
        if 1 <= user_inputMM <= 31:
            print()
            print("baba yaga")
            
            break
                
        else:
            print()
            print("Out of range")
                
    except ValueError:
            print("Invalid input! Please enter an integer.")


    

