# Course: CMPS 3500
# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# Date: 
# Student 1: Bradley Tate 
# Student 2: Ramon Plascencia
# Student 3: Nicholas Romasanta
# Description: Implementation Basic Data Analysis Routines
import pandas as pd
import time 
import re 
#import func as func
from collections import Counter

df_loaded = 0 # Flag for if we have loaded a csv into a dataframe
string_value = 0 # Flag for if we are dealing with a string, used in sorting algorithm
unique_year_list = [] 
unique_crime_list = [] 
unique_location_list = [] 
unique_month_list = [] 

# ---------- Analysis ---------- # 
def printAnalysis(df):
    
    global unique_year_list
    global unique_location_list
    unique_year_list = [] 
    unique_crime_list = [] 
    unique_location_list = [] 
    unique_month_list = []

    
    # ----- Start of work for question 1 ----- #
    print("\n")
    print(getTime() + " Show the total unique count of crimes per year sorted in descending order: ") 
    print("---------------------------------------------")
    year_df = df["year"]
    unCountFunc(year_df, "year")
    unique_year_list = merge_sort(unique_year_list)
    num_years = len(unique_year_list)
    year_to_crime = [] 
    i = 0
    while i < num_years:
        year_to_crime.append(question1(unique_year_list[i], df))
        i =  i + 1
    print("\n")
    
    # make a dataframe in another function
    lists = {'year' : unique_year_list, 'counts': year_to_crime}
    df_tests = convertDF(lists, 'counts')
    
    i = 0
    while i < num_years:
        print(getTime() + " The amount of unique crimes in the year " 
                + str(df_tests.year.iloc[i]) + " is: " + str(df_tests.counts.iloc[i])) 
        i = i + 1
    print("\n")
    




    # ----- Start of work for question 2 ----- #
    print(getTime() + " Show the top 5 areas (AREA NAME) with the most crime events in " +  
            "all years (Sorted by the # of crime events)")
    print("---------------------------------------------")
    location_df = df["AREA NAME"]
    unCountFunc(location_df, "AREA NAME")
    
    unique_location_list = merge_sort(unique_location_list)
    
    num_location = len(unique_location_list)
    location_to_crime = [] 
    i = 0
    while i < num_location:
        #print('Checking location to crime with: ' + unique_location_list[i]) 
        location_to_crime.append(question2(unique_location_list[i], df))
        #print(location_to_crime)
        i =  i + 1
    # make a dataframe in another function
    lists = {'location' : unique_location_list, 'counts': location_to_crime}
    df_tests = convertDF(lists, 'counts')    
    i = 0
    while i < 5:
        print(getTime() + " The amount of unique crimes in the area " + str(df_tests.location.iloc[i]) + " is: " + str(df_tests.counts.iloc[i])) 
        i = i + 1
    




    # ---------- Start of question 3 ---------- #
    print("\n")
    print(getTime() + " Show all the months and the unique total count of crimes sorted in increasing order")
    print("---------------------------------------------")
    regex_pattern = [] 
    regex_pattern.append("^01/\d{2}/\d{4}")
    regex_pattern.append("^02/\d{2}/\d{4}")
    regex_pattern.append("^03/\d{2}/\d{4}")
    regex_pattern.append("^04/\d{2}/\d{4}")
    regex_pattern.append("^05/\d{2}/\d{4}")
    regex_pattern.append("^06/\d{2}/\d{4}")
    regex_pattern.append("^07/\d{2}/\d{4}")
    regex_pattern.append("^08/\d{2}/\d{4}")
    regex_pattern.append("^09/\d{2}/\d{4}")
    regex_pattern.append("^10/\d{2}/\d{4}")
    regex_pattern.append("^11/\d{2}/\d{4}")
    regex_pattern.append("^12/\d{2}/\d{4}")
    date_to_crime = [] 
    month = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    i = 0
    while i < 12:
        date_to_crime.append(question3(regex_pattern[i], df)) 
        i = i + 1
    
    # make a dataframe in another function
    lists = {'month' : month, 'counts': date_to_crime}
    df_tests = convertDF(lists, 'counts')
    
    i = 11
    while i > -1:
        print(getTime() + " The amount of unique crimes in the month " + 
                df_tests.month.iloc[i] + " is: " + str(df_tests.counts.iloc[i])) 
        i = i - 1
    




    # ---------- Start of question 4 ---------- #
    print("\n")
    print(getTime() +  " Show the top 10 streets with the most crimes in LA in 2019" + 
            " Also display the total amount of crimes in each street.") 
    print("---------------------------------------------")
    column_list = list(df["LOCATION"].values)
    street_list = []
    street = r"\d+\s+(.+)"
    i = 0
    for x in column_list:
        street_found = re.match(street, column_list[i])
        if street_found:
            street_name = street_found.group(1)
            street_list.append(street_name)
        i = i + 1
    unique_street_list = list(set(street_list))

    count = Counter(street_list)
    top_10 = count.most_common(10)
    top_10 = list(top_10)
    for x in top_10:
        print(getTime() + " " + str(x).strip())
    




    # ---------- Start of question 5 ---------- #
    print("\n")
    print(getTime() + " Show the top 5 most dangerous times (in hours) to be in Hollywood" + 
            ". Also display the total amount of crimes in each hour.")
    print("---------------------------------------------")
    question5("Hollywood", df)

    



    # ---------- Start of question 6 ---------- #
    print("\n")
    print(getTime() + " Print the details of the crime that took the most time (in hours) to be reported")
    print("---------------------------------------------")
    drno = df["DR_NO"]
    date_rptd = df["Date Rptd"]
    date_occ = df["DATE OCC"]
    time_occ = df["TIME OCC"]
    
    # make a dataframe in another function
    lists = {'DRNO' : drno, 'DR': date_rptd, 'DO': date_occ, 'TO': time_occ}
    df_tests = convertDF(lists, 'DRNO')
    
    df_tests['DR'] = pd.to_datetime(df_tests['DR'], format='%m/%d/%Y %I:%M:%S %p')
    df_tests['DO'] = pd.to_datetime(df_tests['DO'], format='%m/%d/%Y %I:%M:%S %p') 
    
    df_tests['Difference'] = df_tests['DR'] - df_tests['DO']
    df_tests['Difference'] = (df_tests['Difference'].dt.total_seconds() / 3600) + df_tests['TO']
    
    df_tests = df_tests.sort_values('Difference', ascending = False)
    
    print('\n')
    searchval = df_tests.DRNO[0]
    print(df[df['DR_NO'] == searchval])
   
    



    # -------- Start of Question 7 -------- #
    print("\n")
    print(getTime() + " Show the 10 top most common crime types (Crm Cd Desc) overall across all years.")
    print("---------------------------------------------")
    column_list = list(df["Crm Cd Desc"].values)

    count = Counter(column_list)
    top_10 = count.most_common(10)
    top_10 = list(top_10)
    print("\nTop 10 most common crime types:")
    loopcount = 1
    for x in top_10:
        print(getTime() + " " + str(loopcount) + " " + str(x[0]))
        loopcount += 1
    
    



    # -------- Start of Question 8 -------- #
    print("\n")
    print(getTime() + " Are women or men more likely to be victim of a crime in LA betwene lunch" + 
        " time (11:00am and 1:00pm)?")
    print("---------------------------------------------")
    location = df["LOCATION"]
    vict_sex = df["Vict Sex"]
    time_occ = df["TIME OCC"]
    pattern = r"\w*..LA"
    
    lists = {'LOC' : location, 'VS': vict_sex, 'TO': time_occ}
    df_tests = convertDF(lists, 'TO')
    
    df_tests = df_tests[df_tests['LOC'].str.contains('LA', case=False)]
    
    df_tests = df_tests[(df_tests['TO'] >= 1100) & (df_tests['TO'] <= 1300)]
    count = Counter(df_tests['VS'])
    
    print('\n')
    male = count['M']
    female = count['F']
    
    if (male < female):
        print("Females are more likely to be the victim")
    else:
        print("Males are more likely to be the victim")
    print(getTime() + " Value: " + str(max(male, female)))
    print(getTime() + " Compared to: " + str(min(male,female)))
    print(getTime() + " Displacement: " + str(abs(male - female)))
    
    



    # -------- Start of Question 9 -------- #
    print("\n")
    print(getTime() + " What is the month that has the most major credit card frauds in LA in 2019?")
    print("---------------------------------------------")
    i = 0
    regex_pattern = []
    regex_pattern.append("01/\d{2}/2019.")
    regex_pattern.append("02/\d{2}/2019.")
    regex_pattern.append("03/\d{2}/2019.")
    regex_pattern.append("04/\d{2}/2019.")
    regex_pattern.append("05/\d{2}/2019.")
    regex_pattern.append("06/\d{2}/2019.")
    regex_pattern.append("07/\d{2}/2019.")
    regex_pattern.append("08/\d{2}/2019.")
    regex_pattern.append("09/\d{2}/2019.")
    regex_pattern.append("10/\d{2}/2019.")
    regex_pattern.append("11/\d{2}/2019.")
    regex_pattern.append("12/\d{2}/2019.")
    card_crime = []
    while i < 12:
        card_crime.append(question9(regex_pattern[i], df))
        i = i + 1
    i = 0
    #while i < 12:
    #    print(getTime() + " The amount of credit card fraud in the month " + month[i] + " and year 2019"
    #            + " is: " + str(card_crime[i]))
    #    i = i + 1
    
    lists = {'month' : month, 'fraud': card_crime}
    tempdf = pd.DataFrame(lists)

    tempdf = tempdf.sort_values(by=["fraud"], ascending=False)
    print(getTime())
    print(tempdf.head(1).to_string(index=False))
    



    # -------- Start of Question 10 -------- #
    print("\n")
    print(getTime() + " List the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018.")
    print("---------------------------------------------")
    question10(df)


