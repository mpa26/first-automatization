# first-automatization
My first public project with Selenium and Python

# description
In this task, need to write a program that will book us a holiday home at a strictly specified price. 
A higher price does not suit us, but someone else will have time to book an object at a lower price.

The program should execute the following script:

    1) Open page http://suninjuly.github.io/explicit_wait2.html
    2) Wait until the price of the house decreases to $100 (the wait must be set at least 12 seconds)
    3) Press the button "Book"
    4) Solve a math problem and save the solution to the console

To determine when the rental price drops to $ 100, need to use the text_to_be_present_in_element method from the expected_conditions library.