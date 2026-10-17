import tkinter as tk
import customtkinter as ctk


from PIL import Image
from utils.resource_path import resource_path

class ShowSchedulePage(ctk.CTkFrame):
    def __init__(self, master, backend):
        super().__init__(master, fg_color="#ecf4ff")
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
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            
    def show_page(self, name):
        if name in "show_schedule":
            self.show_schedule()
      
    def clear_frame(self):

        for widget in self.winfo_children():
            widget.destroy()
        self.current_frame = None
        
    def selected_color(self, col):
        self.label_color.configure(fg_color=col)
        
    def save_schedule(self, teacher_name, subject_info, time_start, time_end, day1, day2, units, room, color):
    
        for i in range(len(subject_info)):
            s_info = subject_info[i]
            if i == 0:
                subject_name = s_info
            elif i == 1:
                subject_code = s_info
            elif i == 2:
                subject_section = s_info

        self.backend.save_user_schedule(teacher_name, subject_name, subject_code, subject_section, time_start, time_end, day1, day2, units, room, color)
        self.show_schedule()
        
    def remove_schedule(self, rm_data):
        print(rm_data)
        if hasattr(self, "delete_subject"):
            self.delete_subject.pack_forget()
        if hasattr(self, "delete_frame"):
            self.delete_frame.place_forget()
        self.delete_popup_visible = False
        
        self.backend.delete_user_schedule(rm_data)
        
        self.clear_frame()
        self.show_schedule()

      
      
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   
    def show_schedule(self):
        self.clear_frame()
        color1 = "#ffffff"

        
        scrollFrame = ctk.CTkScrollableFrame(self, fg_color=color1, width=1300)
        scrollFrame.pack(fill="y", expand=True, pady=(0, 0))
    
        
        widgetFrame = ctk.CTkFrame(scrollFrame, fg_color=color1,)
        widgetFrame.pack()
        
        ctk.CTkLabel(widgetFrame, text="Time", text_color="black", font=("Ubuntu", 15, "bold")).grid(row=0, column=0, padx=50, pady=0)
        
        line_color = "#CFCFCF"  # light gray
        for i in range(len(self.weeks)):  
            ctk.CTkFrame(widgetFrame, width=1, height=1700, fg_color=line_color, border_width=1).grid(row=0, column=i, rowspan=len(self.time_sched) + 1, sticky="e")
            ctk.CTkLabel(widgetFrame, text=self.weeks[i], font=("Ubuntu", 15, "bold"), fg_color=color1, text_color="black", height=60, width=160,
                         ).grid(row=0, column=i + 1)
            
            
        for i in range(len(self.time_sched)):
            ctk.CTkFrame(widgetFrame, height=1, width=1300, fg_color=line_color, border_width=1).grid(row=i, column=0, columnspan=len(self.weeks) + 1, sticky="s")
            ctk.CTkLabel(widgetFrame, text=self.time_sched[i], font=("Ubuntu", 15, "bold"), fg_color=color1, text_color="black", height=60, width=160,
                         ).grid(row=i+1, column=0)
              
        subject_info = self.backend.get_db_subject_info_for_schedule()
        # print(
        #     f"user_id               {sub_data[0]}\n"
        #     f"subject_id            {sub_data[1]}\n"
        #     f"teacher_name          {sub_data[2]}\n"
        #     f"subject_name          {sub_data[3]}\n"
        #     f"subject_code          {sub_data[4]}\n"
        #     f"subject_section       {sub_data[5]}\n"
        #     f"time_start            {sub_data[6]}\n"
        #     f"time_end              {sub_data[7]}\n"
        #     f"day1                  {sub_data[8]}\n"
        #     f"day2                  {sub_data[9]}\n"
        #     f"units                 {sub_data[10]}\n"
        #     f"room                  {sub_data[11]}\n"
        #     f"color                 {sub_data[12]}\n"
        #     f"rw                    {sub_data[13]}\n"
        #     f"cl_a                  {sub_data[14]}\n"
        #     f"cl_b                  {sub_data[15]}\n"
        #     f"rspan                 {sub_data[16]}"
        # )

        for sub_data in subject_info:

            #sub = subject_info[sub_data]
             
            #setting placement
            rw = int(sub_data[13])
            cl_A = int(sub_data[14])
            cl_B = sub_data[15]
            rwspan = int(sub_data[16])

            
            subject = ctk.CTkButton(widgetFrame, text=f"{sub_data[3]}\n{sub_data[5]}\n{sub_data[11]}", font=("Ubuntu", 14, "bold"), hover_color=sub_data[12],
                                    fg_color=sub_data[12], text_color="black", corner_radius=20,
                                            border_width=1, border_color="#ffffff", command=lambda s=sub_data: self.view_subject_info(s))
            #subject.configure(command=self.view_subject_info)
            subject.grid(row=rw, column=cl_A, rowspan=rwspan, sticky="news", padx=1, pady=(0, 1))
            
            if cl_B == "None":
                pass
            else:
                cl = int(cl_B)
                subject = ctk.CTkButton(widgetFrame, text=f"{sub_data[3]}\n{sub_data[5]}\n{sub_data[11]}", font=("Ubuntu", 14, "bold"), hover_color=sub_data[12],
                                        fg_color=sub_data[12], text_color="black", corner_radius=20,
                                            border_width=1, border_color="#ffffff", command=lambda s=sub_data: self.view_subject_info(s))
                #subject.configure(command=self.view_subject_info)
                subject.grid(row=rw, column=cl, rowspan=rwspan, sticky="news", padx=1, pady=(0, 1))
                    
        # display_sched = ctk.CTkButton(widgetFrame, text="Logic Design\nCCS044\nNet Lab", font=("Ubuntu", 15, "bold"), fg_color="#E0B0FF", text_color="black",
        #                               border_width=2, border_color="#E0B0FF", height=80)
        # display_sched.grid(row=6, column=1, rowspan=2)
        
        self.current_frame = self
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                
    def view_subject_info(self, sub_data=None):
        #check
        print(sub_data)

        if sub_data is not None:
            rm_data = sub_data

        
        color1 = "#ffffff"
        color2 = "#f0f0f0"
        if not hasattr(self, "view_subject_info_visible"):
            self.view_subject_info_visible = False

        # If popup is currently visible → hide it safely
        if self.view_subject_info_visible:
            if getattr(self, "view_subject", None) and self.view_subject.winfo_exists():
                self.view_subject.pack_forget()
            if getattr(self, "bg_frame", None) and self.bg_frame.winfo_exists():
                self.bg_frame.place_forget()
            self.view_subject_info_visible = False
            return

        # Otherwise, show the popup
        self.view_subject_info_visible = True

        # Overlay background (dark transparent frame)
        self.bg_frame = ctk.CTkFrame(self, fg_color=("transparent"))
        self.bg_frame.place(relx=0.5, rely=0.5, relwidth=0.32, relheight=0.70, anchor="center")
        
        self.view_subject = ctk.CTkFrame(self.bg_frame, fg_color=color1, corner_radius=0, border_width=1, border_color="#CFCFCF")
        self.view_subject.pack(pady=1, fill="y", expand=True)
        
        # Popup frame
        self.view_subject.rowconfigure(1, weight=1)
        self.view_subject.columnconfigure(0, weight=1)
        
        close = ctk.CTkButton(self.view_subject, text="×", text_color="#8B8989", height=10, width=15, font=("Ubuntu", 20),
                                        fg_color=color1, hover_color="#DADADA", corner_radius=100, anchor="ew",
                                        command=self.view_subject_info)
        close.grid(row=0, column=0, sticky="e", padx=10, pady=(10, 0))
        
        scroll = ctk.CTkScrollableFrame(self.view_subject, fg_color=color1, width=430)
        scroll.grid(row=1, column=0, padx=(1, 10), sticky="ns")
        
        ctk.CTkFrame(self.view_subject, fg_color="#FFFFFF", height=1, border_width=1).grid(row=2, column=0, pady=10) #gap/spacing
        
        #Subject Information
        sub_label = ctk.CTkLabel(scroll, text="Subject Information", text_color="#606060", font=("Ubuntu", 20, "bold"))
        sub_label.grid(row=1, column=0, sticky="w", padx=20, pady=(0, 15))
        
        ctk.CTkLabel(scroll, text="Teacher name", text_color="#606060", font=("Ubuntu", 12)).grid(row=2, column=0, sticky="w", padx=20)

        teacher_name = ctk.CTkEntry(scroll, text_color="black", border_width=1, border_color="#e6e6e6", font=("Arial", 15), 
                                    width=400, height=45, fg_color=color1
        )
        #     user_id               sub_data[0]
        #     subject_id            sub_data[1]
        #     teacher_name          sub_data[2]
        #     subject_name          sub_data[3]
        #     subject_code          sub_data[4]
        #     subject_section       sub_data[5]
        #     time_start            sub_data[6]
        #     time_end              sub_data[7]
        #     day1                  sub_data[8]
        #     day2                  sub_data[9]
        #     units                 sub_data[10]
        #     room                  sub_data[11]
        #     sched_color           sub_data[12]
        #     rw                    sub_data[13]
        #     cl_a                  sub_data[14]
        #     cl_b                  sub_data[15]
        #     rspan                 sub_data[16]

        
        teacher_name.insert(0, sub_data[2])
        teacher_name.configure(state="readonly")
        teacher_name.grid(row=3, column=0, padx=20, pady=(0, 15), sticky="w")
        
        sub_label_names = ["Subject Name", "Subject Code", "Section"]
        sub_info_names = [f"{sub_data[3]}", f"{sub_data[4]}", f"{sub_data[5]}"]
        rw_b = 4
        for i in range(len(sub_label_names)):
            names = sub_info_names[i]
            ctk.CTkLabel(scroll, text=sub_label_names[i], text_color="#606060", font=("Ubuntu", 12)).grid(row=rw_b, column=0, sticky="w", padx=20)
            rw_b += 1
            subject_info = ctk.CTkEntry(scroll, text_color="black", fg_color=color1, border_width=1, border_color="#e6e6e6", font=("Arial", 15),
                                    width=400, height=45)
            subject_info.insert(0, names)
            subject_info.configure(state="readonly")
            subject_info.grid(row=rw_b, column=0, padx=20, pady=(0, 15), sticky="w")
            rw_b += 1
   
        #Time
        ctk.CTkLabel(scroll, text="Time", text_color="#606060", font=("Ubuntu", 12)).grid(row=10, column=0, sticky="w", padx=20)
        ctk.CTkLabel(scroll, text="to", text_color="#606060", font=("Ubuntu", 12)).grid(row=11, column=0, padx=(0, 0), sticky="n")
        time_start = ctk.CTkEntry(scroll, text_color="black", fg_color=color1, border_width=1, border_color="#e6e6e6", font=("Arial", 15),
                                    width=180, height=45)
        time_start.insert(0, sub_data[6])
        time_start.configure(state="readonly")
        time_start.grid(row=11, column=0, padx=20, pady=(0, 15), sticky="w")
                        # choose_color.bind("<Enter>", lambda e, b=choose_color: b.configure(height=25, width=25))
            # choose_color.bind("<Leave>", lambda e, b=choose_color: b.configure(height=20, width=20))
        time_end = ctk.CTkEntry(scroll, text_color="black", fg_color=color1, border_width=1, border_color="#e6e6e6", font=("Arial", 15),
                                    width=180, height=45)
        time_end.insert(0, sub_data[7])
        time_end.configure(state="readonly")
        time_end.grid(row=11, column=0, padx=20, pady=(0, 15), sticky="e")
        
        #Day
        ctk.CTkLabel(scroll, text="Day", text_color="#606060", font=("Ubuntu", 12)).grid(row=12, column=0, sticky="w", padx=20)
        ctk.CTkLabel(scroll, text="and", text_color="#606060", font=("Ubuntu", 12)).grid(row=13, column=0, padx=(0, 0), sticky="n")
        day1 = ctk.CTkEntry(scroll, text_color="black", fg_color=color1, border_width=1, border_color="#e6e6e6", font=("Arial", 15),
                                    width=180, height=45)
        day1.insert(0, sub_data[8])
        day1.configure(state="readonly")
        day1.grid(row=13, column=0, padx=20, pady=(0, 15), sticky="w")
        
        day2 = ctk.CTkEntry(scroll, text_color="black", fg_color=color1, border_width=1, border_color="#e6e6e6", font=("Arial", 15),
                                    width=180, height=45)
        day2.insert(0, sub_data[9])
        day2.configure(state="readonly")
        day2.grid(row=13, column=0, padx=20, pady=(0, 15), sticky="e")
        
        #Room
        ctk.CTkLabel(scroll, text="Room", text_color="#606060", font=("Ubuntu", 12)).grid(row=14, column=0, sticky="w", padx=20)  
        room = ctk.CTkEntry(scroll, text_color="black", fg_color=color1, border_width=1, border_color="#e6e6e6", font=("Arial", 15),
                                    width=200, height=45)
        room.insert(0, sub_data[11])
        room.configure(state="readonly")
        room.grid(row=15, column=0, padx=20, pady=(0, 15), sticky="w")

        #Units
        ctk.CTkLabel(scroll, text="Units", text_color="#606060", font=("Ubuntu", 12)).grid(row=14, column=0, sticky="e", padx=(0, 150))  
        units = ctk.CTkEntry(scroll, text_color="black", fg_color=color1, border_width=1, border_color="#e6e6e6", font=("Arial", 15),
                                    width=160, height=45)
        units.insert(0, sub_data[10])
        units.configure(state="readonly")
        units.grid(row=15, column=0, padx=20, pady=(0, 15), sticky="e")
        
        #Chosen color
        ctk.CTkLabel(scroll, text="Color", text_color="#606060", font=("Ubuntu", 12), anchor="n").grid(row=16, column=0, sticky="w", padx=20, pady=(10, 0))

        sub_color = ctk.CTkLabel(scroll, text="", fg_color=sub_data[12], width=110, height=30, corner_radius=50)
        sub_color.grid(row=17, column=0, sticky="w", padx=20, pady=(0, 15))
  
        option = ctk.CTkButton(scroll, text="Delete", text_color="#ffffff", height=40, width=20, font=("Ubuntu", 15),
                                        fg_color="#C80909", hover_color="#F63737", corner_radius=100, anchor="ew",
                                        command=lambda r=rm_data: self.delete_schedule(r))  
        option.grid(row=18, column=0, padx=20, pady=(0, 15), sticky="e")
            
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  
    def delete_schedule(self, rm_data=None):

        if rm_data is not None:
            remove_data = rm_data
        color1 = "#ffffff"
        color2 = "#f0f0f0"
        
        if not hasattr(self, "delete_popup_visible"):
            self.delete_popup_visible = False
            
            # Hide safely if frames exist
        if self.delete_popup_visible:
            if getattr(self, "delete_subject", None) and self.delete_subject.winfo_exists():
                self.delete_subject.pack_forget()
            if getattr(self, "delete_frame", None) and self.delete_frame.winfo_exists():
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
                                        command=self.delete_schedule)
        close.grid(row=0, column=0, sticky="e", padx=10, pady=(10, 0))
        
        ctk.CTkLabel(self.delete_subject, text="Are you sure?", text_color="#606060", font=("Ubuntu", 15), anchor="s", height=15).grid(row=0, column=0, padx=20, pady=(30, 0))
        
        ctk.CTkButton(self.delete_subject, text="Yes", text_color="#ffffff", height=40, width=20, font=("Ubuntu", 15),
                                        fg_color="#091CC8", hover_color="#374AF6", corner_radius=100, anchor="ew",
                                        command=lambda r=remove_data: self.remove_schedule(r)
                                        ).grid(row=1, column=0, padx=40, pady=(15, 10), sticky="e")
        ctk.CTkButton(self.delete_subject, text="No", text_color="#ffffff", height=40, width=20, font=("Ubuntu", 15),
                                        fg_color="#C80909", hover_color="#F63737", corner_radius=100, anchor="ew",
                                        command=lambda: self.delete_schedule()
                                        ).grid(row=1, column=0, padx=40, pady=(15, 10), sticky="w")         
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def show_popup_schedule(self, mode=None):
        color1 = "#ffffff"
        color2 = "#f0f0f0"
        
        if not hasattr(self, "create_schedule_visible"):
            self.create_schedule_visible = False

        # If popup is currently visible → hide it safely
        if self.create_schedule_visible:
            if getattr(self, "create_sched", None) and self.create_sched.winfo_exists():
                self.create_sched.pack_forget()
            if getattr(self, "overlay", None) and self.overlay.winfo_exists():
                self.overlay.place_forget()
            self.create_schedule_visible = False
            return

        self.create_schedule_visible = True

        # Place overlay based on mode
        self.overlay = ctk.CTkFrame(self, fg_color=("transparent"))
        self.create_sched = ctk.CTkFrame(self.overlay, fg_color=color1, corner_radius=15)
        
        if mode is None:
            self.overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.create_sched.pack(pady=20, fill="y", expand=True)
        # elif mode == "view_info":
        #     self.overlay.place(relx=0.5, rely=0.5, relwidth=0.32, relheight=0.70, anchor="center")
        #     self.create_sched.configure(corner_radius=0, border_width=1, border_color="#CFCFCF")
        #     self.create_sched.pack(pady=1, fill="y", expand=True)
        
        
        # Popup frame
        self.create_sched.rowconfigure(1, weight=1)
        self.create_sched.columnconfigure(0, weight=1)
        
        close = ctk.CTkButton(self.create_sched, text="×", text_color="#8B8989", height=10, width=15, font=("Ubuntu", 20),
                                        fg_color=color1, hover_color="#DADADA", corner_radius=100, anchor="ew",
                                        command=self.show_popup_schedule)
        close.grid(row=0, column=0, sticky="e", padx=10, pady=(10, 0))
        
        scroll = ctk.CTkScrollableFrame(self.create_sched, fg_color=color1, width=430)
        scroll.grid(row=1, column=0, padx=(1, 10), sticky="ns")
        
        ctk.CTkFrame(self.create_sched, fg_color="#FFFFFF", height=1, border_width=1).grid(row=2, column=0, pady=10) #gap/spacing
        
        #Subject Information
        sub_label = ctk.CTkLabel(scroll, text="Subject Information", text_color="#606060", font=("Ubuntu", 20, "bold"))
        sub_label.grid(row=1, column=0, sticky="w", padx=20, pady=(0, 5))
        
        ctk.CTkLabel(scroll, text="Teacher Name", text_color="#606060", font=("Ubuntu", 12)).grid(row=2, column=0, sticky="w", padx=20)

        teacher_name = ctk.CTkEntry(scroll, placeholder_text="Add name", text_color="black", fg_color=color1, border_width=1, 
                            border_color="#e6e6e6", font=("Arial", 15), width=400, height=45)
        teacher_name.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="w")
        
        sub_label_names = ["Subject Name", "Subject Code", "Section"]
        sbu_text_holder = ["Add name", "Add code", "Add section"]
        sub_entries = []
        rw_b = 4
        for i in range(len(sub_label_names)):
            ctk.CTkLabel(scroll, text=sub_label_names[i], text_color="#606060", font=("Ubuntu", 12)).grid(row=rw_b, column=0, sticky="w", padx=20)
            rw_b += 1
            subject_info = ctk.CTkEntry(scroll, placeholder_text=sbu_text_holder[i], text_color="black", fg_color=color1, border_width=1, 
                                border_color="#e6e6e6", font=("Arial", 15), width=400, height=45)
            subject_info.grid(row=rw_b, column=0, padx=20, pady=(0, 10), sticky="w")
            rw_b += 1
            sub_entries.append(subject_info)
        
        #Time
        ctk.CTkLabel(scroll, text="Time", text_color="#606060", font=("Ubuntu", 12)).grid(row=10, column=0, sticky="w", padx=20)
        ctk.CTkLabel(scroll, text="to", text_color="#606060", font=("Ubuntu", 12)).grid(row=11, column=0, padx=(0, 0), sticky="n")
        time_start = ctk.CTkOptionMenu(scroll, values=self.time_sched, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                        button_color="#ACACAC", button_hover_color="#DADADA", width=180,
                                        dropdown_fg_color=color1, dropdown_text_color="black")
        time_start.grid(row=11, column=0, padx=20, pady=(0, 10), sticky="w")
                        # choose_color.bind("<Enter>", lambda e, b=choose_color: b.configure(height=25, width=25))
            # choose_color.bind("<Leave>", lambda e, b=choose_color: b.configure(height=20, width=20))
        time_end = ctk.CTkOptionMenu(scroll, values=self.time_sched, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                        button_color="#ACACAC", button_hover_color="#DADADA", width=180,
                                        dropdown_fg_color=color1, dropdown_text_color="black")
        time_end.grid(row=11, column=0, padx=20, pady=(0, 10), sticky="e")
        
        #Day
        ctk.CTkLabel(scroll, text="Day", text_color="#606060", font=("Ubuntu", 12)).grid(row=12, column=0, sticky="w", padx=20)
        ctk.CTkLabel(scroll, text="and", text_color="#606060", font=("Ubuntu", 12)).grid(row=13, column=0, padx=(0, 0), sticky="n")
        day1 = ctk.CTkOptionMenu(scroll, values=self.weeks0, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                        button_color="#ACACAC", button_hover_color="#DADADA", width=180,
                                        dropdown_fg_color=color1, dropdown_text_color="black")
        day1.grid(row=13, column=0, padx=20, pady=(0, 10), sticky="w")
        
        day2 = ctk.CTkOptionMenu(scroll, values=self.weeks1, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                        button_color="#ACACAC", button_hover_color="#DADADA", width=180,
                                        dropdown_fg_color=color1, dropdown_text_color="black")
        day2.grid(row=13, column=0, padx=20, pady=(0, 10), sticky="e")
        
        #Room
        ctk.CTkLabel(scroll, text="Room", text_color="#606060", font=("Ubuntu", 12)).grid(row=14, column=0, sticky="w", padx=20)  
        room = ctk.CTkEntry(scroll, placeholder_text="Add room", text_color="black", fg_color=color1, border_width=1, 
                                border_color="#e6e6e6", font=("Arial", 15), width=200, height=45)
        room.grid(row=15, column=0, padx=20, pady=(0, 10), sticky="w")

        #Units
        ctk.CTkLabel(scroll, text="Units", text_color="#606060", font=("Ubuntu", 12)).grid(row=14, column=0, sticky="e", padx=(0, 150))  
        units = ctk.CTkOptionMenu(scroll, values=self.sub_units, fg_color="#f1f1f1", text_color="black", font=("Arial", 14),
                                        button_color="#ACACAC", button_hover_color="#DADADA", width=160,
                                        dropdown_fg_color=color1, dropdown_text_color="black")
        units.grid(row=15, column=0, padx=20, pady=(0, 10), sticky="e")
        
        #Choose a color
        ctk.CTkLabel(scroll, text="Choose any color for your Schedule", text_color="#606060", font=("Ubuntu", 12), anchor="n").grid(row=16, column=0, sticky="w", padx=20, pady=(10, 0))

        self.label_color = ctk.CTkLabel(scroll, text="", fg_color=color1, width=110, height=30, corner_radius=50)
        self.label_color.grid(row=17, column=0, sticky="w", padx=30, pady=(100, 0))
        spacing_X = 30
        spacing_Y = 0

        for i in range(len(self.choose_color)):
            color = self.choose_color[i]
            if spacing_X == 150:
                spacing_X = 30
                spacing_Y += 50
                
            choose_color = ctk.CTkButton(scroll, text="", height=20, width=20, cursor="hand2", fg_color=color, 
                                hover_color=color, corner_radius=100, command=lambda c=color: self.selected_color(c))
            choose_color.grid(row=17, column=0, padx=spacing_X, pady=(10, spacing_Y), sticky="w")
            spacing_X += 30      
        
            choose_color.bind("<Enter>", lambda e, b=choose_color: b.configure(height=25, width=25))
            choose_color.bind("<Leave>", lambda e, b=choose_color: b.configure(height=20, width=20))
        
        if mode is None:
            save_schedule = ctk.CTkButton(scroll, text="Save", text_color="#ffffff", height=40, width=20, font=("Ubuntu", 15),
                                            fg_color="#2068C6", hover_color="#4C82CA", corner_radius=100, anchor="ew",
                                            command=lambda: (
                                                        self.show_popup_schedule(),
                                                        self.save_schedule(
                                                            teacher_name.get(),                        
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
            save_schedule.grid(row=18, column=0, padx=20, pady=(0, 15), sticky="e")
        elif mode == "view_info":
            sub_label.configure(text="View Subject Information", height=None, width=None)
                    