# ------ Creates a dataframe and returns it ------ #
def convertDF(lists, names):
    df = pd.DataFrame(lists)
    df_s = df.sort_values(names, ascending = False)
    return df_s

def question1(element, df):
    count = 0
    
    # get the dataframe where it's only that year
    df = df[df.year == element]
    newArr = df["Crm Cd Desc"]
    
    # get the count of unique crimes
    count =  unCountFunc(newArr, " ")
    return count

def question2(element, df):
    count = 0
    
    # get the dataframe where it's only that location
    df = df[df["AREA NAME"] == element]
    newArr = df["Crm Cd Desc"]
    
    # get the count of unique crimes
    count =  unCountFunc(newArr, " ")
    return count

def question3(element, df):
    count = 0
    
    # get the dataframe where it's only that location
    df = df[df["DATE OCC"].str.match(element)]
    newArr = df["Crm Cd Desc"]
    
    count =  unCountFunc(newArr, " ")
    return count

def question5(element, df):
    count = 0

    # get the dataframe where it's only that location
    df = df[df["AREA NAME"] == element]
    newArr = df["TIME OCC"]
    unique_time = unCountFunc(newArr, " " )
    sorted_arr = merge_sort(list(newArr))
    time = []
    occurence = []
    i = 0
    j = 0
    counter = 0
    while j < unique_time and i < len(sorted_arr):
        counter = 0
        x = sorted_arr[i]
        while i < len(sorted_arr) and sorted_arr[i] == x:
            counter = counter + 1
            i = i + 1

        time.append(sorted_arr[i-1])
        occurence.append(counter)
        j = j + 1

    lists = {'time' : time, 'occurence': occurence}
    df = pd.DataFrame(lists)
    df = df.sort_values(by=["occurence"], ascending=False)

    print(getTime()) 
    print(df.head(5).to_string(index=False))
    #print(df_tests)


