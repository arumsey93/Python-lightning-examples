
# * Write a function that takes a list, a number, and a string as args.
# * The string parameter should have a default value.
# * In the function body, loop over the list and print the items, each one prefaced by the value of the string argument
# * One example output might then be "I have visited the city of San Francisco" if "San Francisco" was an item in the list, 
# and the string argument was "I have visited the city of "
# * Try it out! Execute the function both with and without passing in a value for the string parameter


def travel_sites(cities, str="I have visited the city of "):
    for city in cities:
        print(f'{str} {city}')

travel_sites(["San Francisco", "Boston", "Sandusky"])
travel_sites(["Duluth", "Boring", "Paris"], "I have not visited this loser place: ")