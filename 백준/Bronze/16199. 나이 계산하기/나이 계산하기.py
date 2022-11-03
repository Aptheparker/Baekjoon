from datetime import datetime


def american_age(birthday, standard):
    if standard.month - birthday.month > 0:
        age = standard.year - birthday.year
    elif standard.month == birthday.month:
        if standard.day - birthday.day >= 0:
            age = standard.year - birthday.year
        else:
            age = standard.year - birthday.year - 1
    else:
        age = standard.year - birthday.year - 1
    
    return age
    
    
def korean_age(birthday, standard):
    age = standard.year - birthday.year + 1
    
    return age
    
def year_age(birthday, standard):
    
    age = standard.year - birthday.year
    
    return age


def three_ages_used_in_korea(birthday, standard):
    birth_year, birth_month, birth_day = map(int, birthday.split())
    standard_year, standard_month, standard_day = map(int, standard.split())
    
    birthday = datetime(year=birth_year, month=birth_month, day=birth_day)
    standard = datetime(year=standard_year, month=standard_month, day=standard_day)
    
    age_1 = american_age(birthday, standard)
    age_2 = korean_age(birthday, standard)
    age_3 = year_age(birthday, standard)
    
    return age_1, age_2, age_3


if __name__ == "__main__":
    birthday = input()
    standard = input()
    age_1, age_2, age_3 = three_ages_used_in_korea(birthday, standard)
    
    print(age_1)
    print(age_2)
    print(age_3)