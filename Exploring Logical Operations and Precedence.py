#Task 1: Validating Calculations
#Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. 
#Compare the two results to see if they match.

A = 10 + 20 * 1 - 3
B = 10 + 20 * (1-3)
C = A == B 
print(C)
#they did not match#

#Task 2: Mix and Match
#Combine arithmetic (+), logical (or), and comparison (>) operators in a single expression and predict the outcome. 
#Then, compute the expression to see if the prediction was correct.

Answer = 10 + 5 * 8 > 15 and (10 * 2 == 20 or 30 / 10 <= 20)
print(Answer)
#My prediction was correct