# Anything below here are for testing purpose only
balance = 999999
annualInterestRate = 0.18


# End of testing stuff

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
    epsilon = 0.01

    monthly_payment_lower_bound = balance / 12.0
    monthly_payment_upper_bound = (balance * (1 + annualInterestRate / 12) ** 12) / 12.0
    monthly_payment_mid = (monthly_payment_upper_bound + monthly_payment_lower_bound) / 2

    end_of_year_balance = calcEndOfYearBalance(balance, annualInterestRate, monthly_payment_mid)

    while abs(end_of_year_balance) >= epsilon:
        if end_of_year_balance < 0:
            monthly_payment_upper_bound = monthly_payment_mid
        elif end_of_year_balance > 0:
            monthly_payment_lower_bound = monthly_payment_mid

        monthly_payment_mid = (monthly_payment_upper_bound + monthly_payment_lower_bound) / 2
        end_of_year_balance = calcEndOfYearBalance(balance, annualInterestRate, monthly_payment_mid)

    print "Lowest Payment: " + str(round(monthly_payment_mid, 2))


calculateMinFixedMonthlyPayment(balance, annualInterestRate)
