class UserAccount:
    def __init__(self):
        # self.accounts = {'asd': 
        #                     {
        #                     'u_account': {
        #                         'user_id': 1, 
        #                         'username': 'asd', 
        #                         'password': 'asdasd'
        #                     }, 
        #                     'personal_info': {
        #                         'status': None, 
        #                         'full_name': None, 
        #                         'personal_gmail': None
        #                     }, 
        #                     'student_info': {
        #                         'smc_gmail': None, 
        #                         'student_id': None, 
        #                         'course': None, 
        #                         'year_level': None, 
        #                         'days_present': None, 
        #                         'days_absent': None
        #                     }, 
        #                     'subject_info': [{
        #                         'teacher_info': {
        #                             'teacher_name': None, 
        #                             'teacher_smc_gmail': None, 
        #                             'teacher_id': None
        #                         }, 
        #                         'subject_name': None, 
        #                         'subject_code': None, 
        #                         'section': None, 
        #                         'time': None, 
        #                         'day': None, 
        #                         'room': None, 
        #                         'units': None
        #                         }], 
        #                     'schedule': [], 
        #                     'to_do_list': [], 
        #                     'task': [{
        #                         'title': "Today's deadline",
        #                         'month': 'October', 
        #                         'day': '6', 
        #                         'year': '2025', 
        #                         'hour': '12', 
        #                         'minutes': '23', 
        #                         'period': 'AM', 
        #                         'description': 'OH NOOO!!'
        #                         }]
        #                     }
        #                 }
        # self.current_user = None



            # 'asd': {
            #     'u_account': {
            #         'user_id': 1,
            #         'username': 'asd',
            #         'password': 'asdasd'
            #     },
            #     'personal_info': {
            #         'status': None,
            #         'full_name': None,
            #         'personal_gmail': None
            #     },
            #     'student_info': {
            #         'smc_gmail': None,
            #         'student_id': None,
            #         'course': None,
            #         'year_level': None,
            #         'days_present': None,
            #         'days_absent': None
            #     },
            #     'subject_info': {
            #         'subject_0': {
            #             'teacher_name': 'Justine Cua',
            #             'subject_name': 'OOP',
            #             'subject_code': '123',
            #             'section': '321',
            #             'time_start': '07:30 AM',
            #             'time_end': '09:00 AM',
            #             'day1': 'Tuesday',
            #             'day2': 'Wednesday',
            #             'room': 'CC3',
            #             'units': '3',
            #             'sched_color': '#E0B0FF',
            #             "row": '6',
            #             "columnA": '1',
            #             "columnB": '2',
            #             "rowspan": '2',
            #             "height": '130'
            #         }
            #     },
            #     'schedule': [],
            #     'to_do_list': [],
            #     'task': {
            #         'task_1': {
            #             'title': 'adsd', 
            #              'month': 'October', 
            #              'day': '10', 
            #              'year': '2025', 
            #              'hour': 'asd', 
            #              'minutes': 'as', 
            #              'period': 'AM', 
            #              'description': 'dasdas'
            #              }, 
            #         'task_2': {
            #             'title': 'asd', 
            #              'month': 'October', 
            #              'day': '10', 
            #              'year': '2025', 
            #              'hour': 'asd', 
            #              'minutes': 'asd', 
            #              'period': 'AM', 
            #              'description': 'adsasd'
            #              }, 
            #         'task_3': {
            #             'title': 'NONO', 
            #             'month': 'October', 
            #             'day': '10', 
            #             'year': '2025', 
            #             'hour': 'asd', 
            #             'minutes': 'asd', 
            #             'period': 'AM', 
            #             'description': 'daadad'
            #         }
                    
            #     }
            # }






# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


            # ctk.CTkLabel(scroll, text="Subject Code", text_color="#606060", font=("Ubuntu", 12)).grid(row=12, column=0, sticky="w", padx=20)
            
            # subject_code = ctk.CTkEntry(scroll, placeholder_text="Add code", text_color="black", fg_color=color1, border_width=1, 
            #                      border_color="#e6e6e6", font=("Arial", 15), width=400, height=45)
            # subject_code.grid(row=13, column=0, padx=20, pady=(0, 10), sticky="w")
            
            # ctk.CTkLabel(scroll, text="Section", text_color="#606060", font=("Ubuntu", 12)).grid(row=14, column=0, sticky="w", padx=20)
            
            # subject_section = ctk.CTkEntry(scroll, placeholder_text="Add section", text_color="black", fg_color=color1, border_width=1, 
            #                      border_color="#e6e6e6", font=("Arial", 15), width=400, height=45)
            # subject_section.grid(row=15, column=0, padx=20, pady=(0, 10), sticky="w")
            
            
            
            
            
            
            
            
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

           
            
    # def button_popup_option(self, button, color):
    #     pass
    #     color1 = "#ffffff"
    #     color2= "#ECF4FF"
    #     # Check if popup already exists
    #     if hasattr(self, "option_frame"):
    #         # If popup is visible and same button clicked → hide it
    #         if getattr(self, "option_popup_visible", False) and getattr(self, "last_button_clicked", None) == button:
    #             self.option_frame.place_forget()
    #             self.option_popup_visible = False
    #             return
    #         else:
    #             # Hide popup before moving it
    #             self.option_frame.place_forget()

    #     # Mark this button as last clicked
    #     self.last_button_clicked = button
    #     self.option_popup_visible = True

    #     # Get button position
    #     bx = button.winfo_rootx() - self.winfo_rootx()  # X relative to parent
    #     by = button.winfo_rooty() - self.winfo_rooty()
    #     bw = button.winfo_width()
    #     bh = button.winfo_height()

    #     # Create popup frame (if not exists yet)
    #     if not hasattr(self, "option_frame"):
    #         self.option_frame = ctk.CTkFrame(self, fg_color=color1, corner_radius=12)

    #     # Place it below the button
    #     self.option_frame.place(x=bx+5, y=by+7)

    #     # Clear old widgets before adding new (optional)
    #     for widget in self.option_frame.winfo_children():
    #         widget.destroy()

    #     # Example popup content
    #     ctk.CTkButton(self.option_frame, text="View Info", text_color="black", fg_color=color2, height=20, width=100, 
    #                   font=("Ubuntu", 12, "bold"), anchor="w", bg_color=color, hover_color=color2
    #                   ).grid(row=0, column=0)

    #     ctk.CTkButton(self.option_frame, text="Edit", text_color="black", fg_color=color2, height=20, width=100, 
    #                   font=("Ubuntu", 12, "bold"), anchor="w", bg_color=color, hover_color=color2
    #                   ).grid(row=1, column=0)
    
    #     ctk.CTkButton(self.option_frame, text="Delete", text_color="black", fg_color=color2, height=20, width=100, 
    #                   font=("Ubuntu", 12, "bold"), anchor="w", bg_color=color, hover_color=color2
    #                   ).grid(row=1, column=0)
    
    
    
    
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    
    
        # def view_subject_info(self, sub_info=None, subject_data=None):
        # #check
            # print(sub_info)
            # print(subject_data)
            # if sub_info is not None and subject_data is not None:
            #     sub = subject_data[sub_info]
            #     rm_data = sub_info
            #     print(sub)
            
            # color1 = "#ffffff"
            # color2 = "#f0f0f0"
            # if not hasattr(self, "view_subject_info_visible"):
            #     self.view_subject_info_visible = False

            # # If popup is currently visible → hide it safely
            # if self.view_subject_info_visible:
            #     if getattr(self, "view_subject", None) and self.view_subject.winfo_exists():
            #         self.view_subject.pack_forget()
            #     if getattr(self, "bg_frame", None) and self.bg_frame.winfo_exists():
            #         self.bg_frame.place_forget()
            #     self.view_subject_info_visible = False
            #     return

            # # Otherwise, show the popup
            # self.view_subject_info_visible = True

            # # Overlay background (dark transparent frame)
            # self.bg_frame = ctk.CTkFrame(self, fg_color=("transparent"))
            # self.bg_frame.place(relx=0.5, rely=0.5, relwidth=0.32, relheight=0.70, anchor="center")
            
            # self.view_subject = ctk.CTkFrame(self.bg_frame, fg_color=color1, corner_radius=0, border_width=1, border_color="#CFCFCF")
            # self.view_subject.pack(pady=1, fill="y", expand=True)
            
            # # Popup frame
            # self.view_subject.rowconfigure(1, weight=1)
            # self.view_subject.columnconfigure(0, weight=1)
            
            # close = ctk.CTkButton(self.view_subject, text="×", text_color="#8B8989", height=10, width=15, font=("Ubuntu", 20),
            #                                 fg_color=color1, hover_color="#DADADA", corner_radius=100, anchor="ew",
            #                                 command=self.view_subject_info)
            # close.grid(row=0, column=0, sticky="e", padx=10, pady=(10, 0))
            


            # scroll = ctk.CTkScrollableFrame(self.view_subject, fg_color=color1, width=430)
            # scroll.grid(row=1, column=0, padx=(1, 10), sticky="ns")
            
            # ctk.CTkFrame(self.view_subject, fg_color="#FFFFFF", height=1, border_width=1).grid(row=2, column=0, pady=10) #gap/spacing
            
            # #Subject Information
            # sub_label = ctk.CTkLabel(scroll, text="Subject Information", text_color="#606060", font=("Ubuntu", 20, "bold"))
            # sub_label.grid(row=1, column=0, sticky="w", padx=20, pady=(0, 15))
            
            # ctk.CTkLabel(scroll, text="Teacher name", text_color="#606060", font=("Ubuntu", 12)).grid(row=2, column=0, sticky="w", padx=20)

            # teacher_name = ctk.CTkLabel(scroll, text=f"{sub['teacher_name']}", text_color="black", fg_color=color1, font=("Ubuntu", 20, "bold"), 
            #                             width=400, height=20, anchor="w")
            # teacher_name.grid(row=3, column=0, padx=20, pady=(0, 15), sticky="w")
            
            # sub_label_names = ["Subject Name", "Subject Code", "Section"]
            # sub_info_names = [f"{sub['subject_name']}", f"{sub['subject_code']}", f"{sub['section']}"]
            # rw_b = 4
            # for i in range(len(sub_label_names)):
            #     names = sub_info_names[i]
            #     ctk.CTkLabel(scroll, text=sub_label_names[i], text_color="#606060", font=("Ubuntu", 12)).grid(row=rw_b, column=0, sticky="w", padx=20)
            #     rw_b += 1
            #     subject_info = ctk.CTkLabel(scroll, text=names, text_color="black", fg_color=color1, font=("Ubuntu", 20, "bold"), 
            #                             width=400, height=20, anchor="w")
            #     subject_info.grid(row=rw_b, column=0, padx=20, pady=(0, 15), sticky="w")
            #     rw_b += 1

            
            # #Time
            # ctk.CTkLabel(scroll, text="Time", text_color="#606060", font=("Ubuntu", 12)).grid(row=10, column=0, sticky="w", padx=20)
            # ctk.CTkLabel(scroll, text="to", text_color="#606060", font=("Ubuntu", 12)).grid(row=11, column=0, padx=(0, 0), sticky="n")
            # time_start = ctk.CTkLabel(scroll, text=f"{sub['time_start']}", text_color="black", fg_color=color1, font=("Ubuntu", 20, "bold"), 
            #                             width=180, height=20, anchor="w")
            # time_start.grid(row=11, column=0, padx=20, pady=(0, 15), sticky="w")
            #                 # choose_color.bind("<Enter>", lambda e, b=choose_color: b.configure(height=25, width=25))
            #     # choose_color.bind("<Leave>", lambda e, b=choose_color: b.configure(height=20, width=20))
            # time_end = ctk.CTkLabel(scroll, text=f"{sub['time_end']}", text_color="black", fg_color=color1, font=("Ubuntu", 20, "bold"), 
            #                             width=180, height=20, anchor="e")
            # time_end.grid(row=11, column=0, padx=20, pady=(0, 15), sticky="e")
            
            # #Day
            # ctk.CTkLabel(scroll, text="Day", text_color="#606060", font=("Ubuntu", 12)).grid(row=12, column=0, sticky="w", padx=20)
            # ctk.CTkLabel(scroll, text="and", text_color="#606060", font=("Ubuntu", 12)).grid(row=13, column=0, padx=(0, 0), sticky="n")
            # day1 = ctk.CTkLabel(scroll, text=f"{sub['day1']}", text_color="black", fg_color=color1, font=("Ubuntu", 20, "bold"), 
            #                             width=180, height=20, anchor="w")
            # day1.grid(row=13, column=0, padx=20, pady=(0, 15), sticky="w")
            
            # day2 = ctk.CTkLabel(scroll, text=f"{sub['day2']}", text_color="black", fg_color=color1, font=("Ubuntu", 20, "bold"), 
            #                             width=180, height=20, anchor="e")
            # day2.grid(row=13, column=0, padx=20, pady=(0, 15), sticky="e")
            
            # #Room
            # ctk.CTkLabel(scroll, text="Room", text_color="#606060", font=("Ubuntu", 12)).grid(row=14, column=0, sticky="w", padx=20)  
            # room = ctk.CTkLabel(scroll, text=f"{sub['room']}", text_color="black", fg_color=color1, font=("Ubuntu", 20, "bold"), 
            #                             width=200, height=20, anchor="w")
            # room.grid(row=15, column=0, padx=20, pady=(0, 15), sticky="w")

            # #Units
            # ctk.CTkLabel(scroll, text="Units", text_color="#606060", font=("Ubuntu", 12)).grid(row=14, column=0, sticky="e", padx=(0, 150))  
            # units = ctk.CTkLabel(scroll, text=f"{sub['units']}", text_color="black", fg_color=color1, font=("Ubuntu", 20, "bold"), 
            #                             width=160, height=20, anchor="e")
            # units.grid(row=15, column=0, padx=20, pady=(0, 15), sticky="e")
            
            # #Chosen color
            # ctk.CTkLabel(scroll, text="Color", text_color="#606060", font=("Ubuntu", 12), anchor="n").grid(row=16, column=0, sticky="w", padx=20, pady=(10, 0))

            # sub_color = ctk.CTkLabel(scroll, text="", fg_color=sub['sched_color'], width=110, height=30, corner_radius=50)
            # sub_color.grid(row=17, column=0, sticky="w", padx=20, pady=(0, 15))

            

            # option = ctk.CTkButton(scroll, text="Delete", text_color="#ffffff", height=40, width=20, font=("Ubuntu", 15),
            #                                 fg_color="#C80909", hover_color="#F63737", corner_radius=100, anchor="ew",
            #                                 command=lambda r=rm_data: self.delete_schedule(r))  
            # option.grid(row=18, column=0, padx=20, pady=(0, 15), sticky="e")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#             # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#     # - - - - - - - - - - - - - 
