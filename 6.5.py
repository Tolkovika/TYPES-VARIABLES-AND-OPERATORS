###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
formatted_phone = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
print(f"Phone number: {formatted_phone}")