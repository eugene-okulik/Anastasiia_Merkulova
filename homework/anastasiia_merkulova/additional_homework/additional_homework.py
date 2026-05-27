def check_age(age):
    age = input('Enter your age: ')
    if not age.isdigit():
        return "not number"
    else:
        return int(age)


def check_age_category(age):
    result = {}
    if age > 0 and age <= 2:
        result['status'] = 'error'
        result['category'] = 'baby'
        result['can_vote'] = False
    elif age > 2 and age <= 13:
        result['status'] = 'error'
        result['category'] = 'child'
        result['can_vote'] = False
    elif age > 13 and age <= 17:
        result['status'] = 'error'
        result['category'] = 'teenager'
        result['can_vote'] = False
    else:
        result['status'] = 'success'
        result['category'] = 'adult'
        result['can_vote'] = True
    return result


age = check_age(8)

if age == "not number":
    print("not number")
else:
    print(age)
    print(check_age_category(age))


