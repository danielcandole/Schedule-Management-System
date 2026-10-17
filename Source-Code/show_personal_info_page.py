import tkinter as tk
import customtkinter as ctk


from PIL import Image
from utils.resource_path import resource_path

class ShowPersonalInfoPage(ctk.CTkFrame):
    def __init__(self, master, backend):
        super().__init__(master, fg_color="#f0f0f0")
        self.current_frame = None
        self.backend = backend
              
# initializing ↑ ↑ ↑ ↑ ↑  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            
    def show_page(self, name):
        if name in "show_personal_info":
            self.show_personal_info()
      
    def clear_frame(self):

        for widget in self.winfo_children():
            widget.destroy()
        self.current_frame = None
        
    def testing_function(self, name):
        print(name, "button is working!")
              
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  
    def show_personal_info(self):
        self.clear_frame()
        color1 = "#ffffff"

        
        
        mainFrame = ctk.CTkFrame(self, fg_color=color1)
        mainFrame.pack(fill="y", expand=True)
        ctk.CTkLabel(mainFrame, text="1", width=1300).pack()    #Setting width (DO NOT REMOVE)
        
        
        btn_frame = ctk.CTkFrame(mainFrame)
    
        
        
        self.current_frame = self
        return self