def question9(element, df):
    newdf = df[df["DATE OCC"].str.contains(element, regex=True)]
    crimedesc = "CREDIT CARDS, FRAUD USE ($950 & UNDER"
    newArr = newdf[newdf["Crm Cd Desc"] == crimedesc]
    #newArr = df[df["year"] == element]
    count = len(newArr)
    return count

def question10(df):
    element = "12/\d{2}/2018."
    newdf = df[df["DATE OCC"].str.contains(element, regex=True)]
    agedf = newdf[newdf["Vict Age"] >= 65]
    area_list = agedf["AREA NAME"].values
    area_list = merge_sort(list(area_list))
    area = []
    occurence = []
    i = 0
    j = 0
    counter = 0
    while j < len(unique_location_list) and i < len(area_list):
        counter = 0
        x = area_list[i]
        while i < len(area_list) and area_list[i] == x:
            counter = counter + 1
            i = i + 1

        area.append(area_list[i-1])
        occurence.append(counter)
        j = j + 1

    lists = {'area' : area, 'occurences': occurence}
    df = pd.DataFrame(lists)

    df = df.sort_values(by=["occurences"], ascending=False)
    print(getTime())
    print(df.head(5).to_string(index=False))


# ~~~~~~~~~~ End of Code Related to Analysis ~~~~~~~~~ #

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
    num_col = num_col - 1
    if (num_col == 0):
        df_loaded = 0
    return newDf

