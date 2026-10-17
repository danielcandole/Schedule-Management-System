import tkinter as tk
import customtkinter as ctk


from PIL import Image
from utils.resource_path import resource_path

class ShowSchedulePage(ctk.CTkFrame):
    def __init__(self, master, backend):
        super().__init__(master, fg_color="#f0f0f0")
        self.current_frame = None
        self.backend = backend
        
        self.weeks = ["Monday" ,"Tuesday" ,"Wednesday" ,"Thursday" ,"Friday" ,"Saturday" ,"Sunday",  ]
        self.weeks0 = ["Monday" ,"Tuesday" ,"Wednesday" ,"Thursday" ,"Friday" ,"Saturday"  ]
        self.weeks1 = ["Monday" ,"Tuesday" ,"Wednesday" ,"Thursday" ,"Friday" ,"Saturday" , "None (once a week)" ]
        
        # self.time = [
        #     "07:30 AM - 08:00 AM", "08:00 AM - 08:30 AM", "08:30 AM - 09:00 AM", "09:00 AM - 09:30 AM", "09:30 AM - 10:00 AM",
        #     "10:00 AM - 10:30 AM", "10:30 AM - 11:00 AM", "11:00 AM - 11:30 AM", "11:30 AM - 12:00 PM", "12:00 PM - 12:30 PM",
        #     "12:30 PM - 01:00 PM", "01:00 PM - 01:30 PM", "01:30 PM - 02:00 PM", "02:00 PM - 02:30 PM", "02:30 PM - 03:00 PM",
        #     "03:00 PM - 03:30 PM", "03:30 PM - 04:00 PM", "04:00 PM - 04:30 PM", "04:30 PM - 05:00 PM", "05:00 PM - 05:30 PM",
        #     "05:30 PM - 06:00 PM", "06:00 PM - 06:30 PM", "06:30 PM - 07:00 PM", "07:00 PM - 07:30 PM"
        # ]
                
        self.time_sched = [
            "07:30 AM", "08:00 AM", "08:30 AM", "09:00 AM", "09:30 AM",
            "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM", "12:00 PM",
            "12:30 PM", "01:00 PM", "01:30 PM", "02:00 PM", "02:30 PM",
            "03:00 PM", "03:30 PM", "04:00 PM", "04:30 PM", "05:00 PM",
            "05:30 PM", "06:00 PM", "06:30 PM", "07:00 PM", "07:30 PM"
        ]
        self.sub_units = ["1", "2", "3", "4", "5"]
        
        self.choose_color = [
            "#FADADD",  # Soft Rose
            "#BFD7ED",  # Powder Blue
            "#E6E6FA",  # Lavender Mist
            "#CAE7F1",  # Frost Blue
            "#E2CFEA",  # Pale Lilac
            "#F8C8C8",  # Baby Blush
            "#C3CDE6",  # Periwinkle
            "#D8BFD8",  # Dusty Mauve
            "#E0B0FF",  # Light Orchid
            "#B0C4DE",  # Pale Sky
            "#EEC9D2",  # Blush Rose
            "#D0D6F0"   # Misty Periwinkle
        ]
        
              
