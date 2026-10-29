def detect_overeating(intake_list):
    avg = sum(intake_list) / len(intake_list)
    if intake_list[-1] > avg * 1.3:
        return True
    return False


def detect_low_activity(steps_list):
    avg = sum(steps_list) / len(steps_list)
    if avg < 5000:
        return True
    return False


def detect_sleep_deprivation(sleep_list):
    return sleep_list[-1] < 6