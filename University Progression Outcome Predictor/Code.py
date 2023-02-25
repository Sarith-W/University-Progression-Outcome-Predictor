#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID: w1912785 / 20210010
#Date: 27.03.2022

#Defining functions
def option_menu():
    "This function is to get the user input version to continue the program"
    global version_option
    version_option = 0   #Initializing the 'version_option' variable to '0'
    print("\nYou have 3 options:\n\tOption 1 - Student Version\n\tOption 2 - Staff Version\n\tOption 3 - Quit the program\n")
    try:
        version_option = int(input("Enter your option number (1/2/3) : "))
        if not 1 <= version_option <= 3:
            print("Invalid Input! The option can only be 1,2 or 3!\n")  #validating the range           
    except ValueError:
        print("Invalid Input! Please enter a number only!\n")    #validating the data type
#____________________________________________________________________________________________

def validation(Pass,defer,fail):
    "This function is to validate the input data type and range of the main_process function"
    global error
    #Storing the ranges in a list
    ranges = [0,20,40,60,80,100,120]

    #Validating the data type
    try:
        int(Pass)
        int(defer)
        int(fail)
        error = False    #If an error occurs, it becomes 'True'
    except ValueError:
        print("Invalid Input! Integer required!\n")
        error = True
        return error

    #Validating the range
    if int(Pass) not in ranges or int(defer) not in ranges or int(fail) not in ranges:
        print("Invalid Input! Out of range!\n")
        error = True
        return error
#____________________________________________________________________________________________

def main_process():
    "This function contains the main version of the program"
    #Getting user input for the number of credits at Pass, defer and fail
    global progress_histro, trailer_histro, retriever_histro, exclude_histro, Pass, defer, fail

    while True:
        #Initializing the Pass, defer and fail values to '0'
        Pass = 0
        defer = 0
        fail = 0

        #Getting the user inputs and validating
        Pass = input("Please enter your credits at pass : ")
        validation(Pass,defer,fail)
        if error:         #If error is 'True', then the loop continues from the begining
            continue
        defer = input("Please enter your credits at defer : ")
        validation(Pass,defer,fail)
        if error:
            continue
        fail = input("Please enter your credits at fail : ")
        validation(Pass,defer,fail)
        if error:
            continue

        #Type casting the user inputs to integar
        Pass = int(Pass)
        defer = int(defer)
        fail = int(fail)
    
        #Validating the total of credits
        if Pass + defer + fail != 120:
            print("Total incorrect!\n")
        
        #Store the user inputs in a tuple
        credit = (Pass,defer,fail)

        #Process of deciding the Progression Outcome
        if Pass == 120 and defer == 0 and fail == 0:
            print("Progress\n")
            progress_histro += 1     #Count of the progress increased by 1
            progress_store.append(credit)
        
        elif credit in trailer:
            print("Progress (module trailer)\n")
            trailer_histro += 1         #Count of the trailer increased by 1
            trailer_store.append(credit)

        elif credit in retriever:
            print("Module retriever\n")
            retriever_histro += 1         #Count of the retriever increased by 1
            retriever_store.append(credit)

        elif credit in exclude:
            print("Exclude\n")
            exclude_histro += 1         ##Count of the exclude increased by 1
            exclude_store.append(credit)
        break
#____________________________________________________________________________________________

