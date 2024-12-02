# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:07:55 2024

@author: aravi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load the data
q1_2019 = pd.read_csv("Divvy_Trips_2019_Q1.csv")
q1_2020 = pd.read_csv("Divvy_Trips_2020_Q1.csv")

# Rename columns to make them consistent
q1_2019 = q1_2019.rename(columns={
    'trip_id': 'ride_id',
    'bikeid': 'rideable_type',
    'start_time': 'started_at',
    'end_time': 'ended_at',
    'from_station_name': 'start_station_name',
    'from_station_id': 'start_station_id',
    'to_station_name': 'end_station_name',
    'to_station_id': 'end_station_id',
    'usertype': 'member_casual'
})

# Convert ride_id and rideable_type to strings
q1_2019['ride_id'] = q1_2019['ride_id'].astype(str)
q1_2019['rideable_type'] = q1_2019['rideable_type'].astype(str)

# Combine datasets
all_trips = pd.concat([q1_2019, q1_2020], ignore_index=True)

# Drop unnecessary columns
all_trips = all_trips.drop(columns=['start_lat', 'start_lng', 'end_lat', 'end_lng', 'birthyear', 'gender', 'tripduration'], errors='ignore')

# Clean and reformat data
# Replace "Subscriber" with "member" and "Customer" with "casual"
all_trips['member_casual'] = all_trips['member_casual'].replace({'Subscriber': 'member', 'Customer': 'casual'})

# Add date-related columns
all_trips['date'] = pd.to_datetime(all_trips['started_at']).dt.date
all_trips['month'] = pd.to_datetime(all_trips['date']).dt.month
all_trips['day'] = pd.to_datetime(all_trips['date']).dt.day
all_trips['year'] = pd.to_datetime(all_trips['date']).dt.year
all_trips['day_of_week'] = pd.to_datetime(all_trips['date']).dt.day_name()

# Calculate ride_length in seconds
all_trips['ride_length'] = (pd.to_datetime(all_trips['ended_at']) - pd.to_datetime(all_trips['started_at'])).dt.total_seconds()

# Remove invalid rides
all_trips_v2 = all_trips[~((all_trips['start_station_name'] == "HQ QR") | (all_trips['ride_length'] < 0))]

# Descriptive analysis on ride_length
ride_length_stats = all_trips_v2['ride_length'].agg(['mean', 'median', 'max', 'min'])
print(ride_length_stats)

# Aggregate data
summary = all_trips_v2.groupby('member_casual')['ride_length'].agg(['mean', 'median', 'max', 'min'])
print(summary)

# Average ride time by member type and weekday
all_trips_v2['weekday'] = pd.to_datetime(all_trips_v2['started_at']).dt.day_name()
avg_ride_time = all_trips_v2.groupby(['member_casual', 'weekday'])['ride_length'].mean().reset_index()

# Visualizations
# Number of rides by weekday
ride_counts = all_trips_v2.groupby(['member_casual', 'weekday']).size().reset_index(name='number_of_rides')
sns.barplot(data=ride_counts, x='weekday', y='number_of_rides', hue='member_casual', dodge=True)
plt.title('Number of Rides by Member Type and Weekday')
plt.show()

# Average ride duration by weekday
sns.barplot(data=avg_ride_time, x='weekday', y='ride_length', hue='member_casual', dodge=True)
plt.title('Average Ride Duration by Member Type and Weekday')
plt.show()

# Export summary to CSV
avg_ride_time.to_csv('avg_ride_length.csv', index=False)
