# Arthrex_assignment
Overview:
This program implements an auto-suggest (type-ahead) feature similar to Google Search. It takes up to 5 words as input and a search pattern, then outputs a list of words from the input that contain the part or phrase entered in the search pattern. 
The search pattern can include wildcards (*), which are handled as follows:

* at the beginning of the pattern matches any suffix of the word.
* at the end of the pattern matches any prefix of the word.
* at both ends of the pattern matches any substring of the word.
No * in the pattern matches any part of the word.

Program Files:
auto_suggest.py: Contains the auto_suggest function and the main program logic.
test_auto_suggest.py: Contains the unit tests for the auto_suggest function.

Approach:
In the guidelines, it was encouraged to solve the assignment without using library functions hence I have used list to store and update data while if-else for conditional filtering.

The auto_suggest function is responsible for filtering and suggesting words from the input list based on the search pattern provided.

Helper Function matches: This function determines if a given word matches the search pattern as below:
If the pattern starts and ends with *, it checks if the substring (excluding the * characters) is found anywhere in the word.
If the pattern starts with *, it checks if the word ends with the substring following the *.
If the pattern ends with *, it checks if the word starts with the substring before the *.
If the pattern contains no *, it checks if the pattern is found anywhere within the word.

It iterates through each word in input_words and uses the matches function to check if the word matches the search pattern. If it does, the word is added to the output list and returned.

Testing:
In test_auto_suggest.py, the 'unittest' module is used to create the test cases, and the 'auto_suggest function' is imported from auto_suggest.py to be tested.
    Total Test Cases: 18
    Passed Test Cases: 15
    Failed Test Cased: 3

Running Test Cases:
On VS Code:
1. Keep auto_suggest.py and test_auto_suggest.py in the same folder.
2. Run the auto_suggest.py (Optional)
3. Run the test_auto_suggest.py as:
   python -m unittest test_auto_suggest.py
