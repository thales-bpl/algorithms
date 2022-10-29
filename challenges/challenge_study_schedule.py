def study_schedule(permanence_period, target_time):
    counter = 0
    for user in permanence_period:
        try:
            if user[0] <= target_time <= user[1] and target_time is not None:
                counter += 1
        except TypeError:
            return None

    return counter
