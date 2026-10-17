#standard library
import tkinter as tk

#third-party
import customtkinter as ctk
from PIL import ImageTk, Image

#local imports
from authActivity.backend.UserAccount import UserAccount



class ContentsFrame():
    def __init__(self, master):
        self.master = master
        self.current_frame = None
        
        
    def bar_topFrame(self):
        self.clear_frame()
        self.bar_leftFrame()

        # Topbar (spans across both columns)
        topbarFrame = tk.Frame(self.backFrame, bg="#ffffff", borderwidth=1, relief="raised", height=60)
        topbarFrame.pack(fill="x", side="top")
        topbarFrame.pack_propagate(False)
        

        self.current_frame = self.backFrame   
         
    def bar_leftFrame(self):
        self.clear_frame()
        
        self.backFrame = tk.Frame(self, bg="#F0FFF0", borderwidth=1, relief="raised")
        self.backFrame.pack(fill="both", expand=True)
        sidecolor = "#ffffff"
        
        # Sidebar (left side)
        sidebarFrame = tk.Frame(self.backFrame, bg=sidecolor, borderwidth=1, relief="raised", width=200)
        sidebarFrame.pack(fill="y", side="left")
        sidebarFrame.pack_propagate(False)
        
        design = ctk.CTkButton(sidebarFrame, text="design/logo", text_color="black", hover_color=sidecolor, width=150, height=40, 
            fg_color=sidecolor, cursor="hand2", anchor="w", font=("Ubuntu", 20))
        design.grid(row=0, column=0, padx=(0, 0), pady=(20, 5))
            
        button_names = [
            ("Dashboard", self.show_dashboard),
            ("Personal Information", self.show_personal_info),
            ("Create Schedule", self.show_create_sched),
            ("Schedule", self.show_schedule),
            ("To Do", self.show_to_do) ,
            ("Calendar", self.show_calendar),
        ]
        icons = [
            "assets/images/sidebar_icons/home1.png",
            "assets/images/sidebar_icons/personal_info2.png",
            "assets/images/sidebar_icons/create1.png",
            "assets/images/sidebar_icons/schedule2.png",
            "assets/images/sidebar_icons/to-do-list1.png",
            "assets/images/sidebar_icons/calendar1.png",
        ]
        index = 0
        for btn_name in button_names:
            name, cmd = btn_name
            icn = Image.open(icons[index]).resize((20, 20))
            picture = ImageTk.PhotoImage(icn)
            pic1 = tk.Label(sidebarFrame, image=picture, bg="#ffffff")
            pic1.image = picture  
            pic1.grid(row=index + 1, column=0, padx=(30, 0), sticky="w")
            

            btn = ctk.CTkButton(sidebarFrame, text=name, text_color="black", hover_color=sidecolor, width=155, height=40, 
                fg_color=sidecolor, cursor="hand2", anchor="w", command=cmd)
            btn.grid(row=index + 1, column=0, padx=(60, 0), pady=5)


            btn.bind("<Enter>", lambda e, b=btn: b.configure(text_color="blue"))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(text_color="black"))
        
            index += 1
        
        ctk.CTkButton(sidebarFrame, text="logout",
            fg_color="#4c40f7", hover_color="#003a92", width=100, height=30,
            command=self.show_login).pack(padx=20, pady=20, side="bottom")
        
                # Main content (right side, below topbar)

        self.current_frame = self.backFrame    
        
    def show_dashboard(self):
        self.clear_frame()
        self.bar_topFrame()
        mainFrame = tk.Frame(self.backFrame, bg="#e0e0e0", borderwidth=1, relief="raised", height=60)
        mainFrame.pack(fill="both", side="right", expand=True)
        
        widgetFrame = tk.Frame(mainFrame, bg="#ffffff")
        widgetFrame.pack(expand=True)

        
        
        tk.Label(widgetFrame, text="Dashboard", font=("Calibri", 20)).pack(fill="x", expand=True)
        
        
        
        self.current_frame = self.backFrame
        
        
    def show_personal_info(self):
        self.clear_frame()
        self.bar_topFrame()
        mainFrame = tk.Frame(self.backFrame, bg="#e0e0e0", borderwidth=1, relief="raised", height=60)
        mainFrame.pack(fill="both", side="right", expand=True)
        
        widgetFrame = tk.Frame(mainFrame, bg="#ffffff")
        widgetFrame.pack(expand=True)
        
        
        tk.Label(widgetFrame, text="Personal Information", font=("Calibri", 20)).pack(fill="x", expand=True)
        
                
        self.current_frame = self.backFrame
        
    def show_create_sched(self):
        self.clear_frame()
        self.bar_topFrame()
        mainFrame = tk.Frame(self.backFrame, bg="#e0e0e0", borderwidth=1, relief="raised", height=60)
        mainFrame.pack(fill="both", side="right", expand=True)

        widgetFrame = tk.Frame(mainFrame, bg="#ffffff")
        widgetFrame.pack(expand=True)
        
        
        tk.Label(widgetFrame, text="Create Schedule", font=("Calibri", 20)).pack(fill="x", expand=True)
             
        
        self.current_frame = self.backFrame
        
    def show_schedule(self):
        self.clear_frame()
        self.bar_topFrame()
        mainFrame = tk.Frame(self.backFrame, bg="#e0e0e0", borderwidth=1, relief="raised", height=60)
        mainFrame.pack(fill="both", side="right", expand=True)
        
        
        bg_color = "#ffffff"
        widgetFrame = tk.Frame(mainFrame, bg=bg_color)
        widgetFrame.pack(side="top")
        top_label = [
            "Time", "Monday" ,"Tuesday" ,"Wednesday" ,"Thursday" ,"Friday" ,"Saturday" ,"Sunday",  
        ]
        time = [
            "7:30 AM - 8:00 AM", "8:00 AM - 8:30 AM", "8:30 AM - 9:00 AM", "9:00 AM - 9:30 AM", "9:30 AM - 10:00 AM", 
            "10:00 AM - 10:30 AM", "10:30 AM - 11:00 AM", "11:00 AM - 11:30 AM", "11:30 AM - 12:00 PM", "12:00 PM - 12:30 PM", 
            "12:30 PM - 1:00 PM", "1:00 PM - 1:30 PM", "1:30 PM - 2:00 PM", "2:00 PM - 2:30 PM", "2:30 PM - 3:00 PM", 
            "3:00 PM - 3:30 PM", "3:30 PM - 4:00 PM", "4:00 PM - 4:30 PM", "4:30 PM - 5:00 PM", "5:00 PM - 5:30 PM", 
            "5:30 PM - 6:00 PM", "6:00 PM - 6:30 PM", "6:30 PM - 7:00 PM", "7:00 PM - 7:30 PM"
        ]
        
        for i in range(len(top_label)):
            ctk.CTkLabel(widgetFrame, text=top_label[i], font=("Calibri", 15, "bold"), fg_color=bg_color, text_color="black"
                ).grid(row=0, column=i, padx=30, pady=10)
            
            
        for i in range(len(time)):
            ctk.CTkLabel(widgetFrame, text=time[i], font=("Calibri", 15, "bold"), fg_color=bg_color, text_color="black"
                ).grid(row=i + 1, column=0, padx=10, pady=10)
            

        ctk.CTkLabel(widgetFrame, text="Wala pa nahuman", font=("Calibri", 50, "bold"), fg_color=bg_color, text_color="black"
            ).grid(row=1, column=1, padx=10, pady=10)
            
        # for i in range(len()):
        #     tk.Label(widgetFrame, text=top_label[i], font=("Calibri", 12), bg=bg_color).grid(row=0, column=i, padx=30)
            
            
            
            
        
               
        self.current_frame = self.backFrame
        
        
    def show_to_do(self):
        self.clear_frame()
        self.bar_topFrame()
        mainFrame = tk.Frame(self.backFrame, bg="#e0e0e0", borderwidth=1, relief="raised", height=60)
        mainFrame.pack(fill="both", side="right", expand=True)
        
        widgetFrame = tk.Frame(mainFrame, bg="#ffffff")
        widgetFrame.pack(expand=True)
        
        
        tk.Label(widgetFrame, text="To Do", font=("Calibri", 20)).pack(fill="x", expand=True)
        
        
        self.current_frame = self.backFrame
        
    def show_calendar(self):
        self.clear_frame()
        self.bar_topFrame()
        mainFrame = tk.Frame(self.backFrame, bg="#e0e0e0", borderwidth=1, relief="raised", height=60)
        mainFrame.pack(fill="both", side="right", expand=True)
        
        widgetFrame = tk.Frame(mainFrame, bg="#ffffff")
        widgetFrame.pack(expand=True)
        
        
        tk.Label(widgetFrame, text="Calendar", font=("Calibri", 20)).pack(fill="x", expand=True)
        
        
        self.current_frame = self.backFrame    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
