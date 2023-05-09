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
    
    convertedArr = convertInt(newArr) 
    
    #print(newArr)
    sorted_arr = merge_sort(convertedArr)
    #print(newArr)
    #print(sorted_arr)
    #print("According to this: " + str(newArr[len(newArr)-1]))
    #Used to test
    number = minFunc(sorted_arr)
    print("Minimum: " + str(number))

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

def partition(arr, low, high):
    pivot = len(arr[high])/2
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr):
    stack = []
    stack.append((0, len(arr) - 1))

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot = partition(arr, low, high)

            if pivot - low < high - pivot:
                stack.append((low, pivot))
                stack.append((pivot + 1, high))
            else:
                stack.append((pivot + 1, high))
                stack.append((low, pivot))

    return arr

# -------- Min Function -------- #
def minFunc(Arr):
    #Arr = Arr.dropna(how='any',axis=0)
    #newArr = dropZero(Arr)
    #newArr = quick_sort(newArr, 0, len(newArr) - 1)
    minimum = Arr[0]
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


# -------- Int Conversion Function -------- #
def convertInt(Arr):
    #newArr = Arr.values
    newArr = []
    for x in Arr:
        #try:
        y = int(x)
        if (y < 0):
            print("Negative number detected: " + str(y))
        elif (y > 0):
            newArr.append(y)
        #except:
        #    print("invalid: " + str(x))
    
    return list(newArr)


# -------- Merge Sort Function -------- #
# Notes:
# 1) Make a function to divide all the arrays until the length of the array is 1, meaning fully divided
# 2) Send our arrays into a "merge" helper which will sort the array, combine it into a bigger array,
#    and it will keep doing that until everything is back as a whole
# 3) O(n log n) because of how much space we're using making all these arrays 

def merge_sort(arr):
    # If the arr size is equal to one, we are finally done
    if len(arr) == 1:
        return arr

    # Get the middle index of the current array
    middle = int(len(arr) / 2)
    # Slice the array in half
    left = arr[:middle]
    right = arr[middle:]

    # Send the sliced array over to this again, we're gonna keep slicing
    # This is gonna stop calling recursively once we reach base case of len(arr) == 1
    left = merge_sort(left)
    right = merge_sort(right)

    # Start next recursive "merge" function
    # Send over the arrays which will return the sorted array
    return merge(left, right)


def merge(left, right):
    merged_arr = []
    # These will be the indicies because we're working with TWO ARRAYS 
    left_in = 0
    right_in = 0

    # one_pos is the first position of the first array
    # two_pos is the first position of the second array
    # compare element in first array with element in second array
    #

    # Keep iterating while the left array has elements or the right array has elements
    while left_in < len(left) and right_in < len(right):
        if left[left_in] <= right[right_in]:
            # Place the smaller element in the earliest position possible in the array
            merged_arr.append(left[left_in])
            left_in += 1
            # Jump to the top of the while look and check again if the left has an element less than right
        #elif (right[right_in] <=left[left_in]):
        # Implied already that the first element in the right index is the smallest in that array
        # because we've been comparing the left array with everything in the right array
        # so just append it
        else: 
            merged_arr.append(right[right_in])
            right_in += 1

    # Append any remaining elements
    while left_in < len(left):
        merged_arr.append(left[left_in])
        left_in += 1
    while right_in < len(right):
        merged_arr.append(right[right_in])
        right_in += 1

    # Return the merged subarray 
    return merged_arr









