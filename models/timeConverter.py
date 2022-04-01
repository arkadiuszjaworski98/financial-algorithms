def convert_time(time_type, time):
    if time_type == 1:  # minutes
        return time / 525600

    elif time_type == 2:  # hours
        return time / 8760

    elif time_type == 3:  # days
        return time / 365

    elif time_type == 4:  # weeks
        return time / 52

    elif time_type == 5:  # months
        return time / 12

    else:
        return time
