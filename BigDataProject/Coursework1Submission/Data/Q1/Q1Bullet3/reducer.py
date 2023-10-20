#!/usr/bin/env python

import sys

current_date = None
total_dew_point_temp = 0
total_squared_dew_point_temp = 0
count = 0

# Input comes from standard input (STDIN)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into key and value
    date, dew_point_temp = line.split("\t")

    # Convert dew_point_temp to float
    dew_point_temp = float(dew_point_temp)

    # Check if the current date is the same as the previous one
    if current_date is None:
       current_date = date

    if date != current_date:
        # Calculate mean and variance for the current key
        average_dew_point_temp = total_dew_point_temp / count
        variance = (total_squared_dew_point_temp / count) - (average_dew_point_temp ** 2)

        # Emit the result for the current date
        print(f"{current_date}\t{average_dew_point_temp}\t{variance}")


        # Reset the variables for the new key
        current_date = date
        total_dew_point_temp = 0
        total_squared_dew_point_temp = 0
        count = 0

    # Update the variables
    total_dew_point_temp += dew_point_temp     #sum of total 
    count += 1
    total_squared_dew_point_temp += dew_point_temp ** 2     #sum square

# Calculate and output the average for the last date
average_dew_point_temp = total_dew_point_temp / count
variance = (total_squared_dew_point_temp / count) - (average_dew_point_temp ** 2)

print(f"{current_date}\t{average_dew_point_temp}\t{variance}")