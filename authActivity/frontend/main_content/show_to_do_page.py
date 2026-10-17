import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import calendar



# from CTkDatePicker.CTkDatePicker.ctk_date_picker import CTkDatePicker

from PIL import Image
from utils.resource_path import resource_path



class ShowToDoPage(ctk.CTkFrame):
    def __init__(self, master, backend):
        super().__init__(master, fg_color="#ecf4ff")
        self.current_frame = None
        self.backend = backend

        # # Create calendar page and pass this to it
        # self.calendar_page = ShowCalendarPage(master=master, backend=backend, show_to_do_page=self)

                 
# initializing ↑ ↑ ↑ ↑ ↑  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            
    def show_page(self, name):
        if name in "show_to_do":
            self.show_to_do()
      
    def clear_frame(self):

        for widget in self.winfo_children():
            widget.destroy()
        self.current_frame = None
        
    def testing_function(self, name):
        #check
        print(name, "button is working!")
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
       
    def save_task(self, title, month, day, year, hour, minutes, period, description):
        self.backend.save_user_task(title, month, day, year, hour, minutes, period, description)
        # print(title)
        # print(month)
        # print(day)
        # print(year)
        # print(hour)
        # print(minutes)
        # print(period)
        # print(description)
        self.show_to_do()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def edit_task(self, title, month, day, year, hour, minutes, period, description, task_id):
        # print(title)
        # print(month)
        # print(day)
        # print(year)
        # print(hour)
        # print(minutes)
        # print(period)
        # print(description)
        # print(task_id)
        self.backend.edit_user_task(title, month, day, year, hour, minutes, period, description, task_id)
        
        self.show_to_do()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def show_to_do(self):
        self.clear_frame()
        #Colors
        color1 = "#ffffff"
        fg = "#ffffff"
        FGlightgrey = "#f0f0f0"
        BGlightgrey = "#f0f0f0"
        box_border_color = "#CFCFCF"
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        #Missing Task     | BOX 1
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        
        mainFrame = ctk.CTkFrame(self, fg_color="#ecf4ff")
        mainFrame.pack()
        
        self.backend.check_task_due_date()                      #To check if tasks are beyond due date
        tasks = self.backend.get_db_task_for_to_do()            #get user task record

        box1_frame = ctk.CTkFrame(mainFrame, fg_color=color1, bg_color=BGlightgrey, border_color=box_border_color, border_width=1, corner_radius=15)
        box1_frame.grid(row=0, column=0, rowspan=2, pady=(10, 0))

        #Width setting
        #ctk.CTkLabel(box1_frame, text="", width=500, height=1).grid(row=0, column=0, pady=1)
        ctk.CTkFrame(box1_frame, fg_color=fg, border_width=1, height=1, width=500).grid(row=0, column=0, sticky="n", pady=5) #width setting (DO NOT REMOVE)
        label = ctk.CTkLabel(box1_frame, text="My Tasks", text_color="black", font=("Ubuntu", 18, "bold"))
        label.grid(row=0, column=0, sticky="w", padx=(20, 0), pady=15)
        
        
        if not tasks:
            openf_icon = Image.open(resource_path("assets/images/main_contents/to_do_icons/no_task.png"))
            icon_img = ctk.CTkImage(light_image=openf_icon, dark_image=openf_icon, size=(100, 100))
            note = ctk.CTkLabel(box1_frame, image=icon_img, text="        ", compound="right")
            note.grid(row=2, column=0, pady=(50, 5))
            
            note = ctk.CTkLabel(box1_frame, text="No tasks yet", text_color="#8B8989", font=("Ubuntu", 15))
            note.grid(row=3, column=0, pady=(10, 310))
        else:
            index = 0
            
            scroll = ctk.CTkScrollableFrame(box1_frame, fg_color=color1, width=500, height=480)
            scroll.grid(row=index + 1, column=0, padx=1)
                    
        # print("\n0    user_id",       task_data[0]
        #       "\n1    task_id",       task_data[1]
        #       "\n2    title",         task_data[2]
        #       "\n3    month",         task_data[3]
        #       "\n4    day",           task_data[4]
        #       "\n5    year",          task_data[5]
        #       "\n6    hour",          task_data[6]
        #       "\n7    minutes",       task_data[7]
        #       "\n8    period",        task_data[8]
        #       "\n9    status",        task_data[9]
        #       "\n10   description",   task_data[10]
        # )
        
            
            for task_data in tasks:
              if task_data[9] == "incomplete":                  
                    
                    check_box_frame = ctk.CTkFrame(scroll, fg_color=color1, corner_radius=15, width=500)
                    check_box_frame.grid(row=index, column=0, sticky="n")
                    
                    width = ctk.CTkFrame(check_box_frame, fg_color=color1, width=490, height=1)
                    width.grid(row=index, column=0, sticky="n")
                    
                    #Three dots
                    three_dots = ctk.CTkButton(check_box_frame, text="⋮", height=10, width=10, corner_radius=15, font=("Ubuntu", 20), text_color="black",
                                            fg_color=color1, hover_color="#e1e1e1")
                    three_dots.configure(command=lambda t=task_data, b=three_dots: self.button_popup_option(t, b, None))
                    three_dots.grid(row=index, column=0, sticky="w", padx=20, pady=(10, 0))
                    
                    
                    task_title = ctk.CTkLabel(check_box_frame, text=f"{task_data[2]}", font=("Arial", 15), text_color="black", wraplength=250)
                    task_title.grid(row=index, column=0, sticky="w", padx=45, pady=(10, 0))
                    
                    date = ctk.CTkLabel(check_box_frame, text=f"{task_data[3]} {task_data[4]}, {task_data[5]}", font=("Arial", 15), text_color="black",)
                    date.grid(row=index, column=0, sticky="e", padx=25, pady=(5, 0))

                    
                    
                    index += 1
                    
                    task_description = ctk.CTkLabel(check_box_frame, text=f"{task_data[10]}", font=("Arial", 15), text_color="#7A7878", height=1,
                                                    wraplength=250, justify="left")
                    task_description.grid(row=index, column=0, sticky="w", padx=45, pady=(0, 5))

                    time = ctk.CTkLabel(check_box_frame, text=f"{task_data[6]}:{task_data[7]} {task_data[8]}", font=("Arial", 15), text_color="black", height=1)
                    time.grid(row=index, column=0, sticky="e", padx=25, pady=(0, 5))
                    index += 1

            spacing = ctk.CTkLabel(box1_frame, text="", height=1)
            spacing.grid(row=2, column=0)
        
    
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                   
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        #Missing Task     | BOX 2
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -               
    
        box2_frame = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=BGlightgrey, border_color=box_border_color, border_width=1, corner_radius=15)
        box2_frame.grid(row=0, column=1, sticky="ns", padx=(20, 0), pady=(20, 20))
        
        ctk.CTkFrame(box2_frame, fg_color=fg, border_width=1, height=1, width=350).grid(row=0, column=0, sticky="n", pady=5) #width setting (DO NOT REMOVE)
        
        ctk.CTkLabel(box2_frame, text=f"Missing", text_color="black", font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 10), padx=10)
        
        scroll_b2 = ctk.CTkScrollableFrame(box2_frame, height=200, width=350, fg_color=fg)
        scroll_b2.grid(row=1, column=0, padx=1)

        index_b2 = 0
   
        for task_data in tasks:
            if task_data[9] == "missing":

                completed_taskframe = ctk.CTkFrame(scroll_b2, fg_color=color1, corner_radius=15, width=350)
                completed_taskframe.grid(row=index_b2, column=0, sticky="n")
        
                ctk.CTkFrame(completed_taskframe, fg_color=color1, width=350, height=1).grid(row=index_b2, column=0, sticky="n")
                
                #Three dots
                three_dots = ctk.CTkButton(completed_taskframe, text="⋮", height=10, width=10, corner_radius=15, font=("Ubuntu", 20), text_color="black",
                                         fg_color=color1, hover_color="#e1e1e1")
                three_dots.configure(command=lambda t=task_data, b=three_dots: self.button_popup_option(t, b, None))
                three_dots.grid(row=index, column=0, sticky="w", padx=20, pady=(10, 0))
                
                
                task_title = ctk.CTkLabel(completed_taskframe, text=f"{task_data[2]}", font=("Arial", 15), text_color="black", wraplength=150)
                task_title.grid(row=index, column=0, sticky="w", padx=45, pady=(10, 0))
                
                date = ctk.CTkLabel(completed_taskframe, text=f"{task_data[3]} {task_data[4]}, {task_data[5]}", font=("Arial", 15), text_color="#950F23",)
                date.grid(row=index, column=0, sticky="e", padx=25, pady=(5, 0))

                
                
                index += 1
                
                task_description = ctk.CTkLabel(completed_taskframe, text=f"{task_data[10]}", font=("Arial", 15), text_color="#7A7878", height=1,
                                                wraplength=150, justify="left")
                task_description.grid(row=index, column=0, sticky="w", padx=45, pady=(0, 5))

                time = ctk.CTkLabel(completed_taskframe, text=f"{task_data[6]}:{task_data[7]} {task_data[8]}", font=("Arial", 15), text_color="#950F23", height=1)
                time.grid(row=index, column=0, sticky="e", padx=25, pady=(0, 5))
                index += 1
                
                index_b2 += 1
    
        
        ctk.CTkFrame(box2_frame, fg_color=fg, border_width=1, height=1, width=350).grid(row=2, column=0, sticky="n", pady=5) #bottom width setting (DO NOT REMOVE)
        

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        #Completed Task     | BOX 3
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -               
    

        
        box3_frame = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=BGlightgrey, border_color=box_border_color, border_width=1, corner_radius=15)
        box3_frame.grid(row=1, column=1, sticky="ns", padx=(20, 0), pady=(0, 20))
        
        ctk.CTkFrame(box3_frame, fg_color=fg, border_width=1, height=1, width=350).grid(row=0, column=0, sticky="n", pady=5) #width setting (DO NOT REMOVE)
        
        ctk.CTkLabel(box3_frame, text=f"Done ", text_color="black", font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 10), padx=10)

        scroll_b3 = ctk.CTkScrollableFrame(box3_frame, height=200, width=350, fg_color=fg)
        scroll_b3.grid(row=1, column=0, padx=1)
        
        index_b3 = 0
        for task_data in tasks:
            if task_data[9] == "complete":

                completed_taskframe = ctk.CTkFrame(scroll_b3, fg_color=color1, corner_radius=15, width=350)
                completed_taskframe.grid(row=index_b3, column=0, sticky="n")
        
                ctk.CTkFrame(completed_taskframe, fg_color=color1, width=350, height=1).grid(row=index_b3, column=0, sticky="n")
                
                #Three dots
                three_dots = ctk.CTkButton(completed_taskframe, text="⋮", height=10, width=10, corner_radius=15, font=("Ubuntu", 20), text_color="black",
                                         fg_color=color1, hover_color="#e1e1e1")
                three_dots.configure(command=lambda t=task_data, b=three_dots: self.button_popup_option(t, b, "not done"))
                three_dots.grid(row=index, column=0, sticky="w", padx=20, pady=(10, 0))
                
                
                task_title = ctk.CTkLabel(completed_taskframe, text=f"{task_data[2]}", font=("Arial", 15), text_color="black", wraplength=120)
                task_title.grid(row=index, column=0, sticky="w", padx=45, pady=(10, 0))
                
                date = ctk.CTkLabel(completed_taskframe, text=f"{task_data[3]} {task_data[4]}, {task_data[5]}", font=("Arial", 15), text_color="black",)
                date.grid(row=index, column=0, sticky="e", padx=25, pady=(5, 0))

                
                
                index += 1
                
                task_description = ctk.CTkLabel(completed_taskframe, text=f"{task_data[10]}", font=("Arial", 15), text_color="#7A7878", height=1,
                                                wraplength=120, justify="left")
                task_description.grid(row=index, column=0, sticky="w", padx=45, pady=(0, 5))

                time = ctk.CTkLabel(completed_taskframe, text=f"{task_data[6]}:{task_data[7]} {task_data[8]}", font=("Arial", 15), text_color="black", height=1)
                time.grid(row=index, column=0, sticky="e", padx=25, pady=(0, 5))
                index += 1
                
                index_b3 += 1
        

        ctk.CTkFrame(box3_frame, fg_color=fg, border_width=1, height=1, width=300).grid(row=2, column=0, sticky="n", pady=5) #bottom width setting (DO NOT REMOVE)
        
        self.current_frame = self
        return self
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def button_popup_option(self, task_data, button, mode=None):
        color1 = "#ffffff"
        color2= "#ECF4FF"
        # Check if popup already exists
        if hasattr(self, "option_frame"):
            # If popup is visible and same button clicked → hide it
            if getattr(self, "option_popup_visible", False) and getattr(self, "last_button_clicked", None) == button:
                self.option_frame.place_forget()
                self.option_popup_visible = False
                return
            else:
                if self.option_frame.winfo_exists():
                    self.option_frame.place_forget()

        # Mark this button as last clicked
        self.last_button_clicked = button
        self.option_popup_visible = True

    # Get button position

        bx = button.winfo_rootx() - self.winfo_rootx()  # X relative to parent
        by = button.winfo_rooty() - self.winfo_rooty()
        bw = button.winfo_width()
        bh = button.winfo_height()

        # Create popup frame (if not exists yet)
        if not hasattr(self, "option_frame") or not self.option_frame.winfo_exists():
            self.option_frame = ctk.CTkFrame(self, fg_color=color1, corner_radius=12)

        # Place it below the button
        self.option_frame.place(x=bx+25, y=by+25)

        # Clear old widgets before adding new (optional)
        for widget in self.option_frame.winfo_children():
            widget.destroy()


        ctk.CTkButton(self.option_frame, text="Edit", text_color="black", fg_color=color2, height=27, width=100, 
                    font=("Ubuntu", 12, "bold"), anchor="w", bg_color=color1, hover_color="#D7E8FF", command=lambda t=task_data:(self.create_task("edit", t), self._close_option_popup())
                    ).grid(row=0, column=0)

        ctk.CTkButton(self.option_frame, text="Delete", text_color="black", fg_color=color2, height=27, width=100, 
                    font=("Ubuntu", 12, "bold"), anchor="w", bg_color=color1, hover_color="#D7E8FF", command=lambda t=task_data: (self.delete_task(t), self._close_option_popup())
                    ).grid(row=1, column=0)
        opt = ctk.CTkButton(self.option_frame, text="Done", text_color="black", fg_color=color2, height=27, width=100, 
                    font=("Ubuntu", 12, "bold"), anchor="w", bg_color=color1, hover_color="#D7E8FF", )
        opt.grid(row=2, column=0)
        
        if mode is None:
            opt.configure(text="Done", command=lambda: self.pop_up_options("done", task_data))
        elif mode == "not done":
            opt.configure(text="Not Done", command=lambda: self.pop_up_options("not done", task_data))
      
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def create_task(self, mode=None, task_data=None):

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
                                        command=lambda: self.create_task())
        close.grid(row=0, column=0, pady=(10, 5), sticky="e")
        
        label = ctk.CTkLabel(self.create_to_do, text="", text_color="#606060", font=("Ubuntu", 20, "bold"))
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
        
        if mode == "create":
            label.configure(text="Create")
            save_task.configure(command=lambda: (
                                        self.create_task("create"),
                                        self.save_task(
                                            title.get(),                        
                                            month_opt.get(),                   
                                            day_opt.get(),                      
                                            year_opt.get(),                     
                                            hour.get(),                          
                                            minutes.get(),                      
                                            period.get(),                        
                                            description.get("1.0", "end-1c")     
                                            )
                                        ))
        elif mode == "edit" and task_data is not None:
            
            label.configure(text="Edit")

            title.insert(0, task_data[2])                       # For CTkEntry
            month_opt.set(task_data[3])                         # For CTkOptionMenu
            day_opt.set(task_data[4])                             # For CTkOptionMenu
            year_opt.set(task_data[5])                           # For CTkOptionMenu
            hour.insert(0, task_data[6])                         # For CTkEntry
            minutes.insert(0, task_data[7])                   # For CTkEntry
            period.set(task_data[8])                           # For CTkOptionMenu
            description.insert("1.0", task_data[10])  
            
            save_task.configure(command=lambda t_id=task_data: (
                                        self.create_task("edit"),
                                        self.edit_task(
                                            title.get(),                        
                                            month_opt.get(),                   
                                            day_opt.get(),                      
                                            year_opt.get(),                     
                                            hour.get(),                          
                                            minutes.get(),                      
                                            period.get(),                        
                                            description.get("1.0", "end-1c"),
                                            task_data[1]
                                            )
                                        ))

 # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
    def _close_option_popup(self):
        if getattr(self, "option_frame", None) and self.option_frame.winfo_exists():
            self.option_frame.destroy()
        self.option_popup_visible = False 
                          
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def delete_task(self, task_data=None):

        if task_data is not None:

            task_d = task_data
            #check
            print(task_d)
        color1 = "#ffffff"
        color2 = "#f0f0f0"
        
        if not hasattr(self, "delete_popup_visible"):
            self.delete_popup_visible = False
            
        # Hide safely if frames exist
        if self.delete_popup_visible:
            if getattr(self, "delete_subject") and self.delete_subject.winfo_exists():
                self.delete_subject.pack_forget()
            if getattr(self, "delete_frame") and self.delete_frame.winfo_exists():
                self.delete_frame.place_forget()
            self.delete_popup_visible = False
            return

    
        self.delete_popup_visible = True

        # Overlay background (dark transparent frame)
        self.delete_frame = ctk.CTkFrame(self, fg_color=("transparent"))
        self.delete_frame.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.15, anchor="center")
        
        self.delete_subject = ctk.CTkFrame(self.delete_frame, fg_color=color1, corner_radius=0, border_width=1, border_color="#CFCFCF")
        self.delete_subject.pack(pady=1, fill="both", expand=True)
        
        # Popup frame
        self.delete_subject.rowconfigure(1, weight=1)
        self.delete_subject.columnconfigure(0, weight=1)
        
        close = ctk.CTkButton(self.delete_subject, text="×", text_color="#8B8989", height=10, width=15, font=("Ubuntu", 20),
                                        fg_color=color1, hover_color="#DADADA", corner_radius=100, anchor="ew",
                                        command=lambda: self.delete_task())
        close.grid(row=0, column=0, sticky="e", padx=10, pady=(10, 0))
        
        ctk.CTkLabel(self.delete_subject, text="Are you sure?", text_color="#606060", font=("Ubuntu", 15), anchor="s", height=15).grid(row=0, column=0, padx=20, pady=(30, 0))
        
        ctk.CTkButton(self.delete_subject, text="Yes", text_color="#ffffff", height=40, width=20, font=("Ubuntu", 15),
                                        fg_color="#091CC8", hover_color="#374AF6", corner_radius=100, anchor="ew",
                                        command=lambda t=task_d: (self.delete_task(), self.pop_up_options("remove", t))
                                        ).grid(row=1, column=0, padx=40, pady=(15, 10), sticky="e")
        ctk.CTkButton(self.delete_subject, text="No", text_color="#ffffff", height=40, width=20, font=("Ubuntu", 15),
                                        fg_color="#C80909", hover_color="#F63737", corner_radius=100, anchor="ew",
                                        command=lambda: self.delete_task()
                                        ).grid(row=1, column=0, padx=40, pady=(15, 10), sticky="w") 
        
        
        
 # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      
    def pop_up_options(self, mode, task_data):
    
        # if getattr(self, "option_popup_visible", False) and getattr(self, "last_button_clicked", None) == button:
        #     self.option_frame.place_forget()
        #     self.option_popup_visible = False
        
        if getattr(self, "delete_subject", None) and self.delete_subject.winfo_exists():
            self.delete_subject.destroy()
        if getattr(self, "delete_frame", None) and self.delete_frame.winfo_exists():
            self.delete_frame.destroy()
        self.delete_popup_visible = False  
        
        if mode == "remove":
            self.backend.delete_user_task(task_data)
        elif mode == "done":
            self.backend.change_task_status("done", task_data)
        elif mode == "not done":
            self.backend.change_task_status("not done", task_data)
        
        self.show_to_do()