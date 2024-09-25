import time
class ATM():
    def v(self,usernames,passwords,pin,balance):
        user = input("Enter the username:")
        if user not in usernames:
            print("invalid user")
        else:  
            index = usernames.index(user)  
            pas = input("enter password:")
            if pas not in passwords[index]:
                for i in range(2,-1,-1):
                    print("incorrect password",i,"attempts left")
                    if i == 0:
                        print("maximum limit reached")
                        break
                        exit()
                    pas = input("enter password:")
            else:
                print("select an option:")
                print("1.Withdraw")
                print("2.deposit")
                print("3.Account balanace")
                print("4.change password")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    amount = int(input("enter the amount:"))
                    avail_balance = balance[index]-amount
                    pin_number = int(input("enter your pin:"))
                    if pin_number != pin[index]:
                        print("invalid pin")
                    else:
                        if amount<=balance[index]:
                            print("collect the amount")
                            time.sleep(2)
                            print("Available Balance:",avail_balance)
                        else:
                            print("Insufficient balance")
                elif choice == 2:
                    deposit_amount = int(input("Enter the amount:"))
                    av_balance = balance[index]+deposit_amount
                    pin_number = int(input("enter your pin:"))
                    if pin_number != pin[index]:
                        print("invalid pin")
                    else:
                        print("amount deposited successfully")
                        print("Available Balance:",av_balance)
                elif choice == 3:
                    pin_number = int(input("enter your pin:"))
                    if pin_number != pin[index]:
                        print("invalid pin")
                    else:
                        print("available balance:",balance[index])
                elif choice == 4:
                    pas = input("enter password:")
                    if pas not in passwords[index]:
                        print("incorrect password")
                    else:
                        new_password = input("Enter your new password:")
                        confirm_password = input("please confirm the password:")
                        while new_password != confirm_password:
                            print("Re-Enter the password")
                            new_password = input("Enter your new password:")
                            confirm_password = input("please confirm the password:")
                        else:
                            print("password changed successfully")
                            exit()
                else:
                    print("invalid selection")
usernames = ["isha08","deepika19","kavya30","kalyani"]
passwords = ["jahnavi18","kallu7","vaishu26","siri57"]
pin = [1357,2459,7020,3459]
balance = [2067,1579,7239]
B = ATM()
B.v(usernames,passwords,pin,balance)
