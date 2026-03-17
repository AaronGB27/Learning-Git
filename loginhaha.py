creating_username = input("Enter a name: ").capitalize()
creating_pin = int(input("Enter a pin: "))
print("Enter your own credentials your username and pin to get the access")
user = input("Username: ").capitalize
pin = int("Pin: ")
if user == creating_username:
  if pin == creating_pin :
    print("Access allowed")
  else:
    print("Denied access")
else:
  print("Error username incorrect, Denied access")
