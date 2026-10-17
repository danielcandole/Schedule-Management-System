import tkinter as tk
import customtkinter as ctk
from datetime import datetime, timedelta
import calendar
from utils.resource_path import resource_path


class ShowCalendarPage(ctk.CTkFrame):
    
    def __init__(self, master, backend, show_to_do_page=None, show_notification=None): 
        super().__init__(master, fg_color="#ecf4ff")
        self.current_frame = None
        self.backend = backend
        
        self.show_to_do_page = show_to_do_page
        
       
        now = datetime.now()

        self.current_year = now.year
        self.current_month = now.month
        
        self.date_entry = ctk.CTkEntry(self)
        self.date_entry.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        self.popup = None
        
        self.selected_date = None
        self.date_format = "%m/%d/%Y"
        
        self.allow_manual_input = True
        self.allow_change_month = True
        
        self.add_months = 0
        self.subtract_months = 0
        
        self.borrowed_books = {}
        
        self.active_popup = None
        self.show_notification = show_notification  

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def show_page(self, name):
        if name in "show_calendar":
            self.show_calendar()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.current_frame = None

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.show_calendar()

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.show_calendar()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def select_date(self, day):
        # Destroy any active popup
        if self.active_popup:
            for w in self.active_popup:
                w.destroy()
            self.active_popup = None

        selected_date = datetime(self.current_year, self.current_month, day)
        self.selected_date = selected_date

        # Find button widget coordinates
        btn_widget = self.day_buttons.get(day)
        if not btn_widget:
            return

        x = btn_widget.winfo_x()
        y = btn_widget.winfo_y() - 40  # place above the day
        parent = btn_widget.master

        # Center Add Task button if Sunday
        if selected_date.weekday() == 6:  # Sunday
            add_task_x = x + btn_widget.winfo_width() // 2 - 40  # button width = 80
        else:
            add_task_x = x - 40  # default left offset

        # Use the existing show_to_do_page instance
        if self.show_to_do_page:  
            add_task_btn = ctk.CTkButton(
                parent,
                text="Add Task",
                width=80,
                height=25,
                fg_color="#354eab",
                text_color="white",
                command=lambda: self.create_add_event()
            )
            add_task_btn.place(x=add_task_x, y=y)
            self.active_popup = [add_task_btn]
        else:
            self.active_popup = []

        # Only show Borrowed Book button if NOT Sunday
        if selected_date.weekday() != 6:
            borrowed_btn = ctk.CTkButton(
                parent,
                text="Borrowed Book",
                width=120,
                height=25,
                fg_color="#007B83",
                text_color="white",
                command=lambda: self.borrow_book(selected_date)
            )
            borrowed_btn.place(x=x + 50, y=y)
            self.active_popup.append(borrowed_btn)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def add_task(self, date):
        if self.active_popup:
            for w in self.active_popup:
                w.destroy()
            self.active_popup = None

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def show_calendar(self):
        self.clear_frame()
        color1 = "#ffffff"
        mainFrame = ctk.CTkFrame(self, fg_color="#ecf4ff")
        mainFrame.pack(fill="y", expand=True)

        if hasattr(self, "calendar_frame"):
            self.calendar_frame.destroy()

        self.calendar_frame = ctk.CTkFrame(mainFrame, fg_color=color1)
        self.calendar_frame.pack(pady=20)

        if self.add_months < 0:
            raise ValueError("add_months cannot be negative")
        for i in range(self.add_months):
            if self.current_month == 12:
                self.current_month = 1
                self.current_year += 1
            else:
                self.current_month += 1

        if self.subtract_months < 0:
            raise ValueError("subtract_months cannot be negative")
        for i in range(self.subtract_months):
            if self.current_month == 1:
                self.current_month = 12
                self.current_year -= 1
            else:
                self.current_month -= 1

        month_label = ctk.CTkLabel(
            self.calendar_frame,
            text=f"{calendar.month_name[self.current_month].capitalize()} {self.current_year}",
            text_color="black",
            font=("Ubuntu", 30, "bold"),
        )
        month_label.grid(row=0, column=1, columnspan=5, pady=(20, 30))

        if self.allow_change_month:
            prev_month_button = ctk.CTkButton(
                self.calendar_frame,
                text="⮜",
                text_color="white",
                width=50,
                command=self.prev_month,
                font=("Ubuntu", 40, "bold"),
                fg_color="#0047A3",
                hover_color="#5CA3FF",
            )
            prev_month_button.grid(row=0, column=0)

            next_month_button = ctk.CTkButton(
                self.calendar_frame,
                text="⮞",
                text_color="white",
                width=50,command=self.next_month,
                font=("Ubuntu", 40, "bold"),
                fg_color="#0047A3",
                hover_color="#5CA3FF",
            )
            next_month_button.grid(row=0, column=6)

            days = [calendar.day_name[i][:3].capitalize() for i in range(7)]
            for i, day in enumerate(days):
                text_color = "#950F23" if i == 6 else "black"
                lbl = ctk.CTkLabel(
                    self.calendar_frame,
                    text=day,
                    text_color=text_color,
                    font=("Ubuntu", 20, "bold"),
                )
                lbl.grid(row=1, column=i, padx=70, pady=30)

        
        month_days = calendar.monthrange(self.current_year, self.current_month)[1]
        start_day = calendar.monthrange(self.current_year, self.current_month)[0]

        book_user_data = self.backend.get_db_task_for_calendar()
        
        self.day_buttons = {}
        day = 1
        for week in range(2, 8):
            for day_col in range(7):
                if week == 2 and day_col < start_day:
                    lbl = ctk.CTkLabel(self.calendar_frame, text="")
                    lbl.grid(row=week, column=day_col)
                elif day > month_days:
                    lbl = ctk.CTkLabel(self.calendar_frame, text="")
                    lbl.grid(row=week, column=day_col)
                else:
                    text_color = "#950F23" if day_col == 6 else "black"
                    fg_color = "transparent"
                    
    
                    date_key = datetime(self.current_year, self.current_month, day).strftime("%Y-%m-%d")
                    status = None
                    data = None
                    return_date = None
                    for column in book_user_data:
                        date = column[2]
                        status = column[1]
                        return_date = column[5]
                        # determine if this date is teal (return date)
                        
                        #not self.borrowed_books[date_key]["returned"]
                        if status == "Not Returned" and return_date == date_key:
                            fg_color = "#00B5AD"  # teal
                            break
                        else:
                            fg_color = "transparent"

                    btn = ctk.CTkButton(
                        self.calendar_frame,text=str(day), width=100,
                        height=80,command=lambda day=day: self.handle_day_click(day),font=("Ubuntu", 20, "bold"), 
                        fg_color=fg_color,text_color=text_color,hover_color="#E6F1FF",)
                    btn.grid(row=week, column=day_col, pady=(0, 30))
                    self.day_buttons[day] = btn
                    day += 1

        self.current_frame = self
        return self

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def handle_day_click(self, day):
        date_clicked = datetime(self.current_year, self.current_month, day)
        date_key = date_clicked.strftime("%Y-%m-%d")
        


        # Destroy old popups
        if self.active_popup:
            for w in self.active_popup:
                w.destroy()
            self.active_popup = None

        btn_widget = self.day_buttons.get(day)
        if not btn_widget:
            return

        x = btn_widget.winfo_x()
        y = btn_widget.winfo_y() - 40
        parent = btn_widget.master
        self.active_popup = []

        #if sunday no borrow button
        if date_clicked.weekday() == 6:  # 6 = Sunday
            add_task_btn = ctk.CTkButton(
                parent,text="Add Task",width=80,
                height=25,fg_color="#5CA3FF", text_color="white", command=lambda: self.create_add_event())
            #center add task
            add_task_btn.place(
                x=x + (btn_widget.winfo_width() // 2) - 50, y=y)
            self.active_popup.append(add_task_btn)
            return

        # task button left side
        add_task_btn = ctk.CTkButton(
            parent, text="Add Task", width=70,
            height=25, fg_color="#5CA3FF", text_color="white", command=lambda: self.create_add_event())
        add_task_btn.place(x=x - 40, y=y)
        self.active_popup.append(add_task_btn)
        
        book_user_data = self.backend.get_db_task_for_calendar()
        
        status = None
        data = None
        
        for column in book_user_data:
           date = column[2]
           status = column[1]
            
        #date_key in self.borrowed_books and not self.borrowed_books[date_key]["returned"]    
        #If borrowed and not returned
        if status == "Not Returned": #
            print(date_key)
            # book_data = self.borrowed_books[date_key]
            # renew_count = book_data.get("renew_count", 0)
   
            return_btn = ctk.CTkButton(
                parent, text="Returned Book", width=100, height=25,
                fg_color="#009688", text_color="white", command=lambda: self.mark_returned(date_clicked.date()),)
            return_btn.place(x=x + 40, y=y)
            self.active_popup.append(return_btn)
            

            # Renew button max 2 times
            # if renew_count < 2:
            #     renew_btn = ctk.CTkButton(
            #         parent, text=f"Renew Book[{renew_count}/2]", width=100,
            #         height=25, fg_color="#FF9800", text_color="white", command=lambda: self.renew_book(date_clicked),)
            #     renew_btn.place(x=x + 150, y=y)
            #     self.active_popup.append(renew_btn)

        else:
            # Normal day → show Borrow Book button
            borrowed_btn = ctk.CTkButton(
                parent,text="Borrowed Book", width=90, height=25,
                fg_color="#009688", text_color="white",command=lambda: self.borrow_book(date_clicked)
            )
            borrowed_btn.place(x=x + 40, y=y)
            self.active_popup.append(borrowed_btn)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def renew_book(self, current_return_date):
        date_key = current_return_date.strftime("%Y-%m-%d")

        if date_key not in self.borrowed_books:
            if self.show_notification:
                self.show_notification("No borrowed record found for this date.")
            return

        book_data = self.borrowed_books[date_key]
        renew_count = book_data.get("renew_count", 0)
        current_count = book_data.get("book_count", 1)
        original_count = book_data.get("original_count", current_count)

        if renew_count >= 2:
            if self.show_notification:
                self.show_notification("Maximum renewals reached (2).")
            return

        # Compute new count and new return date
        new_count = current_count + original_count
        new_return_date = current_return_date + timedelta(days=3)
        if new_return_date.weekday() == 6:
            new_return_date += timedelta(days=1)

        new_key = new_return_date.strftime("%Y-%m-%d")

        # Store new data (update local record)
        self.borrowed_books[new_key] = {
            "borrowed_date": book_data["borrowed_date"],
            "returned": False,
            "book_count": new_count,
            "original_count": original_count,
            "renew_count": renew_count + 1
        }

        #Remove old record
        del self.borrowed_books[date_key]

        # Update the backend with new count and status
        self.backend.borrowed_method(
            action="renew",           # still "add" because it extends borrowing
            count=original_count,   # only add the new borrowed amount
            status="not returned"   # mark it as still borrowed
        )
        #NOTIF SA USER  
        if self.show_notification:
            self.show_notification(
                f"The current book count is: {new_count}\n"
                f"New return date: {new_return_date.date()} (Renewal #{renew_count + 1})"
            )

        # Refresh calendar UI
        self.show_calendar()

   
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def mark_returned(self, date_clicked):
        # date_key = date_clicked.strftime("%Y-%m-%d")

        # book_user_data = self.backend.get_db_task_for_calendar()
        
        # status = None
        # data = None
        # return_date = None
        
        # for column in book_user_data:
        #     date = column[2]
        #     status = column[1]
        #     return_date = column[5]
           
           
        # if status == "Not Returned":
        #     if self.show_notification:
        #         self.show_notification("No borrowed record found for this date.")
        #     return
        
        
        # record = self.borrowed_books[date_key]
        # record["returned"] = True

        # Update backend correctly (use 'return' not 'add')
        # self.backend.borrowed_method(
        #     action="return",
        #     count=record["book_count"],
        #     status="returned"
        # )
        
        
        self.backend.update_book_status(date_clicked)
        print(date_clicked)
        
        

        # Notify and refresh
        if self.show_notification:
            self.show_notification(f"Book returned on {date_clicked} — Very Good!")

        self.show_calendar()

        if self.active_popup:
            for w in self.active_popup:
                w.destroy()
            self.active_popup = None


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def borrow_book(self, borrow_date):
        # Close any existing popup
        if self.active_popup:
            for w in self.active_popup:
                w.destroy()
            self.active_popup = None

        # Popup frame
        popup_frame = ctk.CTkFrame(self.calendar_frame, fg_color="#E8F6F3", corner_radius=10)
        popup_frame.place(relx=0.5, rely=0.5, anchor="center")

        lbl = ctk.CTkLabel(popup_frame, text="How many books you borrow?", text_color="black")
        lbl.grid(row=0, column=0, columnspan=2, pady=(8, 4), padx=10)

        count_entry = ctk.CTkEntry(popup_frame, placeholder_text="Enter number", width=100)
        count_entry.grid(row=1, column=0, columnspan=2, pady=(0, 4), padx=10)

        # Confirm button
        confirm_btn = ctk.CTkButton(
            popup_frame,
            text="Confirm",
            fg_color="#354eab",
            text_color="white",
            command=lambda: self.confirm_borrow_book(
                borrow_date,
                count_entry.get(),
                popup_frame
            )
        )
        confirm_btn.grid(row=2, column=0, pady=(6, 8), padx=(10, 5))

        # Cancel button
        cancel_btn = ctk.CTkButton(
            popup_frame,
            text="Cancel",
            fg_color="#b0b0b0",
            text_color="black",
            hover_color="#999999",
            command=lambda: self.cancel_borrow(popup_frame)
        )
        cancel_btn.grid(row=2, column=1, pady=(6, 8), padx=(5, 10))

        self.active_popup = [popup_frame]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def confirm_borrow_book(self, borrow_date, count_text, popup_frame=None):
        
        try:
            count = int(count_text)
            if count <= 0:
                raise ValueError
        except ValueError:
            if self.show_notification:
                self.show_notification("Please enter a valid number of books.")
            return

        date = borrow_date.date()
        num_books_borrowed = count_text
        self.backend.save_borrowed_books(date, num_books_borrowed)

        # # Check if user still has unreturned books
        # for record in self.borrowed_books.values():
        #     if not record["returned"]:
        #         if self.show_notification:
        #             self.show_notification("You must return your current book before borrowing another.")
        #         return

        # # Calculate return date (3 days rule)
        # return_date = borrow_date + timedelta(days=3)
        # if return_date.weekday() == 6:  # Sunday = 6
        #     return_date += timedelta(days=1)

        # # Get previous total books (after renews)

        # Add new borrowed amount to previous total
        
        #new_total = self.backend.get_db_task_for_calendar()
        
        # # Store new record
        # date_key = return_date.strftime("%Y-%m-%d")
        # self.borrowed_books[date_key] = {
        #     "borrowed_date": borrow_date.strftime("%Y-%m-%d"),
        #     "returned": False,
        #     "book_count": new_total,     # running total of all books
        #     "original_count": count,     # amount borrowed this time
        #     "renew_count": 0
        # }

        # # ✅ Update backend (NO TITLE)
        # self.backend.borrowed_method(
        #     action="add",
        #     count=count,
        #     status="not returned"
        # )

        if self.show_notification:
            #self.show_notification(f"Total borrowed books: {new_total}")
            self.show_notification(f"Borrowed {count} book(s) on {borrow_date.date()} ") #return by {return_date.date()}

        # Close popup and refresh UI
        if popup_frame and popup_frame.winfo_exists():
            popup_frame.destroy()

        self.active_popup = None
        self.show_calendar()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def cancel_borrow(self, popup_frame):
        # Check if the popup frame exists before trying to destroy it
        if popup_frame and popup_frame.winfo_exists():
            popup_frame.destroy()  # Closes the popup window

        # Remove any reference to the popup (no active popup now)
        self.active_popup = None

        # If the app supports notifications, show a message to the user
        if self.show_notification:
            self.show_notification("Borrowing canceled.")

    # Calculates total borrowed books and those not yet returned

    def sum_all_borrowed_books(self):
        # Count total number of books borrowed from all records
        total_books = sum(record.get("book_count", 0) for record in self.borrowed_books.values())
        
        # Count only the books that are not returned yet
        unreturned_books = sum(
            record.get("book_count", 0)
            for record in self.borrowed_books.values()
            if not record["returned"]  # Only include if "returned" is False
        )

        # Return both totals as a tuple
        return total_books, unreturned_books


    # ======================================================
    # Updates the borrowed summary display in the UI
    # ======================================================
    def update_borrowed_summary(self):
        """Show borrowed book totals in the UI"""

        # Get total and unreturned counts using the previous function
        total, unreturned = self.sum_all_borrowed_books()

        # Format the text that will appear in the interface
        summary_text = f"Total Borrowed: {total} | Unreturned: {unreturned}"

        # If the main window (master) has a dashboard display, update it
        if hasattr(self.master, "show_dashboard"):
            self.master.show_dashboard()
        else:
            # Otherwise, create a label on the calendar showing the summary
            self.borrow_summary_label = ctk.CTkLabel(
                self.calendar_frame,              # Parent frame
                text=summary_text,                # Text to display
                font=("Ubuntu", 18, "bold"),      # Font styling
                text_color="black",               # Text color
            )

            # Place the label properly inside the layout (grid system)
            self.borrow_summary_label.grid(
                row=0, column=5, columnspan=2,
                sticky="e", padx=20, pady=10
            )


    # ======================================================
    # Gets the number of books from the most recent borrowing record
    # ======================================================
    def get_last_book_total(self):
        # If there are no borrowed books, return 0
        if not self.borrowed_books:
            return 0

        # Get the latest date key (assuming the keys are dates)
        last_key = max(self.borrowed_books.keys())

        # Return how many books were borrowed on that latest record
        return self.borrowed_books[last_key].get("book_count", 0)
    
    
    
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def create_add_event(self):

        color1 = "#ffffff"
        color2 = "#f0f0f0"
        
        if not hasattr(self, "create_task_visible"):
            self.create_task_visible = False

        # If popup is currently visible → hide it safely
        if self.create_task_visible:
            if getattr(self, "create_to_do", None) and self.create_to_do.winfo_exists():
                self.create_to_do.pack_forget()
            if getattr(self, "overlay", None) and self.overlay.winfo_exists():
                self.overlay.place_forget()
            self.create_task_visible = False
            return

        self.create_task_visible = True
        

        # Overlay background (dark transparent frame)
        self.overlay = ctk.CTkFrame(self, fg_color=("transparent"))
        self.overlay.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Popup frame
        self.create_to_do = ctk.CTkFrame(self.overlay, fg_color=color1, corner_radius=15)
        self.create_to_do.pack(pady=20)
        
        close = ctk.CTkButton(self.create_to_do, text="×", text_color="#8B8989", height=20, width=15, font=("Ubuntu", 20),
                                        fg_color=color1, hover_color="#DADADA", corner_radius=100, anchor="ew",
                                        command=lambda: self.create_add_event())
        close.grid(row=0, column=0, pady=(10, 5), sticky="e")
        
        label = ctk.CTkLabel(self.create_to_do, text="Task", text_color="#606060", font=("Ubuntu", 20, "bold"))
        label.grid(row=0, column=0, sticky="w", padx=20, pady=(10, 5))
        
        #Title
        ctk.CTkLabel(self.create_to_do, text="Title", text_color="#606060", font=("Ubuntu", 12)).grid(row=1, column=0, sticky="w", padx=20)
        
        title = ctk.CTkEntry(self.create_to_do, placeholder_text="Add Title", text_color="black", fg_color=color1, border_width=1, 
                                border_color="#e6e6e6", font=("Arial", 15), width=400, height=45)
        title.grid(row=2, column=0, padx=20, pady=(0, 10), columnspan=4, sticky="w")
        
        #Date
        ctk.CTkLabel(self.create_to_do, text="Date", text_color="#606060", font=("Ubuntu", 12)).grid(row=3, column=0, sticky="w", padx=20)
        
        month = [calendar.month_name[m] for m in range(1, 13)]
        month_opt = ctk.CTkOptionMenu(self.create_to_do, values=month, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                        button_color="#ACACAC", button_hover_color="#DADADA", 
                                        dropdown_fg_color=color1, dropdown_text_color="black")
        month_opt.set(calendar.month_name[datetime.now().month])
        month_opt.grid(row=4, column=0, padx=(20, 0), pady=(0, 10), sticky="w")

        day = [str(d) for d in range(1, 32)]
        day_opt = ctk.CTkOptionMenu(self.create_to_do, values=day, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                        button_color="#ACACAC", button_hover_color="#DADADA", width=70,
                                        dropdown_fg_color=color1, dropdown_text_color="black")
        day_opt.set(str(datetime.now().day))
        day_opt.grid(row=4, column=0, padx=(200, 0), pady=(0, 10), sticky="w")

        year = [str(y) for y in range(2010, datetime.now().year + 11)]
        year_opt = ctk.CTkOptionMenu(self.create_to_do, values=year, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                        button_color="#ACACAC", button_hover_color="#DADADA", width=90,
                                        dropdown_fg_color=color1, dropdown_text_color="black")
        year_opt.set(str(datetime.now().year))
        year_opt.grid(row=4, column=0, padx=(300, 0), pady=(0, 10), sticky="w")
        
        #Time
        ctk.CTkLabel(self.create_to_do, text="Deadline", text_color="#606060", font=("Ubuntu", 12)).grid(row=5, column=0, sticky="w", padx=20)
        
        hour = ctk.CTkEntry(self.create_to_do, placeholder_text="hour", text_color="black", fg_color=color1, border_width=1, 
                            border_color="#e6e6e6", font=("Arial", 15), width=90, height=30)
        hour.grid(row=6, column=0, padx=(20, 0), pady=(0, 10), sticky="w")
        
        colon = ctk.CTkLabel(self.create_to_do, text=":", text_color="black")
        colon.grid(row=6, column=0, padx=(118, 0), pady=(0, 10), sticky="w")
        
        minutes = ctk.CTkEntry(self.create_to_do, placeholder_text="minutes", text_color="black", fg_color=color1, border_width=1, 
                                border_color="#e6e6e6", font=("Arial", 15), width=90, height=30)
        minutes.grid(row=6, column=0, padx=(130, 0), pady=(0, 10), sticky="w")
        
        

        period = ctk.CTkOptionMenu(self.create_to_do, values=["AM", "PM"], fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                        button_color="#ACACAC", button_hover_color="#DADADA", width=90,
                                        dropdown_fg_color=color1, dropdown_text_color="black")
        period.grid(row=6, column=0, padx=(240, 0), pady=(0, 10), sticky="w")

        #Description
        ctk.CTkLabel(self.create_to_do, text="Description", text_color="#606060", font=("Ubuntu", 12)).grid(row=7, column=0, sticky="w", padx=20)
        
        description = ctk.CTkTextbox(self.create_to_do, text_color="black", width=400, height=90, 
                                    fg_color=color1, border_width=1, font=("Arial", 15),
                                        border_color="#e6e6e6", corner_radius=10)
        description.grid(row=8, column=0, padx=(20, 0), pady=(0, 30))
        
        
                                        
        save_task = ctk.CTkButton(self.create_to_do, text="Save", text_color="#ffffff", height=40, width=20, font=("Ubuntu", 15),
                                        fg_color="#2068C6", hover_color="#4C82CA", corner_radius=100, anchor="ew",
                                        command=None)  
        save_task.grid(row=9, column=0, pady=(10, 15), sticky="e")
        
        # if mode is None:
        #     label.configure(text="Create")
        #     save_task.configure(command=lambda: (
        #                                 self.create_task("create"),
        #                                 self.save_task(
        #                                     title.get(),                        
        #                                     month_opt.get(),                   
        #                                     day_opt.get(),                      
        #                                     year_opt.get(),                     
        #                                     hour.get(),                          
        #                                     minutes.get(),                      
        #                                     period.get(),                        
        #                                     description.get("1.0", "end-1c")     
        #                                     )
        #                                 ))
        # elif mode == "edit" and task_data is not None:
            
        #     label.configure(text="Edit")

        #     title.insert(0, task_data[2])                       # For CTkEntry
        #     month_opt.set(task_data[3])                         # For CTkOptionMenu
        #     day_opt.set(task_data[4])                             # For CTkOptionMenu
        #     year_opt.set(task_data[5])                           # For CTkOptionMenu
        #     hour.insert(0, task_data[6])                         # For CTkEntry
        #     minutes.insert(0, task_data[7])                   # For CTkEntry
        #     period.set(task_data[8])                           # For CTkOptionMenu
        #     description.insert("1.0", task_data[10])  
            
        #     save_task.configure(command=lambda t_id=task_data: (
        #                                 self.create_task("edit"),
        #                                 self.edit_task(
        #                                     title.get(),                        
        #                                     month_opt.get(),                   
        #                                     day_opt.get(),                      
        #                                     year_opt.get(),                     
        #                                     hour.get(),                          
        #                                     minutes.get(),                      
        #                                     period.get(),                        
        #                                     description.get("1.0", "end-1c"),
        #                                     task_data[1]
        #                                     )
        #                                 ))