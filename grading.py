mark = float(input("Enter the stundent mark between 0 and 100: "))
if mark >= 91 and mark <= 100:
    grade = "A+"
elif mark >= 80 and mark <=91:
    grade = "A"
elif mark >= 70 and mark <=80:
    grade  = "B"
elif mark >= 60 and mark <=70:
    grade ="c" 
elif mark >= 50 and mark <=60:
    grade = "D" 
elif mark >=40 and mark <=50:
    grade = "E" 
elif mark >=30 and mark <=40:
    grade = "F"
elif mark >=20 and mark <=30:
    grade = "G"
elif mark >=10 and mark <=20:
    grade = "H"
elif mark >=0 and mark <=10:
    grade = "I"

else: 
    print ("invalid mark.")
