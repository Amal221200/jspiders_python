from time import ctime
from colors import bcolors

ID = 'amal@123'
pin = 1234
balance = 1500
mobile_no = 3489247857
otp = 4545
mini_state = 'This is your history.\nYou deposited Rs.500 on Mon Aug 2 12:45:13 2022.'

print(f'{bcolors.BOLD}Hello...\nWelcome to ICICI Bank.{bcolors.ENDC}\n')

processing = True
while processing:
    user_id = input(f'{bcolors.BOLD}Enter your user id: {bcolors.ENDC}')
    user_pin = int(input(f'{bcolors.BOLD}Enter your pin: {bcolors.ENDC}'))
    if ID == user_id and pin == user_pin:
    # if ID == 'amal@123' and pin == 1234:
        options_processing = True
        while options_processing:
            print('These are the options available',
                  f'{bcolors.BOLD}1{bcolors.ENDC} to check balance',
                  f'{bcolors.BOLD}2{bcolors.ENDC} for withdrawal',
                  f'{bcolors.BOLD}3{bcolors.ENDC} for mini statement',
                  f'{bcolors.BOLD}4{bcolors.ENDC} to deposit',
                  f'{bcolors.BOLD}5{bcolors.ENDC} to change your pin',
                  f'{bcolors.BOLD}6{bcolors.ENDC} to change your mobile number',
                  f'{bcolors.BOLD}7{bcolors.ENDC} to exit',
                  sep='\n')

            option = int(
                input(f'{bcolors.UNDERLINE}Choose your option:{bcolors.ENDC} '))
            # code for checking balance
            if option == 1:
                print(
                    f'\n{bcolors.OKBLUE}Your current balance is {bcolors.UNDERLINE}Rs.{balance}.{bcolors.ENDC}\n')
            # code for withdrawal
            elif option == 2:
                withd_processing = True
                while withd_processing:
                    money_to_withd = int(
                        input(f'{bcolors.BOLD}Enter the money to withdraw:{bcolors.ENDC} '))

                    if money_to_withd % 100 != 0:
                        print(
                            f'\n{bcolors.WARNING}You must withdraw money in hundreds.{bcolors.ENDC}\n')
                    elif money_to_withd == 0:
                        print(
                            f'\n{bcolors.WARNING}Enter a valid balance.{bcolors.ENDC}\n')
                    elif money_to_withd > balance:
                        print(
                            f'\n{bcolors.FAIL}You have insufficient balance to perform this withdrawal.{bcolors.ENDC}\n')
                        withd_processing = False
                    elif money_to_withd <= balance:
                        balance -= money_to_withd
                        mini_state += f'\nYou withdrawn Rs.{money_to_withd} on {ctime()}.'
                        print(f'\n{bcolors.OKGREEN}You have successfully withdrawn {bcolors.UNDERLINE}Rs.{money_to_withd} on {ctime()}{bcolors.ENDC}{bcolors.OKGREEN}, and your current balance is Rs.{bcolors.UNDERLINE}{balance}{bcolors.ENDC}.\n')
                        withd_processing = False
            # code for mini statement
            elif option == 3:
                print(f'\n{bcolors.OKBLUE}{mini_state}{bcolors.ENDC}\n')
            # code for deposit
            elif option == 4:
                dep_processing = True
                while dep_processing:
                    money_to_dep = int(
                        input(f'{bcolors.BOLD}Enter the amount to deposit:{bcolors.ENDC} '))

                    if money_to_dep == 0:
                        print(
                            f'\n{bcolors.WARNING}Enter a valid amount.{bcolors.ENDC}\n')
                    elif money_to_dep % 10 != 0:
                        print(
                            f'\n{bcolors.WARNING}The amount should be a round figure like 10, 20, 30, 100, etc.{bcolors.ENDC}\n')
                    else:
                        balance += money_to_dep
                        mini_state += f'\nYou deposited Rs.{money_to_dep} on {ctime()}.'
                        print(
                            f'\n{bcolors.OKGREEN}You have successfully deposited {bcolors.UNDERLINE}Rs.{money_to_dep} on {ctime()}{bcolors.ENDC}{bcolors.OKGREEN}, and your current balance is {bcolors.UNDERLINE}Rs.{balance}.{bcolors.ENDC}\n')
                        dep_processing = False

            # code for change pin
            elif option == 5:
                otp_processing = True
                print(
                    f'\n{bcolors.OKBLUE}Your request to change the PIN has been initiated.\nWe have send you an OTP to proceed with this request.{bcolors.ENDC}\n')

                while otp_processing:
                    user_otp = int(
                        input(f'{bcolors.BOLD}Enter the 4 digit OTP that has been sent to your mobile number:{bcolors.ENDC} '))

                    if user_otp == otp:
                        otp_processing = False
                        new_pin_processing = True
                        while new_pin_processing:
                            new_pin_validating = True
                            confirm_pin_validating = True
                            while new_pin_validating:
                                new_pin = int(
                                    input(f'{bcolors.BOLD}Enter the new 4 digit pin: {bcolors.ENDC}'))
                                if len(str(new_pin)) != 4:
                                    print(
                                        f'\n{bcolors.WARNING}The pin should be four digits, try again.{bcolors.ENDC}\n')
                                else:
                                    new_pin_validating = False
                            while confirm_pin_validating:
                                confirm_pin = int(
                                    input(f'{bcolors.BOLD}Enter the new 4 digit pin again: {bcolors.ENDC}'))
                                if len(str(confirm_pin)) != 4:
                                    print(
                                        f'\n{bcolors.WARNING}The pin should be four digits, try again.{bcolors.ENDC}\n')
                                else:
                                    confirm_pin_validating = False
                            if new_pin == confirm_pin:
                                pin = new_pin
                                print(
                                    f'\n{bcolors.OKGREEN}Your PIN has been successfully changed.{bcolors.ENDC}\n')
                                new_pin_processing = False
                            else:
                                print(
                                    f'\n{bcolors.WARNING}The PIN doesn\'t match, try again.{bcolors.ENDC}\n')
                    else:
                        print(
                            f'\n{bcolors.WARNING}Enter the valid OTP.{bcolors.ENDC}\n')

            # code for changing mobile number
            elif option == 6:
                print(
                    f'\n{bcolors.OKBLUE}Your request to change the mobile number has been initiated.{bcolors.ENDC}\n')

                new_ph_no_proccesing = True
                while new_ph_no_proccesing:
                    user_ph_no = int(
                        input(f'{bcolors.BOLD}Enter your mobile no.:{bcolors.ENDC} '))

                    if len(str(user_ph_no)) == 10:
                        new_ph_no_proccesing = False
                        print(
                            f'\n{bcolors.OKBLUE}An OTP has been sent to your new mobile no.{bcolors.ENDC}\n')

                        mb_otp_processing = True
                        while mb_otp_processing:
                            user_otp = int(
                                input(f'{bcolors.BOLD}Enter the OTP:{bcolors.ENDC} '))
                            if user_otp == otp:
                                mb_otp_processing = False
                                mobile_no = user_ph_no
                                print(
                                    f'\n{bcolors.OKGREEN}Your mobile no. has been successfully changed.{bcolors.ENDC}\n')
                            else:
                                print(
                                    f'\n{bcolors.WARNING}Enter the valid otp, try again.{bcolors.ENDC}\n')
                    else:
                        print(
                            f'\n{bcolors.WARNING}Enter the valid mobile number.{bcolors.ENDC}\n')

            # code for exit
            elif option == 7:
                options_processing = False

            # code for invalid option
            else:
                print(f'\n{bcolors.WARNING}Enter a valid option.{bcolors.ENDC}\n')
                options_processing = True

        processing = False
    else:
        print(f'\n{bcolors.WARNING}Enter a valid user id and pin.{bcolors.ENDC}\n')
        processing = True

if not processing:
    print(f'\n{bcolors.BOLD}Thankyou for using our service. Please come again.{bcolors.ENDC}\n')
