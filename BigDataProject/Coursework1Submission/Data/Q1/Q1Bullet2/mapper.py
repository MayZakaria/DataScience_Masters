#!/usr/bin/env python

import sys

# Read the first line as the header
header = sys.stdin.readline().strip()

# Split the header into columns assuming comma-separated values
columns = header.split(',')

# Find the index of the desired columns with case-sensitive matching
relative_humidity_column = columns[11]
relative_humidity_index = columns.index(relative_humidity_column)

# Process each input value from standard input (stdin)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into columns assuming comma-separated values
    values = line.split(',')
    # Check if the line has the expected number of columns
    if len(values) >= relative_humidity_index:
        # Extract the value from the desired column
        date_value = values[1]
        relative_humidity_value = values[relative_humidity_index]
        # Check if the wind speed value is valid
        merged_relative_humidity_values=""
        if relative_humidity_value and relative_humidity_value != "-":
            try:
                for value in relative_humidity_value.split('\t'):
                    merged_relative_humidity_values += value.strip()


                merged_relative_humidity_values=int(merged_relative_humidity_values)
                # Emit the column name and value as key-value pair
                print('%s\t%s' % (date_value, merged_relative_humidity_values))

            except ValueError:
                continue