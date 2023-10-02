User="MariyaStephen"
Pin=1011
No_attempt=3
while No_attempt>0:
  try:
    User_name=input("Enter the user name: ")
    if User_name==User:
      Password=int(input("Enter your password: "))
      if Password==Pin:
        print("Login sucess")
        break
      else:
        No_attempt=No_attempt-1
        if No_attempt==2:
          print("Entered password is incorrect. Please enter correct password! You have remaining ",No_attempt," attempts.")
        else:
          if No_attempt==1:
            print("Entered password is incorrect. Please enter correct password! You have remaining ",No_attempt," attempts. Otherewise your account will be blocked.")
          else:
            print("You have exceed your attempt! Your account is blocked.")
    else:
      No_attempt=No_attempt-1
      if No_attempt==2:
          print("Entered user name is incorrect. Please enter correct user name! You have remaining ",No_attempt," attempts.")
      else:
          if No_attempt==1:
            print("Entered user name is incorrect. Please enter correct user name! You have remaining ",No_attempt," attempts. Otherewise your account will be blocked.")
          else:
            print("You have exceed your attempt! Your account is blocked.")
  except ValueError:
    print("Enter the password using numbers only")
  except:
    print("Enter the credential in correct format")
    break
