# -*- coding: utf-8 -*-

from datetime import datetime as dt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import re
def parse_number(string, numwords=None):
    branch = set()
    res = _parse_number(string, branch, numwords)
    with open('parse_number@textParser.py.branch', 'a') as branch_file:
        branch_file.write('total: %s\n' % str(13))
        branch_file.write('activated: %s\n' % str(len(branch)))
        branch_file.write('set: %s\n' % str(branch))
        branch_file.write('--------------\n')
    return res


def _parse_number(string, branch, numwords=None):
    """
    Parse the given string to an integer.

    This supports pure numerals with or without ',' as a separator between digets.
    Other supported formats include literal numbers like 'four' and mixed numerals
    and literals like '24 thousand'.
    :return: (skip, value) containing the number of words separated by whitespace,
             that were parsed for the number and the value of the integer itself.
    """
    if numwords is None:
        branch.add(29)
        numwords = {}
    if not numwords:
        branch.add(32)
        units = ["zero", "one", "two", "three",
                 "four", "five", "six", "seven", "eight", "nine", "ten",
                 "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                 "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty",
                "sixty", "seventy", "eighty", "ninety"]
        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):
            branch.add(43)
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            branch.add(46)
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            branch.add(49)
            numwords[word] = (10 ** (idx * 3 or 2), 0)

    skip = 0
    value = 0
    elements = string.replace(",", "").split()
    current = 0
    for d in elements:
        branch.add(57)
        number = d.split("-")
        for word in number:
            branch.add(60)
            if word not in numwords:
                branch.add(62)
                try:
                    scale, increment = (1, int(word))
                    branch.add(65)
                except ValueError:
                    branch.add(67)
                    value += current
                    return skip, value
            else:
                branch.add(71)
                scale, increment = numwords[word]
                if not current and scale > 100:
                    branch.add(74)
                    current = 1
            current = current * scale + increment
            if scale > 100:
                branch.add(78)
                value += current
                current = 0
        skip += 1
    value += current
    return skip, value

def parse_date(string):
    branch = set()
    res = _parse_date(string, branch)
    with open('parse_date@textParser.py.branch', 'a') as branch_file:
            branch_file.write('total: %s\n' % str(28))
            branch_file.write('activated: %s\n' % str(len(branch)))
            branch_file.write('set: %s\n' % str(branch))
            branch_file.write('--------------\n')
    return res

def _parse_date(string, branch):
    """
    Parse the given string for a date or timespan.

    The number for a timespan can be everything supported by parseNumber().

    Supported date formats:
        2017-03-22 and 17-03-22
        22.03.2017 and 22.03.17
    Supported time formats:
        17:30
        5:30PM
    Supported timespan formats:
        in one second/minute/hour/day/week/month/year
        next monday
    :return: (skip, time) containing the number of words separated by whitespace,
             that were parsed for the date and the date itself as datetime.
    """
    elements = string.split()
    parse_day = False
    parse_delta_value = False
    parse_delta_unit = 0
    delta_value = 0
    ret_date = dt.now().date()
    ret_time = dt.now().time()
    skip = 0
    for index, d in enumerate(elements):
        branch.add(101)
        if parse_day:
            branch.add(103)
            d += dt.today().strftime(" %Y %W")
            try:
                ret_date = dt.strptime(d, "%a %Y %W").date()
                branch.add(107)
            except ValueError:
                branch.add(109)
                try:
                    ret_date = dt.strptime(d, "%A %Y %W").date()
                    branch.add(112)
                except ValueError:
                    branch.add(114)
                    break
            if ret_date <= dt.now().date():
                branch.add(117)
                ret_date += timedelta(days=7)
            parse_day = False
        elif parse_delta_value:
            branch.add(121)
            parse_delta_unit, delta_value = parse_number(
                " ".join(elements[index:]))
            parse_delta_value = False
        elif parse_delta_unit:
            branch.add(126)
            new_time = dt.combine(ret_date, ret_time)
            if "year" in d:
                branch.add(129)
                ret_date += relativedelta(years=delta_value)
            elif "month" in d:
                branch.add(132)
                ret_date += relativedelta(months=delta_value)
            elif "week" in d:
                branch.add(135)
                ret_date += timedelta(weeks=delta_value)
            elif "day" in d:
                branch.add(138)
                ret_date += timedelta(days=delta_value)
            elif "hour" in d:
                branch.add(141)
                new_time += timedelta(hours=delta_value)
                ret_date = new_time.date()
                ret_time = new_time.time()
            elif "minute" in d:
                branch.add(146)
                new_time += timedelta(minutes=delta_value)
                ret_date = new_time.date()
                ret_time = new_time.time()
            elif "second" in d:
                branch.add(151)
                new_time += timedelta(seconds=delta_value)
                ret_date = new_time.date()
                ret_time = new_time.time()
            elif parse_delta_unit == 1:
                branch.add(156)
                print("Missing time unit")
            parse_delta_unit -= 1

        elif re.match("^[0-9]{2}-[0-1][0-9]-[0-3][0-9]$", d):
            branch.add(161)
            ret_date = dt.strptime(d, "%y-%m-%d").date()
        elif re.match("^[1-9][0-9]{3}-[0-1][0-9]-[0-3][0-9]$", d):
            branch.add(164)
            ret_date = dt.strptime(d, "%Y-%m-%d").date()
        elif re.match("^[0-3][0-9]\.[0-1][0-9]\.[0-9]{2}$", d):
            branch.add(167)
            ret_date = dt.strptime(d, "%d.%m.%y").date()
        elif re.match("^[0-3][0-9]\.[0-1][0-9]\.[1-9][0-9]{3}$", d):
            branch.add(170)
            ret_date = dt.strptime(d, "%d.%m.%Y").date()

        elif re.match("^[0-1][0-9]:[0-5][0-9][AP]M$", d):
            branch.add(174)
            ret_time = dt.strptime(d, "%I:%M%p").time()
        elif re.match("^[1-9]:[0-5][0-9][AP]M$", d):
            branch.add(177)
            ret_time = dt.strptime("0" + d, "%I:%M%p").time()
        elif re.match("^[0-2][0-9]:[0-5][0-9]$", d):
            branch.add(180)
            ret_time = dt.strptime(d, "%H:%M").time()
        elif re.match("^[1-9]:[0-5][0-9]$", d):
            branch.add(183)
            ret_time = dt.strptime("0" + d, "%H:%M").time()

        elif d == "next":
            branch.add(187)
            parse_day = True
        elif d == "in" or d == "and":
            branch.add(190)
            parse_delta_value = True
        else:
            branch.add(193)
            break
        skip += 1
    return skip, dt.combine(ret_date, ret_time)
