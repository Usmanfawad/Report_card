print("Report Card Generation")

user_marks=[]
user_subjects=[]
user_name= input("Enter your name: ")
user_id= int(input("Enter your unique id: "))

for sub in range(3):
    sub_name= input("Enter Subject" +str(sub+1) +":")
    sub_marks= int(input("Enter Subject" +str(sub+1) +" marks: "))
    user_marks.append(sub_marks)
    user_subjects.append(sub_name.title())
    if sub_marks > 100:
        print("Marks cannot be greater than 100")
        print("Please try again")
        break
percentage= (sum(user_marks)/300)*100

print('\n\n')
print("       FINAL REPORT CARD")
print(u"\u25A0"*32)
print('{:<17}:{}'.format("Name",user_name.title()))
print('{:<17}:{}'.format("Roll number",user_id))
print(u"\u25A0"*32)
print("_"*32)
print (": Subjects       |Score")
for x in range(len(user_subjects)):
    print(x+1,'{:<15}|{}'.format(user_subjects[x],user_marks[x]))

print("_"*32)
print('{:<17}|{}'.format("Total marks",sum(user_marks)))
print('{:<17}|{}'.format("Percentage","%.2f" % round(percentage,2)))
print("_"*32)
