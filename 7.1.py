###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
#
age = int(input('Enter age: '))
no_tax = age <= 26  # Exempt if age is 26 or below

print(f'Exemption from paying taxes: {no_tax}')