def process_loop():
    "This function appears only in the staff version and asks from the user whether to continue the main_process or not"
    while True:
        #Getting user input to continue the program
        print("Would you like to enter another set of data?")
        choice = input("Enter 'y' for yes or 'q' to quit and view results : ")
        print("\n")

        #Deciding whether to continue or to quit the program
        if choice == "y":
            main_process()
        elif choice == "q":
            while True:
                #Displaying an option menu to display data
                print("Option menu to display data:\n\t1 - Horizontal Histogram\n\t2 - Vertical Histogram\n\t3 - Progression Data List\n\t4 - Text File\n")

                #Getting the user option number and validating
                try:
                    menu_option = int(input("Enter the option number (1/2/3/4) : "))
                    if not 1 <= menu_option <= 4:
                        print("Invalid Input! The input can only be 1, 2, 3 or 4!\nPlease Try Again!\n")    #Validating the range
                        continue
                except ValueError:
                    print("Invalid Input! Please enter a number and Try Again!\n")      #Validating the data type
                    continue
                break

            #Deciding how to display the data based on the user option
            if menu_option == 1:
                horizontal_histogram()
            elif menu_option == 2:
                vertical_histogram(progress_histro,trailer_histro,retriever_histro,exclude_histro)
            elif menu_option == 3:
                progression_data()
            else:
                text_file()
            break
        else:
            print("Invalid Input! Please try again!\n")
            continue
#____________________________________________________________________________________________
        
def horizontal_histogram():
    "This function is to display the horizontal histogram in the staff version"
    print("------------------------------------------------------------------------------\n")
    #Displaying the horizontal histogram
    print("Horizontal Histogram\n")
    print("Progress",progress_histro," :","*"*progress_histro)        #Multiplying a '*' sign by the count of each progression outcome to get the Horizontal Histogram
    print("Trailer",trailer_histro,"  :","*"*trailer_histro)               
    print("Retriever",retriever_histro,":","*"*retriever_histro)
    print("Excluded",exclude_histro," :","*"*exclude_histro)
    total = progress_histro+trailer_histro+retriever_histro+exclude_histro
    print("\n",total,"outcomes in total\n\n") 
#____________________________________________________________________________________________

def vertical_histogram(progress_histro,trailer_histro,retriever_histro,exclude_histro):
    "This function is to display the vertical histogram in the staff version"
    print("------------------------------------------------------------------------------\n")
    #Displaying the vertical histogram
    print("\nVertical Histogram\n")
    total = progress_histro+trailer_histro+retriever_histro+exclude_histro

    #Displaying the names of the progression outcomes horizontally
    print("Progress",progress_histro,"| Trailer",trailer_histro,"| Retriever",retriever_histro,"| Excluded",exclude_histro)

    #This for loop displays the stars line by line (horizontally) based on the count of each progression outcome
    #Each excecution round of this for loop equals to a one line
    for i in range(max(progress_histro,trailer_histro,retriever_histro,exclude_histro)):  #Using the 'max()' function to get the highest count as the range
        if progress_histro != 0:
            print("     *",end="")
            progress_histro -= 1      #Printing a star and reducing the progress count by 1 until it becomes zero(0)
        print("\t\t",end="")
    
        if trailer_histro != 0:
            print("*",end="")
            trailer_histro -= 1      #Printing a star and reducing the trailer count by 1 until it becomes zero(0)
        print("\t",end="")
    
        if retriever_histro != 0:
            print("     *",end="")
            retriever_histro -= 1       #Printing a star and reducing the retriever count by 1 until it becomes zero(0)
        print("\t\t",end="")
    
        if exclude_histro != 0:
            print("   *")
            exclude_histro -= 1      #Printing a star and reducing the exclude count by 1 until it becomes zero(0)
        print("\n")

    print(total,"outcomes in total\n\n")
    
#____________________________________________________________________________________________
    
def progression_data():
    "This function is to display the input progression data list in the staff version"
    print("------------------------------------------------------------------------------\n")
    print("Progression Data List\n")
    #Displaying progress inputs stored in the progress_store list
    for i in progress_store:
        print("Progress -",*i)

    #Displaying trailer inputs stored in the trailer_store list
    for i in trailer_store:
        print("Trailer -",*i)

    #Displaying retriever inputs stored in the retriever_store list
    for i in retriever_store:
        print("Retriever -",*i)

    #Displaying exclude inputs stored in the exclude_store list
    for i in exclude_store:
        print("Exclude -",*i)   
#____________________________________________________________________________________________

