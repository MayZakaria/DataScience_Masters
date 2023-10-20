#!/usr/bin/env python

import sys

# Read the first line as the header
header = sys.stdin.readline().strip()

# Split the header into columns assuming comma-separated values
columns = header.split(',')

# Find the index of the desired columns with case-sensitive matching
dry_bulb_temp_column = columns[8]
relative_humidity_column = columns[11]
wind_speed_column = columns[12]

dry_bulb_temp_index = columns.index(dry_bulb_temp_column)
relative_humidity_index = columns.index(relative_humidity_column)
wind_speed_index = columns.index(wind_speed_column)

# Process each input value from standard input (stdin)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into columns assuming comma-separated values
    values = line.split(',')

    # Check if the line has the expected number of columns
    if (len(values) >= dry_bulb_temp_index) and (len(values) >= relative_humidity_index) and (len(values) >= wind_speed_index):
        # Extract the value from the desired column
        date_value = values[1]
        dry_bulb_temp_value = values[dry_bulb_temp_index]
        relative_humidity_value = values[relative_humidity_index]
        wind_speed_value = values[wind_speed_index]

        # Check if the wind speed value is valid
        merged_dry_bulb_temp_values=""
        merged_relative_humidity_values=""
        merged_wind_speed_values=""

        if dry_bulb_temp_value and relative_humidity_value and wind_speed_value and dry_bulb_temp_value != "-" and relative_humidity_value != "-" and wind_speed_value != "-":
            try:
                for value in dry_bulb_temp_value.split('\t'):
                    merged_dry_bulb_temp_values += value.strip()

                for value in relative_humidity_value.split('\t'):
                    merged_relative_humidity_values += value.strip()

                for value in wind_speed_value.split('\t'):
                    merged_wind_speed_values += value.strip()

                merged_dry_bulb_temp_values=float(merged_dry_bulb_temp_values)
                merged_relative_humidity_values=float(merged_relative_humidity_values)
                merged_wind_speed_values=float(merged_wind_speed_values)
                
                # Emit the column name and value as key-value pair
                print('%s\t%s,%s,%s' % (date_value, merged_dry_bulb_temp_values,merged_relative_humidity_values,merged_wind_speed_values))

            except ValueError:
                continue