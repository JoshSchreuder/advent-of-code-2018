import re
import itertools
from datetime import datetime, timedelta


def asleep(load_shifts):
    shifts = load_shifts()
    shifts.sort()

    guard_id = None
    fell_asleep_at = None
    woke_up_at = None

    total_asleep = {}
    times_asleep = {}

    for shift in shifts:
        if "begins shift" in shift:
            match = re.search('#(\d+)', shift)
            guard_id = int(match.group(1))
        elif "falls asleep" in shift:
            fell_asleep_at = parse_mins(shift)
        elif "wakes up" in shift:
            woke_up_at = parse_mins(shift)
            total_asleep.setdefault(guard_id, 0)
            total_asleep[guard_id] += woke_up_at - fell_asleep_at

            times_asleep.setdefault(guard_id, {})

            for i in range(fell_asleep_at, woke_up_at):
                times_asleep[guard_id].setdefault(i, 0)
                times_asleep[guard_id][i] += 1

    most_sleepy = max(total_asleep, key=total_asleep.get)
    times_asleep_for_most_sleepy = times_asleep[most_sleepy]
    time_most_asleep = max(
        times_asleep_for_most_sleepy, key=times_asleep_for_most_sleepy.get)

    return most_sleepy * time_most_asleep


def parse_mins(shift):
    match = re.search('\d+:(\d+)', shift)
    return int(match.group(1))
