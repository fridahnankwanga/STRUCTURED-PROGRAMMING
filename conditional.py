score = int(input("Enter your numeric score:"))
if 80 <= score <=100:
    grade = 'A'
elif 70 <= score <=79:
    grade = 'B'
elif 60 <= score <=69:
    grade = 'C' 
elif 50 <= score <=59:
    grade ='D'
elif score < 50:
    grade = 'F'
else:
    grade = 'invalid score' 
print (f"your grade is:   {grade}") 

