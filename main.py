def add_time(start, duration, day=None):
    start_hours = int(start.split(':')[0])
    start_minutes = int(start.split(':')[1][:2])
    start_meridian = start.split(':')[1][3:]
    
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1][:2])

    # Convert start time to 24-hour format
    if start_meridian == 'PM' and start_hours != 12:
        start_hours += 12
    elif start_meridian == 'AM' and start_hours == 12:
        start_hours = 0

    # Add duration
    total_hours = start_hours + duration_hours
    total_minutes = start_minutes + duration_minutes
    
    # Handle overflow of minutes
    if total_minutes >= 60:
        total_hours += total_minutes // 60
        total_minutes %= 60

    # Calculate days later
    days_later = total_hours // 24
    hours_later = total_hours % 24
    
    # Determine AM/PM and convert to 12-hour format
    if hours_later == 0:
        hours_later = 12
        meridian = 'AM'
    elif hours_later < 12:
        meridian = 'AM'
    elif hours_later == 12:
        meridian = 'PM'
    else:
        hours_later -= 12
        meridian = 'PM'
    
    # Handle the day of the week
    if day:
        days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        day_index = days_of_week.index(day.capitalize())
        final_day_index = (day_index + days_later) % 7
        final_day = days_of_week[final_day_index]
    else:
        final_day = None

    # Format the result
    formatted_time = f'{hours_later}:{total_minutes:02d} {meridian}'
    if final_day:
        formatted_time += f', {final_day}'
    
    # Add the day info if needed
    if days_later == 1:
        formatted_time += ' (next day)'
    elif days_later > 1:
        formatted_time += f' ({days_later} days later)'

    return formatted_time

# Testing the function
print(add_time('2:59 AM', '24:00', 'saturDay'))
