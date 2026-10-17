import os
import shlex
from datetime import datetime


class UserAccount:
    def __init__(self):


        self.borrowed_books = {}

        self.current_user = None
        self.current_user_id = None

        #initialize .txt file path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_all_user_account = os.path.join(base_dir, "db_for_all_user_account.txt")
        self.db_all_user_schedule = os.path.join(base_dir, "db_for_all_user_schedule.txt")
        self.db_all_user_task = os.path.join(base_dir, "db_for_all_user_task.txt")
        self.db_all_id_numbers = os.path.join(base_dir, "db_id_numbers.txt")
        self.db_all_user_books = os.path.join(base_dir, "db_for_all_user_borrowed_books.txt")





# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def register(self, nickname, email, username, password):
        # === VALIDATION ===
        nickname = nickname.strip()
        email = email.strip()
        username = username.strip()
        password = password.strip()
        
        
        check_user_exist = None
        with open(self.db_all_user_account, "r") as file:    #open txt database 
            lines = file.readlines()
    
        for row in lines:   #read rows
            column = shlex.split(row)    #turning a single column into multiple columns by splitting it using ".split()"
            
            if column:
                if username == column[1]:
                    check_user_exist = column[1]

        if not nickname or not email:
            return "Name and Email cannot be empty"
        elif " " in username:
            return "Username must not have spaces"
        elif "@" not in email or "." not in email:
            return "Invalid email format"

        elif not username or not password:
            return "Username and Password cannot be empty"
        
        elif len(password) < 6:
            return "Password should be at least 6 characters"

        elif username != check_user_exist:  
            # === CREATE ACCOUNT ===
            
            #To create a unique id for every user
            with open(self.db_all_id_numbers, "r") as file: #open txt database
                lines = file.readlines()    #reading all rows
                user_id = len(lines)    #count all rows and assign the value into a variable

            with open(self.db_all_id_numbers, "a") as file: #open txt database
                file.write(str(user_id) + "\n")    #append the newly created id
                
            print("New user ID:", user_id)   #check the value
            
            user_data = [str(user_id), username, password, email, f'"{nickname}"']
            line = " ".join(user_data)
            with open(self.db_all_user_account, "a") as file:    #open txt database
                file.write(line + "\n")     #append data to database

                
            return "Registration successful"
        else:
            print(check_user_exist)

            return "User already exists"


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def login(self, username, password):
        
        #Initialize
        get_db_name = None
        get_db_password = None  #output: "mypassword"
        get_db_user_id = None
        with open(self.db_all_user_account, "r") as file: #read txt database
            lines = file.readlines()    #"line" variable is assigned for getting the value of "file"
            
        for row in lines:    #read rows from database
            column = shlex.split(row)    #turn single column into multiple columns

            if column:
                if username == column[1]:     #check if username matches with the stored username inside the database
                    get_db_name = column[1]     #get the username from database
                    get_db_password = column[2]    #get password and store the value into a variable
                    get_db_user_id = column[0]    #get user id from database
                    print(column[4])
        
        
        
        if username == get_db_name and password == get_db_password:
            self.current_user = username
            self.current_user_id = get_db_user_id
            #check 
            print(self.current_user)
            print(self.current_user_id)
            return "Login successful"
        elif username == get_db_name and password != get_db_password :
            return "Wrong password"
        elif username == "" or password == "":
            return "Please fill in all fields"
        else:
            return "User not found"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def forgot_password(self, username, new_pass, confirm_pass):
   
        username_in_db = None
        with open(self.db_all_user_account, "r") as file: #read txt database
            lines = file.readlines()
            
        for row in lines:    #read rows from database
            column = shlex.split(row)    #turn single column into multiple columns
            
            if column: 
                if username == column[1]:
                    username_in_db = column[1]
        
        
        if not username or not new_pass or not confirm_pass:
            return "Please fill in all fields"



        if new_pass != confirm_pass:
            return "Passwords do not match!"

        elif len(new_pass) < 6:
            return "Password should be at least 6 characters!"
        elif username != username_in_db:
            return "Username not found!"
        else:

            with open(self.db_all_user_account, "r") as file:
                lines = file.readlines()


            updated_lines = []
            for row in lines:
                column = shlex.split(row)
                
                if column: 
                    if username == column[1]:    #check if data matches with the username
                        column[2] = new_pass    #overwrite a column
                        data_list = [column[0], column[1], column[2], column[3], f'"{column[4]}"']

                        row = " ".join(data_list) + "\n"    #stitch all multiple columns and turn it into a single text column
                        
                    updated_lines.append(row)

            with open(self.db_all_user_account, "w") as file:    #open txt database
                file.writelines(updated_lines)    #rewrite a line
                
            return "Password successfully updated!"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   
    def logout_user(self):
        self.current_user = None
        self.current_user_id = None
        
        return "Logged out!"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   
    def save_user_task(self, title, month, day, year, hour, minutes, period, description):


        with open(self.db_all_user_task, "r") as file:
            lines = file.readlines()
            
        last_task_id_num = -1
        for row in lines:   #read rows
            column = shlex.split(row)    #turning a single column into multiple columns by splitting it using ".split()"
            
            if column:
                if self.current_user_id == column[0]:
                    task_str = column[1]
                    task_num = int(task_str.split("_")[1])
                    if task_num > last_task_id_num:
                        last_task_id_num = task_num
                        
        task_id = f"task_{last_task_id_num + 1}"
        
                    #       user_id        task id      title     month  day  year  hour  minutes  period     status         description        
        task_list = [self.current_user_id, task_id, f'"{title}"', month, day, year, hour, minutes, period, "incomplete", f'"{description}"']
        
        line = " ".join(task_list)  #stitch all columns to turn into a string
        
        with open(self.db_all_user_task, "a") as file:
            file.write(line + "\n")
            
        return "Task Added!"
            


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
    def edit_user_task(self, title, month, day, year, hour, minutes, period, description, task_id):
       
        with open(self.db_all_user_task, "r") as file:
            lines = file.readlines()
            
        updated_task = []    
        for row in lines:
            column = shlex.split(row)
            
            if column:
                if self.current_user_id == column[0] and task_id == column[1]:
                    
                    print(column[0], column[1], column[2], column[3], column[4], 
                          column[5], column[6], column[7], column[8], column[9], column[10])
                    
                    column[2] = title
                    column[3] = month
                    column[4] = day
                    column[5] = year
                    column[6] = hour
                    column[7] = minutes
                    column[8] = period
                    column[10] = description
                    
                    data_list = [column[0], column[1], f'"{column[2]}"', column[3], column[4], 
                                 column[5], column[6], column[7], column[8], column[9], f'"{column[10]}"']
                    row = " ".join(data_list) + "\n"
                    
                    
                    print(column[0], column[1], column[2], column[3], column[4], 
                          column[5], column[6], column[7], column[8], column[9], column[10])
                    
            updated_task.append(row)
        
        with open(self.db_all_user_task, "w") as file:
            file.writelines(updated_task)
            
        return "Task Edited!"
                   
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     
    def save_user_schedule(self, teacher_name, subject_name, subject_code, subject_section, time_start, time_end, day1, day2, units, room, color):
        
        weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "None (once a week)"]

        time_sched = [
            "07:30 AM", "08:00 AM", "08:30 AM", "09:00 AM", "09:30 AM",
            "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM", "12:00 PM",
            "12:30 PM", "01:00 PM", "01:30 PM", "02:00 PM", "02:30 PM",
            "03:00 PM", "03:30 PM", "04:00 PM", "04:30 PM", "05:00 PM",
            "05:30 PM", "06:00 PM", "06:30 PM", "07:00 PM", "07:30 PM"
        ]
        
        #create unique user subject id
        with open(self.db_all_user_schedule, "r") as file:
            lines = file.readlines()
        
        last_subject_id_num = -1
        for row in lines:   #read rows
            column = shlex.split(row)    #turning a single column into multiple columns by splitting it using ".split()"
            
            if column:
                if self.current_user_id == column[0]:
                    subject_str = column[1]
                    subject_num = int(subject_str.split("_")[1])
                    if subject_num > last_subject_id_num:
                        last_subject_id_num = subject_num
        
        
        subject_id = f"subject_{last_subject_id_num + 1}"
        #Conversion for getting the value of rows, column, and rowspan
        if time_start in time_sched and time_end in time_sched and day1 in weeks and day2 in weeks:
            
            
            index_time1 = time_sched.index(time_start)  #ex. output: (index) 5
            index_time2 = time_sched.index(time_end)  #ex. output: (index) 3
            
            if index_time2 > index_time1:    #ex. 11:00 AM should always be greater than the time before it. Otherwise, invalid time format
                rw = index_time1 + 1
                print("row", rw)
                
                #Convert a day into column index
                index_day1 = weeks.index(day1)
                index_day2 = weeks.index(day2)
                
                cl_a = index_day1 + 1
                cl_b = index_day2 + 1
                
                #Set the value to None if schedule is one a weekk
                if index_day2 == 6 or index_day1 == index_day2:
                    index_day2 = None
                    cl_b = None

                print("column", cl_a,"and column", cl_b)
        
                #To get rowspan
                rowspan = index_time2 - index_time1
                rspan = rowspan + 1
                
                print("rowspan", rspan)
            

                
                with open(self.db_all_user_schedule, "r") as file:
                    lines = file.readlines()
                
                for row in lines:
                    column = shlex.split(row)
        
                    if column:
                        pass
                
                
                sub_data = [self.current_user_id, subject_id, f'"{teacher_name}"', f'"{subject_name}"', f'"{subject_code}"', f'"{subject_section}"', 
                            f'"{time_start}"', f'"{time_end}"', day1, day2, str(units), f'"{room}"', color, str(rw), str(cl_a), str(cl_b), str(rspan)]
                line = " ".join(sub_data)
                
                with open(self.db_all_user_schedule, "a") as file:
                    file.write(line + "\n")
                

                return "Schedule Added!"
            elif index_time2 == index_time1:
                return "Invalid timetable. Please check for any mistakes."
            elif index_time2 < index_time1:
                return "Invalid timetable. Please check for any mistakes."
        else:
            return "Invalid timetable. Please check for any mistakes."
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
 
    def delete_user_schedule(self, schedule_data):
        
        with open(self.db_all_user_schedule, "r") as file:
            lines = file.readlines()

        update_data = []
        for row in lines:
            column = shlex.split(row)
            
            if column:
                if self.current_user_id == column[0] and schedule_data[1] == column[1]:
                    continue
                else:
                    update_data.append(row)
        
        with open(self.db_all_user_schedule, "w") as file:
            file.writelines(update_data)
            
        return "Subject Deleted!"        
        
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -    
         
    def check_task_due_date(self):
        
        with open(self.db_all_user_task, "r") as file:
            lines = file.readlines()
            
        updated_lines = []   
        for row in lines:
            column = shlex.split(row)
            
            if column:
                # print("\n0    user_id",       column[0], 
                #       "\n1    ask_id",        column[1], 
                #       "\n2    title",         column[2], 
                #       "\n3    month",         column[3], 
                #       "\n4    day",           column[4], 
                #       "\n5    year",          column[5], 
                #       "\n6    hour",          column[6], 
                #       "\n7    minutes",       column[7], 
                #       "\n8    period",        column[8], 
                #       "\n9    status",        column[9], 
                #       "\n10   description",   column[10])
                
                #Convert to 24-hour format
                hour = int(column[6])
                if column[8].upper() == 'PM' and hour != 12:
                    hour += 12
                elif column[8].upper() == 'AM' and hour == 12:
                    hour = 0
                    
                # Convert to datetime
                due_date_str = f"{column[4]} {column[3]} {column[5]} {hour}:{column[7]}"
                due_date = datetime.strptime(due_date_str, "%d %B %Y %H:%M")
        
                # Get current date and time
                now = datetime.now()

                # Compare
                if now > due_date and column[9] == "incomplete":
                    print("Beyond due date!")
                    column[9] = "missing"
                    
                # elif column[9] == "complete": 
                #     print("Task completed!") 
                # elif column[9] == "missing":
                #     print("Task missing!") 
                # else:
                #     print("Still on time.")
                    
                data_list = [column[0], column[1], f'"{column[2]}"', column[3], column[4], 
                                column[5], column[6], column[7], column[8], column[9], f'"{column[10]}"']
                
                row = " ".join(data_list) + "\n"
    
            updated_lines.append(row)
            
        with open(self.db_all_user_task, "w") as file:
            file.writelines(updated_lines)
        

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
 
    def handle_change_password(self, username, current_pass, new_pass, confirm_pass):
        if not username or not current_pass or not new_pass or not confirm_pass:
            return "Please fill in all fields!"

        # Look for user account
        user_found = None
        for acc_name in self.accounts:
            acc_data = self.accounts[acc_name]
            if acc_data["u_account"]["username"] == username:
                user_found = acc_data
                break

        if not user_found:
            return "Username not found!"

        # Check current password
        if user_found["u_account"]["password"] != current_pass:
            return "Incorrect current password!"

        # Confirm new password match
        if new_pass != confirm_pass:
            return "Passwords do not match!"

        # Check password length
        if len(new_pass) < 6:
            return "Password should be at least 6 characters!"

        # Update password
        user_found["u_account"]["password"] = new_pass
        print(f"Password updated for user: {username}")
        return "Password successfully changed!"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def borrowed_method(self, action=None, count=1, status=None):
        pass
    #     # 1. Make sure a user is logged in
    #     if not self.current_user:
    #         return "No user logged in"

    #     # 2. Get user's data
    #     user_data = self.accounts.setdefault(self.current_user, {})
    #     borrowed_books = user_data.setdefault("borrowed_books", [])

    #     # ----------------------------
    #     # ACTION: BORROW BOOKS
    #     # ----------------------------
    #     if action == "add":
    #         borrowed_books.append({
    #             "original_count": count,   # fixed borrow amount (for returned / not returned)
    #             "current_count": count,    # grows when renew
    #             "renew_count": 0,
    #             "status": "not returned"
    #         })
    #         return "Book borrowed successfully."

    #     # ----------------------------
    #     # ACTION: RETURN BOOK (only original count)
    #     # ----------------------------
    #     elif action == "return":
    #         for book in borrowed_books:
    #             if book["status"] == "not returned":
    #                 book["status"] = "returned"
    #                 # store how many were actually returned
    #                 book["returned_count"] = book["original_count"]
    #                 return "Book returned successfully."
    #         return "No active borrowed book to return."

    #     # ----------------------------
    #     # ACTION: RENEW BOOK
    #     # ----------------------------
    #     elif action == "renew":
    #         for book in reversed(borrowed_books):
    #             if book["status"] == "not returned":
    #                 if book["renew_count"] >= 2:
    #                     return "Maximum renewals reached."

    #                 original = book["original_count"]
    #                 current = book["current_count"]

    #                 # add original to current total
    #                 book["current_count"] = current + original
    #                 book["renew_count"] += 1

    #                 return f"Book renewed successfully. New total = {book['current_count']}"
    #         return "No active borrowed book to renew."

    #     # ----------------------------
    #     # ACTION: STATS
    #     # ----------------------------
    #     elif action == "stats":
    #         total = 0
    #         returned = 0
    #         not_returned = 0

    #         for book in borrowed_books:
    #             total += book["current_count"]

    #             if book["status"] == "returned":
    #                 returned += book.get("returned_count", 0)
    #             else:
    #                 not_returned += book["original_count"]

    #         return {
    #             "total": total,
    #             "returned": returned,
    #             "not_returned": not_returned
    #     }
    


    def get_last_borrow_info(self, username):
        # Helper function that gets the most recent borrow record for a user.
        user = self.accounts.get(username)
        if not user:
            return None
        borrowed_books = user.get("borrowed_books", [])
        # Return the latest borrowed record if available
        return borrowed_books[-1] if borrowed_books else None


        return borrowed_books[-1]  # last record


    def renew_book(self, title, count):
        # Check if book already exists in borrowed_books
        found = False
        for book in self.accounts[self.current_user]["borrowed_books"]:
            if book["title"] == title:
                # Add the renewed count to the existing count
                book["count"] += count
                found = True
                break

        if not found:
            # If not found, add it as a new book
            self.borrowed_method("add", title=title, count=count)
            
            
            
    def save_borrowed_books(self):
        pass
        # with open(self.db_all_user_books, "r") as file:
        #     lines = file.readlines() 
            
        # last_task_id_num = -1
        # for row in lines:   #read rows
        #     column = shlex.split(row)    #turning a single column into multiple columns by splitting it using ".split()"
            
        #     if column:
        #         if self.current_user_id == column[0]:
        #             task_str = column[1]
        #             task_num = int(task_str.split("_")[1])
        #             if task_num > last_task_id_num:
        #                 last_task_id_num = task_num
                        
        # task_id = f"task_{last_task_id_num + 1}"
        
        #             #       user_id        task id      title     month  day  year  hour  minutes  period     status         description        
        # task_list = [self.current_user_id, task_id, f'"{title}"', month, day, year, hour, minutes, period, "incomplete", f'"{description}"']
        
        # line = " ".join(task_list)  #stitch all columns to turn into a string
        
        # with open(self.db_all_user_task, "a") as file:
        #     file.write(line + "\n")
            
        # return "Task Added!"  
            
            
            
            
            
            
            
