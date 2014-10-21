############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.


ongoing = True
while (ongoing == True):
    print 'Type your temperature'
    userinput = int(raw_input())
    print 'Have you been sick in the last 24 hours?'
    userinput2 = raw_input()
    print 'Have you been to West Africa recently?'
    userinput3 = raw_input()
    if userinput > 105:
        print 'You need to go to the hospital!'
    if userinput > 102 and userinput2 == 'yes':
        print 'You need to go to the hospital!'
    if userinput > 100 or userinput2 == 'yes' and userinput3 == 'yes':
        print 'You need to go to the hospital!'
        print 'Are there any more patients?'
        userinput4 = raw_input()
    print '--------------------------------------------'
    if userinput4 == 'no':
        ongoing = False

