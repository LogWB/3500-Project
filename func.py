import pandas as pd

# ---------- Function to help verify input ---------- # 
def prompt_verification(select, _min, _max) :
    if (select): # Verify that something was input
        check = select.isnumeric() # make sure it is ALL numbers (NO char or whitespace)
        if (check): # If all num is true
            select = int(select) # Convert input into an integer for comparison
            if (select < _min or select > _max): # Check if input was in range
                return -1
            else: 
                return select
        else: # If all num is false
            return -1
    else: # No input, return -1
        return -1

# Store entire column as an array, used to assist other functions
def createArray(df, colName):  
    array = df[colName].values
    return array

# List out all the column names in dataframe
def listColumns(df):
    counter = 1
    for col in df.columns: 
        print("[" + str(counter) + "] " + col)
        counter += 1
    print("\n")
    return counter # Return the number of columns we have, used in other functions

# Drop a column
def dropColumn(df):
    valid = 1

    print("\n(22) Drop Columns:")
    print("\n**********")
    print("\nSelect a column number to drop from the list:")
    num_col = listColumns(df)
    array = df.columns
    selected_col = 0 # Temporary, will be changed

    while(valid):
        selected_col = input("Select: ")
        check = prompt_verification(selected_col, 1, num_col-1)
        if check < 0:
            print("Please select a valid option!")
            valid = 1
        else:
            valid = 0

    colName = array[int(selected_col)-1]
    newDf = df.drop(colName, axis=1)
    return newDf




