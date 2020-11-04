from user import authentication
from transactions import journal
import banking
from sys import argv

if __name__ == "__main__":
    amount = 100

    for i in range(1,len(argv)):
        print(argv[i])

    authentication.authenticate_user()
    journal.receive_income(amount)
    journal.pay_expense(amount)
    banking.reconciliation.do_reconciliation()
