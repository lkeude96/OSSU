# Anything below here are for testing purpose only
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


# End of testing stuff

def payminimum(balance, annualInterestRate, monthlyPaymentRate):
    """
    Calculates the credit card balance after one year if a person only pays the minimum monthly payment

    :param balance: the outstanding balance on the credit card
    :param annualInterestRate: annual interest rate as a decimal
    :param monthlyPaymentRate: minimum monthly payment rate as a decimal
    """
    total_paid = 0
    monthly_interest_rate = annualInterestRate / 12.0
    for month in range(1, 12 + 1):
        minimum_monthly_payment = monthlyPaymentRate * balance
        total_paid += minimum_monthly_payment
        monthly_unpaid_balance = balance - minimum_monthly_payment
        updated_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        balance = updated_balance

        print "Month: " + str(month)
        print "Minimum monthly payment: " + str(round(minimum_monthly_payment, 2))
        print "Remaining balance: " + str(round(balance, 2))

    print "Total paid: " + str(round(total_paid, 2))
    print "Remaining balance: " + str(round(balance, 2))


payminimum(balance, annualInterestRate, monthlyPaymentRate)
