#!/usr/bin/env python

import sys

# Read the first line as the header
header = sys.stdin.readline().strip()

# Split the header into columns assuming comma-separated values
columns = header.split(',')

# Find the index of the desired columns with case-sensitive matching
dew_point_temp_column = columns[9]
dew_point_temp_index = columns.index(dew_point_temp_column)

# Process each input value from standard input (stdin)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into columns assuming comma-separated values
    values = line.split(',')
    # Check if the line has the expected number of columns
    if len(values) >= dew_point_temp_index:
        # Extract the value from the desired column
        date_value = values[1]
        dew_point_temp_value = values[9]
        # Check if the wind speed value is valid
        merged_dew_point_temp_values=""
        if dew_point_temp_value and dew_point_temp_value != "-":
            try:
                for value in dew_point_temp_value.split('\t'):
                    merged_dew_point_temp_values += value.strip()

                merged_dew_point_temp_values=float(merged_dew_point_temp_values)

                # Emit the column name and value as key-value pair
                print('%s\t%s' % (date_value, merged_dew_point_temp_values))

            except ValueError:
                continue