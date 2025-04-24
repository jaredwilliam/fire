from typing import List, Optional


class Account:
    """Base class for all types of accounts."""

    def __init__(self, name: str, balance: float = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdrawal(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Funds")

    def __str__(self) -> str:
        return f"{self.name}: ${self.balance:.2f}"


# Asset Classes
class CashAccount(Account):
    # checking account
    # savings account
    # money market account
    pass


class InvestmentAccount(Account):
    # stocks
    # bonds
    # mutual funds
    # exchange traded funds (ETFs)
    # Real Estate Invesment Trusts (REITs)
    # cryptocurrency
    pass


class RetirementAccount(Account):
    # individual retirement account
    # 401k, 403b
    # roth ira
    # pension plan
    # health savings account
    pass


class RealEstate(Account):
    # primary residence
    # rental property
    # vacation home
    # land
    pass


class PersonalProperty(Account):
    # vehicles
    # jewelry
    # art collections
    # other collectibles
    pass


class Receivable(Account):
    # accounts receivable
    # other receivables
    pass


# Liability Classes
class CurrentLiability(Account):
    # credit card debt
    # short-term loans
    # utility bills
    # rent or mortgage
    pass


class LongTermLiability(Account):
    # mortgage loans
    # car loans
    # student loans
    # personal loans
    pass


class OtherLiability(Account):
    # taxes payable
    # other payables
    pass


if __name__ == "__main__":
    checking = CashAccount("Checking Account", 1500)
    savings = CashAccount("Savings Account", 5000)
    mortgage = LongTermLiability("Mortgage", 200000)

    checking.deposit(500)
    savings.withdrawal(1000)
    print(checking)
    print(savings)
    print(mortgage)
