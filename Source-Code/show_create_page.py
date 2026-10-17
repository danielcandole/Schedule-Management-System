import tkinter as tk
import customtkinter as ctk

from PIL import Image

class ShowCreatePage(ctk.CTkFrame):
    def __init__(self, master, backend):
        super().__init__(master, fg_color="#f0f0f0")
        self.current_frame = None
        self.backend = backend
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      
    def show_page(self, name):
        if name in "show_create":
            self.show_create()
      
    def clear_frame(self):

        for widget in self.winfo_children():
            widget.destroy()
        self.current_frame = None
        
    def testing_function(self, name):
        print(name, "is working and is now a clickable label")
              
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  
    def show_create(self):
        self.clear_frame()
        color1 = "#ffffff"
        mainFrame = ctk.CTkFrame(self, fg_color=color1)
        mainFrame.pack(fill="y", expand=True)
        ctk.CTkLabel(mainFrame, text="", width=1320).pack()    #Setting width (DO NOT REMOVE)
        
        add_open_f = Image.open("assets/images/main_content/create_icons/add.png")
        add_img = ctk.CTkImage(light_image=add_open_f, dark_image=add_open_f, size=(40, 40)) 
        
        images = [
            "assets/images/main_content/create_icons/clock.png",
            "assets/images/main_content/create_icons/check_list.png",
            "assets/images/main_content/create_icons/planner.png"
        ]
        name = ["Schedule", "To Do", "Plan"]
        btn_color = "#e7e7e7"
        buttonsFrame = ctk.CTkFrame(mainFrame, fg_color=color1)
        buttonsFrame.pack(side="left", fill="y", padx=10)
        for i in range(len(images)):
            open_img_file = Image.open(images[i])
            img_display = ctk.CTkImage(light_image=open_img_file, dark_image=open_img_file, size=(140, 140)) 
            
            
            btn_frame = ctk.CTkFrame(buttonsFrame, corner_radius=10, fg_color="#e7e7e7", border_color="black", border_width=1, cursor="hand2")
            btn_frame.grid(row=0, column=i, padx=30)
            
            text_label = ctk.CTkLabel(btn_frame, text=name[i], text_color="black", font=("Ubuntu", 20, "bold"), fg_color=btn_color, cursor="hand2")
            text_label.grid(row=0, column=0, padx=30, pady=20)

            img_label = ctk.CTkLabel(btn_frame, image=img_display, text="", fg_color=btn_color, cursor="hand2")
            img_label.grid(row=1, column=0, padx=60, pady=5)
            
            create_icon = ctk.CTkLabel(btn_frame, image=add_img, text="", fg_color=btn_color, cursor="hand2")
            create_icon.grid(row=2, column=0, padx=30, pady=20) # sticky="e"
            
            def on_enter(event, f=btn_frame, t=text_label, i=img_label, a=create_icon):
                f.configure(fg_color="#CFCFCF")  # darker on hover
                t.configure(fg_color="#CFCFCF")
                i.configure(fg_color="#CFCFCF")
                a.configure(fg_color="#CFCFCF")
            def on_leave(event, f=btn_frame, t=text_label, i=img_label, a=create_icon):
                f.configure(fg_color="#e7e7e7")  # reset
                t.configure(fg_color="#e7e7e7")
                i.configure(fg_color="#e7e7e7")
                a.configure(fg_color="#e7e7e7")

            btn_frame.bind("<Enter>", on_enter)
            btn_frame.bind("<Leave>", on_leave)
            text_label.bind("<Enter>", on_enter)
            text_label.bind("<Leave>", on_leave)
            img_label.bind("<Enter>", on_enter)
            img_label.bind("<Leave>", on_leave)
            create_icon.bind("<Enter>", on_enter)
            create_icon.bind("<Leave>", on_leave)
            
            #Make all widgetclickable
            btn_frame.bind("<Button-1>", lambda event, text=name[i]: self.testing_function(text))
            text_label.bind("<Button-1>", lambda event, text=name[i]: self.testing_function(text))
            img_label.bind("<Button-1>", lambda event, text=name[i]: self.testing_function(text))
            create_icon.bind("<Button-1>", lambda event, text=name[i]: self.testing_function(text))

        
        
        
        self.current_frame = mainFrame
        return mainFrame