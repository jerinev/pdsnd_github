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
	Three cities are being considered: Chicago,New York,Washington
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Enter city name:").lower()
    while city not in ['chicago','new york city','washington']:
        print("Not a valid city. Please enter again")
        city=input("Enter city name:").lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Enter month:").lower()
    while month not in ['all','january','february','march','april','may','june','july','august','september','october','november','december']:
        print("Not a valid month.")
        month=input("Enter a month:").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Enter day:").lower()
    while day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        print("Not a valid day.")
        day=input("Enter a day:").lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.User can choose to display all months or specific months.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    file_name=city+'.csv'
    print(file_name)
    df=pd.read_csv(file_name)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
   
    df['hour'] = df['Start Time'].dt.hour
  
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
       
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()
    print("Most common month is:",common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()
    print("Most common day of the week is:",common_day_of_week)
    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("Most common hour:",common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Common start station:",common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End'] = df['Start Station'] + ' ' + df['End Station']
    common_start_end_station = df['Start and End'].mode()[0]
    print("Frequent combination of start station and end station trip is:",common_start_end_station)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time:")
    print(df['Trip Duration'].sum())
    

    # TO DO: display mean travel time
    print("Mean travel time:")
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Count of user types:",df['User Type'].value_counts())
    try:
        # TO DO: Display counts of gender
        print("Count of gender:",df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    
        print("Earliest birth year:")
        print(df['Birth Year'].min())
        print("Most recent birth year:")
        print(df['Birth Year'].max())
        print("Most common year of birth")
        print(df['Birth Year'].mode()[0])
    except:
        print("Birth year/gender not present in the file")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_raw_data(raw_df):
    response=input("Do you want to view raw data?")
    start_pos=0
    end_pos=5
    while response == 'yes':
        
        print(raw_df.iloc[start_pos:end_pos])
        start_pos+=5
        end_pos+=5
        response = input("Do you want to view more records:")
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_df=load_data(city, month, day)
        get_raw_data(raw_df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
