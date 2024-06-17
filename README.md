# Basic Ciphers
A collection of basic ciphers by me (if these already exist I do not know about them)

# 1. "Difference Data Cipher"
This cipher takes a string consisting of the 26 letters of the alphabet and whitespaces only and finds their position in the alphabet and the difference between that and the position of the key (a single letter from the 26 in the alphabet) which is the difference part of the cipher.
The "data" part is including basic ways to read data, like the length of it and the range of the values (only with integers). So the previously generated number from the difference is added together with the range and length of the string (excluding whitespaces) and then the final output is printed.
When running the python file it also prints out various stages of the process, but all you need to know is the final print() - same with the decoder.

Important to remember with the decoder is that it takes the final output which is printed like x x x / x x (length and fowards slashes vary), not the values which are printed as [[x, x, x], [x, x]] (again, varies bases on the string you inputted)

TODO: Allow the user to enter no key and then brute force all the 26 letters of the alphabet, allowing the user to chose the one that makes the most sense grammatically and english-wise.
