
from datetime import datetime as dt

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(dt.today())
    print(dt.now().strftime("%d. %B. %Y. %A"))









