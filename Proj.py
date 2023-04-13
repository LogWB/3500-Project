# Course: CMPS 3500
# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# Date: 
# Student 1:  
# Student 2: Ramon Plascencia
# Student 3: Nicholas Romasanta
# Description: Implementation Basic Data Analysis Routines
import pandas as pd
import time
import func as func
df_loaded = 0 # Flag for if we have loaded a csv into a dataframe

main_menu = "Main Menu:" 
main_menu += "\n**********"
main_menu += "\n(1) Load Data"
main_menu += "\n(2) Exploring Data"
main_menu += "\n(3) Data Analysis"
main_menu += "\n(4) Print Data Set"
main_menu += "\n(5) Quit"
main_menu += "\nSelect: "

explore_menu = "Exploring Data:" 
explore_menu += "\n(Output of each option is a placeholder)" 
explore_menu += "\n**********"
explore_menu += "\n(21) List all columns:"
explore_menu += "\n(22) Drop columns:"
explore_menu += "\n(23) Describe columns:"
explore_menu += "\n(24) Search Element in Column:"
explore_menu += "\n(25) Back to Main Menu:"


# ---------- Function to get current time ---------- #
def getTime():
    global local_time
    t = time.localtime()
    local_time = time.strftime("%H:%M:%S", t)
    return local_time


# ---------- Function to initialize load data menu ---------- # 
# This is so that the strings will have updated their times every time this is called
def init_loadPrompt():
    load_prompt = "Load Data Set:"  
    load_prompt += "\n**********"
    load_prompt += "\n" + getTime() + " Select the number of the file to load from the list below:"
    load_prompt += "\nPlease select an option:"
    load_prompt += "\n[1] Crime_Data_from_2017_to_2019.csv"
    load_prompt += "\n[2] Crime_Data_from_2020_to_2021.csv"
    load_prompt += "\n[3] Test.csv"
    load_prompt += "\n" + getTime() + ": "
    return load_prompt


# ---------- Function to display menu  ---------- # 
def menu(prompt, _min, _max): 
    verify = 0
    while verify == 0:
        user_input = input(prompt)  # Prompt user for input
        user_selection = func.prompt_verification(user_input, _min, _max) # will receive -1 for invalid inputs
        if (user_selection < 0): # If invalid input 
            print("Please enter a valid option\n") 
            verify = 0 
        elif (user_selection == 5): # If user wants to quit
            print("Bye!") # User want's to leave :(
            quit()
        else: # If a valid option was selected
            verify = 1
    return user_selection


# ~~~~~~~~~~ Start ~~~~~~~~~~ #
cont = True
while(cont): # This will keep going until the user inputs '5' at the main menu
    try:
        option = menu(main_menu, 1, 5) # At the top, so use main menu
        if (option == 1):
            load_menu = init_loadPrompt() # Give user the load data menu
            load_opt = menu(load_menu, 1, 3)
            if (load_opt == 1):
                df = pd.read_csv('Crime_Data_from_2017_to_2019.csv')
                print(getTime() + " Total Columns Read: " + str(len(df.columns))) 
                print(getTime() + " Total Rows Read: " + str(len(df)))
                print("File loaded successfully!")    
                print("Time to load <blank> sec\n")
                df_loaded = 1
            elif (load_opt == 2): 
                df = pd.read_csv('Crime_Data_from_2020_to_2021.csv')
                print(getTime() + " Total Columns Read: " + str(len(df.columns))) 
                print(getTime() + " Total Rows Read: " + str(len(df)))
                print("File loaded successfully!")    
                print("Time to load <blank> sec\n")
                df_loaded = 1
            elif (load_opt == 3):
                df = pd.read_csv('Test.csv')
                print(getTime() + " Total Columns Read: " + str(len(df.columns))) 
                print(getTime() + " Total Rows Read: " + str(len(df)))
                print("File loaded successfully!")    
                print("Time to load <blank> sec\n")
                df_loaded = 1
        if (option == 2):
            explore_opt = menu(explore_menu, 21, 25)
            if (explore_opt == 21):
                print("\n(21) List all columns:")
                print("**********")
                func.listColumns(df)
            elif (explore_opt == 22): 
                #using this as a test
                df = func.dropColumn(df)
                #print("You selected drop all columns\n")
            elif (explore_opt == 23):
                print("You selected describe all columns\n")
                func.colStat(df)
                # test
            elif (explore_opt == 24):
                print("You selected search element in all columns\n")
            elif (explore_opt == 25):
                print("You selected back to main menu\n")
        if (option == 3):
                print("[PLACEHOLDER] Data has been analzyed [PLACEHOLDER]\n")
        if (option == 4):
            if(df_loaded==1):
                print(df)
            else:
                print("No dataframe has been loaded\n")
    # Error Handling
    except ValueError as e:
        print("ValueError:", e)
    except KeyboardInterrupt:
        print("\nPython program cannot handle SIGINT signal, enter '5' to exit the program")
    except TypeError as e:
        print("A debug error has occured somewhere", e)
    except NameError:
        print("File has not been loaded yet")
    except FileNotFoundError:
        print("This file either does not exist or an unexpected error has occured")


