person1={"name":"yaman","age":20,"adress":"irbid","phone number":779701230,"email":"yamanobiedat108@gmail.com"}
person2={"name":"ahmad","age":22,"adress":"amman","phone number":1111111111,"email":"ahmad@gmail.com"}
person3={"name":"mohamad","age":30,"adress":"Aqaba","phone number":22222222,"email":"mohamad@gmail.com"}
person4={"name":"kaled","age":40,"adress":"as-Salt","phone number":33333333,"email":"kaled@gmail.com"}
person5={"name":"waleed","age":12,"adress":"Ma'an","phone number":444444444,"email":"waleed@gmail.com"}
#----------------------------------------------
print(person1["name"],person1["email"])
print(person2["name"],person2["email"])
print(person3["name"],person3["email"])
print(person4["name"],person4["email"])
print(person5["name"],person5["email"])
print(50*'-')
#-----------------------------------------------
person1["age"]=24
person2["age"]=33
person3["age"]=23
person4["age"]=26
person5["age"]=38
#-----------------------------------------------
print(person1["age"])
print(person2["age"])
print(person3["age"])
print(person4["age"])
print(person5["age"])
# ----------------------------------------------
print(50*"*")
name="yaman obiedat"
print(name[2])
print(name[-1])
print(name[7:10])
# ----------------------------------------------
#name2=input("inter your name: ")
#x=len(name2)

#for i in range(x):
 #   if name2[i]=="l":
  #      print('found')
  #-------------------------------------------------

name2="loae"
name2="*"+name2[1:]
print(name2)

name3="salem"
name3=name3[0:1]+"*"+name3[3:]
# -------------------------------------------------
name4="salem"
for i in range(len(name4)):
    if name4[i]=='l':
        name4=name4[0:i]+"*"+name4[i+1:]
        print(name4)

# -------------------------------------------------
name5="salem"
for i in range(len(name4)):
    if name4[i]=='l':
        name5=name5[0:i]+"*"+name5[i+1:]
print(name4)
# ------------------------------------------------
print("*"*50)
name6="sallem"
for i in range(len(name4)):
    if name6[i]=='l':
        name6=name6.replace("l","*")
print(name6)        
#------------------------------------------------
#num1=float(input("inter your number: "))
#if num1%2==0:
#    print("even")
#else:
 #   print("odd") 
#------------------------------------------------   
#prime numder 
num2=int(input("inter your number: "))
 
for i in range (2,num2):
   
   if num2%i ==0:
       print("is not") 
       break

else:
    print("is prime ")   

    
      






