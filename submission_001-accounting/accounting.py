import user.authentication
import transactions.journal
#import banking.reconciliation
#import banking.fvb.reconciliation
#import banking.ubsa.reconciliation
import banking
import sys

def system_arguments():
    for i in range(1,len(sys.argv)):
        print(sys.argv[i])

def run_accounting():

    system_arguments()
    user.authentication.authenticate_user()

    transactions.journal.receive_income(100)
    transactions.journal.pay_expense(100)

    banking.reconciliation.do_reconciliation()

if __name__ == "__main__":
    run_accounting()
    #help("modules")
    #system_arguments()  