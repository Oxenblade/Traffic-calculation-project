import csv

filename = "traffic_data15062024.csv"

with open (filename, "r" ) as traffic:
    
    csv_reader = csv.reader(traffic)


    #first initialization - Initial comments 
    
    headerline = next(traffic)
    My_list = []
    My_second_list =[]
    New_list=[]
    Vehicles=[]
    My_third_list=[]
    My_fouth_list=[]
    Time_list_1= []
    Time_list_2= []
    Time_list_3= []
    Time_list_4= []
    Time_list_5= []
    Time_list_6= []
    Time_list_7= []
    Time_list_8= []
    Time_list_9= []
    Time_list_10= []
    Time_list_11= []
    Time_list_12= []
    Time_list_13= []
    Time_list_14= []
    Time_list_15= []
    Time_list_16= []
    Time_list_17= []
    Time_list_18= []
    Time_list_19= []
    Time_list_20= []
    Time_list_21= []
    Time_list_22= []
    Time_list_23= []
    Time_list_24= []

    Total_Time_list=[]
    
    for i in csv_reader:
        My_list.append(i[8])
        My_second_list.append(i[9])
        
        if ( i[0] == "Elm Avenue/Rabbit Road" and i[4] == "N"):
            New_list.append(i[8])
        if  i[6]< i[7]:
            Vehicles.append(i[8])
        if i[0] == "Elm Avenue/Rabbit Road":
            My_third_list.append(i[8])
        if i[0] == "Hanley Highway/Westway":
            My_fouth_list.append(i[8])
            
        if (i[2]>= "0:00:00" and i[2]<= "1:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "1:00:00" and i[2]<= "2:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "2:00:00" and i[2]<= "3:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "3:00:00" and i[2]<= "4:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "4:00:00" and i[2]<= "5:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "5:00:00" and i[2]<= "6:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "6:00:00" and i[2]<= "7:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "7:00:00" and i[2]<= "8:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "8:00:00" and i[2]<= "9:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "9:00:00" and i[2]<= "10:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "10:00:00" and i[2]<= "11:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "11:00:00" and i[2]<= "12:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "12:00:00" and i[2]<= "13:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "13:00:00" and i[2]<= "14:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "14:00:00" and i[2]<= "15:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "15:00:00" and i[2]<= "16:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "16:00:00" and i[2]<= "17:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "17:00:00" and i[2]<= "18:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "18:00:00" and i[2]<= "19:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "19:00:00" and i[2]<= "20:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "20:00:00" and i[2]<= "21:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "21:00:00" and i[2]<= "22:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "22:00:00" and i[2]<= "23:00:00") and (i[0] == "Hanley Highway/Westway") :
            Total_Time_list.append([len(i[8])])
        if (i[2]>= "23:00:00" and i[2]<= "0:00:00") and (i[0] == "") :
            Total_Time_list.append([len(i[8])])
            

    #calculations        
    two_wheel_vechicles = My_list.count("Bicycle"), My_list.count ("Motorcycle"), My_list.count("Scooter")
    
    number =  My_list.count("Truck")/ len(My_list)
    Percentage = "{:.0%}".format(number)
    average_number = My_list.count("Bicycle")/ 24
    percentage_of_scooters = My_third_list.count("Scooter")/ len(My_third_list)
    percentage_value_of_scooters = "{:.0%}".format(percentage_of_scooters)
    
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

print(Total_Time_list)












#Commented out code 




''''import csv

filename = "traffic_data15062024.csv"

with open (filename, "r" ) as traffic:
    csv_reader = csv.reader(traffic)

    header = next(csv_reader)
    print("header:", header)
    My_list=[]


    for row in csv_reader:
        #row = row.rstrip()
        #row = row.replace('',"")
        #row = row.split(',')
        My_list.append(row[8])
        
        #print("row:",row[8])
print(My_list.count("Truck"))
        #print(row[8].count("Truck"))




import csv


filename = "traffic_data15062024.csv"

with open(filename, "r") as traffic:
    csv_reader = csv.reader(traffic)

    header = next(csv_reader)


    My_list = []
    truck_count = 0

    for i in csv_reader:
        if len(i) > 8: 
            My_list.append(i[8])
            if i[8].strip() == "Truck":
                truck_count += 1

    print("Total count of 'Truck':", truck_count)

    My_second_list = []
    electric_vechiles = 0

    for row in csv_reader:
        if len(row)> 8:
            My_second_list.append(row[8])

            if row[9].strip()== True:
                electric_vechiles += 1
    print("Total count of Electrical Vechiles:", electric_vechiles)

    My_third_list = []
    two_wheel_vechicles = 0

    for row in csv_reader:
        if len(row)> 8:
            My_third_list.append(row[8])

            if row[8].strip()== "Bicycle":
                two_wheel_vechicles += 1
    print("Total count of two wheel vechicles:", two_wheel_vechicles)'''


    
