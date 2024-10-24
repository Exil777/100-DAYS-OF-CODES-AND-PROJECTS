# find the highest score

student_scores = [150, 140, 125, 199, 160, 70, 90, 85]

# find the sum of the student scores
total_score = sum(student_scores)
print(total_score)

sum = 0
for score in student_scores:
    sum += score
print(sum)

# find the max student scores
max_score = max(student_scores)
# finding the max student score with the max function
print(max_score)

# define a variable and assign the number 0 
max_student_score = 0
# use the for loop to go through each score and assign each score the variable score
for score in student_scores:
    # checking if max_student_score is less then each student score
    if max_student_score < score:
        # assign each student score to max_student_score
        max_student_score = score
# and it keep going as long as max_student_score is less than score until it the maximun score 
print(max_student_score)

# sum up the number from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)
