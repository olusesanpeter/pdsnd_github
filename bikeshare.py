import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()
    city = city.lower()
    
    while city not in ['chicago', 'new york city', 'washington']:
        print('\nYour input is invalid, Please try again.\n')
        city = input('Choose a city between Chicago, New York City and Washington: ').lower()
        city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nChoose a month between January and June you want data for. Please enter \'all\' if you would like to see all months\n').lower()
    
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print('\nYour input is invalid, Please try again.\n')
        month = input('Choose a month between January and June you want data for. Please enter \'all\' if you would like to see all months').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nChoose a day of the week you want data for. Please enter \'all\' if you would like to see all days\n').lower()
    
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print('\nYour input is invalid, Please try again.\n')
        day = input('Choose a day of the week you want data for. Please enter \'all\' if you would like to see all days').lower()

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
        df - Pandas DataFrame containing city data filtered by month and day
    """

     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Converts the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracts month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common month: ', common_month)

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Day: ', common_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most Common Hour of Day: ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station: ', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End station: ', common_end_station)

    # display most frequent combination of start station and end station trip
    df['Trips'] = df['Start Station'] + ' - ' + df['End Station']

    common_trip = df['Trips'].mode()[0]
    print('Most Common Trip from Start Station to End Station: ', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time was {} seconds.'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time was {} seconds.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User Types: ', user_type)

    # Display counts of gender
    if 'Gender' in df:
        gender_type = df['Gender'].value_counts()
        print('Gender Types: ', gender_type)
    else:
        print('There\'s no gender data for this city.')
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_yob = df['Birth Year'].min()
        print('Earliest year of birth: ', earliest_yob)
    else:
        print('There\'s no birth year data for this city.')
    
    if 'Birth Year' in df:
        recent_yob = df['Birth Year'].max()
        print('Most recent year of birth: ', recent_yob)
    else:
        print('There\'s no birth year data for this city.')
    
    if 'Birth Year' in df:
        common_yob = df['Birth Year'].mode()
        print('Most common year of birth is: ', common_yob)
    else:
        print('There\'s no birth year data for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 additional rows of data if the user specifies that they would like to"""
    
    start_index = 0
    end_index = 5
    
    additional_data = input('\nWould you like to view the raw city data? Please enter yes or no.\n')
    
    while additional_data not in ['yes', 'no']:
        print('Your input is invalid, Please enter yes or no')
        additional_data = input('\nWould you like to view the raw city data? Please enter yes or no.\n')
        
    if additional_data == 'no':
        return
    elif additional_data == 'yes':
        print(df.iloc[start_index:end_index])
    
    display_more = input('\nWould you like to view more data? Enter yes or no.\n').lower()
    
    if display_more == 'no':
        return
    while display_more == 'yes':
            print(df.iloc[start_index + 5: end_index + 5])
            start_index += 5
            end_index += 5
            display_more = input('\nWould you like to view more data? Enter yes or no.\n').lower()
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
         


if __name__ == "__main__":
	main()