def text_file():
    "This function is to save the input progression data list in a text file and to read the text file"
    #Creating a text file
    fo = open("inputs.txt","w")

    #Accessing progress inputs stored in the progress_store list
    for tuples in progress_store:
        
        #Displaying it in a text file
        fo.write("Progress - ")
    
        #Accessing each value in the tuple and displaying them in the text file
        for val in tuples:
            fo.write(str(val))
            fo.write(" ")
        fo.write("\n")

     #Accessing trailer inputs stored in the trailer_store list
    for tuples in trailer_store:
    
        #Displaying it in a text file
        fo.write("Progress (module trailer) - ")
    
        #Accessing each value in the tuple and displaying them in the text file
        for val in tuples:
            fo.write(str(val))
            fo.write(" ")
        fo.write("\n")
    
    #Accessing retriever inputs stored in the retriever_store list
    for tuples in retriever_store:
    
        #Displaying it in a text file
        fo.write("Module retriever - ")
    
        #Accessing each value in the tuple and displaying them in the text file
        for val in tuples:
            fo.write(str(val))
            fo.write(" ")
        fo.write("\n")

    #Accessing exclude inputs stored in the exclude_store list
    for tuples in exclude_store:

        #Displaying it in a text file
        fo.write("Exclude - ")
    
        #Accessing each value in the tuple and displaying them in the text file
        for val in tuples:
            fo.write(str(val))
            fo.write(" ")
        fo.write("\n")

    #Closing the text file 
    fo.close()

    print("------------------------------------------------------------------------------\n")
    print("The results have been stored in a text file called 'inputs.txt'")
    print("The stored results in the text file as below\n")

    #Opening the text file to read
    fo = open("inputs.txt","r")

    #Reading from the text file line by line
    with fo:
        for line in fo:
            print(line)

    
#---------------------Main Program---------------------
#Create Variables
version_option = 0  #To get the version option (student/staff/quit)
menu_option = 0   #To get the menu option to display data (histograms / progression data list / text file)
error = 0   #If error is True, then the main_process in the program runs again to get a valid input 
Pass = 0  #To get the 'pass' value from the user
defer = 0 #     "     'defer'     "
fail = 0  #     "     'fail'      "
credit = 0  #To use as a tuple to store the pass,defer and fail values
choice = 0  #To get the user input to continue the loop or to break the loop
progress_histro = 0  #To count how many times the 'progress' appears as the progression outcome
trailer_histro = 0   #             "              'trailer'              "
retriever_histro = 0 #             "              'retriever'            "
exclude_histro = 0   #             "              'exclude'              " 
total = 0  #To get the total of all the progression outcomes
trailer = []    #To store the credits of the progression outcome 'Trailer'
retriever = []  #                 "                             'Retriever'
exclude = []    #                 "                             'Exclude'
progress_store = []  #To store the user input credits of the progression outcome 'Progress'
trailer_store = []    #                        "                                 'Trailer'
retriever_store = []  #                        "                                 'Retriever'
exclude_store = []    #                        "                                 'Exclude'
fo = 0  #To open a new text file 

#Storing the credits of each Progression Outcomes in a list as tuples
trailer = [(100,20,0),(100,0,20)]
retriever = [(80,40,0),(80,20,20),(80,0,40),(60,60,0),(60,40,20),(60,20,40),(60,0,60),(40,80,0),(40,60,20),(40,40,40),(40,20,60),(20,100,0),(20,80,20),(20,60,40),(20,40,60),(0,120,0),(0,100,20),(0,80,40),(0,60,60)]
exclude = [(40,0,80),(20,20,80),(20,0,100),(0,40,80),(0,20,100),(0,0,120)]


#Calling out the functions
while True:
    #Displaying the version menu intro and calling the option_menu function
    print("\n-----------------------------Version Menu---------------------------------------")
    option_menu()
    print("________________________________________________________________________________\n")

    #Deciding which version to continue based on the user input in option_menu function
    if version_option == 1:
        print("\nStudent Version:\n")
        main_process()

    elif version_option == 2:
        print("\nStaff Version:\n")
        main_process()
        process_loop()

    elif version_option == 3:
        print("End of the program")
        break

#Program ends        

