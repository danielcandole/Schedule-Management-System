# # page_content.py
# import tkinter as tk
# import customtkinter as ctk



# class PageContent(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#f5f5f5")
#         self.current_frame = None
        
#     def navigate(self, method_name):
#         getattr(self, method_name, lambda: None)()
        
#     def clear_frame(self):
#         for widget in self.winfo_children():
#             widget.destroy()
#         self.current_frame = None

#     def show_dashboard(self):
#         self.clear_frame()
#         frame = tk.Frame(self, bg="#e0e0e0")
#         frame.pack(expand=True)
#         tk.Label(frame, text="Dashboard", font=("Calibri", 20)).pack(expand=True)
#         self.current_frame = frame

#     def show_personal_info(self):
#         self.clear_frame()
#         frame = tk.Frame(self, bg="#e0e0e0")
#         frame.pack(fill="both", expand=True)
#         tk.Label(frame, text="Personal Information", font=("Calibri", 20)).pack(expand=True)
#         self.current_frame = frame

#     def show_create_sched(self):
#         self.clear_frame()
#         frame = tk.Frame(self, bg="#e0e0e0")
#         frame.pack(fill="both", expand=True)
#         tk.Label(frame, text="Create Schedule", font=("Calibri", 20)).pack(expand=True)
#         self.current_frame = frame

#     def show_schedule(self):
#         self.clear_frame()
#         frame = ctk.CTkScrollableFrame(self, fg_color="#e0e0e0")
#         frame.pack(fill="both", expand=True)
#         tk.Label(frame, text="Schedule", font=("Calibri", 20)).pack(expand=True)
        
#         color1 = "#ffffff"
#         widgetFrame = tk.Frame(frame, bg=color1)
#         widgetFrame.pack(side="top")
#         top_label = [
#             "Time", "Monday" ,"Tuesday" ,"Wednesday" ,"Thursday" ,"Friday" ,"Saturday" ,"Sunday",  
#         ]
#         time = [
#             "7:30 AM - 8:00 AM", "8:00 AM - 8:30 AM", "8:30 AM - 9:00 AM", "9:00 AM - 9:30 AM", "9:30 AM - 10:00 AM", 
#             "10:00 AM - 10:30 AM", "10:30 AM - 11:00 AM", "11:00 AM - 11:30 AM", "11:30 AM - 12:00 PM", "12:00 PM - 12:30 PM", 
#             "12:30 PM - 1:00 PM", "1:00 PM - 1:30 PM", "1:30 PM - 2:00 PM", "2:00 PM - 2:30 PM", "2:30 PM - 3:00 PM", 
#             "3:00 PM - 3:30 PM", "3:30 PM - 4:00 PM", "4:00 PM - 4:30 PM", "4:30 PM - 5:00 PM", "5:00 PM - 5:30 PM", 
#             "5:30 PM - 6:00 PM", "6:00 PM - 6:30 PM", "6:30 PM - 7:00 PM", "7:00 PM - 7:30 PM"
#         ]
        
#         for i in range(len(top_label)):
#             ctk.CTkLabel(widgetFrame, text=top_label[i], font=("Calibri", 15, "bold"), fg_color=color1, text_color="black"
#                 ).grid(row=0, column=i, padx=30, pady=10)
            
            
#         for i in range(len(time)):
#             ctk.CTkLabel(widgetFrame, text=time[i], font=("Calibri", 15, "bold"), fg_color=color1, text_color="black"
#                 ).grid(row=i + 1, column=0, padx=10, pady=10)
            

#         ctk.CTkLabel(widgetFrame, text="Wala pa nahuman", font=("Calibri", 50, "bold"), fg_color=color1, text_color="black"
#             ).grid(row=1, column=1, padx=10, pady=10)
            
#         # for i in range(len()):
#         #     tk.Label(widgetFrame, text=top_label[i], font=("Calibri", 12), bg=bg_color).grid(row=0, column=i, padx=30)
        
        
        
        
        
        
#         self.current_frame = frame

#     def show_to_do(self):
#         self.clear_frame()
#         frame = tk.Frame(self, bg="#e0e0e0")
#         frame.pack(fill="both", expand=True)
#         tk.Label(frame, text="To Do", font=("Calibri", 20)).pack(expand=True)
#         self.current_frame = frame

#     def show_calendar(self):
#         self.clear_frame()
#         frame = tk.Frame(self, bg="#e0e0e0")
#         frame.pack(fill="both", expand=True)
#         tk.Label(frame, text="Calendar", font=("Calibri", 20)).pack(expand=True)
#         self.current_frame = frame




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

            # open_img_file = Image.open(images[i])
            # img_display = ctk.CTkImage(light_image=open_img_file, dark_image=open_img_file, size=(140, 140)) 
            
            
            # btn_frame = ctk.CTkFrame(buttonsFrame, corner_radius=10, fg_color="#e7e7e7")
            # btn_frame.grid(row=1, column=i, padx=30)
            
            # img_label = ctk.CTkLabel(btn_frame, image=img_display, text="", fg_color=btn_color)
            # img_label.grid(row=0, column=0, padx=60, pady=(40, 30))
            
            # borderFrame = ctk.CTkFrame(btn_frame, fg_color=btn_color, border_color="black", border_width=1)
            # borderFrame.grid(row=1, column=0, sticky="ew")
            
            # text_label = ctk.CTkLabel(borderFrame, text=name[i], text_color="black", font=("Ubuntu", 20, "bold"), fg_color=btn_color)
            # text_label.pack(side="left", padx=10, pady=10)
            
            
            # add_icon = ctk.CTkLabel(borderFrame, image=add_img, text="", fg_color=btn_color)
            # add_icon.pack(side="right", padx=10, pady=10)