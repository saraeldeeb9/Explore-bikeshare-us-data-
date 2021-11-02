#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input('Enter city: ').lower()
    while city not in ['chicago','new york city','washington']:
        city=input('please choose from 3 cities: chicago, new york city or washington')

    # get user input for month (all, january, february, ... , june)
    # i use while loop to handle invalid inputs
    month= input('Enter month: ').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
        month = input('enter month from january, february, ... , june : ')
        
    # get user input for day of week
    # i use while loop to handle any invalid inputs
    day=input('Enter day: ').lower()
    while day not in['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day= input('please choose a day from ( monday, tuesday, ... sunday)')
        print('-'*40)
        


    return city,month,day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df["month"] = df['Start Time'].dt.month
    df["day"] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all': 
        # filter by month to create the new filtered dataframe
        df = df[df['month'] == month.title()]
    if day != 'all':
        df=df[df['day']== day.title()]        

    
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    #to display the most common month
    common_month=df['month'].mode()[0]
    print("The most common month:",common_month)
    # display the most common day of week 
    common_day=df['day'].mode()[0]
    print("The most common day:",common_day)
    # display the most common start hour using hour.mode
    df['hour'] = df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print("The most common hour is: ", common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    #this will count values of each station and then get the max of them which will be the most commonly used start station
    print("The most common start station is: ", df ['Start Station'].value_counts().idxmax())
    # display most commonly used end station
    #this will count all of the end stations and the get the mo=ax one of them which will be most commoly end station
    print("The most common end station is: ", df['End Station'].value_counts().idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
        """Displays statistics on the total and average trip duration."""
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()
        # display total travel time
        """total travel time will be determine using sum function after that will be divide bt 3600 to turn it into hours"""
        total_travel_duration = df['Trip Duration'].sum() / 3600.0
        print("total travel time in hours : ", total_travel_duration)
        # display mean travel time
        """ here we will determine the mean using the mean function and also divided be 3600 to  be turned to hours"""
        mean_travel_duration = df['Trip Duration'].mean() / 3600.0
        print("mean travel time in hours : ", mean_travel_duration)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    #we will use value count function to count user types
    usertypes = df['User Type'].value_counts()
    print(usertypes)
    # Display counts of gender
    # using value count of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nThe users gender are :\n",gender)
    except:
        print("\nThere is no 'Gender' column in this file.")

    # Display earliest, most recent, and most common year of birth
    #to determine the earliest year of birth year i will use the min function
    try:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year is:" ,earliest_year,"\nThe most recent year is: ",recent_year,"\nThe most common year is: ",common_year)
    except:
        print("There are no 'birth year' column in this file.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def view_data(city):
    df = pd.read_csv(CITY_DATA[city])
    print('\nRaw data is available to check... \n')
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        if view_data not in ['yes', 'no']:
            print('That\'s invalid choice, pleas type yes or no')
        elif view_data=='yes' :
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
        elif view_data== 'no':
            print('\nExiting...')
        
            break
    
    
def main():
    while True:
        filters = get_filters()
        if filters is not None:
            city, month, day = filters
            df = load_data(city, month, day)
            station_stats(df)
            trip_duration_stats(df)
            time_stats(df)
            user_stats(df)
            view_data(city)
        restart = input('Thank you \nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
                      


# In[ ]:





# In[ ]:





# In[ ]:




