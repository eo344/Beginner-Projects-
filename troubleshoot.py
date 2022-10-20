import random

number = random.randint(10000, 99999)
print(
    "Please answer these questions with either y or n unless advised otherwise"
)

q1 = input('Is your phone broken?: \n').lower()
if q1 == 'y' or q1 == 'yes':
    q2 = input('Is the phone turning on: \n').lower()
    if q2 == 'n' or q2 == 'no':
        q3 = input('Is it of suitable charge: \n').lower()
        if q3 == 'y' or q3 == 'yes':
            q4 = ('Is the screen cracked?: \n').lower()
            if q4 == 'y' or q4 == 'yes':
                print('bring it in for repair')
            else:
                q5 = input('Are there any missing pieces: \n').lower()
                if q5 == 'yes' or q5 == 'y':
                    q6 = input('What parts are missing?: \n')
                    print('Bring it in and we will replace the %s for you' %
                          q6)
                elif q5 == 'no' or q5 == 'n':
                    print(
                        "'Here's a code for you to use to get extended help:\n"
                    )
                    print(number)
        else:
            print('Charge it first')
    else:
        q4 = ('Is the screen cracked?: \n').lower()
        if q4 == 'y' or q4 == 'yes':
            print('bring it in for repair')
        else:
            q5 = input('Are there any missing pieces: \n').lower()
            if q5 == 'yes' or q5 == 'y':
                q6 = input('What parts are missing?: \n')
                print('Bring it in and we will replace the %s for you' % q6)
            elif q5 == 'no' or q5 == 'n':
                print("'Here's a code for you to use to get extended help:\n")
                print(number)
else:
    print('Then why are you here?')