# ---------- Mean Function ---------- 
def getMean(df, colName):
    column_list = df[colName]
    column_list = column_list.dropna(how='any',axis=0)
    #size = countFunc(df[colName])
    size = countFunc(column_list)
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
    global string_value
    string_value = 0
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
    
    unumber = unCountFunc(newArr, "")
    print("Unique: " + str(unumber))
    
    error = 0
    
    newArr = newArr.dropna(how='any',axis=0)
    try:
        convertedArr = convertInt(newArr) 
        #print(newArr)
        sorted_arr = merge_sort(convertedArr)
    except:
        #print("non-numerical detected")
        string_value = 1
        error = 1
        sorted_arr = merge_sort(list(newArr))
    finally:
        if (colName == "LON"):
            error = 0
        #print(sorted_arr)
        if (error == 0):
            # Mean Section
            mean = getMean(df, colName)
            print("Mean: " + str(mean))
        
            # Median Section
            if (number % 2 == 1):
                # If odd, print the middle
                try:
                    median = MedFunc(sorted_arr, int((number+1)/2))
                    print("Median: " + str(median))
                except:
                    print("2nd variable is not an int value")
            else:
                # If even, print the lower value
                try:
                    median = MedFunc(sorted_arr, int(number/2))
                    print("Median: " + str(median))
                except:
                    print("2nd variable is not an int value")
                
            modeval = modeFunc(sorted_arr)
            print("Mode: " + str(modeval[0]))
        
            try:
                vari = varianceFunc(lambda x: x > 0, newArr, mean)
                print("Variance: " + str(vari))
                stddev = vari**0.5
                print("Standard Deviation: " + str(stddev))
            except:
                print("Variance: NaN")
                print("Standard Deviation: NaN")
            
        
            number = minFunc(sorted_arr)
            print("Minimum: " + str(number))
        
            number = maxFunc(sorted_arr)
            print("Maximum: " + str(number))
        
        else:
            # Mean Section
            print("Mean: NaN")
        
            # Median Section
            print("Median: NaN")
        
            # Mode
            print("Mode: NaN")
        
            # Variance
            print("Variance: NaN")
        
            # Standard Deviation
            print("Standard Deviation: NaN")
        
            # Minimum
            print("Minimum: NaN")
        
            # Maximum
            print("Maximum: NaN")

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
def unCountFunc(Arr, colName):
    global unique_year_list
    Arr = Arr.dropna(how='any',axis=0)
    newArr = Arr.drop_duplicates()
    newArr = dropZero(newArr)
    counter = 0
    custom_list = [] 
    custom_flag = 0
    for item in newArr:
        if item:
            counter += 1
            if (colName == "year"):
                unique_year_list.append(item)
            if (colName == "crime"):
                unique_crime_list.append(item)
            if (colName == "AREA NAME"):
                unique_location_list.append(item)

    return counter

# ---------- Median Function ---------- #
def MedFunc(Arr, middle):
    median = Arr[middle]
    return median

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


# -------- Min Function -------- #
def minFunc(Arr):
    #Arr = Arr.dropna(how='any',axis=0)
    #newArr = dropZero(Arr)
    #newArr = quick_sort(newArr, 0, len(newArr) - 1)
    minimum = Arr[0]
    return minimum

# -------- Max Function -------- #
def maxFunc(Arr):
    #Arr = Arr.dropna(how='any',axis=0)
    #newArr = dropZero(Arr)
    #newArr = quick_sort(newArr, 0, len(newArr) - 1)
    size = len(Arr)
    maximum = Arr[(size-1)]
    return maximum

# -------- Mode Function -------- #
def modeFunc(Arr):
    mode = {}
    
    for items in Arr:
        for items in mode:
            mode[items] += 1
        else:
            mode[items] = 1
    return [key for key in mode.keys() if mode[key] == max(mode.values())]
    
# -------- Print Function -------- #
def printDataFrame(df):
    print("\n(4) Select how many rows you would like to print: (Press Ctrl+C to cancel)")
    print("**********")
    print("41) 100 Rows ")
    print("42) 1000 Rows ")
    print("43) 5000 Rows ")
    row_count = len(df)
    selected = 0 # Temporary, will be changed
    
    selected = checkValid(41, 44, selected)
    selected = int(selected)
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 200)
   
    if (selected == 41):
        if (row_count >= 100):
            print(df.head(100))
        else:
            print("Cannot print this amount of elements, dataframe too small")
    elif (selected == 42):
        if (row_count >= 1000):
            print(df.head(1000))
        else:
            print("Cannot print this amount of elements, dataframe too small")
    elif (selected == 43):
        if (row_count >= 5000):
            print(df.head(5000))
        else:
            print("Cannot print this amount of elements, dataframe too small")

