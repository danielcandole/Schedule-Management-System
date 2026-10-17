# import tkinter as tk
# from tkinter.font import Font

# class TkPersonalSchedule():
#     def __init__(self, display):
#         # Background colors
#         self.bg_clr = ["floralwhite", "snow2"]
        
#         self.display = display
#         self.display.geometry("1500x900")
#         self.display.title("Schedule Organizer")
#         self.display.configure(bg=self.bg_clr[0])
        
#         # Fonts
#         self.fname = ["Ubuntu"]
#         self.fsize = [12, 20]
#         self.font1 = Font(family=self.fname[0], size=self.fsize[0])
#         self.font1b = Font(family=self.fname[0], size=self.fsize[1], weight="bold")

#         # Frames (pages)
#         self.main_frame = tk.Frame(self.display, bg=self.bg_clr[1])
#         self.schedule_frame = tk.Frame(self.display, bg=self.bg_clr[0])

#         # Initialize main menu
#         self.main_py()
#         self.show_frame(self.main_frame)

#     #-------------------- Switch Frame --------------------
#     def show_frame(self, frame):
#         """Hide all frames and show only the given one"""
#         for f in (self.main_frame, self.schedule_frame):
#             f.pack_forget()
#         frame.pack(fill="both", expand=True)

#     #-------------------- Schedule Data --------------------
#     def sched_arr_init(self):
#         self.table_time = ["Time","7:30 AM - 8:00 AM", "8:00 AM - 8:30 AM", "8:30 AM - 9:00 AM", "9:00 AM - 9:30 AM",
#                            "9:30 AM - 10:00 AM","10:00 AM - 10:30 AM", "10:30 AM - 11:00 AM", "11:00 AM - 11:30 AM", 
#                            "11:30 AM - 12:00 PM", "12:00 PM - 12:30 PM", "12:30 PM - 1:00 PM"]
#         self.table_layout = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#     #-------------------- Schedule Page --------------------
#     def sched_create_widgets(self):
#         self.show_frame(self.schedule_frame)
#         self.sched_arr_init()

#         for widget in self.schedule_frame.winfo_children():
#             widget.destroy()

#         h = [1]
#         w = [18]

#         lab1 = tk.Label(self.schedule_frame, text="My Schedule", font=self.font1b, bg=self.bg_clr[0])
#         lab1.grid(row=0, column=0, columnspan=10, padx=5, pady=5)

#         # Days header
#         for i in range(len(self.table_layout)):
#             labi = tk.Label(self.schedule_frame, text=self.table_layout[i], font=self.font1, 
#                             bg=self.bg_clr[0], height=h[0], width=w[0], relief="groove")
#             cl = i + 1
#             labi.grid(row=1, column=cl, padx=3, pady=0)

#         # Times column
#         for i in range(len(self.table_time)):
#             labi = tk.Label(self.schedule_frame, text=self.table_time[i], font=self.font1, 
#                             bg=self.bg_clr[0], height=h[0], width=w[0], relief="groove")
#             rw = i + 1
#             labi.grid(row=rw, column=0, padx=3, pady=0)

#         # Go back button
#         button1 = tk.Button(self.schedule_frame, text="Go Back", font=self.font1, 
#                             bg=self.bg_clr[0], command=self.main_py)
#         button1.grid(row=len(self.table_time)+2, column=0, columnspan=10, pady=20)

#     #-------------------- Main Menu --------------------
#     def main_py(self):
#         self.show_frame(self.main_frame)

#         for widget in self.main_frame.winfo_children():
#             widget.destroy()

#         h = [1]
#         w = [18]

#         label1 = tk.Label(self.main_frame, text="Welcome!", font=self.font1b, 
#                           bg=self.bg_clr[1], height=h[0], width=w[0])
#         label1.pack(pady=(50, 20))

#         button1 = tk.Button(self.main_frame, text="Create a schedule", font=self.font1, 
#                             bg=self.bg_clr[0], height=h[0], width=w[0], relief="groove")
#         button1.pack(pady=5)

#         button2 = tk.Button(self.main_frame, text="See schedule", font=self.font1, 
#                             bg=self.bg_clr[0], height=h[0], width=w[0], relief="groove",
#                             command=self.sched_create_widgets)
#         button2.pack(pady=5)

# # Run app
# display = tk.Tk()
# main_dis = TkPersonalSchedule(display)
# display.mainloop()


#--------------------------------------------------------------------------------------------------------------



# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.geometry("300x200")

# options = ["Math", "English", "Science", "History", "PE", "Music", "Computer"]

# combo = ttk.Combobox(root, values=options, font=("Arial", 12))
# combo.pack(pady=20)

# # Preselect first value
# combo.current(0)

# # Function to get selected value
# def show_selected():
#     print("Selected:", combo.get())

# btn = tk.Button(root, text="Get Selected", command=show_selected)
# btn.pack()

# root.mainloop()

#-------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x200")

label = tk.Label(root, text="Choose Subject:", font=("Arial", 12))
label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

combo = ttk.Combobox(root, values=["Math", "English", "Science", "History"], font=("Arial", 12), width=20)
combo.grid(row=0, column=1, padx=10, pady=10, sticky="w")  # align beside the label

root.mainloop()


