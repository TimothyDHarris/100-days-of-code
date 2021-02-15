import datetime

print("Welcome to the RMD Calculator.")
birth_year = int(input("Please type in the year your client was born. (Format YYYY)\n"))
current_year = datetime.datetime.now().year
age = current_year - birth_year
if age <= 71:
  print("Your client is not old enough to have to take an RMD.\nAn RMD is only required if the client is 72 years or older by the end of this calendar year or if the cliet inherited an IRA account from someone would would be 72 years old this year.\nIf that is the case, this calculator is not set up to calculate an inherited IRA RMD.")
else:
  account_balance = float(input("What was the account balance for the account as of 12/31 of the last year?\n").replace(',', '').replace("$", ""))
  # single_client = input('The RMD can be complex so we need a few questions to make sure we do the math right. Is your client single.\nRespond "yes" or "no".\n').lower()
  if age == 72:
    age_factor = 25.6
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 73:
    age_factor = 24.7
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 74:
    age_factor = 23.8
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 75:
    age_factor = 22.9
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 76:
    age_factor = 22.0
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 77:
    age_factor = 21.2
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 78:
    age_factor = 20.3
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 79:
    age_factor = 19.5
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 80:
    age_factor = 18.7
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 81:
    age_factor = 17.9
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 82:
    age_factor = 17.1
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 83:
    age_factor = 16.3
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 84:
    age_factor = 15.5
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 85:
    age_factor = 14.8
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 86:
    age_factor = 14.1
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 87:
    age_factor = 13.4
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 88:
    age_factor = 12.7
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 89:
    age_factor = 12.0
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 90:
    age_factor = 11.4
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 91:
    age_factor = 10.8
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 92:
    age_factor = 10.2
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 93:
    age_factor = 9.6
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 94:
    age_factor = 9.1
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 95:
    age_factor = 8.6
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 96:
    age_factor = 8.1
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 97:
    age_factor = 7.6
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 98:
    age_factor = 7.1
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 99:
    age_factor = 6.7
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  elif age == 100:
    age_factor = 6.3
    RMD_unrounded = (account_balance / age_factor)
    RMD_rounded = round(RMD_unrounded, 2)
    RMD = "{:,}".format(RMD_rounded)
    print(f"The RMD is ${RMD}")
  else:
    print("Your client is over 100 years old.\nI have not put in the age factor for the age of your.")