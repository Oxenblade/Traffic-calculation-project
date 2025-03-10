import csv

filename = "traffic_data15062024.csv"

with open (filename, "r" ) as traffic:
    
    csv_reader = csv.reader(traffic)
    
    headerline = next(traffic)
    My_list = []
    My_second_list =[]
    New_list=[]
    Vehicles=[]
    My_third_list=[]
    My_fouth_list=[]
    Time_list= []
    for i in csv_reader:
        Time_list.append(i[2])

print(Time_list.count(12))

















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


    
