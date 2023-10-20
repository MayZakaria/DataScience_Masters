#!/usr/bin/env python

import sys

current_date = None
min_wind_speed = float('inf')
max_wind_speed = float('-inf')

# Process each input line from standard input (stdin)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into key and value assuming tab-separated values
    date, wind_speed = line.split('\t')
    print(wind_speed)
    wind_speed = int(wind_speed)

    # Check if the date has changed
    if current_date is None:
#        print("current_date is None")
       current_date = date

    if current_date != date:
        # Emit the result for the previous date
        if min_wind_speed != float('inf') and max_wind_speed != float('-inf'):
           print(f'{current_date}\t{max_wind_speed - min_wind_speed}')

        # Reset the variables for the new date
        current_date = date
        min_wind_speed = float('inf')
        max_wind_speed = float('-inf')

    # Update the min and max wind speeds
    min_wind_speed = min(min_wind_speed, wind_speed)
    max_wind_speed = max(max_wind_speed, wind_speed)

    
# Emit the result for the last date
if min_wind_speed != float('inf') and max_wind_speed != float('-inf'):
    print(f'{current_date}\t{max_wind_speed - min_wind_speed}')



