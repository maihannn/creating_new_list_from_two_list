# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

# Exercise 10: Create a new list from two two list using the following condition.

# Given 2 list.
list_1 = [12, 35, 47, 69, 80]
list_2 = [23, 40, 64, 86, 97]
new_list = []

def combined_list (list_1, list_2): 
    # Get odd numbers from 1st list.
    for i in list_1:
        if i % 2 !=0:
            new_list.append(i)

        # Get even numbers from the 2nd list.
    for i in list_2:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

# Display the new list.

print ("The new list is: ", combined_list(list_1, list_2))


