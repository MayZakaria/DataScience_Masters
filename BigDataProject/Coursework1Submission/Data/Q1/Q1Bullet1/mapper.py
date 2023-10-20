#!/usr/bin/env python

import sys

# Read the first line as the header
header = sys.stdin.readline().strip()

# Split the header into columns assuming comma-separated values
columns = header.split(',')

# Find the index of the desired columns with case-sensitive matching
wind_speed_column = columns[12]
wind_speed_index = columns.index(wind_speed_column)

# Process each input value from standard input (stdin)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into columns assuming comma-separated values
    values = line.split(',')
    # Check if the line has the expected number of columns
    if len(values) >= wind_speed_index:
        # Extract the values from the desired columns
        date_value = values[1]
        wind_Speed_value = values[wind_speed_index]

        merged_wind_speed_values=""
        
        # Check if the wind speed value is valid
        if wind_Speed_value and wind_Speed_value != "-":
            try:
                for value in wind_Speed_value.split('\t'):
                    merged_wind_speed_values += value.strip()

                merged_wind_speed_values=int(merged_wind_speed_values)
                # Emit the column name and value as key-value pair
                print('%s\t%s' % (date_value, merged_wind_speed_values))
            except ValueError:
                continue



 