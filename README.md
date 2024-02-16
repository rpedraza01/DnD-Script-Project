# Script Summary:
1. People can add any name they want.
2. Allow people to choose their race, class, and background or allow the script to randomly choose their race, class, and background.
3. The script will simulate rolling four 6-sided dice dropping the lowest value and returning the highest 3 dice to create and assign a stat value to an attribute.
4. A summary of the new character is generated (maybe create a CSV or PDF of the summary?).
5. The script asks if the user would like to try again or end the program.

## Testing:
This application is using pytest to test the functions and logic. Most of the tests are calling a fixture which contains
and returns a list. Each test is then calling the fixture and invoking the relevant function to test if the application's
logic works as expected.
