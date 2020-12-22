#FOR IMPORT

class Node: 
    def __init__(self, name,movie,director): 
        self.name = name
        self.movie = movie
        self.director = director 
#** An adjacency list representation of an undirected graph.
class Graph(object):

    #CONSTRUCTOR
    def __init__(self):
        self.graph = {}

    #FUNCTIONS
    #***Adds a new performer to the map with performerName
    #as key, and an empty node list as value****************
    def add_performer(self,performer_name):
        self.graph[performer_name] = []
    #** Adds a new node to the list of performer1
    #* using performer2, movieTitle and director data, and
    #* adds a new node to the list of performer2
    #* using performer1, movieTitle and director data. */
    def add_edge(self,movie_title,performer1,performer2,director):
        new_node_performer1 = Node(performer1,movie_title,director)
        new_node_performer2 = Node(performer2,movie_title,director)
        self.graph[performer1].append(new_node_performer1)
        self.graph[performer2].append(new_node_performer2)


    #** Given a performer name, returns all movies
    #* in which the performer performed as a list of string.
    def get_movies(self,performer_name):
        x = []

        if not performer_name in self.graph.keys():
            return
            
        for value in self.graph[performerName]:
            x.append(value.movie)
        return x


    #** Deletes all performers who played in a movie
    #* directed by himself/herself from the graph and returns
    #* those performers as a list of string.
    def delete_performers(self):
        director_performers = []
        
        for key,value in self.graph.items():
            for i in range(len(value)):
                if key == value[i].director:
                    if key not in director_performers:
                        director_performers.append(key)

        for i in range(len(director_performers)):
            self.graph.pop(director_performers[i])

        return director_performers

    #** Returns performer(s) who played highest number of movies
    #* as a map where performer name is key and
    #* the number of movies is value. */
    def get_most_active_performers(self):
        most_active_performers = {}
        maximum = -1
        max_performer = ""
        for key,value in self.graph.items():
            if(len(value) >= maximum):
                maximum = len(value)
                max_performer = key
        print(max_performer)
        print(maximum)
        most_active_performers[max_performer] = []
        for value in self.graph[max_performer]:
            most_active_performers[max_performer].append(value.movie)
        return most_active_performers

    #** Given a performer name, returns his/her most frequent
    #* partners as a map where the performer name is key
    #* and the number of movies they played together is value
    def get_frequent_partner(self,performer_name):

        if not performer_name in self.graph.keys():
            print("There is not a performer in that name\n")
            return

        freq_partners = {}
        movie_list = self.get_movies(performer_name)
        partner_movies = {}
        maximum  = -1
        movie_counter = 0
        #print(movie_list)
        #GETTING THE PARTNERS
        for key,value in self.graph.items():
            if key != performer_name:
                performer_movie_list = set(self.get_movies(key))
                intersect_movie_list = performer_movie_list.intersection(movie_list)
                if(len(intersect_movie_list) > 0):
                    maximum = max(maximum,len(intersect_movie_list))
                    #print(key,"-",len(intersect_movie_list))
                    partner_movies[key] = list(intersect_movie_list)
        #print(partner_movies)
        for key,value in partner_movies.items():
            if(len(value) == maximum):
                freq_partners[key] = value
        #print(freq_partners)
        return freq_partners
        

        


    #** Given a performer name, returns his/her most frequent
    #* director as a map where the director name is key
    #* and the number of movies they were together is value
    def get_frequent_director(self,performer_name):

        if not performer_name in self.graph.keys():
            print("There is not a performer in that name\n")
            return
        performer_director = {}
        director_list = []
        for value in self.graph[performer_name]:
            director_list.append(value.director)
        freq_director = max(set(director_list), key = director_list.count) 
        performer_director[performer_name] = freq_director
        return performer_director

