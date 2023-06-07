# simple-calculator
Simple Calculator

Step 1:
Add
Subtract
Multiply
3 functions. These are fairly straight-forward, think back to  operators!

To run tests, use these commands in the command line:
# For the add() function
$run test_add.py

# For the subtract() function
$run test_subtract.py

# For the mulitply() function
$ run test_multiply.py


Step 2
Divide
You'll notice here that divide is the only function that has two tests for it - that's because you'll need to program some exceptional behavior in case the user tries to divide by 0!

If 0 is passed as a denominator when using this function, instead of an integer, return a string warning the user not to divide by 0. You can chose any message you want, for example return "Invalid value for denominator, cant't divide by 0!"

$run test_divide.py


Step 3
Square
Power
Square Root
Rounding out the last three tests are functions dealing with powers. They can be kind of tricky (especially finding the square root!)

$run test_square.py
$run test_power.py
$run test_sqrt.py