# -------- Int Conversion Function -------- #
def convertInt(Arr):
    #newArr = Arr.values
    newArr = []
    for x in Arr:
        #try:
        y = int(x)
        if (y < 0):
            # print("Negative number detected: " + str(y))
            pass
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

    
    # Keep iterating while the left array has elements or the right array has elements
    while left_in < len(left) and right_in < len(right):
        
        if (string_value == 1): 
            left_val = str(left[left_in]) 
            right_val = str(right[right_in])
        else:
            left_val = left[left_in] 
            right_val = right[right_in]

        if left_val < right_val:
            # Place the smaller element in the earliest position possible in the array
            merged_arr.append(left_val)
            left_in += 1
            # Jump to the top of the while look and check again if the left has an element less than right
        else: 
            merged_arr.append(right_val)
            right_in += 1

    # Append any remaining elements
    while left_in < len(left):
        if string_value == 1:
            left_val = str(left[left_in]) 
        else:
            left_val = left[left_in] 
            
        merged_arr.append(left_val)
        left_in += 1
    while right_in < len(right):
        if string_value == 1: 
            right_val = str(right[right_in])
        else:
            right_val = right[right_in] 

        merged_arr.append(right_val)
        right_in += 1

    # Return the merged subarray 
    return merged_arr

# -------- Search Function -------- #
# Using to check column contents and also stores it in an array
def searchFunction(df):
    num_col = listColumns(df)
    selected_col = 0
    print("Selected a column to search in: (Press Ctrl+C to cancel)")
    selected_col = checkValid(1, num_col, selected_col)
    array = df.columns
    colName = array[int(selected_col)-1]
    
    # \/ This will print it as a column, useful for debugging \/
    #print(df[colName].to_string(index=False))
    
    column_list = list(df[colName].values)
    #print(column_list)
    date_query = re.match("(?i)^date", colName)
    if (date_query): 
        print("IMPORTANT: Please enter with the format of: mm/dd/yyyy")
    else: 
        pass

    while True:
        print("Enter a value to search for: ") 
        element = input("Select: ")
        # If the user wants to look for a date...
        if (date_query):
            valid_date = re.match("^\d{2}/\d{2}/\d{4}$", element) 
            # Format is valid, get out of this loop
            if (valid_date):
                break
            # Format is invalid, continue loop
            else:
                print("Invalid date format. Please try again, or press Ctrl+C to exit")
                pass
        # Not a date query, break out of this loop
        else:
            break
    i = 0
    count = 0
    j = 0
    index_found = []

    start_time = time.time()
    for x in column_list:
        # If the person is searching for a date
        if(date_query):
            # Dataframe had the format of mm/dd/yyyy 12:00:00AM. Need to cut off the time at the end.
            # .split will cut off the string from the whitespace
            temp = str(column_list[i]).split()
            dataframe_element = temp[0]
        else:
            dataframe_element = str(column_list[i])
        if (str(element) == dataframe_element):
            index_found.append(i)
            # Keep track of how many elements found with count
            count = count + 1
            i = i + 1
        else:
            i = i + 1
    end_time = time.time()
    total_time = (end_time) - (start_time)
    total_time = round(total_time, 5)

    print("Element found in " + str(count) + " row(s)")
    print("Search was successful! Time to search was " + str(total_time) + " sec.")
    
    # Note: The below code was mostly juts used for making sure the search was indeed correct.
    # Since it is unnecessary for the project, it is commented out

    # Only offer user the option to print rows if the amount of found elements is more than one 
    #if (count > 0):
    #    print("Would you like to print the rows that match this search element?")
    #    print("Please note, this will print a lot of elements take some time. If you would like to cancel at any time, please press CTRL+C")
    #    answer = input("[Y/N]: ")
    #    if((answer =="Y") or (answer == "y") or (answer == "yes") or (answer == "Yes") or (answer == "YES")):
    #        #print(index_found)
    #        # While our index `j` is less than the amount of elements we found, increment through the array 
    #        while j < (count):
    #            print(df.loc[[index_found[j]]])
    #            j = j + 1
    #    if((answer =="N") or (answer == "n") or (answer == "no") or (answer == "No") or (answer == "NO")):
    #        pass
    #    else:
    #        print("Invalid option, returning to main menu")

