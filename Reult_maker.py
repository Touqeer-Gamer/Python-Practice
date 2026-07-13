# Result Maker ..

student = input("Enter Your Name : ")
print("Student Name : ",student)

roll = input("Enter Your Roll Number : ")
print("Student's Roll Number : " ,roll)

dep = input("Enter Your Department : ")
print("depratment Name : " ,dep)

sem = input("Enter Your Semester : ")
print("Semester : " ,sem)






english_marks = int(input("Enter Your English Marks : "))
print("English Marks = ", english_marks)
if english_marks <= 49 :
    print(" You're marks are below 50 you are failed ")
else :
    pass    


islamiyat_marks = int(input("Enter Your Islamiyat Marks : "))
print("Islamiyat Marks = ", islamiyat_marks)
if islamiyat_marks <= 49 :
    print(" You're marks are below 50 you are failed ")
else :
    pass 


calculus_marks = int(input("Enter Your Calculus Marks : "))
print("Calculus Marks =  ", calculus_marks)
if calculus_marks <= 49 :
    print(" You're marks are below 50 you are failed ")
else :
    pass 


pakstudy_marks = int(input("Enter Your Pak Study Marks : "))
print("Pak Study Marks = ", pakstudy_marks)
if pakstudy_marks <= 49 :
    print(" You're marks are below 50 you are failed ")
else :
    pass 


programming_marks = int(input("Enter Your Programming Marks : "))
print("Programming Marks = ", programming_marks)
if programming_marks <= 49 :
    print(" You're marks are below 50 you are failed ")
else :
    pass 


physics_marks = int(input("Enter Your Physics Marks : "))
print("Phyics Marks = ", physics_marks  )
if physics_marks <= 49 :
    print(" You're marks are below 50 you are failed ")
else :
    pass 


total_marks = int(input("Enter Your Total Marks : "))
print("Total Marks Of All Exams : ",total_marks)


obtained_marks = physics_marks + programming_marks + pakstudy_marks + calculus_marks + islamiyat_marks + english_marks 
print('Obtained Marks = ' , obtained_marks)

percent = (obtained_marks*100)/total_marks
print("%age : " , percent)
if percent < 50 :
    print("You're Failed.....Work Hard For the Next Time.")
else :
    print("***Congratulatons***")








