from graph import *
import csv
routes = [
        ("Ankara","Istanbul"),
        ("Istanbul","Gent"),
        ("Gent","Paris"),
        ("Istanbul","Paris"),
        ("Istanbul","Koala Lumpur"),
        ("Paris","New York"),
        ("Paris","Sacramento"),

    ]
 
#GETTING DATA FROM CSV
with open('path_set.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader_2 = csv.reader(csv_file,delimiter=',')
    line_count = 0
    line_count_2 = 1
    for row in csv_reader:
        if line_count == 0:
            line_count +=1
        else:
            routes.append((row[0],row[1]))
            line_count += 1
    print(f'Processed {line_count} lines.')

route_graph = Graph(routes)  
print("Welcome to Flight Track!")
while True:
    print("------------------------")
    print("Select an Option")
    print("1---See All the flights from one city to another")
    print("2---See the Shortest Path from one city to another")
    print("3---Exit the Program")
    selection = int(input(":"))
    if selection == 1:
        print("-----------THIS IS FOR GETTING THE PATH---------")
        path_from = input("Select the takeoff point:")
        path_to = input("Select the destination:")
        print(f"Paths between {path_from} and {path_to} : ",route_graph.get_paths(path_from,path_to))
    elif selection == 2:
        print("---------THIS IS FOR GETTING THE SHORTEST PATH------------")
        path_from = input("Select the takeoff point:")
        path_to = input("Select the destination:")
        print(f"Paths between {path_from} and {path_to} : ",route_graph.get_shortest_path(path_from,path_to))
    elif selection == 3:
        break
    else:
        print("Please select an option between 1 and 3")
