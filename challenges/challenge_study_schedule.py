def study_schedule(permanence_period, target_time):
    counter = 0
    for usr_schedl in permanence_period:
        try:
            if usr_schedl[0] <= target_time <= usr_schedl[1] and target_time is not None:
                counter += 1
        except TypeError:
            return None

    return counter
