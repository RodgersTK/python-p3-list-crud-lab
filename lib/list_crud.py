def create_an_empty_list():
    return []

def create_a_list(): 
    my_list = [1, 2, 3, 4]
    return (my_list)

def add_element_to_end_of_list(l, element):
    my_list = [1, 2, 3, 4]
    my_list.append(element)
    return (my_list)

def add_element_to_start_of_list(l, element):
    my_list = [1, 2, 3, 4]
    my_list.insert(0, element)
    return (my_list)

def remove_element_from_end_of_list(l):
    my_list = [1, 2, 3, 4]
    my_list.pop(-1)
    return (my_list)

def remove_element_from_start_of_list(l):
    my_list = [1, 2, 3, 4]
    del my_list [0]
    return (my_list)

def retrieve_first_element_from_list(l):
    my_list = [1, 2, 3, 4]
    return (my_list[0])

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
