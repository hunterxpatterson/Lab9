############################################
#                                          # 
#                   85pt                   #
#             Who has a fever?             #
############################################

# Create a for loop that will search through temperatureList
# and create a new list that includes only numbers greater than 100

myList = [102,98,96,101,100,99,103,97,98,105]
myList2 = []
# Insert for loop here
for x in myList:
    print x
    if x > 100:
        myList2.append(x)

# This should print [102,101,103,105]
print myList2
