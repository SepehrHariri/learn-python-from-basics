# Exercise Password Checker

username = input('Enter your username:\t')
password = input('Enter you password:\t')

length_password = len(password)
secret_password = length_password * '*'
print(f'Hey {username}, your password {secret_password} is {length_password}  letters long.')