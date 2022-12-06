global inp
global index
record = []                        
                
def new_student():
  while True:                 
    if len(record) > 20 :                                        
      print("Student data limit exceeded!!")
      return
    data = [] 
    try:  
      name = input("ENTER STUDENT NAME : ")
      reg_no = (input("ENTER STUDENT SR-CODE: "))
      age = int(input("ENTER STUDENT AGE: "))
      major = input("ENTER STUDENT MAJOR: ")
      email = input("ENTER STUDENT E-MAIL ID: ")
      address = input ("ENTER STUDENT ADDRESS: ")
    except ValueError:
      print("You must input integer value!")
      continue
    else:
      data.append(name)
      data.append(reg_no)
      data.append(age)
      data.append(major)
      data.append(email)
      data.append(address)
      record.append(data)                                         
      print("--------------------------")
      print("Student Data Inserted successfully")
      print("--------------------------")
    return
