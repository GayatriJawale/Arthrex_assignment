# Arthrex_assignment
#Problem Statement:
  Implement an auto-suggest / type-ahead feature (as we see in case of Google Search) with
  a regex, “*”.
  Input1: Upto 5 words with similar spellings
  Input2: part of the words entered above in
  Input1
  Output: List of words from Input1 containing the part / phrase entered in Input2
  Example:
  Input1: take, make, check, ack, rake
  Input2: ke
  Output: take, make, rake
  Input1: take, make, check, ack, rake
  Input2: *k
  Output: check, ack

Approach:
In the guidelines, it was encouraged to solve the assignment without using library functions hence I have used list to solve this problem.

auto_suggest.py: This file contains the primary code 
