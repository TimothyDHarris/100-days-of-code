# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age_days =  (90 * 365) - (int(age) * 365)
age_weeks = (90 * 52) - (int(age) * 52)
age_months =  (90 * 12) - (int(age) * 12)

print(f"You have {age_days} days, {age_weeks} weeks, and {age_months} months left until you turn 90.")
