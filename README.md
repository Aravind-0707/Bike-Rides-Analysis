# Divvy Bike Sharing Data Analysis

This project involves analyzing the Divvy bike sharing data for the first quarter of 2019 and 2020. The goal is to clean, process, and visualize the data to gain insights into bike usage patterns.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Data Analysis](#data-analysis)
- [Visualization](#visualization)
- [Authors](#authors)

## Installation

To run this project, ensure you have Python 3.x and the following packages installed:

```bash

pip install pandas numpy matplotlib seaborn.

```

## Usage

Load the data: The data for Q1 2019 and Q1 2020 is loaded into Pandas DataFrames.

Rename columns: Standardizes column names for consistency.

Combine datasets: Merges the two datasets into a single DataFrame.

Clean data: Drops unnecessary columns and formats data appropriately.

Add date-related columns: Adds columns for date, month, day, year, and day of the week.

Calculate ride length: Computes the duration of each ride in seconds.

Remove invalid rides: Filters out invalid rides.

Descriptive analysis: Performs descriptive statistics on ride length.

Aggregate data: Summarizes ride length by user type.

Visualization: Generates visualizations for number of rides and average ride duration by weekday and member type.

## Features

Data Cleaning: Standardizes column names, drops unnecessary columns, and formats date columns.

Data Analysis: Calculates ride length and performs descriptive statistics.

Visualization: Creates bar plots for ride count and average ride duration by weekday.

## Data-Analysis

Descriptive Analysis: Calculate mean, median, max, and min of ride lengths.

Aggregate Data: Summarize ride length by member_casual.

## Visualization

Number of Rides by Weekday:

``` python
sns.barplot(data=ride_counts, x='weekday', y='number_of_rides', hue='member_casual', dodge=True)
plt.title('Number of Rides by Member Type and Weekday')
plt.show()
```

Average Ride Duration by Weekday:

```python
sns.barplot(data=avg_ride_time, x='weekday', y='ride_length', hue='member_casual', dodge=True)
plt.title('Average Ride Duration by Member Type and Weekday')
plt.show()
```
## Capstone (average duration)

![img](https://github.com/Aravind-0707/Bike-Rides-Analysis/blob/main/capstone(average%20duration).png)


## Aapstone (no.of riders by rider type)
![img](https://github.com/Aravind-0707/Bike-Rides-Analysis/blob/main/capstone%20(no.of%20riders%20by%20rider%20type).png)

## Authors

Aravi

This `README.md` should give a clear overview of your project and guide users through installation, usage, and the various features. How does that look?