# db = UserAccount() #create the object            
# print(db.register("John", "John@gmail.com", "Asher", "asdasd"))    #insert data


    

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
        #FUNCTIONS FOR FRONT END
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   

    def get_db_nickname_for_dashboard(self):
        
        nickname = None
        with open(self.db_all_user_account, "r") as file:
            lines = file.readlines()
        
        for row in lines:
            column = shlex.split(row)
            
            if column:
                if self.current_user_id == column[0]:
                    nickname = column[4]
                                 
        return nickname
        

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
 
    def get_db_email_for_dashboard(self):
        
        email = None
        with open(self.db_all_user_account, "r") as file:
            lines = file.readlines()
        
        for row in lines:
            column = shlex.split(row)
            
            if column:
                if self.current_user_id == column[0]:
                    email = column[3]
                
        return email
 
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
 
 
    def get_db_subject_info_for_schedule(self):
        
        subject_info = []
        with open(self.db_all_user_schedule, "r") as file:
            lines = file.readlines()
        
        for row in lines:
            column = shlex.split(row)
            
            if column:
                if self.current_user_id == column[0]:
                    subject_info.append(column)
                                   
        # print(
        #     f"user_id               {column[0]}\n"
        #     f"subject_id            {column[1]}\n"
        #     f"teacher_name          {column[2]}\n"
        #     f"subject_name          {column[3]}\n"
        #     f"subject_code          {column[4]}\n"
        #     f"subject_section       {column[5]}\n"
        #     f"time_start            {column[6]}\n"
        #     f"time_end              {column[7]}\n"
        #     f"day1                  {column[8]}\n"
        #     f"day2                  {column[9]}\n"
        #     f"units                 {column[10]}\n"
        #     f"room                  {column[11]}\n"
        #     f"color                 {column[12]}\n"
        #     f"rw                    {column[13]}\n"
        #     f"cl_a                  {column[14]}\n"
        #     f"cl_b                  {column[15]}\n"
        #     f"rspan                 {column[16]}"
        # )
        
        return subject_info
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
    
    def get_db_task_for_to_do(self):
        
        with open(self.db_all_user_task, "r") as file:
            lines = file.readlines()
            
        task_data = []
        for row in lines:
            column = shlex.split(row)
            
            if column:
                if self.current_user_id == column[0]:
                    task_data.append(column)
                else:
                    task_data.append(None)
                       
        return task_data      

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
 
    def get_db_task_for_calendar(self):
        
        with open(self.db_all_user_books, "r") as file:
            lines = file.readlines()
            
        book_data = []
        for row in lines:
            column = shlex.split(row)
            
            if column:
                if self.current_user_id == column[0]:
                    book_data.append(column)
         
                    
        
        return book_data
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
 
 
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
 
 
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
 
           
db = UserAccount() #create the object
#print(db.register("John", "John@gmail.com", "Asher", "asdasd"))    #insert data
print(db.login("asd", "asdasd"))
#print("\n")


#print(db.forgot_password("Mark", "123123", "123123"))
#print(db.save_user_task("Testing Task", "October", "10", "2025", "11", "14", "AM", "I don't know the deadline"))
                            #teacher_name, subject_name, subject_code, subject_section, time_start, time_end, day1, day2, units, room, color
#print(db.edit_user_task("My Second Assignment", "October", "10", "2025", "11", "14", "AM", "I don't know the deadline", "task_1"))
#print(db.save_user_schedule("Cua", "OOP", "CCS123", "CS321", "10:30 AM", "12:00 PM", "Monday", "None (once a week)", "3", "CC1", "#E0B0FF"))
#db.check_task_due_date()
#print(db.get_db_nickname_for_dashboard())
#print(db.get_db_email_for_dashboard())
#print(db.get_db_subject_info_for_schedule())
#print(db.get_db_task_for_to_do())
print(db.get_db_task_for_calendar())
#print(db.save_borrowed_books())
db.logout_user()