# initializing ↑ ↑ ↑ ↑ ↑  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            
    def show_page(self, name):
        if name in "show_schedule":
            self.show_schedule()
      
    def clear_frame(self):

        for widget in self.winfo_children():
            widget.destroy()
        self.current_frame = None
        
    def selected_color(self, col):
        self.label_color.configure(fg_color=col)
        
    def save_schedule(self, teacher_info, subject_info, time_start, time_end, day1, day2, units, room, color):
        for i in range(len(teacher_info)):
            t_info = teacher_info[i]
            if i == 0:
                teacher_name = t_info
            elif i == 1:
                teacher_smc_gmail = t_info
            elif i == 2:
                teacher_id = t_info
        for i in range(len(subject_info)):
            s_info = subject_info[i]
            if i == 0:
                subject_name = s_info
            elif i == 1:
                subject_code = s_info
            elif i == 2:
                subject_section = s_info

        self.backend.save_user_schedule(teacher_name, teacher_smc_gmail, teacher_id, subject_name, subject_code, subject_section, time_start, time_end, day1, day2, units, room, color)
        
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def create_schedule(self):
        color1 = "#ffffff"
        color2 = "#f0f0f0"
        if hasattr(self, "create_schedule_visible") and self.create_schedule_visible:
            # Hide safely if frames exist
            if hasattr(self, "create_sched"):
                self.create_sched.pack_forget()
            if hasattr(self, "overlay"):
                self.overlay.place_forget()
            self.create_schedule_visible = False
            return

        else:
            self.create_schedule_visible = True

            # Overlay background (dark transparent frame)
            self.overlay = ctk.CTkFrame(self, fg_color=("transparent"))
            self.overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
            
            # Popup frame
            self.create_sched = ctk.CTkFrame(self.overlay, fg_color=color1, corner_radius=15)
            self.create_sched.pack(pady=20, fill="y", expand=True)
            
            self.create_sched.rowconfigure(1, weight=1)
            self.create_sched.columnconfigure(0, weight=1)
            
            close = ctk.CTkButton(self.create_sched, text="×", text_color="#8B8989", height=10, width=15, font=("Ubuntu", 20),
                                           fg_color=color1, hover_color="#DADADA", corner_radius=100, anchor="ew",
                                           command=self.create_schedule)
            close.grid(row=0, column=0, sticky="e", padx=10, pady=(10, 0))

            scroll = ctk.CTkScrollableFrame(self.create_sched, fg_color=color1, width=430)
            scroll.grid(row=1, column=0, padx=(0, 10), sticky="ns")
            
            ctk.CTkFrame(self.create_sched, fg_color="#FFFFFF", height=1, border_width=1).grid(row=2, column=0, pady=10) #gap/spacing
            
            
            #Teacher Information
            tea_label = ctk.CTkLabel(scroll, text="Teacher Information", text_color="#606060", font=("Ubuntu", 20, "bold"))
            tea_label.grid(row=1, column=0, sticky="w", padx=20, pady=(0, 5))
            
            tea_label_names = ["Teacher Name", "SMC Gmail", "Teacher ID"]
            tea_text_holder = ["Add name", "Add gmail", "Add ID"]
            tea_entries = []
            rw_a = 2
            for i in range(len(tea_label_names)):
                ctk.CTkLabel(scroll, text=tea_label_names[i], text_color="#606060", font=("Ubuntu", 12)).grid(row=rw_a, column=0, sticky="w", padx=20)
                rw_a += 1
                teacher_info = ctk.CTkEntry(scroll, placeholder_text=tea_text_holder[i], text_color="black", fg_color=color1, border_width=1, 
                                    border_color="#e6e6e6", font=("Arial", 15), width=400, height=45)
                teacher_info.grid(row=rw_a, column=0, padx=20, pady=(0, 10), sticky="w")
                rw_a += 1
                tea_entries.append(teacher_info)
            
            
            #line
            ctk.CTkFrame(scroll, fg_color="#BCBCBC", height=1, width=390, border_width=1).grid(row=8, column=0, sticky="s", pady=(20, 30))
            
            
            #Subject Information
            sub_label = ctk.CTkLabel(scroll, text="Subject Information", text_color="#606060", font=("Ubuntu", 20, "bold"))
            sub_label.grid(row=9, column=0, sticky="w", padx=20, pady=(0, 5))
            
            sub_label_names = ["Subject Name", "Subject Code", "Section"]
            sbu_text_holder = ["Add name", "Add code", "Add section"]
            sub_entries = []
            rw_b = 10
            for i in range(len(sub_label_names)):
                ctk.CTkLabel(scroll, text=sub_label_names[i], text_color="#606060", font=("Ubuntu", 12)).grid(row=rw_b, column=0, sticky="w", padx=20)
                rw_b += 1
                subject_info = ctk.CTkEntry(scroll, placeholder_text=sbu_text_holder[i], text_color="black", fg_color=color1, border_width=1, 
                                    border_color="#e6e6e6", font=("Arial", 15), width=400, height=45)
                subject_info.grid(row=rw_b, column=0, padx=20, pady=(0, 10), sticky="w")
                rw_b += 1
                sub_entries.append(subject_info)
            
            #Time
            ctk.CTkLabel(scroll, text="Time", text_color="#606060", font=("Ubuntu", 12)).grid(row=16, column=0, sticky="w", padx=20)
            ctk.CTkLabel(scroll, text="to", text_color="#606060", font=("Ubuntu", 12)).grid(row=17, column=0, padx=(0, 0), sticky="n")
            time_start = ctk.CTkOptionMenu(scroll, values=self.time_sched, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                         button_color="#ACACAC", button_hover_color="#DADADA", width=180,
                                         dropdown_fg_color=color1, dropdown_text_color="black")
            time_start.grid(row=17, column=0, padx=20, pady=(0, 10), sticky="w")
                            # choose_color.bind("<Enter>", lambda e, b=choose_color: b.configure(height=25, width=25))
                # choose_color.bind("<Leave>", lambda e, b=choose_color: b.configure(height=20, width=20))
            time_end = ctk.CTkOptionMenu(scroll, values=self.time_sched, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                         button_color="#ACACAC", button_hover_color="#DADADA", width=180,
                                         dropdown_fg_color=color1, dropdown_text_color="black")
            time_end.grid(row=17, column=0, padx=20, pady=(0, 10), sticky="e")
            
            #Day
            ctk.CTkLabel(scroll, text="Day", text_color="#606060", font=("Ubuntu", 12)).grid(row=18, column=0, sticky="w", padx=20)
            ctk.CTkLabel(scroll, text="and", text_color="#606060", font=("Ubuntu", 12)).grid(row=19, column=0, padx=(0, 0), sticky="n")
            day1 = ctk.CTkOptionMenu(scroll, values=self.weeks0, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                         button_color="#ACACAC", button_hover_color="#DADADA", width=180,
                                         dropdown_fg_color=color1, dropdown_text_color="black")
            day1.grid(row=19, column=0, padx=20, pady=(0, 10), sticky="w")
            
            day2 = ctk.CTkOptionMenu(scroll, values=self.weeks1, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                         button_color="#ACACAC", button_hover_color="#DADADA", width=180,
                                         dropdown_fg_color=color1, dropdown_text_color="black")
            day2.grid(row=19, column=0, padx=20, pady=(0, 10), sticky="e")
            
            #Room
            ctk.CTkLabel(scroll, text="Room", text_color="#606060", font=("Ubuntu", 12)).grid(row=20, column=0, sticky="w", padx=20)  
            room = ctk.CTkEntry(scroll, placeholder_text="Add room", text_color="black", fg_color=color1, border_width=1, 
                                    border_color="#e6e6e6", font=("Arial", 15), width=200, height=45)
            room.grid(row=21, column=0, padx=20, pady=(0, 10), sticky="w")

            #Units
            ctk.CTkLabel(scroll, text="Units", text_color="#606060", font=("Ubuntu", 12)).grid(row=20, column=0, sticky="e", padx=(0, 150))  
            units = ctk.CTkOptionMenu(scroll, values=self.sub_units, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                         button_color="#ACACAC", button_hover_color="#DADADA", width=160,
                                         dropdown_fg_color=color1, dropdown_text_color="black")
            units.grid(row=21, column=0, padx=20, pady=(0, 10), sticky="e")
            
            #Choose a color
            ctk.CTkLabel(scroll, text="Choose any color for your Schedule", text_color="#606060", font=("Ubuntu", 12), anchor="n").grid(row=22, column=0, sticky="w", padx=20, pady=(10, 0))

            self.label_color = ctk.CTkLabel(scroll, text="", fg_color=color1, width=110, height=30, corner_radius=50)
            self.label_color.grid(row=23, column=0, sticky="w", padx=30, pady=(100, 0))
            spacing_X = 30
            spacing_Y = 0

            for i in range(len(self.choose_color)):
                color = self.choose_color[i]
                if spacing_X == 150:
                    spacing_X = 30
                    spacing_Y += 50
                    

                choose_color = ctk.CTkButton(scroll, text="", height=20, width=20, cursor="hand2", fg_color=color, 
                                    hover_color=color, corner_radius=100, command=lambda c=color: self.selected_color(c))
                choose_color.grid(row=23, column=0, padx=spacing_X, pady=(10, spacing_Y), sticky="w")
                spacing_X += 30

                
            
                choose_color.bind("<Enter>", lambda e, b=choose_color: b.configure(height=25, width=25))
                choose_color.bind("<Leave>", lambda e, b=choose_color: b.configure(height=20, width=20))
            
            save_schedule = ctk.CTkButton(scroll, text="Save", text_color="#ffffff", height=40, width=20, font=("Ubuntu", 15),
                                            fg_color="#2068C6", hover_color="#4C82CA", corner_radius=100, anchor="ew",
                                            command=lambda: (
                                                        self.create_schedule(),
                                                        self.save_schedule(
                                                            [t_info.get() for t_info in tea_entries],                        
                                                            [s_info.get() for s_info in sub_entries],                   
                                                            time_start.get(),                      
                                                            time_end.get(),                     
                                                            day1.get(),                          
                                                            day2.get(),
                                                            room.get(),               
                                                            units.get(),
                                                            self.label_color.cget("fg_color")                  
                                                            )
                                                        ))  
            save_schedule.grid(row=24, column=0, padx=20, pady=(0, 15), sticky="e")
            
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  
    def show_schedule(self):
        self.clear_frame()
        color1 = "#ffffff"

        
        scrollFrame = ctk.CTkScrollableFrame(self, fg_color=color1, width=1300)
        scrollFrame.pack(fill="y", expand=True, pady=(0, 0))
    
        
        widgetFrame = ctk.CTkFrame(scrollFrame, fg_color=color1,)
        widgetFrame.pack()
        
        ctk.CTkLabel(widgetFrame, text="Time", text_color="black", font=("Calibri", 15, "bold")).grid(row=0, column=0, padx=50, pady=10)
        
        for i in range(len(self.weeks)):
            ctk.CTkLabel(widgetFrame, text=self.weeks[i], font=("Calibri", 15, "bold"), fg_color=color1, text_color="black", 
                         ).grid(row=1, column=i + 1, padx=50, pady=10)
            
        for i in range(len(self.time_sched)):
            ctk.CTkLabel(widgetFrame, text=self.time_sched[i], font=("Calibri", 15, "bold"), fg_color=color1, text_color="black"
                         ).grid(row=i + 2, column=0, pady=10)
            
        display_sched = ctk.CTkLabel(widgetFrame, text="HAHA", font=("Calibri", 15, "bold"), fg_color="black", text_color="black")
        display_sched.grid(row=1, column=1)
            
            
        
        
        
        
        
        
        self.current_frame = self