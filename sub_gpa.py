#python program to assign grade to a student considering 6 subjects
#using 'elif' ladder
s1,s2,s3,s4,s5,s6 = [int(x) for x in input("Enter the 6 subjects marks = ").split()]
total = s1 + s2 + s3 + s4 + s5 + s6
gpa =(total / 600) * 100
if gpa < 75 :
    print("Fail")
elif gpa <= 75 :
    print("Grade E")
elif gpa >= 75 and gpa <= 80 :
    print("Grade D")
elif gpa >= 80 and gpa <= 85 :
    print("Grade C")
elif gpa >= 85 and gpa <= 90 :
    print("Grade B")
elif gpa >= 90 and gpa <= 100:
    print("Grade A")
elif gpa > 100 :
    print("Grade S")
else :
    print("NULL")
