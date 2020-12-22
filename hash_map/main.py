from h_map import *
import csv


#****READ THE CSV FILE OF THE MONTH JANUARY**********************************
movie_data_set = Graph()
with open('movie_dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            movie = row[0]
            performer_1 = row[1]
            performer_2 = row[2]
            director = row[3]
            movie_data_set.add_performer(performer_1)
            movie_data_set.add_performer(performer_2)
            line_count += 1
    print(f'Processed {line_count} lines.')
#*****FILLING THE MOVIES*****************************
with open('movie_dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            movie = row[0]
            performer_1 = row[1]
            performer_2 = row[2]
            director = row[3]
            movie_data_set.add_edge(movie,performer_1,performer_2,director)
            line_count += 1
    print(f'Processed {line_count} lines.')
#******DECISION MENU**************************
decision = -1
print("****Welcome to Movie Data Set****\n")
print("Select an Option: ")
print("1- See movies of a performer")
print("2- Delete performers who directed the movie in which s/he played")
print("3- Find performer(s) who played in highest number of movies")
print("4- Find performer(s) who played in highest number of movies with a given performer")
print("5- Find director(s) who directed highest number of movies of a given performer")
print("6- Exit")
#*****************USAGE OF THE HASH MAP
while True:
    decision = int(input("Select an Option: "))
    if decision == 1:
        performer_name = input("Select which actor/actress's movies you'd like to view: ")
        movie_list = movie_data_set.get_movies(str(performer_name))
        print(movie_list)
    elif decision == 2:
        movie_data_set.delete_performers()
        print("The director performers have been deleted")
    elif decision == 3:
        most_active_performers = movie_data_set.get_most_active_performers()
        print(most_active_performers)
    elif decision == 4:
        performer_name = input("Select which actor/actress's movies you'd like to view: ")
        freq_part = {}
        freq_part = movie_data_set.get_frequent_partner(str(performer_name))
        print(freq_part)
    elif decision == 5:
        performer_name = input("Select which actor/actress's director that he/she has worked the most you'd like to view: ")
        freq_dict = movie_data_set.get_frequent_director(str(performer_name))
        print(freq_dict)
    elif decision == 6:
        break
    else:
        print("Please enter between 1 and 6")
#**************USAGE OF THE HASH MAP********************