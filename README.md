Certainly! The provided Python program is a basic console-based login system that allows a user to attempt logging in with a username and password combination. Let's break down how the program works:

### Program Logic:
1. **Initialization:**
   - The correct username is set as `"MariyaStephen"`.
   - The correct password is set as `1011`.
   - `No_attempt` is set to `3`, representing the number of login attempts allowed.

2. **Login Attempt Loop:**
   - The program enters a `while` loop that continues as long as there are remaining login attempts (`No_attempt > 0`).

3. **User Input:**
   - The user is prompted to enter a username using `input("Enter the user name: ")`.

4. **Username Validation:**
   - If the entered username matches the correct username (`User == User_name`), the user is prompted to enter a password.

5. **Password Validation:**
   - If the entered password matches the correct password (`Password == Pin`), the program prints `"Login success"` and exits the loop using the `break` statement, allowing the user to successfully log in.

6. **Handling Incorrect Attempts:**
   - If the entered username or password is incorrect:
     - The `No_attempt` variable is decremented by 1.
     - The program provides feedback to the user based on the number of attempts left and the correctness of the entered credentials.
     - Different messages are displayed depending on the number of attempts remaining.

7. **Exception Handling:**
   - The program uses `try-except` blocks for error handling:
     - If the user enters a non-integer value for the password, a `ValueError` exception is caught, and the program prints `"Enter the password using numbers only"`.
     - If any other exception occurs, the generic `except` block catches it and prints `"Enter the credential in correct format"`, then breaks out of the loop.

8. **End of the Program:**
   - If the user successfully logs in or exceeds the maximum number of attempts, the program ends.

### Program Flow:
1. The user is prompted to enter a username.
2. If the username is correct, the user is prompted to enter a password.
3. If both the username and password are correct, the program prints `"Login success"` and the program ends.
4. If the username or password is incorrect, the user is informed about the remaining attempts.
5. If the user exceeds the allowed attempts or enters invalid inputs, appropriate error messages are displayed, and the program ends.

Please note that while this program provides a basic structure for a login system, it lacks security measures typically used in real-world applications, such as password hashing and proper user authentication protocols.
