def check_month(month: int):
    if 0 < month <= 12:
        if month == 12 or month == 1 or month == 2:
            result = 'Зима'
        elif month == 3 or month == 4 or month == 5:
            result = 'Весна'
        elif month == 6 or month == 7 or month == 8:
            result = 'Лето'
        else:
            result = 'Осень'
    else:
        result = 'Некорректный номер месяца'
    return result


def reverse(string: str) -> str:
    return string[::-1].lower()

def vote(votes):
    count = 0
    for vote in votes:
        count_vote = votes.count(vote)
        if count_vote > count:
            count = count_vote
            result = vote
    return result

def check_auth(login: str, password: str):

    if login == 'admin' and password == 'password':
        result = 'Добро пожаловать'
    else:
        result = 'Доступ ограничен'

    return result