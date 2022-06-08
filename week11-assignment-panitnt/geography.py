import csv

# open Cities.csv file with csv.DictReader and read its content into a list of dictionary, cities_data
cities_data = []
with open('Cities.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)

# open Countries.csv file with csv.DictReader and read its content into a list of dictionary, countries_data
countries_data = []
with open('Countries.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries_data.append(r)


def min_max_temp(cities_data):
    """Returns a list whose first and second elements are the min and the max
    temperatures of all the cities in cities_data.
    """
    temps = []
    for r in cities_data:
        temps.append(float(r['temperature']))
    return [min(temps), max(temps)]


def country_list(cities_data):
    """Returns a list of all the countries represented in cities_data.
    """
    countries = []
    for r in cities_data:
        if r['country'] not in countries:
            countries.append(r['country'])
    return countries


def average_country_temp(cities_data):
    """
    Return a dictionary whose key:value pair is country name:its average temp.
    The size of the returned dictionary must equal the number of countries
    represented.

    Notes: the test results below are printed out with two decimal places to
    get around floating-point errors.

    >>> temp_dict = average_country_temp(cities_data)
    >>> for key in sorted(temp_dict):
    ...    print(f"{key} {temp_dict[key]:.2f}")
    Albania 15.18
    Andorra 9.60
    Austria 6.14
    Belarus 5.95
    Belgium 9.65
    Bosnia and Herzegovina 9.60
    Bulgaria 10.44
    Croatia 10.87
    Czech Republic 7.86
    Denmark 7.62
    Estonia 4.59
    Finland 3.49
    France 10.15
    Germany 7.87
    Greece 16.90
    Hungary 9.60
    Ireland 9.30
    Italy 13.47
    Latvia 5.27
    Lithuania 6.14
    Macedonia 9.36
    Moldova 8.41
    Montenegro 9.99
    Netherlands 8.76
    Norway 3.73
    Poland 7.25
    Portugal 14.47
    Romania 9.22
    Serbia 9.85
    Slovakia 8.48
    Slovenia 9.27
    Spain 14.24
    Sweden 3.59
    Switzerland 7.25
    Turkey 11.73
    Ukraine 7.42
    United Kingdom 8.65
    """
    countries = country_list(cities_data)  # to get list of country
    sum_tem_country = {}  # create to add country as keys and list of temperature as value
    for i in range(len(countries)):
        sum_tem_country[countries[i]] = []  # create to append data to this list in the next step
    for i in range(len(cities_data)):
        city_data = cities_data[i]
        tem, country = float(city_data['temperature']), city_data['country']  # to get temperature and country
        list_of_tem = sum_tem_country[country]  # to get value(list) in sum_tem_country dict
        list_of_tem.append(tem)  # append to list
    avg_tem_country = {}  # to create new dict that value is average of temperature
    for i in range(len(countries)):
        avg_tem = sum(sum_tem_country[countries[i]]) / len(sum_tem_country[countries[i]])  # find average
        avg_tem_country[countries[i]] = avg_tem
    return avg_tem_country


def country_max_diff_temperature(cities_data):
    """Returns a tuple with information about a country whose minimum and
    maximum city temperatures differ the most in the following format: (the
    country whose minimum and maximum city temperatures differ the most, min
    temperature, max temperature, max temperature - min temperature)

    Notes: the test results below are printed out with two decimal places to
    get around floating-point errors.

    >>> result = country_max_diff_temperature(cities_data)
    >>> type(result)
    <class 'tuple'>
    >>> country, temp_min, temp_max, temp_diff = result
    >>> f"{country} {temp_min:.2f} {temp_max:.2f} {temp_diff:.2f}"
    'Turkey 5.17 18.67 13.50'
    """
    min_tem, max_tem = min_max_temp(cities_data)  # get max-min
    str_max = str(max_tem)
    country_name = ''
    for i in range(len(cities_data)):
        if cities_data[i]['temperature'] == str_max:  # to check where is equal to str_max
            country_name = cities_data[i]['country']  # change to country name
    #  to get data of temperature of this country
    tem_country = [float(x['temperature']) for x in cities_data if x['country'] == country_name]
    min_tem_country = min(tem_country)  # find min temperature of this country
    return country_name, min_tem_country, max_tem, (max_tem - min_tem_country)


def western_eastern_most_cities(cities_data):
    """Returns a list of tuples with information about the westernmost and
    easternmost cities together with their associated countries in the
    following format:

    [(westernmost city, its country, its longitude), (easternmost city, its country, its longitude)]

    Notes: the test results below are printed out with two decimal places to
    get around floating-point errors.

    >>> results = western_eastern_most_cities(cities_data)
    >>> for city, country, lon in results:
    ...     print(f"{city} {country} {lon:.2f}")
    Lisbon Portugal -9.14
    Siirt Turkey 41.93
    """
    list_longitude = []
    for i in range(len(cities_data)):
        list_longitude.append(float(cities_data[i]['longitude']))  # append longitude to list
    max_long, min_long = max(list_longitude), min(list_longitude)  # and find min and max longitude
    west_city, east_city = '', ''
    west_country, east_country = '', ''
    for i in range(len(cities_data)):
        if cities_data[i]['longitude'] == f'{min_long}':
            west_city, west_country = cities_data[i]['city'], cities_data[i]['country']  # to find where is west
        elif cities_data[i]['longitude'] == f'{max_long}':
            east_city, east_country = cities_data[i]['city'], cities_data[i]['country']  # to find where is east
    return [(west_city, west_country, min_long), (east_city, east_country, max_long)]


def average_EU_city_temperature(cities_data, countries_data):
    """Returns a tuple with two elements: (the average temperature of all the
    cities in EU countries, the average temperature of all the cities not in
    EU countries)

    Notes: the test results below are printed out with two decimal places to
    get around floating-point errors.

    >>> result = average_EU_city_temperature(cities_data, countries_data)
    >>> type(result)
    <class 'tuple'>
    >>> eu, non_eu = result
    >>> f"{eu:.2f} {non_eu:.2f}"
    '9.69 9.03'
    """
    tem_in_eu = []  # create list to append temperature city that in EU
    tem_not_eu = []  # create list to append temperature city that not in EU
    for i in range(len(cities_data)):
        name = cities_data[i]['country']
        for j in range(len(countries_data)):
            if countries_data[j]['country'] == name:
                if countries_data[j]['EU'] == 'yes':  # to find that country is in EU or not
                    tem_in_eu.append(float(cities_data[i]['temperature']))
                elif countries_data[j]['EU'] == 'no':
                    tem_not_eu.append(float(cities_data[i]['temperature']))
    avg_in_eu, avg_not_eu = sum(tem_in_eu) / len(tem_in_eu), sum(tem_not_eu) / len(tem_not_eu)
    return avg_in_eu, avg_not_eu
