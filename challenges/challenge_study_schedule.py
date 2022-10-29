def study_schedule(permanence_period, target_time):
    counter = 0
    for user_schedule in permanence_period:
        try:
            if user_schedule[0] <= target_time <= user_schedule[1] and target_time is not None: counter += 1
        except TypeError:
            return None

    return counter
