from colorama import Fore
from utilities.GeneralUtilities import print_say
import six
from . import mapps
from . import umbrella


def maps(loc, s):
    if s == 'umbrella':
        umbrella.main(str(loc))
        return True
    return mapps.weather(str(loc))


def main(memory, self, s):
    if six.PY2:
        inputfn = raw_input
    else:
        inputfn = input

    location = memory.get_data('city')  # Will return None if no value
    if location is None:
        city = mapps.get_location()['city']
        print_say("It appears you are in " +
                  city + " Is this correct? (y/n)", self, Fore.RED)
        i = inputfn()
        if i == 'n' or i == 'no':
            print_say("Enter Name of city: ", self)
            i = inputfn()
            city = i
        city_found = True
        city_found = maps(city, s)
        if city_found:
            memory.update_data('city', city)
            memory.save()
    else:
        loc = str(location)
        city = mapps.get_location()['city']
        if city != loc:
            print_say("It appears you are in " + city +
                      ". But you set your location to " + loc, self, Fore.RED)
            print_say("Do you want weather for " +
                      city + " instead? (y/n)", self, Fore.RED)
            i = inputfn()
            if i == 'y' or i == 'yes':
                try:
                    print_say("Would you like to set " + city +
                              " as your new location? (y/n)", self, Fore.RED)
                    i = inputfn()
                    if i == 'y' or i == 'yes':
                        memory.update_data('city', city)
                        memory.save()
                    maps(city, s)
                except:
                    print_say("I couldn't locate you", self, Fore.RED)
                return
        try:
            maps(loc, s)
        except:
            print_say("I couldn't locate you", self, Fore.RED)