#         #Pending   | ROW 1
#     # - - - - - - - - - - - - -
   
#         display4 = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=bg, height=400, border_color=box_border_color, border_width=1, corner_radius=15)
#         display4.grid(row=1, column=0, sticky="w", padx=(70, 0), pady=(0, 30))
        
#         ctk.CTkFrame(display4, fg_color=box_border_color, border_width=1, height=1, width=550).grid(row=0, column=0, sticky="n", padx=10) #width setting (DO NOT REMOVE)
        
#         ctk.CTkLabel(display4, text=f"Pending", text_color="black", font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 70), padx=10)
        
        
        
        
        
        
        
        

# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#     # - - - - - - - - - - - - - - - - 
#         #Tomorrow's Due   | ROW 1
#     # - - - - - - - - - - - - - - - - 
   
#         display5 = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=bg, height=400, border_color=box_border_color, border_width=1, corner_radius=15)
#         display5.grid(row=1, column=0, sticky="e", padx=(0, 70), pady=(0, 30))
        
#         ctk.CTkFrame(display5, fg_color=box_border_color, border_width=1, height=1, width=550).grid(row=0, column=0, sticky="n", padx=10) #width setting (DO NOT REMOVE)
        
#         ctk.CTkLabel(display5, text=f"Tomorrow's Due", text_color="black", font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 70), padx=10)
        







# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#     # - - - - - - - - - - - - - - - 
#         #Missing Tasks   | ROW 2
#     # - - - - - - - - - - - - - - - 
        
#         display1 = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=bg, height=200, border_color=box_border_color, border_width=1, corner_radius=15)
#         display1.grid(row=2, column=0, sticky="w", padx=(70, 0), pady=(0, 30))

#         ctk.CTkFrame(display1, fg_color=box_border_color, border_width=1, height=1, width=250).grid(row=0, column=0, sticky="n", padx=10) #width setting (DO NOT REMOVE)
        
#         ctk.CTkLabel(display1, text=f"Missing Tasks", text_color="black", font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 70), padx=10)









# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#     # - - - - - - - - - - - - - - - - 
#         #Completed Tasks   | ROW 2
#     # - - - - - - - - - - - - - - - - 
   
#         display2 = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=bg, height=200, border_color=box_border_color, border_width=1, corner_radius=15)
#         display2.grid(row=2, column=0, sticky="w", padx=(370, 0), pady=(0, 30))
        
#         ctk.CTkFrame(display2, fg_color=box_border_color, border_width=1, height=1, width=250).grid(row=0, column=0, sticky="n", padx=10) #width setting (DO NOT REMOVE)
        
#         ctk.CTkLabel(display2, text=f"Completed Tasks", text_color="black", font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 70), padx=10)
        
        
        
        
        
        
        
        
        

# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#     # - - - - - - - - - - - - - - - - 
#         #Number of Books   | ROW 2
#     # - - - - - - - - - - - - - - - - 
   
#         display3 = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=bg, height=200, border_color=box_border_color, border_width=1, corner_radius=15)
#         display3.grid(row=2, column=0, sticky="e", padx=(0, 370), pady=(0, 30))
        
#         ctk.CTkFrame(display3, fg_color=box_border_color, border_width=1, height=1, width=250).grid(row=0, column=0, sticky="n", padx=10) #width setting (DO NOT REMOVE)
        
#         ctk.CTkLabel(display3, text=f"Number of Books", text_color="black", font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 70), padx=10)
        

    
    
    
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#     # - - - - - - - - - - - - - - - - 
#         #Number of Subjects   | ROW 2
#     # - - - - - - - - - - - - - - - - 
   
#         display3 = ctk.CTkFrame(mainFrame, fg_color="#ffffff", bg_color=bg, height=200, border_color=box_border_color, border_width=1, corner_radius=15)
#         display3.grid(row=2, column=0, sticky="e", padx=(0, 70), pady=(0, 30))
        
#         ctk.CTkFrame(display3, fg_color=box_border_color, border_width=1, height=1, width=250).grid(row=0, column=0, sticky="n", padx=10) #width setting (DO NOT REMOVE)
        
#         ctk.CTkLabel(display3, text=f"Number of Subjects", text_color="black", font=("Ubuntu", 15, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 70), padx=10)