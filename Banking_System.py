from random import randint
import datetime

# Bank
bank = {}
prefixed_no = 592000411000


# Creating Account
def accounts(name, address, dob, mobile_no, balance = 0):
  acc_no = len(bank) + prefixed_no + 1
  details = {
      'Name':name,
      'Address':address,
      'DOB':dob,
      'Pin':randint(1000,9999),
      'Mobile_no':mobile_no,
      'Balance':balance,
      'Transaction':[]
    }
  bank.setdefault(acc_no, details.copy())
  return acc_no, details


# Account Details
def acc_detail(accno):
  details = bank.get(accno)
  if details:
    print("Account Number:", accno)
    for key, value in details.items():
      print(f"{key}: {value}")
  else:
    print("Account not found.")


# Cash Deposite
def deposite(accno, amount):
  tr = {
      'tr_type':'cr',
      'datetime': datetime.datetime.now(),
      'amount': float(amount)
  }
  if accno in bank:
    bank[accno]['Balance'] += amount
    print(f"Deposit successful. Available balance: {bank[accno]['Balance']}")
    user_input = input("Print Transaction? yes/no:")
    if user_input == 'yes':
      bank[accno]['Transaction'].append(tr)
      tr_flds = bank[accno]['Transaction'][0].keys()
      for t in bank[accno]['Transaction'][::-1]:
        for v in t.values():
          print(v, end = " ")
        print()
    elif user_input == 'no':
      print("Thank You!")
  else:
    print("Invalid Account no!")


# Cash Withdraw
def withdraw(accno, amount):
  tr = {
      'tr_type':'dr',
      'datetime': datetime.datetime.now(),
      'amount': float(amount)
  }

  if accno in bank:
    bank[accno]['Balance'] -= amount
    print(f"Withdraw successful. Available balance: {bank[accno]['Balance']}")
    user_input = input("Print Transaction? yes/no:")
    if user_input == 'yes':
      bank[accno]['Transaction'].append(tr)
      tr_flds = bank[accno]['Transaction'][0].keys()
      for t in bank[accno]['Transaction'][::-1]:
        for v in t.values():
          print(v, end = " ")
        print()
    elif user_input == 'no':
      print("Thank You!")
  else:
    print("Invalid Account no!")


# Mini Statement
def mini_stmt(accno):
  print("------------Mini Statement------------")
  if accno in bank:
    tr_flds = bank[accno]['Transaction']
    for trans in bank[accno]['Transaction'][::-1]:
      for v in trans.values():
        print(v, end = ' ')
      print()
  else:
    print("Invalid Account No!")

  print(f"Available balance: {bank[accno]['Balance']}")

# Event Driven (Taking input from user)
while True:
  print("--------------------Bank--------------------")
  print("1. Create Account")
  print("2. Account Information")
  print("3. Deposite")
  print("4. Withdrawl")
  print("5. Mini Statement")
  print("6. Exit")

  choice = input("Enter a Choice: ")
  if choice == "1":
    acc_no = len(bank) + prefixed_no + 1
    print("Account number: ", acc_no)
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    dob = input("Enter your birth date: ")
    mobile_no = input("Enter your mobile no: ")
    accounts(name, address, dob, mobile_no)
    print("Account Created Successfully")

  elif choice == "2":
    details = input("Enter your account number: ")
    print(acc_detail(accno))

  elif choice == "3":
    accno = int(input("Enter your account number: "))
    amount = float(input("Enter amount to deposite: "))
    deposite(accno, amount)

  elif choice == "4":
    accno = int(input("Enter your account number: "))
    amount = float(input("Enter amount to withdraw: "))
    withdraw(accno, amount)

  elif choice == "5":
    accno = int(input("Enter your account number: "))
    mini_stmt(accno)

  elif choice == "6":
    print("Thank You. Visit Again! ")
    break

  else:
    print("Invalid Choice. please try again.")