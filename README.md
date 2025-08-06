# sum-even-numbers
A Python script that asks the user for 6 numbers and calculates the sum of only the numbers that are even.

# ➕ Even Numbers Sum-up

This is a command-line Python program that prompts the user to enter six integers. The program then calculates and displays the final sum of only the even numbers that were entered.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `sum_even_numbers.py`).
3.  Open your terminal or command prompt.
4.  Run the script with the following command:
    ```sh
    python sum_even_numbers.py
    ```
5.  The program will prompt you to enter one number at a time, for six times.
6.  After the sixth number is entered, the sum of all the even numbers you typed will be displayed.

## Program Logic

* **Accumulator Variable:** A variable, `number_added`, is initialized to `0`. It will be used to store the running total of the even numbers.
* **Looping:** The program uses a `for` loop with `range(0, 6)` to ensure it asks the user for exactly six numbers.
* **Evenness Check:** Inside the loop, each number entered by the user is checked with the condition `if user_number % 2 == 0`.
* **Conditional Sum:** If the number is even, it is added (`+`) to the `number_added` variable. If it's odd, nothing happens, and the loop continues to the next iteration.
* **Final Result:** After the loop finishes, the final value of the `number_added` variable is printed to the screen.
