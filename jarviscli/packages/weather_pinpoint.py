from colorama import Fore
from utilities.GeneralUtilities import print_say
import six
from . import mapps
from . import umbrella

def main(memory, self, s):
    branch = set()
    _main(memory, self, s, branch)
    with open('main@weather_pinpoint.py.branch', 'a') as branch_file:
        branch_file.write('total: %s\n' % str(31))
        branch_file.write('activated: %s\n' % str(len(branch)))
        branch_file.write('set: %s\n' % str(branch))
        branch_file.write('--------------\n')

def _main(memory, self, s, branch):
    location = memory.get_data('city')  # Will return None if no value
    if location is None:
        branch.add(19)
        city = mapps.get_location()['city']
        print_say("It appears you are in " +
                  city + " Is this correct? (y/n)", self, Fore.RED)
        if six.PY2:
            branch.add(24)
            i = raw_input()
        else:
            branch.add(27)
            i = input()
        if i == 'n' or i == 'no':
            branch.add(30)
            print_say("Enter Name of city: ", self)
            if six.PY2:
                branch.add(33)
                i = raw_input()
            else:
                branch.add(36)
                i = input()
            city = i
        city_found = True
        if s == 'umbrella':
            branch.add(41)
            umbrella.main(str(city))
        else:
            branch.add(44)
            city_found = mapps.weather(str(city))
        if city_found:
            branch.add(47)
            memory.update_data('city', city)
            memory.save()
    else:
        branch.add(51)
        loc = str(location)
        city = mapps.get_location()['city']
        if city != loc:
            branch.add(55)
            print_say("It appears you are in " + city +
                      ". But you set your location to " + loc, self, Fore.RED)
            print_say("Do you want weather for " +
                      city + " instead? (y/n)", self, Fore.RED)
            if six.PY2:
                branch.add(61)
                i = raw_input()
            else:
                branch.add(64)
                i = input()
            if i == 'y' or i == 'yes':
                branch.add(67)
                try:
                    print_say("Would you like to set " + city +
                              " as your new location? (y/n)", self, Fore.RED)
                    if six.PY2:
                        branch.add(72)
                        i = raw_input()
                    else:
                        branch.add(75)
                        i = input()
                    if i == 'y' or i == 'yes':
                        branch.add(78)
                        memory.update_data('city', city)
                        memory.save()
                    if s == 'umbrella':
                        branch.add(82)
                        umbrella.main(city)
                    else:
                        branch.add(85)
                        mapps.weather(city)
                    branch.add(87)
                except:
                    branch.add(89)
                    print_say("I couldn't locate you", self, Fore.RED)
            else:
                branch.add(92)
                try:
                    if s == 'umbrella':
                        branch.add(95)
                        umbrella.main(loc)
                    else:
                        branch.add(98)
                        mapps.weather(loc)
                    branch.add(100)
                except:
                    branch.add(102)
                    print_say("I couldn't locate you", self, Fore.RED)
        else:
            branch.add(105)
            try:
                if s == 'umbrella':
                    branch.add(108)
                    umbrella.main(loc)
                else:
                    branch.add(111)
                    mapps.weather(loc)
                branch.add(113)
            except:
                branch.add(115)
                print_say("I couldn't locate you", self, Fore.RED)
