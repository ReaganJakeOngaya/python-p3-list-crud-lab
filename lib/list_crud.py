def create_an_empty_list():
    return []

empty_list = create_an_empty_list()

print(empty_list)

def create_a_list():
    return ["name", "gender", "height", "nationality"]

my_list = create_a_list()

print(my_list)

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

one_list = ['apple', 'banana', 'cherry']

new_list =  add_element_to_end_of_list(one_list, "mango")
print(new_list)

def add_element_to_start_of_list(l, element):
    l.insert( 0, element)
    return l

shoe_list = ['Nike', 'Reebox', 'Adidas']

new_shoes =  add_element_to_start_of_list(shoe_list, "Jordans")
print(new_shoes)

def remove_element_from_end_of_list(l):
    l.pop()
    return l
favourite_songs = ['Runaway by Breezy', 'Desesperados by Rauw ', 'Mia by Bad Bunny']
new_songs = remove_element_from_end_of_list(favourite_songs)
print(new_songs)

def remove_element_from_start_of_list(l):
    if l:
        del l[0]
    return l

my_albums =['11:11 by Breezy', 'Indigo by Breezy', 'Its only me by Lil Baby']
new_albums = remove_element_from_start_of_list(my_albums)
print(new_albums)


def retrieve_first_element_from_list(l):
    return l[0]
my_artists = ['Breezy', 'Polo G', 'Rauw' , 'Jimin', 'Jack Harlow']
new_artists = retrieve_first_element_from_list(my_artists) 
print(new_artists)

def retrieve_element_from_index(l, index):
        return l[index]
my_artists = ['Breezy', 'Polo G', 'Rauw' , 'Jimin', 'Jack Harlow']
new_artists = retrieve_element_from_index(my_artists , 3) 
print(new_artists)

def retrieve_last_element_from_list(l):
        return l[-1]
my_artists = ['Breezy', 'Polo G', 'Rauw' , 'Jimin', 'Jack Harlow']
new_artists = retrieve_last_element_from_list(my_artists) 
print(new_artists)
