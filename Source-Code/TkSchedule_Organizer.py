import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

class TkPersonalSchedule():
    def __init__(self, display):
        #https://www.plus2net.com/python/tkinter-colors.php
        self.bg_clr = ["snow2", "white", "white"]
        
        self.display = display
        self.display.geometry("1500x900")
        self.display.title("Schedule Organizer")
        self.display.configure(bg=self.bg_clr[0])
        
        #Frame setting
        self.pages_ls = []
        
        self.main_frame = tk.Frame(self.display, bg=self.bg_clr[0])
        self.schedule_frame = tk.Frame(self.display, bg=self.bg_clr[0])
        self.create_sched_frame = tk.Frame(self.display, bg=self.bg_clr[0])
        
        self.pages_ls.extend([self.main_frame, self.schedule_frame, self.create_sched_frame])
 
        
        #Font setting
        self.fname = ["Ubuntu"]
        self.fsize = [12, 20]
        self.font1 = Font(family=self.fname[0], size=self.fsize[0])
        self.font1b = Font(family=self.fname[0], size=self.fsize[1], weight="bold")


        #Call out functions
        self.main_py()
    #-------------------------------------------






    #-------------------------------------------
    
    def sched_arr_init(self):
        # self.subject_ls = []
        # self.subject = ["Logic Design", "IT 222", "CCS030 (Net Lab)"]
        # for i in self.subject:
        #     labi = tk.Label(self.frame, text=i,font=(self.fname[0], self.fsize[0]), bg=self.bg_clr[0], height=h[0], width=w[0],
        #                     relief="groove") #wraplength=127
        #     self.subject_ls.append(labi)        
    
        self.table_time = ["7:30 AM - 8:00 AM", "8:00 AM - 8:30 AM", "8:30 AM - 9:00 AM", "9:00 AM - 9:30 AM", "9:30 AM - 10:00 AM", 
                            "10:00 AM - 10:30 AM", "10:30 AM - 11:00 AM", "11:00 AM - 11:30 AM", "11:30 AM - 12:00 PM", "12:00 PM - 12:30 PM", 
                            "12:30 PM - 1:00 PM", "1:00 PM - 1:30 PM", "1:30 PM - 2:00 PM", "2:00 PM - 2:30 PM", "2:30 PM - 3:00 PM", 
                            "3:00 PM - 3:30 PM", "3:30 PM - 4:00 PM", "4:00 PM - 4:30 PM", "4:30 PM - 5:00 PM", "5:00 PM - 5:30 PM", 
                            "5:30 PM - 6:00 PM", "6:00 PM - 6:30 PM", "6:30 PM - 7:00 PM", "7:00 PM - 7:30 PM"
                        ]

        self.table_layout = ["Time", "Monday" ,"Tuesday" ,"Wednesday" ,"Thursday" ,"Friday" ,"Saturday" ,"Sunday",  
                        ]

        self.sched_info = ["Subject: ", "Code: ", "Section: ", "Schedule: ", "Room: "]


    def show_page(self):
        for frame in self.pages_ls:
            frame.pack_forget()
            
            
    def sched_create_widgets(self):
        self.sched_arr_init()
        self.show_page()
        self.schedule_frame.pack(expand=False)
        
        for widget in self.schedule_frame.winfo_children():
            widget.destroy()
        
        h = [1]
        w = [18]
        self.lab1 = tk.Label(self.schedule_frame, text="My Schedule", font=self.font1b, bg=self.bg_clr[0])
        self.lab1.grid(row=0, column=0, columnspan=10, padx=0, pady=(30, 10))
        
        for i in range(len(self.table_layout)):
            #in
            labi = tk.Label(self.schedule_frame, text=self.table_layout[i], font=self.font1, bg=self.bg_clr[1], height=h[0], width=w[0],
                            relief="groove")
            #out
            cl = i % 8 + 0
            labi.grid(row=1, column=cl, padx=3, pady=0)
            
        for i in range(len(self.table_time)):
            #in
            labi = tk.Label(self.schedule_frame, text=self.table_time[i], font=self.font1, bg=self.bg_clr[1], height=h[0], width=w[0],
                            relief="groove")
            #out
            rw = i // 1 + 2
            cl = i % 1 + 0
            labi.grid(row=rw, column=cl, padx=3, pady=0)   
        
        button1 = tk.Button(self.schedule_frame, text="Go Back", font=self.font1, bg=self.bg_clr[1], command=self.main_py)
        button1.grid(row=26, column=0, pady=(100, 0))


    def main_py(self):
        self.show_page()
        self.main_frame.pack(expand=True, fill="both")
        
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        h = [1]
        w = [18]
        label1 = tk.Label(self.main_frame, text="Welcome!", font=self.font1b, bg=self.bg_clr[0], height=h[0], width=w[0])
        label1.pack(padx=0, pady=(30, 10)) 
        
        button1 = tk.Button(self.main_frame, text="Create a schedule", font=self.font1, bg=self.bg_clr[1], height=h[0], width=w[0],
                            relief="groove", command=self.create_sched)
        button1.pack(padx=5, pady=5)
        
        button2 = tk.Button(self.main_frame, text="See schedule", font=self.font1, bg=self.bg_clr[1], height=h[0], width=w[0],
                            relief="groove", command=self.sched_create_widgets)
        button2.pack(padx=5, pady=(0, 30))
        
       
    def create_sched(self):
        self.show_page()
        self.sched_arr_init()
        self.create_sched_frame.pack(expand=False)
        
        for widget in self.create_sched_frame.winfo_children():
            widget.destroy()
            
        h = [1]
        w = [18]
        
        label1 = tk.Label(self.create_sched_frame, text="Create a Schedule", font=self.font1b, bg=self.bg_clr[0], height=h[0], width=w[0])
        label1.grid(row=0, column=0, padx=0, pady=(30, 10), columnspan=10)
        
        
        for i in range(len(self.sched_info)):
            label2 = tk.Label(self.create_sched_frame, text=self.sched_info[i], font=self.font1, bg=self.bg_clr[0])
            rw = i // 1 + 1
            cl = i % 1 + 0           
            label2.grid(row=rw, column=cl, padx=0, pady=10, sticky="e")
    
        for i in range(len(self.sched_info)):
            rw = i // 1 + 1
            cl = i % 1 + 1   
            if i == 3:
                box = ttk.Combobox(self.create_sched_frame, values=self.table_time, font=self.font1, width=w[0])
                box.grid(row=rw, column=cl, padx=0, pady=10, sticky="w")
            else:
                entry = tk.Entry(self.create_sched_frame, font=self.font1, width=w[0], bg=self.bg_clr[2])
                entry.grid(row=rw, column=cl, padx=0, pady=10, sticky="w")
            
            
        button1 = tk.Button(self.create_sched_frame, text="Back", font=self.font1, bg=self.bg_clr[2], command=self.main_py)
        button1.grid(row=6, column=1, padx=0, pady=(30, 10), sticky="w")
        button2 = tk.Button(self.create_sched_frame, text="Save", font=self.font1, bg=self.bg_clr[2])
        button2.grid(row=6, column=1, padx=0, pady=(30, 10), sticky="e")
        
    

      
display = tk.Tk()
main_dis =  TkPersonalSchedule(display)
display.mainloop()





    # def sched_place_widgets(self):

    #     self.lab1.grid(row=0, column=0, columnspan=10, padx=5, pady=5)
        
    #     for o in range(len(self.table_layout)):
    #         cl = o % 7 + 1
    #         self.table_layout_ls[o].grid(row=1, column=cl, padx=3)
            
    #     for o in range(len(self.table_time)):
    #         rw = o // 1 + 1
    #         cl = o % 1 + 0
    #         self.table_time_ls[o].grid(row=rw, column=cl, padx=3)
            
    #     for o in range(len(self.subject)):
    #         self.subject_ls[o].grid(row=o+3, column=1, padx=3)