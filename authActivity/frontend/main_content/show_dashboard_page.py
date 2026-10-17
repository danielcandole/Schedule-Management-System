import tkinter as tk
import customtkinter as ctk
from PIL import Image
from utils.resource_path import resource_path  # Make sure this exists in your project


class ShowDashboardPage(ctk.CTkFrame):
    def __init__(self, master, backend, calendar_page):
        super().__init__(master, fg_color="#ecf4ff")
        self.current_frame = None
        self.backend = backend
        self.calendar_page = calendar_page

        # Dedicated frame for dynamic content
        self.content_frame = ctk.CTkFrame(self, fg_color="#f0f0f0")
        self.content_frame.pack(fill="both", expand=True)

        # Example: permanent sidebar or buttons (WILL NOT BE DESTROYED)
        # sidebar = ctk.CTkFrame(self, width=200)
        # sidebar.pack(side="left", fill="y")
        # button1 = ctk.CTkButton(sidebar, text="Dashboard", command=self.show_dashboard)
        # button1.pack(pady=10)

        # Labels (for later)
        self.book_count_label = None
        self.returned_label = None
        self.unreturned_label = None
        self.notif_label = None
        


    def show_page(self, name):
        if name == "show_dashboard":
            self.show_dashboard()

    def clear_frame(self):
        for widget in self.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
        self.current_frame = None

    def testing_function(self, name):
        print(name, "button is working!")

    def show_dashboard(self):

        # - - - - - - - - - - - - - - - - 
        #user Profile   | ROW 0
        # - - - - - - - - - - - - - - - - 

        # Clear any previous frames
        self.clear_frame()
        # Colors
        fg = "#ffffff"
        BGlightgrey = "#ecf4ff"


        # Main frame
        mainFrame = ctk.CTkFrame(self, fg_color="#ecf4ff", height=400)
        mainFrame.pack(fill="y", expand=True)

        # width settings (DO NOT REMOVE)
        ctk.CTkFrame(mainFrame, fg_color="#ecf4ff", height=1, width=1100, border_width=1).grid(row=0, column=0, sticky="n")

        # Profile frame
        profileFrame = ctk.CTkFrame(mainFrame, fg_color="#ecf4ff")
        profileFrame.grid(row=0, column=0, padx=70, pady=0, sticky="ew")

        # Profile picture
        openf_pfp = Image.open(resource_path("assets/images/user.png"))
        pfp_img = ctk.CTkImage(light_image=openf_pfp, dark_image=openf_pfp, size=(180, 180))
        pfp_label = ctk.CTkLabel(profileFrame, image=pfp_img, text="")
        pfp_label.grid(row=0, column=0, padx=20, pady=20)

        # Get user info
        nickname = self.backend.get_db_nickname_for_dashboard()
        email = self.backend.get_db_email_for_dashboard()

        # Name label
        name_label = ctk.CTkLabel(
            profileFrame, 
            text=f"Mabuhay! {nickname}", 
            text_color="black", 
            font=("Ubuntu", 45), 
            anchor="w"
        )
        name_label.grid(row=0, column=1, sticky="w", pady=(20, 0), padx=10)

        # Email label 
        email_label = ctk.CTkLabel(
            profileFrame, 
            text=f"{email}", 
            text_color="black", 
            font=("Ubuntu", 14, "italic"), 
            anchor="w"
        )
        email_label.grid(row=0, column=1, sticky="nw", pady=(140, 3), padx=10)

        box_border_color = "#CFCFCF"

        # - - - - - - - - - - - - - - - - 
        #Announcement   | ROW 1
        # - - - - - - - - - - - - - - - - 

        display4 = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=BGlightgrey, border_color=box_border_color, border_width=1, corner_radius=15)
        display4.grid(row=1, column=0, sticky="ns", padx=(0, 500), pady=(0, 30))

        ctk.CTkFrame(display4, fg_color=fg, border_width=1, height=1, width=450).grid(row=0, column=0, sticky="n", pady=5)

        ctk.CTkLabel(display4, text=f"Announcement", text_color="black", font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 10), padx=10)

        scroll1 = ctk.CTkScrollableFrame(display4, height=200, width=450, fg_color=fg)
        scroll1.grid(row=1, column=0, padx=1)

        ctk.CTkFrame(display4, fg_color=fg, border_width=1, height=1, width=450).grid(row=2, column=0, sticky="n", pady=5)

        # - - - - - - - - - - - - - - - - 
        #Reminder   | ROW 1
        # - - - - - - - - - - - - - - - - 

        display5 = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=BGlightgrey, border_color=box_border_color, border_width=1, corner_radius=15)
        display5.grid(row=1, column=0, sticky="ns", padx=(500, 0), pady=(0, 30),rowspan=2)

        ctk.CTkFrame(display5, fg_color=fg, border_width=1, height=1, width=450).grid(row=0, column=0, sticky="n", pady=5)

        ctk.CTkLabel(display5, text=f"Reminder", text_color="black", font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 10), padx=10)

        scroll1 = ctk.CTkScrollableFrame(display5, height=400, width=450, fg_color=fg)
        scroll1.grid(row=1, column=0, padx=1)

        ctk.CTkFrame(display5, fg_color=fg, border_width=1, height=1, width=450).grid(row=2, column=0, sticky="n", pady=5)

        # - - - - - - - - - - - - - - - - 
        # Number of Books   | ROW 2
        # - - - - - - - - - - - - - - - - 
        display1 = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=BGlightgrey,
                                    border_color=box_border_color, border_width=1, corner_radius=15)
        display1.grid(row=2, column=0, sticky="ns", padx=(0, 750), pady=(0, 30))

        ctk.CTkFrame(display1, fg_color=fg, border_width=1, height=1, width=230).grid(row=0, column=0, sticky="n", pady=5)

        ctk.CTkLabel(display1, text="Number of Books", text_color="black",
                        font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 10), padx=10)
        
        book_user_data = self.backend.get_db_task_for_calendar()
        
        status = None
        data = None
        current_borrowed_books = None
        total_books = None
        return_date = None
        
        for column in book_user_data:
            
            status = column[1]

            current_borrowed_books = column[3]
            total_books = column[4]
   

            
        # Display labels
        self.book_count_label = ctk.CTkLabel(
            display1,
            text=f"Total Borrowed Books: {total_books}",
            text_color=("#333333", "#000000"),
            font=("Ubuntu", 14)
        )
        self.book_count_label.grid(row=1, column=0, pady=(10, 5))

        self.returned_label = ctk.CTkLabel(
            display1,
            text=f"Current Borrowed Book: {current_borrowed_books}",
            text_color=("#008000", "#000000"),
            font=("Ubuntu", 14)
        )
        self.returned_label.grid(row=2, column=0, pady=(2, 0))

        self.unreturned_label = ctk.CTkLabel(
            display1,
            text=f"Status: {status}",
            text_color=("#a60000", "#000000"),
            font=("Ubuntu", 14)
        )
        self.unreturned_label.grid(row=3, column=0, pady=(2, 10))

        # Borrowed notification summary
        self.notif_label = ctk.CTkLabel(
            display1,
            text="",
            text_color="black",
            font=("Ubuntu", 12),
            wraplength=200,
            justify="center"
        )
        self.notif_label.grid(row=4, column=0, pady=(5, 10))

        # Refresh stats initially
        #self.refresh_borrowed_stats()

        # - - - - - - - - - - - - - - - - 
        #Accomplishments  | ROW 2
        # - - - - - - - - - - - - - - - - 

        display2 = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=BGlightgrey, border_color=box_border_color, border_width=1, corner_radius=15)
        display2.grid(row=2, column=0, sticky="ns", padx=(0, 255), pady=(0, 30))

        ctk.CTkFrame(display2, fg_color=fg, border_width=1, height=1, width=230).grid(row=0, column=0, sticky="n", pady=5)

        ctk.CTkLabel(display2, text=f"Accomplishments", text_color="black", font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 10), padx=10)
    
    # def refresh_borrowed_stats(self):
        
        
    #     book_user_data = self.backend.get_db_task_for_calendar()
        
    #     status = None
    #     data = None
    #     current_borrowed_books = None
    #     total_books = None
    #     return_date = None
        
    #     for column in book_user_data:
            
    #         status = column[1]

    #         current_borrowed_books = column[3]
    #         total_books = column[4]
        
        
    #     """Refresh the book statistics labels"""
    #     stats = self.backend.borrowed_method("stats")
    #     if stats:
    #         total_books = stats["total"]
    #         returned_books = stats["returned"]
    #         unreturned_books = stats["not_returned"]
    #     else:
    #         total_books = returned_books = unreturned_books = 0

    #     if self.book_count_label:
    #         self.book_count_label.configure(text=f"{total_books}")
    #     if self.returned_label:
    #         self.returned_label.configure(text=f"Returned: {returned_books}")
    #     if self.unreturned_label:
    #         self.unreturned_label.configure(text=f"Not returned: {unreturned_books}")


    #     try:
    #         borrowed_info = self.backend.borrowed_method("recent")
    #         if borrowed_info and self.notif_label:
    #             self.notif_label.configure(text=borrowed_info)
    #     except Exception as e:
    #         print("Error getting recent borrowed info:", e)