"""
Alena Hemminger
Application Development
August 26
Reviewing how to open and sort information in a list
"""

# create function
# here, we set the minimum of the list to the first number. 
# if the number we are iterating over is smaller than our current minimum, set that to the new minimum instead
def find_smallest(search_list):
    smallest = my_list[0]
    for number in my_list:
        if number < smallest:
            smallest = number 
    return smallest

# define the list that the content of the txt file will be added to 
my_list = []

# file is the name of this variable
with open("insertionSort.txt") as file:
    # this is to read in that file
    numbers = file.readline()
    
    # all of the content is stored in a string, so we have to split it so that
    # we can add each individual occurence as an item within the list
    split_numbers = numbers.split()
    
    for number in split_numbers:
        my_list.append(int(number))
    # ****
    
    sorted_list = []
    
    # as long as there is content within this list, we will continue to call the function 
    # that iterates over our list and then move the smallest from one list to another
    # after each full iteration in the function
    while len(my_list):
        
        # we call the function here, with the argument that we are using the list from the txt file
        smallest = find_smallest(my_list)
        
        # once we run through the list, whatever the minimum is, it is removed from that list and added to our sorted list instead
        my_list.remove(smallest)
        sorted_list.append(smallest)
        
        print("Old list:" + str(my_list))
        print("New list:" + str(sorted_list))