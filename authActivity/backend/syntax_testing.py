import shlex


# #REGISTER ALGORITHM
# list = []
# name = "John"
# with open("text_database.txt", "r") as file:
    
#     for row in file:  
#         column = row.split()
#         list.append(column[1])
        
# print(list)


# if name in list:
#     print("User exists")


# #second algorithm
# username = "John_Mark"
# check_user_exist = None

# with open("text_database.txt", "r") as file:
#     lines = file.readlines()  # Read all rows

# for row in lines:
#     # Remove newline, then split only 4 times (so nickname stays intact)
#     columns = row.strip().split(" ", 4)
#     print(columns)

#     user_id = columns[0]
#     user_username = columns[1]
#     user_password = columns[2]
#     user_gmail = columns[3]
#     user_nickname = columns[4] if len(columns) > 4 else ""

#     print(f"User ID: {user_id}")
#     print(f"Username: {user_username}")
#     print(f"Password: {user_password}")
#     print(f"Gmail: {user_gmail}")
#     print(f"Nickname: {user_nickname}")
#     print()

#     # Check if the username exists
#     if username == user_username:
#         check_user_exist = True
#         print(f"✅ Username '{username}' found!")
#         break
# else:
#     check_user_exist = False
#     print(f"❌ Username '{username}' not found.")
    





# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# #LOGIN ALGORITHM
# username = "Jake"
# get_db_name = None
# get_db_password = None
# get_db_user_id = None

# with open("text_database.txt", "r") as file:
#     lines = file.readlines()
    
    
# for row in lines:
#     column = row.split()

#     if username == column[1]: 
#         get_db_name = column[1]
#         get_db_password = column[2]
#         get_db_user_id = column[0]
            
            

# print(get_db_name)
# print(get_db_password)
# print(get_db_user_id)



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# #FORGOT PASSWORD ALGORITHM
# username = "Mike"
# new_password = "321321"

# with open("text_database.txt", "r") as file:
#     lines = file.readlines()


# updated_lines = []
# for row in lines:
#     column = row.split()

#     if username == column[1]:    #check if data matches with the username
#         column[2] = new_password    #overwrite a column

#         row = " ".join(column) + "\n"    #stitch all multiple columns and turn it into a single text column
        
#     updated_lines.append(row)

# with open("text_database.txt", "w") as file:    #open txt database
#     file.writelines(updated_lines)    #rewrite a line


    
    
    
    
    
    
    
    
    
    

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    
# with open("db_for_all_user_task.txt", "r") as file:
#     lines = file.readlines()
            
# for row in lines:
#     column = shlex.split(row)
#     print(column[10])    

    
    
    
    
    
    
    
    

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
username = "Mark"

with open("text_database.txt", "r") as file:    #open txt database 
    lines = file.readlines()
    
    
for row in lines:   #read rows
    column = shlex.split(row)    #turning a single column into multiple columns by splitting it using ".split()"
    if column:
        if username == column[1]:
            check_user_exist = column[1]
    print(column[4])

    
    
    
    

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    
    
    
    
    
    
    
    
    
    
    

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    
    
    
    
    
    
    
    
    
    
    