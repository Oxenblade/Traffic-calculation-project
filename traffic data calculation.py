import csv

filename = "traffic_data21062024.csv" # open karanawa csv file eka

with open (filename, "r" ) as traffic:
    
    csv_reader = csv.reader(traffic)
    
    headerline = next(traffic) # csv file eke heading api skip karanawa
    My_list = []
    My_second_list =[]
    New_list=[]
    Vehicles=[]
    My_third_list=[]
    My_fouth_list=[]

    Total_Time_list=[]
    rain_hours_list=[] # meka rain eke hours string widiyata append karanna hadapu ekak
    

    count = 0 # meka api ganne total rain hours hoyanna

    
    for i in csv_reader:
        My_list.append(i[8])
        My_second_list.append(i[9])

  # meka vechicle calculation ekata adala if conditions   
        if ( i[0] == "Elm Avenue/Rabbit Road" and i[4] == "N"):
            New_list.append(i[8])
        if  i[6]< i[7]:
            Vehicles.append(i[8])
        if i[0] == "Elm Avenue/Rabbit Road":
            My_third_list.append(i[8])
        if i[0] == "Hanley Highway/Westway":
            My_fouth_list.append(i[8])

        if i[0] == "Hanley Highway/Westway":
            Total_Time_list.append(i[2][0:2])

  # rain eka calculate karana if statement 2:
        if i[5] == "Heavy Rain":
            rain_hours_list.append(i[2][0:2])    
        if i[5] == "Light Rain":
            rain_hours_list.append(i[2][0:2])
            
   # meka vechicle calculation ekata adala list specifically total vechicles gana hoyanna:
            
    Total_Vehicle_list = [ Total_Time_list.count("0:"),
            Total_Time_list.count("00"),            
            Total_Time_list.count("01"),
            Total_Time_list.count("02"),
            Total_Time_list.count("03"),
            Total_Time_list.count("04"),
            Total_Time_list.count("05"),
            Total_Time_list.count("06"),
            Total_Time_list.count("07"),
            Total_Time_list.count("08"),
            Total_Time_list.count("09"),
            Total_Time_list.count("10"),
            Total_Time_list.count("11"),
            Total_Time_list.count("12"),
            Total_Time_list.count("13"),
            Total_Time_list.count("14"),
            Total_Time_list.count("15"),
            Total_Time_list.count("16"),
            Total_Time_list.count("17"),
            Total_Time_list.count("18"),
            Total_Time_list.count("19"),
            Total_Time_list.count("20"),
            Total_Time_list.count("21"),
            Total_Time_list.count("22"),
            Total_Time_list.count("23"),
            Total_Time_list.count("24")]
    
    # meka total rain hours gana hoyanna hadapu list ekak, meken ara repeated strings count karanawa:
    
    total_rain_hours = [ rain_hours_list.count("0:"),
            rain_hours_list.count("00"),            
            rain_hours_list.count("01"),
            rain_hours_list.count("02"),
            rain_hours_list.count("03"),
            rain_hours_list.count("04"),
            rain_hours_list.count("05"),
            rain_hours_list.count("06"),
            rain_hours_list.count("07"),
            rain_hours_list.count("08"),
            rain_hours_list.count("09"),
            rain_hours_list.count("10"),
            rain_hours_list.count("11"),
            rain_hours_list.count("12"),
            rain_hours_list.count("14"),
            rain_hours_list.count("15"),
            rain_hours_list.count("16"),
            rain_hours_list.count("17"),
            rain_hours_list.count("18"),
            rain_hours_list.count("19"),
            rain_hours_list.count("20"),
            rain_hours_list.count("21"),
            rain_hours_list.count("22"),
            rain_hours_list.count("23"),
            rain_hours_list.count("24")]

    # me for loop eken wenne uda thiyena repeated strings calculated karala +1 ekak denawa count ekata list eke eka index ekaka value eka 1ta wada wadinam:
    for i in total_rain_hours:
        if i >1:
            count += 1

    # me thiyenne vechicle calculation ekata adala variebles and maths calculations        
    two_wheel_vechicles = My_list.count("Bicycle"), My_list.count ("Motorcycle"), My_list.count("Scooter")
    
    number =  My_list.count("Truck")/ len(My_list)
    Percentage = "{:.0%}".format(number)
    average_number = My_list.count("Bicycle")/ 24
    percentage_of_scooters = My_third_list.count("Scooter")/ len(My_third_list)
    percentage_value_of_scooters = "{:.0%}".format(percentage_of_scooters)


# me okkoma print karanawa details

print(len(My_list))
print(My_second_list.count("TRUE"))
print(My_list.count("Truck"))
print(sum(two_wheel_vechicles))

print(New_list.count("Buss"))

print(Percentage)
print(round(average_number))
print(len(Vehicles))
print(len(My_third_list))
print(len(My_fouth_list))
print(percentage_value_of_scooters)

print(max(Total_Vehicle_list))

print(count)









    
