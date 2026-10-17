import tkinter as tk
import customtkinter as ctk

from PIL import Image

class PageContent(ctk.CTkFrame):
    def __init__(self, master, backend):
        super().__init__(master, fg_color="#f0f0f0")
        self.current_frame = None
        self.backend = backend
        
        self.pages = {
            # "show_dashboard": self.show_dashboard,
            # "show_personal_info": self.show_personal_info,
            # "show_to_do": self.show_to_do,
        }
              
# initializing ↑ ↑ ↑ ↑ ↑  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
               
    def show_page(self, name):
        if name in self.pages:
            self.current_frame = self.pages[name]()  
            
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.current_frame = None
        
    def testing_function(self, name):
        print(name, "button is working!")
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    def show_personal_info(self):
        self.clear_frame()
        color1 = "#ffffff"

        
        
        mainFrame = ctk.CTkFrame(self, fg_color=color1)
        mainFrame.pack(fill="y", expand=True)
        ctk.CTkLabel(mainFrame, text="4", width=1320).pack()    #Setting width (DO NOT REMOVE)
        
        
        btn_frame = ctk.CTkFrame(mainFrame)
    
        
        
        self.current_frame = self
        return self
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # def show_schedule(self): (is on a separate file)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def show_to_do(self):
        self.clear_frame()
        color1 = "#ffffff"

        
        
        mainFrame = ctk.CTkFrame(self, fg_color=color1)
        mainFrame.pack(fill="y", expand=True)
        ctk.CTkLabel(mainFrame, text="4", width=1320).pack()    #Setting width (DO NOT REMOVE)
        
        
        btn_frame = ctk.CTkFrame(mainFrame)
    
        
        
        self.current_frame = self
        return self
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # def show_schedule(self): (is on a separate file)
    
    
    
    
    
    
    
    
    
    
    
    
    
# month = [calendar.month_name[m] for m in range(1, 13)]
# month_opt = ctk.CTkOptionMenu(self.create_to_do, values=month, fg_color="#f1f1f1", text_color="black", font=("Arial", 13),
#                              button_color="#ACACAC", button_hover_color="#DADADA", 
#                              dropdown_fg_color=color1, dropdown_text_color="black")
# month_opt.set(calendar.month_name[datetime.now().month])
# month_opt.grid(row=2, column=0, padx=(20, 0), sticky="w")

# day = [str(d) for d in range(1, 32)]
# day_opt = ctk.CTkOptionMenu(self.create_to_do, values=day, fg_color="#f1f1f1", text_color="black", font=("Arial", 13),
#                              button_color="#ACACAC", button_hover_color="#DADADA", width=70,
#                              dropdown_fg_color=color1, dropdown_text_color="black")
# day_opt.set(str(datetime.now().day))
# day_opt.grid(row=2, column=0, padx=(180, 0), sticky="w")

# year = [str(y) for y in range(2010, datetime.now().year + 11)]
# year_opt = ctk.CTkOptionMenu(self.create_to_do, values=year, fg_color="#f1f1f1", text_color="black", font=("Arial", 13),
#                              button_color="#ACACAC", button_hover_color="#DADADA", 
#                              dropdown_fg_color=color1, dropdown_text_color="black")
# year_opt.set(str(datetime.now().year))
# year_opt.grid(row=2, column=0, padx=(270, 0), sticky="w")
