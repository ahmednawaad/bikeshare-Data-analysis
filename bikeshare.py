#!/usr/bin/env python
# coding: utf-8

# In[6]:


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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("What is the city would you like to explore its data Chicago, New york city or Washington?").lower()
        if city.capitalize() in ["Chicago", "New york city", "Washington"]:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("What is the Month would you like to explore its data/n January, February, March, April, May, June or All?").lower()
        if month.capitalize() in ['January', 'February', 'March', 'April', 'May', 'June', 'All']:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("What is the Day would you like to explore its data/n Monday, Tuesday, Wednesday, Thursday, Friday, Suterday, Sunday, or All?").lower()
        if day.capitalize() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Suterday', 'Sunday', 'All']:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.capitalize()]
    
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        popular_month = df['month'].value_counts().idxmax()
        print('Most Frequent Start month:', popular_month)
        

    # TO DO: display the most common day of week
    if day == 'all':
        popular_day = df['day_of_week'].value_counts().idxmax()
        print('Most Frequent Start day:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Popular Start Station:  ', commonly_used_Start_Station)

    # TO DO: display most commonly used end station
    commonly_used_End_Station = df['End Station'].value_counts().idxmax()
    print('Most Popular End Etation:  ', commonly_used_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station']+" To "+ df['End Station']
    commonly_used_route = df['route'].value_counts().idxmax()
    print('Most Popular Route:  ', commonly_used_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time :  ',total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Average travel time :  ',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts().to_string()
    print('\nUser Types:\n',user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = pd.Series(df['Gender'].value_counts()).to_string()
        print('\nGender Counts: \n',gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year:  ',earliest_year)
    
        most_recent = df['Birth Year'].max()
        print('Most Recent Year:  ',most_recent)
    
        most_common = df['Birth Year'].value_counts().idxmax()
        print('Most Common Year:  ',most_common)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)
        
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        temp = 0
        while True:
            view_raw_data = input('\nWould you like to view 5 lines of raw data? Enter yes or no.\n')
            if view_raw_data.lower() == 'yes':
                print(df.head(temp+5))
                temp+=5
            else:
                break
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:




