'''This program is designed to parse movie titles into 3-letter codes'''
'''The 3 letter codes will then be compared to the hash table created in aaazzz in order to determine
x-coordinates for plotting'''

def turnTo3(movieTitle):
    '''Include code to remove the'''
    theRemoved=movieTitle.replace("the ","")
    theRemoved=movieTitle.replace("The ","")


    print(movieTitle)
    print(theRemoved)

    code=theRemoved[:3]
    print(code)


turnTo3("Finding Nemo")


