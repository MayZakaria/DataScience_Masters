#!/usr/bin/env python

import sys

# Initialize variables to hold the column data
dry_bulb_temp_values = []
relative_humidity_values = []
wind_speed_values = []
n=0

# Process each input value from standard input (stdin)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into key and value
    date, values = line.split("\t")

    # Convert values to float and split them into separated columns
    dry_bulb_temp, relative_humidity, wind_speed =  values.split(',')
    dry_bulb_temp=float(dry_bulb_temp)
    relative_humidity=float(relative_humidity)
    wind_speed=float(wind_speed)

    # Append the values to the respective lists
    dry_bulb_temp_values.append(dry_bulb_temp)
    relative_humidity_values.append(relative_humidity)
    wind_speed_values.append(wind_speed)

    n += 1

# Calculate the correlation matrix

# Calculate the sum of each column
relative_humidity_sum = sum(relative_humidity_values)
wind_speed_sum = sum(wind_speed_values) 
dry_bulb_temp_sum = sum(dry_bulb_temp_values) 


# Calculate the sum of products
sum_relative_humidity_wind_speed = sum(relative_humidity_values[i] * wind_speed_values[i] for i in range(n))
sum_relative_humidity_dry_bulb_temp = sum(relative_humidity_values[i] * dry_bulb_temp_values[i] for i in range(n))
sum_wind_speed_dry_bulb_temp = sum(wind_speed_values[i] * dry_bulb_temp_values[i] for i in range(n))

# Calculate the sum of squares
sum_relative_humidity_square = sum(relative_humidity_values[i] * relative_humidity_values[i] for i in range(n))
sum_wind_speed_square = sum(wind_speed_values[i] * wind_speed_values[i] for i in range(n))
sum_dry_bulb_temp_square = sum(dry_bulb_temp_values[i] * dry_bulb_temp_values[i] for i in range(n))

# Calculate the correlation coefficients
correlation_matrix = []
correlation_matrix.append([
    1.0,
    (sum_relative_humidity_wind_speed - (relative_humidity_sum * wind_speed_sum)/n) / (( sum_relative_humidity_square - (relative_humidity_sum * relative_humidity_sum)/n) * ( sum_wind_speed_square - (wind_speed_sum * wind_speed_sum)/n)) ** 0.5,
    (sum_relative_humidity_dry_bulb_temp - (relative_humidity_sum * dry_bulb_temp_sum)/n) / (( sum_relative_humidity_square - (relative_humidity_sum * relative_humidity_sum)/n) * ( sum_dry_bulb_temp_square - (dry_bulb_temp_sum * dry_bulb_temp_sum)/n)) ** 0.5
])
correlation_matrix.append([
    (sum_relative_humidity_wind_speed - (relative_humidity_sum * wind_speed_sum)/n) / ((sum_relative_humidity_square - (relative_humidity_sum * relative_humidity_sum)/n) * (sum_wind_speed_square - (wind_speed_sum * wind_speed_sum)/n)) ** 0.5,
    1.0,
    (sum_wind_speed_dry_bulb_temp - (wind_speed_sum * dry_bulb_temp_sum)/n) / ((sum_wind_speed_square - (wind_speed_sum * wind_speed_sum)/n) * (sum_dry_bulb_temp_square - (dry_bulb_temp_sum * dry_bulb_temp_sum)/n)) ** 0.5
])
correlation_matrix.append([
    (sum_relative_humidity_dry_bulb_temp - (relative_humidity_sum * dry_bulb_temp_sum)/n) / ((sum_relative_humidity_square - (relative_humidity_sum * relative_humidity_sum)/n) * (sum_dry_bulb_temp_square - (dry_bulb_temp_sum * dry_bulb_temp_sum)/n)) ** 0.5,
    (sum_wind_speed_dry_bulb_temp - (wind_speed_sum * dry_bulb_temp_sum)/n) / ((sum_wind_speed_square - (wind_speed_sum * wind_speed_sum)/n) * (sum_dry_bulb_temp_square - (dry_bulb_temp_sum * dry_bulb_temp_sum)/n)) ** 0.5,
    1.0
])

# Output the correlation matrix
for row in correlation_matrix:
    print('\t\t\t\t'.join(map(str, row)))
      