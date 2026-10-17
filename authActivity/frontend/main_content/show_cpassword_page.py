import tkinter as tk
import customtkinter as ctk
from PIL import Image
from utils.resource_path import resource_path # Make sure this exists in your project


from authActivity.backend.UserAccount import UserAccount
from authActivity.frontend.auth  import Auth


class ShowChangePasswordPage(ctk.CTkFrame):
    def __init__(self, master, backend=None):
        super().__init__(master, fg_color="#ecf4ff")
        self.current_frame = None
        self.backend = backend


        self.clear_frame()
        self.change_password()  
   
    def change_password(self, username, new_password, confirm_password):
            if username not in self.accounts:
                return "Username not found."
            if not new_password or not confirm_password:
                return "Please fill in all fields."
            if new_password != confirm_password:
                return "Passwords do not match."
            if len(new_password) < 6:
                return "Password must be at least 6 characters."
            self.accounts[username]["password"] = new_password
            self.save_accounts()
            return "Password successfully updated!"    
   
    def show_page(self, name):
        if name == "change_password":
            self.handle_change_password()  


    def clear_frame(self):
        for widget in self.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
        self.current_frame = None


    def testing_function(self, name):
        print(name, "button is working!")

    def toggle_password_visibility(self, entry, btn):
        if entry.cget("show") == "":
            entry.configure(show="●")
            btn.configure(image=self.close)
        else:
            entry.configure(show="")
            btn.configure(image=self.show)
    def change_password(self):
        self.clear_frame()


        # === MAIN CONTAINER ===
        backFrame = ctk.CTkFrame(
            self,
            fg_color="#ECF4FF",
            width=10,
            height=520,
            corner_radius=20,
        )
        backFrame.pack(expand=True, fill="both")
        backFrame.pack_propagate(False)


        # === LEFT PANEL ===
        leftFrame = ctk.CTkFrame(backFrame, fg_color="#ECF4FF", corner_radius=0)
        leftFrame.place(relx=0.0, rely=0.5, relheight=1.0, relwidth=0.999, anchor="w")


        original_img = Image.open(resource_path("assets/images/bg1.png"))
        bg_image = ctk.CTkImage(light_image=original_img, size=(1500, 900))
        bg_label = ctk.CTkLabel(leftFrame, text="", image=bg_image)
        bg_label.place(relx=0.5, rely=0.5, anchor="center")


        def resize_bg(event):
            new_w, new_h = event.width, event.height
            resized = original_img.resize((new_w, new_h))
            new_ctk_img = ctk.CTkImage(light_image=resized, size=(new_w, new_h))
            bg_label.configure(image=new_ctk_img)
            bg_label.image = new_ctk_img


        leftFrame.bind("<Configure>", resize_bg)


        # === RIGHT PANEL ===
        rightFrame = ctk.CTkFrame(
            backFrame,
            fg_color="#ffffff",
            border_width=2,
            border_color="#9D9D9D",
            corner_radius=45,
        )
        rightFrame.place(relx=0.71, rely=0.60, relheight=1.0, relwidth=0.40, anchor="e")


        # === LOGO ===
        logo = ctk.CTkImage(
            light_image=Image.open(resource_path("assets/images/smslogo1.png")),
            size=(280, 100),
        )
        img_label = ctk.CTkLabel(rightFrame, text="", image=logo, fg_color="transparent")
        img_label.place(relx=0.5, rely=0.11, anchor="center")


        # === TITLE ===
        tk.Label(
            rightFrame,
            text="Change Password",
            bg="#ffffff",
            font=("Ubuntu", 24, "bold"),
            fg="#2d3748",
        ).place(relx=0.23, rely=0.17)


        tk.Label(
            rightFrame,
            text="Update your account password",    
            bg="#ffffff",
            font=("Arial", 12),
            fg="#718096",
        ).place(relx=0.29, rely=0.22)


        self.notif_label = ctk.CTkLabel(
            self,
            text="",
            fg_color="#ffffff",
            text_color="red",
            font=("Arial", 15, "bold"),
        )
        self.notif_label.place(relx=0.515, rely=0.39, anchor="center")




        # === EMAIL ENTRY ===
        tk.Label(
            rightFrame,
            text="Enter your username",
            bg="#ffffff",
            font=("Ubuntu", 12, "bold"),
            fg="#4a5568",
        ).place(relx=0.26, rely=0.33)


        self.email_entry = ctk.CTkEntry(
            rightFrame,
            border_width=2,
            border_color="#d1d1d1",
            font=("Arial", 14, "italic"),
            placeholder_text="Enter username",
            placeholder_text_color="#a8a8a8",
            text_color="black",
            fg_color="#ffffff",
            width=280,
            height=45,
            corner_radius=30,
        )
        self.email_entry.place(relx=0.24, rely=0.36)


        # === NEW PASSWORD ENTRY ===
        tk.Label(
            rightFrame,
            text="New Password",
            bg="#ffffff",
            font=("Ubuntu", 12, "bold"),
            fg="#4a5568",
        ).place(relx=0.26, rely=0.44)


        self.new_password_entry = ctk.CTkEntry(
            rightFrame,
            border_width=2,
            border_color="#d1d1d1",
            font=("Arial", 14, "italic"),
            placeholder_text="Enter New Password",
            placeholder_text_color="#a8a8a8",
            text_color="black",
            fg_color="#ffffff",
            show="●",
            width=280,
            height=46,
            corner_radius=30,
        )
        self.new_password_entry.place(relx=0.24, rely=0.47)


        # === CONFIRM PASSWORD ENTRY ===
        tk.Label(
            rightFrame,
            text="Confirm Password",
            bg="#ffffff",
            font=("Ubuntu", 12, "bold"),
            fg="#4a5568",
        ).place(relx=0.26, rely=0.55)


        self.confirm_password_entry = ctk.CTkEntry(
            rightFrame,
            border_width=2,
            border_color="#d1d1d1",
            font=("Arial", 14, "italic"),
            placeholder_text="Confirm New Password",
            placeholder_text_color="#a8a8a8",
            text_color="black",
            fg_color="#ffffff",
            show="●",
            width=280,
            height=46,
            corner_radius=30,
        )
        self.confirm_password_entry.place(relx=0.24, rely=0.58)


        # === EYE ICONS ===
        self.show = ctk.CTkImage(Image.open(resource_path("assets/images/frontpage_icons/eye.png")), size=(18, 18))
        self.close = ctk.CTkImage(Image.open(resource_path("assets/images/frontpage_icons/hidden.png")), size=(18, 18))


        self.toggle_btn_new = ctk.CTkButton(
            rightFrame,
            image=self.close,
            text="",
            width=35,
            height=35,
            fg_color="#ffffff",
            hover_color="#f0f0f0",
            corner_radius=30,
            command=lambda: self.toggle_password_visibility(self.new_password_entry, self.toggle_btn_new),
        )
        self.toggle_btn_new.place(relx=0.647, rely=0.477)


        self.toggle_btn_confirm = ctk.CTkButton(
            rightFrame,
            image=self.close,
            text="",
            width=35,
            height=35,
            fg_color="#ffffff",
            hover_color="#f0f0f0",
            corner_radius=30,
            command=lambda: self.toggle_password_visibility(self.confirm_password_entry, self.toggle_btn_confirm),
        )
        self.toggle_btn_confirm.place(relx=0.647, rely=0.587)


        # === RESET BUTTON ===
        ctk.CTkButton(
            rightFrame,
            command=self.change_password,
            text="Reset Password",
            text_color="white",
            font=("Arial", 15),
            hover_color="#00145d",
            width=170,
            height=45,
            fg_color="#354eab",
            cursor="hand2",
            corner_radius=35,
        ).place(relx=0.36, rely=0.70)


        # === BACK TO LOGIN ===
        tk.Label(
            rightFrame,
            text="Remembered your password?",
            bg="#ffffff",
            fg="#718096",
            font=("Arial", 10),
        ).place(relx=0.30, rely=0.78)


        back_to_login = tk.Label(
            rightFrame,
            text="Login",
            bg="#ffffff",
            fg="#354eab",
            font=("Arial", 10, "bold"),
            cursor="hand2",
        )


        # self.username_entry.bind("<Return>", self.handle_change_password)
        # self.password_entry.bind("<Return>", self.handle_change_password)




        # self.master.bind("<Escape>", lambda e: self.handle_change_password())




        # self.current_frame = backFrame




    # === Placeholders to prevent crashes ===
    def update_password_action(self):
        print("Update Password button clicked!")


    def switch_to_dashboard(self):
        print("Switching back to Dashboard!")


   


    # def update_password_action(self):
    #     """Validates fields and updates the password via backend."""
    #     username = self.username_entry.get()
    #     current_pass = self.current_password_entry.get()
    #     new_pass = self.new_password_entry.get()
    #     confirm_pass = self.confirm_password_entry.get()


    #     # Call backend
    #     result_message = self.backend.handle_change_password(username, current_pass, new_pass, confirm_pass)


    #     # === SHOW RESULT ===
    #     result_label = ctk.CTkLabel(self.current_frame, text=result_message)
    #     if "successfully" in result_message.lower():
    #         result_label.configure(text_color="green")
    #     else:
    #         result_label.configure(text_color="red")
    #     result_label.pack(pady=(10, 5))


    #     if "successfully" in result_message.lower():
    #         # Optional: return to dashboard after short delay
    #         self.after(1500, self.switch_to_dashboard)