# -------------------------------------------------------------------------#
# Start of main menu interface

main_menu = "Main Menu:" 
main_menu += "\n**********"
main_menu += "\n(1) Load Data"
main_menu += "\n(2) Exploring Data"
main_menu += "\n(3) Data Analysis"
main_menu += "\n(4) Print Data Set"
main_menu += "\n(5) Quit"
main_menu += "\nSelect: "

explore_menu = "\nExploring Data:" 
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
# Used a function so that the strings will have updated their times every time this is called
def init_loadPrompt():
    load_prompt = "\nLoad Data Set:"  
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
        user_selection = prompt_verification(user_input, _min, _max) # will receive -1 for invalid inputs
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
                start_time = time.time()
                df = pd.read_csv('Crime_Data_from_2017_to_2019.csv')
                df = df.drop("Crm Cd 2", axis=1)
                df = df.drop("Crm Cd 3", axis=1)
                df = df.drop("Crm Cd 4", axis=1)
                df = df.drop("Cross Street", axis=1)
                end_time = time.time()
                total_time = (end_time) - (start_time)
                total_time = round(total_time, 5)
                print(getTime() + " Total Columns Read: " + str(len(df.columns))) 
                print(getTime() + " Total Rows Read: " + str(len(df)))
                print("File loaded successfully!") 
                print("Time to load " + str(total_time) + " seconds\n")
                df_loaded = 1
                df2 = df.copy()
            elif (load_opt == 2): 
                start_time = time.time()
                df = pd.read_csv('Crime_Data_from_2020_to_2021.csv') 
                df = df.drop("Crm Cd 2", axis=1)
                df = df.drop("Crm Cd 3", axis=1)
                df = df.drop("Crm Cd 4", axis=1)
                df = df.drop("Cross Street", axis=1)
                end_time = time.time()
                total_time = (end_time) - (start_time)
                total_time = round(total_time, 5)
                print(getTime() + " Total Columns Read: " + str(len(df.columns))) 
                print(getTime() + " Total Rows Read: " + str(len(df)))
                print("File loaded successfully!")    
                print("Time to load " + str(total_time) + " seconds\n")
                df_loaded = 1
                df2 = df.copy()
            elif (load_opt == 3):
                start_time = time.time()
                df = pd.read_csv('Test.csv')
                df = df.drop("Crm Cd 2", axis=1)
                df = df.drop("Crm Cd 3", axis=1)
                df = df.drop("Crm Cd 4", axis=1)
                df = df.drop("Cross Street", axis=1)
                end_time = time.time()
                total_time = (end_time) - (start_time)
                total_time = round(total_time, 5)
                print(getTime() + " Total Columns Read: " + str(len(df.columns))) 
                print(getTime() + " Total Rows Read: " + str(len(df)))
                print("File loaded successfully!")    
                print("Time to load " + str(total_time) + " seconds\n")
                df_loaded = 1
                df2 = df.copy()
        if (option == 2):
            explore_opt = menu(explore_menu, 21, 25)
            if (explore_opt == 21):
                print("\n(21) List all columns:")
                print("**********")
                listColumns(df)
            elif (explore_opt == 22): 
                if df.empty: 
                    print("No columns to drop")
                else: 
                    df = dropColumn(df)
            elif (explore_opt == 23):
                #try:
                if df.empty:
                    print("Dataframe is empty")
                else:
                    colStat(df)
                #except:
                #    print("No min/max for this column")
                # test
            elif (explore_opt == 24):
                if df.empty:
                    print("No columns to search")
                else: 
                    searchFunction(df)
            elif (explore_opt == 25):
                print("You selected back to main menu\n")
        if (option == 3):
                printAnalysis(df2)
        if (option == 4):
            if df.empty:
                print("Dataframe is empty")
            elif(df_loaded==1):
                printDataFrame(df)
            else:
                print("No dataframe has been loaded\n")
    # Error Handling
    except ValueError as e:
        print("ValueError:", e)
    except KeyboardInterrupt:
        print("\nCTRL+C or Cmd+C was pressed")
    except TypeError as e:
        print("A debug error has occured somewhere", e)
    except NameError:
        print("File has not been loaded yet")
    except FileNotFoundError:
        print("This file either does not exist or an unexpected error has occured")
    except Exception as e: # General Exception
        print(e)
    finally:
        print(" ")
        
