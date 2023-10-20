#!/usr/bin/env python

import sys

current_date = None
min_relative_humidity = float('inf')

# Process each input line from standard input (stdin)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into key and value assuming tab-separated values
    date, relative_humidity = line.split('\t')
    relative_humidity = int(relative_humidity)

    # Check if the date has changed
    if current_date is None:
       current_date = date

    if current_date != date:
        # Emit the result for the previous date
        if min_relative_humidity != float('inf'):
           print(f'{current_date}\t{min_relative_humidity}')

        # Reset the variables for the new date
        current_date = date
        min_relative_humidity = float('inf')

    # Update the min relative humidity
    min_relative_humidity = min(min_relative_humidity, relative_humidity)

    
# Emit the result for the last date
if min_relative_humidity != float('inf'):
    print(f'{current_date}\t{min_relative_humidity}')