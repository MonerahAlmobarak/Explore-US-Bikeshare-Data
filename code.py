import time
import pandas as pd
import numpy as np
import calendar as cal

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """Asks user to specify a city, month, and day to analyze."""
    print("Hello! Let's explore some US bikeshare data!")

    # Get city input
    while True:
        city = input("Choose a city: Chicago, New York City, or Washington:\n").lower()
        if city in CITY_DATA:
            break
        print("Invalid input. Please choose a valid city.")

    # Get month input
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Choose a month (January to June) or 'all':\n").lower()
        if month in valid_months:
            break
        print("Invalid input. Please enter a valid month.")

    # Get day input
    valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Choose a day of the week or 'all':\n").lower()
        if day in valid_days:
            break
        print("Invalid input. Please enter a valid day.")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day."""
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday

    if month != 'all':
        month_num = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Month'] == month_num]

    if day != 'all':
        day_num = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'].index(day)
        df = df[df['Weekday'] == day_num]

    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Most common month
    if 'Month' in df:
        common_month = df['Month'].mode()[0]
        print(f"Most Common Month: {cal.month_name[common_month]}")
    
    # Most common day of week
    if 'Weekday' in df:
        common_day = df['Weekday'].mode()[0]
        print(f"Most Common Day: {cal.day_name[common_day]}")

    # Most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print(f"Most Common Start Hour: {common_hour}:00")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("Most Common Start Station:", df['Start Station'].mode()[0])
    print("Most Common End Station:", df['End Station'].mode()[0])

    df['Trip'] = df['Start Station'] + " -> " + df['End Station']
    print("Most Frequent Trip:", df['Trip'].mode()[0])

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()
    mean_duration = df['Trip Duration'].mean()

    print(f"Total Travel Time: {total_duration / 3600:.2f} hours")
    print(f"Average Travel Time: {mean_duration / 60:.2f} minutes")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("\nUser Types:")
    print(df['User Type'].value_counts())

    if city != 'washington':
        if 'Gender' in df:
            print("\nGender Distribution:")
            print(df['Gender'].value_counts())

        if 'Birth Year' in df:
            print("\nBirth Year Stats:")
            print("Earliest:", int(df['Birth Year'].min()))
            print("Most Recent:", int(df['Birth Year'].max()))
            print("Most Common:", int(df['Birth Year'].mode()[0]))
    else:
        print("\nNo gender or birth year data for Washington.")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)


def raw_data(df):
    """Displays 5 lines of raw data at a time upon user request."""
    i = 0
    while True:
        show = input("\nWould you like to see 5 lines of raw data? Enter yes or no: ").lower()
        if show == 'yes':
            print(df.iloc[i:i+5])
            i += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input("\nWould you like to restart? Enter yes or no: ").lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
    main()
