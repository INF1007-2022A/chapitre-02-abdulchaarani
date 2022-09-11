import re

email = input("What's your email? ").strip()

# if "@" and '.' in email:
#   print("Valid")
# else:
#   print("Invalid")

# username, domain = email.split("@")

# # if (username) and ('.' in domain):
# if (username) and domain.endswith(".edu"):
#   print("Valid")
# else:
#   print("Invalid")

if re.search(r"^[^@]+@[^@]+\.edu$", email):
  print("Valid")
else:
  print("Invalid")