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

def display_student():                                            
  index = input("Enter index(From 0) to display student data: ")
  if int(index) == (len(record)):                                 
    print("Student data not found!!")
    display_student()
  else:
    print("----------------------")
    print("NAME: " + str(record[int(index)][0]))           
    print("SR-CODE: " + str(record[int(index)][1]))  
    print("AGE: " + str(record[int(index)][2]))
    print("MAJOR: " + str(record[int(index)][3]))
    print("EMAIL: " + str(record[int(index)][4]))
    print("ADDRESS: " + str(record[int(index)][5]))
    print("----------------------")
  
def update_student():                                              
  upd_index = input("Enter index(From 0) to update data: ")
  if int(upd_index) == (len(record)):
    print("Student data not found!!")
    update_student()                                                  
  else:
    new_name = input("ENTER NEW STUDENT NAME : ")
    new_reg_no = input("ENTER NEW STUDENT SR- CODE: ")
    new_age = input("ENTER NEW STUDENT AGE: ")
    new_major = input("ENTER NEW STUDENT MAJOR: ")
    new_email = input("ENTER NEW STUDENT E-MAIL ID: ")
    new_address = input ("ENTER NEW STUDENT ADDRESS: ")
    record[int(upd_index)][0] = new_name                              
    record[int(upd_index)][1] = new_reg_no
    record[int(upd_index)][2] = new_age
    record[int(upd_index)][3] = new_major
    record[int(upd_index)][4] = new_email
    record[int(upd_index)][5] = new_address
    print("----------------------")
    print("Student Data updated successfully")
    print("----------------------")


def delete_student():                                                      
  del_index = input("Enter index(From 0) to Delete student record: ")
  del record[int(del_index)]                                                
  print("----------------------")
  print("Student Data Deleted successfully")
  print("----------------------") 
  
while True:  
                                                  
  print("PRESS 1 : TO ADD STUDENT INFORMATION.")
  
  if len(record) >= 1:                                          
   print("PRESS 2 : TO DELETE STUDENT INFORMATION.")
  
  if len(record) >= 1:
   print("PRESS 3 : TO UPDATE STUDENT INFORMATION.")

  if len(record) >= 1: 
   print("PRESS 4 : TO DISPLAY STUDENT INFORMATION.")

  if len(record) >= 1:
   print("PRESS 5 : TO EXIT SYSTEM.")
  
  inp = input("ENTER YOUR OPTION: ")                                     

  if int(inp) == 1:
    new_student()                              
 
  elif int(inp) == 2 and len(record) >= 1 :
    delete_student()                           
    
  elif int(inp) == 3 and len(record) >= 1:
    update_student()                          
    
  elif int(inp) == 4 and len(record) >= 1:
    display_student()                          

  else:
    print("Invalid input!")
  continue
