import csv

# open Titanic.csv file with csv.DictReader and read its content into a list of dictionary, titanic_data
titanic_data = []
with open('Titanic.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic_data.append(r)


def number_single_embarked_survived(place_embarked, age_threshold, titanic_data):
    """Returns the number of survived single women over age_threshold embarked at place_embarked
    (Single women are denoted by "Miss")

    >>> number_single_embarked_survived("Southampton", 40, titanic_data)
    4
    >>> number_single_embarked_survived("Cherbourg", 50, titanic_data)
    2
    >>> number_single_embarked_survived("Queenstown", 20, titanic_data)
    3
    """
    number_survived = 0
    for i in range(len(titanic_data)):
        first = titanic_data[i]['first']
        name_split = first.split(' ')
        pref = name_split[0]  # to get name's title
        gender = titanic_data[i]['gender']
        age = titanic_data[i]['age']
        embarked = titanic_data[i]['embarked']
        survived = titanic_data[i]['survived']
        if (pref == 'Miss') and (gender == 'F') and (embarked == place_embarked) and (survived == 'yes'):
            if age == '':  # if don't know age,just pass
                pass
            elif float(age) > age_threshold:
                number_survived += 1
    return number_survived


def class_survival_rate(passenger_class, titanic_data):
    """Returns the survival rate of a given passenger_class

    >>> survival_rate = class_survival_rate("1", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.63'
    >>> survival_rate = class_survival_rate("2", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.47'
    >>> survival_rate = class_survival_rate("3", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.24'
    """
    survival_in_class, all_in_class = 0, 0
    for i in range(len(titanic_data)):
        survived = titanic_data[i]['survived']
        pass_class = titanic_data[i]['class']
        if (pass_class == passenger_class) and (survived == 'yes'):  # if they in this class and survived
            survival_in_class += 1
            all_in_class += 1
        elif (pass_class == passenger_class) and (survived == 'no'):  # if they in this class but not survived
            all_in_class += 1
    return survival_in_class / all_in_class


def average_class_fare(passenger_class, titanic_data):
    """Returns the average fare for a given class, 1, 2 or 3

    >>> average = average_class_fare("1", titanic_data)
    >>> f"{average:.2f}"
    '84.15'
    >>> average = average_class_fare("2", titanic_data)
    >>> f"{average:.2f}"
    '20.66'
    >>> average = average_class_fare("3", titanic_data)
    >>> f"{average:.2f}"
    '13.68'
    """
    list_fare_in_class = []
    for i in range(len(titanic_data)):
        fare = float(titanic_data[i]['fare'])
        pass_class = titanic_data[i]['class']
        if pass_class == passenger_class:  # if they in this class
            list_fare_in_class.append(fare)  # append fare in list to get average of fare
    return sum(list_fare_in_class) / len(list_fare_in_class)


def gender_survival_number(passenger_gender, titanic_data):
    """Returns the number of survivors for a given gender, M (male) or F (female)

    >>> gender_survival_number('M', titanic_data)
    109
    >>> gender_survival_number('F', titanic_data)
    233
    """
    num_survived_gender = 0
    for i in range(len(titanic_data)):
        gender = titanic_data[i]['gender']
        survived = titanic_data[i]['survived']
        if (gender == passenger_gender) and (survived == 'yes'):  # to check gender that survived
            num_survived_gender += 1
    return num_survived_gender


def common_last_name(titanic_data):
    """Returns most common last name

    >>> common_last_name(titanic_data)
    'Andersson'
    """
    lastname_dict = {}
    for i in range(len(titanic_data)):
        lastname = titanic_data[i]['last']  # to get last name
        check_in_dict = lastname_dict.get(lastname, 'no have')
        if check_in_dict == 'no have':  # if they are first in dict
            lastname_dict[lastname] = 1
        else:  # if have this last name in dict
            lastname_dict[lastname] += 1
    list_num_in_family = list(lastname_dict.values())  # to get list of number of family
    max_num_family = max(list_num_in_family)
    max_num_family_lastname = None
    for last, num_in in lastname_dict.items():
        if num_in == max_num_family:
            max_num_family_lastname = last  # to change to family name that have maximum people
    return max_num_family_lastname


if __name__ == "__main__":
    import doctest

    doctest.testmod()
