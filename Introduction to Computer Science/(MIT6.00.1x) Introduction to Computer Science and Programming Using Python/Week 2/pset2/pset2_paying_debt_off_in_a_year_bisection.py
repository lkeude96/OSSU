# Anything below here are for testing purpose only
balance = 3329
annualInterestRate = 0.2

# End of testing stuff
import math


def calcEndOfYearBalance(balance, annualInterestRate, monthlyPayment):
    """
    Calculates the credit card balance after one year for the given monthly payment

    :param balance: the outstanding balance on the credit card
    :param annualInterestRate: annual interest rate as a decimal
    :param monthlyPayment: minimum monthly payment rate as a decimal
    :return:
    """
    monthly_interest_rate = annualInterestRate / 12.0
    for month in range(12):
        balance -= monthlyPayment
        balance += monthly_interest_rate * balance
    return balance


def calculateMinFixedMonthlyPayment(balance, annualInterestRate):
    """
    Calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months

    :param balance: the outstanding balance on the credit card
    :param annualInterestRate: annual interest rate as a decimal
    """
    balance_with_interest = balance + (balance * annualInterestRate)

    monthly_payment = 0
    monthly_payment += int(
        math.ceil(((balance_with_interest / 13.0) - ((balance_with_interest / 13.0) % 10)) / 10.0) * 10)

    while calcEndOfYearBalance(balance, annualInterestRate, monthly_payment) > 0:
        monthly_payment += 10

    print "Lowest Payment: " + str(monthly_payment)


calculateMinFixedMonthlyPayment(balance, annualInterestRate)
