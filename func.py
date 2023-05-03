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

# ---------- List Columns ---------- #
def listColumns(df):
    counter = 1
    for col in df.columns: 
        print("[" + str(counter) + "] " + col)
        counter += 1
    print("\n")
    return counter # Return the number of columns we have, used in other functions

# ---------- Drop Column ---------- #
def dropColumn(df):
    print("\n(22) Drop Columns:")
    print("\n**********")
    print("\nSelect a column number to drop from the list:")
    num_col = listColumns(df)
    array = df.columns
    selected_col = 0 # Temporary, will be changed
    
    selected_col = checkValid(1, num_col, selected_col)

    colName = array[int(selected_col)-1]
    newDf = df.drop(colName, axis=1)
    return newDf

# ---------- Mean Function ---------- 
def getMean(df, colName):
    column_list = df[colName]
    size = countFunc(df[colName])
    list(column_list)
    summation = 0
    for x in column_list:
        summation = int(x) + summation
    #print("The summation is: " + str(summation))
    #print("The array size is: " + str(size))
    #print("The mean is: " + str(summation/size))
    #pandamean = df[colName].mean()
    #print("The mean according to pandas is: " + str(pandamean))
    mean = summation/size
    return mean

# ---------- Column Stats ---------- #
def colStat(df):
    print("\n(23) Describe Columns:")
    print("\n**********")
    print("\nSelect a column number from the list:")
    num_col = listColumns(df)
    array = df.columns
    selected_col = 0 # Temporary, will be changed

    selected_col = checkValid(1, num_col, selected_col)
    
    colName = array[int(selected_col)-1]
    newArr = df[colName]
    
    number = countFunc(newArr)
    print("Count: " + str(number))
    
    number = unCountFunc(newArr)
    print("Unique: " + str(number))
    
    # Mean Section
    mean = getMean(df, colName)
    print("Mean: " + str(mean))
    
    # Variance Section using mean
    vari = varianceFunc(lambda x: x > 0, newArr, mean)
    print("Variance: " + str(vari))
    
    # Standard Deviation from Variance
    stddev = vari**0.5
    print("Standard Deviation: " + str(stddev))

    #Used to test
    #number = minFunc(newArr)
    #print("Minimum: " + str(number))

# ---------- Count Function ---------- #
def countFunc(newArr):
    newArr = newArr.dropna(how='any',axis=0)
    newArr = dropZero(newArr)
    counter = 0
    for item in newArr:
        if item:
            counter += 1
    return counter

# ---------- Unique Count Function ---------- #
def unCountFunc(Arr):
    Arr = Arr.dropna(how='any',axis=0)
    newArr = Arr.drop_duplicates()
    newArr = dropZero(newArr)
    counter = 0
    for item in newArr:
        if item:
            counter += 1
    return counter


# ---------- Variance Function ---------- #
def varianceFunc(func, Arr, mean):
    count = 0
    variance = 0
    for item in Arr:
        if func(item):
            variance += ((item - mean)**2)
            count += 1
    variance = variance/count
    return variance


# ---------- Print Column Contents ---------- #
# Using to check column contents and also stores it in an array
# This isn't necessary for the project
def printColumn(df):
    num_col = listColumns(df)
    selected_col = 0
    print("Selected a column to print out: ")
    selected_col = checkValid(1, num_col, selected_col)
    print("SELECTED_COL = " + selected_col)
    array = df.columns
    colName = array[int(selected_col)-1]
    print("You selected: " + colName)
    # \/ This will print it as a column \/
    # print(df[colName].to_string(index=False))
    column_list = df[colName]
    #print(col_list)

# ---------- checks if the input is valid ---------- #
# The first parameter passed (num) is the maximum value aka the limit
# The first is the minimum value 
# The second should be the maximum value plus one because it will be subtracted by one when passed to prompt_verification
# The third is what the user input
def checkValid(min_val, num, selected):
    valid = 1
    
    while(valid):
        selected = input("Select: ")
        check = prompt_verification(selected, min_val, num-1)
        if check < 0:
            print("Please select a valid option!")
            valid = 1
        else:
            valid = 0
    return selected

def dropZero(array):
    array = [value for value in array if value != 0]
    return array

# -------- Quicksort -------- #
def partition(arr, lo, hi):
    pivot = arr[hi]
    i = low - 1
    for j in range(lo, hi):
        if array[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[hi]) = (arr[hi], arr[i + 1])
    return i + 1
 
def quick_sort(arr, lo, hi):
    if lo < hi:
        pi = partition(arr, lo, hi)
        quick_sort(arr, lo, pi - 1)
        quick_sort(arr, pi + 1, hi)

# -------- Min Function -------- #
def minFunc(Arr):
    Arr = Arr.dropna(how='any',axis=0)
    newArr = dropZero(newArr)
    newArr = quick_sort(newArr, 0, len(newArr) - 1)
    minimum = newArr[0]
    return minimum
	
# -------- Print Function -------- #
def printDataFrame(df):
    print("\n(4) Select how many rows you would like to print:")
    print("**********")
    print("41) 100 Rows ")
    print("42) 1000 Rows ")
    print("43) 5000 Rows ")
    selected = 0 # Temporary, will be changed
    
    selected = checkValid(41, 44, selected)
    selected = int(selected)
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 200)

    if (selected == 41):
        print(df.head(100))
    elif (selected == 42):
        print(df.head(1000))
    elif (selected == 43):
        print(df.head(5000))
