'''
Check username password and login
'''
import random

# I define one expected user,

expected_user: str = 'Daniel'
expected_password: str = '1234'
expected_answer_1: str = 'Yes'
sold: int = 1000
actual_user = input('Please enter a valid user name: ')
assert actual_user == expected_user
actual_password = input('Please enter a valid password: ')
assert actual_password == expected_password
input('Press enter to login!')
print(f'Your sold is:{sold}')
# print(f'Your sold is:',sold, sep='---')


print(f'Do you want to proceed to withdraw money from your account?')
actual_user = input('Please type Yes or No: ')
assert expected_answer_1 == expected_answer_1

actual_user = input('Please press enter to select the desired amount to withrdaw'" ")
amount = int(input(' Withrdaw amount..'" "))
if amount <= 1000:
    print('please confirm')
elif amount > 1000:
    print('insuficient founds')
print('Transaction complete. Your new balance is')
print(sold - amount)
