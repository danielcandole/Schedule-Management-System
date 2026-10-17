#standard library
import tkinter as tk


#third-party
import customtkinter as ctk
from PIL import Image
from utils.resource_path import resource_path


#local imports
from authActivity.backend.UserAccount import UserAccount


class Auth(tk.Frame):
    def __init__(self, master, user_account, on_login_success):
        super().__init__(master, bg="#f5f5f5")
        self.user = user_account
        self.on_login_success = on_login_success
       
        self.pack(fill="both", expand=True)

        self._left_bg_original = None

        self.current_frame = None
   
        # if self.on_login_success:
        #     self.after(100, self.on_login_success)  # schedule callback after Tk loop starts
        #     self.pack_forget()
        #     return
        self.show_login()
             
# initializing ↑ ↑ ↑ ↑ ↑  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
       
    def show_notif(self, message):
        if message:
            self.notif_label.configure(text=message, fg_color="#ffffff")  
            self.notif_label.lift()
            self.after(5000, self.clear_notif)
        else:
            self.clear_notif()

    def clear_notif(self):
        self.notif_label.configure(text="", fg_color='transparent')

    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.current_frame = None

    def switch_to_login(self, event=None):
        self.show_login()

    def switch_to_register(self, event=None):
        self.show_register()

    def handle_login(self, event=None):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()


        message = self.user.login(username, password)
        self.show_notif(message)


        if message == "Login successful":
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            self.pack_forget()
            if self.on_login_success:
                self.on_login_success()

    def forgot_password(self, username, new_password, confirm_password):
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

    def handle_register(self, event=None):
        pname = self.pname_entry.get().strip()
        email = self.email_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()


        result = self.user.register(pname, email, username, password)


        if result == "Registration successful":
            self.notif_label.configure(text="Account created successfully!", text_color="green")
            self.switch_to_login()
        else:
            self.notif_label.configure(text=result, text_color="red")

    def handle_forgot_password(self, event=None):
        username = self.email_entry.get().strip()
        new_pass = self.new_password_entry.get().strip()
        confirm_pass = self.confirm_password_entry.get().strip()

        message = self.user.forgot_password(username, new_pass, confirm_pass)
        self.show_notif(message)

        if "successfully" in message.lower():
            self.notif_label.configure(text=message, text_color="green")
        else:
            self.notif_label.configure(text=message, text_color="red")

    def toggle_password_visibility(self, entry, btn):
        if entry.cget("show") == "":
            entry.configure(show="●")
            btn.configure(image=self.close)
        else:
            entry.configure(show="")
            btn.configure(image=self.show)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   
    def show_register(self):
        self.clear_frame()


        # MAIN CONTAINER 
        backFrame = ctk.CTkFrame(
            self,
            fg_color="#ECF4FF",
            width=10,
            height=520,
            corner_radius=20,
        )
        backFrame.place(relx=0.97, rely=0.60)
        backFrame.pack(expand=True, fill="both")
        backFrame.pack_propagate(False)


        # LEFT PANEL 
        leftFrame = ctk.CTkFrame(
            backFrame,
            fg_color="#ECF4FF",
            corner_radius=0,
        )
        leftFrame.place(relx=0.0, rely=0.5, relheight=1.0, relwidth=0.999, anchor="w")


        # Load and show background image
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


        # RIGHT PANEL 
        rightFrame = ctk.CTkFrame(
            backFrame,
            fg_color="#ffffff",
            border_width=2,
            border_color="#9D9D9D",
            corner_radius=45,
        )
        rightFrame.place(relx=0.71, rely=0.60, relheight=1.0, relwidth=0.40, anchor="e")


        logo = ctk.CTkImage(
        light_image=Image.open(resource_path("assets/images/smslogo1.png")),
        size=(287, 110)
        )


        # Place it inside rightFrame
        img_label = ctk.CTkLabel(
            rightFrame,
            text="",        
            image=logo,
            fg_color="transparent"
        )
        img_label.place(relx=0.5, rely=0.11, anchor="center")


        # TITLE
        tk.Label(
            rightFrame,
            text="Create Account",
            bg="#ffffff",
            font=("Ubuntu", 25, "bold"),
            fg="#2d3748",
        ).place(relx=0.30, rely=0.17)


        tk.Label(
            rightFrame,
            text="Sign up to continue",
            bg="#ffffff",
            font=("Arial", 14),
            fg="#718096",
        ).place(relx=0.36, rely=0.22)

        # NOTIFICATION LABEL
        self.notif_label = ctk.CTkLabel(
            self,
            text="",
            fg_color="#ffffff",
            text_color="red",
            font=("Arial", 13, "bold"),
        )
        self.notif_label.place(relx=0.516, rely=0.365, anchor="center", y=10, x=-10)


        # Preferred name 
        tk.Label(
            rightFrame,
            text="What should we call you?",
            bg="#ffffff",
            font=("Ubuntu", 12, "bold"),
            fg="#4a5568",
        ).place(relx=0.25, rely=0.30)


        self.pname_entry = ctk.CTkEntry(
            rightFrame,
            border_width=2,
            border_color="#d1d1d1",
            font=("Arial", 14, "italic"),
            placeholder_text="Enter preferred name",
            placeholder_text_color="#a8a8a8",
            text_color="black",
            fg_color="#ffffff",
            width=313,
            height=45,
            corner_radius=30,
        )
        self.pname_entry.place(relx=0.24, rely=0.33)


        # Email 
        tk.Label(
            rightFrame,
            text="What is your email?",
            bg="#ffffff",
            font=("Ubuntu", 12, "bold"),
            fg="#4a5568",
        ).place(relx=0.26, rely=0.39)


        self.email_entry = ctk.CTkEntry(
            rightFrame,
            border_width=2,
            border_color="#d1d1d1",
            font=("Arial", 14, "italic"),
            placeholder_text="Please enter a valid email",
            placeholder_text_color="#a8a8a8",
            text_color="black",
            fg_color="#ffffff",
            width=313,
            height=45,
            corner_radius=30,
        )
        self.email_entry.place(relx=0.24, rely=0.42)


        # USERNAME ENTRY 
        tk.Label(
            rightFrame,
            text="Username",
            bg="#ffffff",
            font=("Ubuntu", 12, "bold"),
            fg="#4a5568",
        ).place(relx=0.26, rely=0.48)


        self.username_entry = ctk.CTkEntry(
            rightFrame,
            border_width=2,
            border_color="#d1d1d1",
            font=("Arial", 14, "italic"),
            placeholder_text="Enter Username",
            placeholder_text_color="#a8a8a8",
            text_color="black",
            fg_color="#ffffff",
            width=313,
            height=45,
            corner_radius=30,
        )
        self.username_entry.place(relx=0.24, rely=0.51)


        # PASSWORD ENTRY
        tk.Label(
            rightFrame,
            text="Password",
            bg="#ffffff",
            font=("Ubuntu", 12, "bold"),
            fg="#4a5568",
        ).place(relx=0.26, rely=0.57)
 
        # --- Password entry ---
        self.password_entry = ctk.CTkEntry(
            rightFrame,
            border_width=2,
            border_color="#d1d1d1",
            font=("Arial", 14, "italic"),
            placeholder_text="Enter Password",
            placeholder_text_color="#a8a8a8",
            text_color="black",
            fg_color="#ffffff",
            show="●",
            width=313,
            height=46,
            corner_radius=30,
        )
        self.password_entry.place(relx=0.24, rely=0.60)


        # --- Eye icon images ---
        self.show = ctk.CTkImage(Image.open(resource_path("assets/images/frontpage_icons/eye.png")), size=(18, 18))
        self.close = ctk.CTkImage(Image.open(resource_path("assets/images/frontpage_icons/hidden.png")), size=(18, 18))


        # --- Eye icon button ---
        self.toggle_btn_reg = ctk.CTkButton(
            rightFrame,
            image=self.close,
            text="",
            width=35,
            height=35,
            fg_color="#ffffff",
            hover_color="#f0f0f0",
            corner_radius=30,
            command=lambda: self.toggle_password_visibility(self.password_entry, self.toggle_btn_reg),
        )
        self.toggle_btn_reg.place(relx=0.647, rely=0.607)


        # === REGISTER BUTTON ===
        ctk.CTkButton(
            rightFrame,
            command=self.handle_register,
            text="Register",
            text_color="white",
            font=("Arial", 15),
            hover_color="#00145d",
            width=170,
            height=45,
            fg_color="#354eab",
            cursor="hand2",
            corner_radius=35,
        ).place(relx=0.36, rely=0.70)


        # === SIGN IN LINK ===
        tk.Label(
            rightFrame,
            text="Already have an account?",
            bg="#ffffff",
            fg="#718096",
            font=("Arial", 10),
        ).place(relx=0.32, rely=0.78)


        signuplabel = tk.Label(
            rightFrame,
            text="Login",
            bg="#ffffff",
            fg="#354eab",
            font=("Arial", 10, "bold"),
            cursor="hand2",
        )
        signuplabel.place(relx=0.58, rely=0.78)
        signuplabel.bind("<Enter>", lambda e: signuplabel.config(font=("Arial", 10, "bold", "underline")))
        signuplabel.bind("<Leave>", lambda e: signuplabel.config(font=("Arial", 10, "bold")))
        signuplabel.bind("<Button-1>", self.switch_to_login)


        # === KEY BINDINGS ===
        self.pname_entry.bind("<Return>", self.handle_register)
        self.email_entry.bind("<Return>", self.handle_register)
        self.username_entry.bind("<Return>", self.handle_register)
        self.password_entry.bind("<Return>", self.handle_register)


        self.master.bind("<Escape>", lambda e: self.switch_to_login())


        self.current_frame = backFrame

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def show_login(self):
        self.clear_frame()


        # === MAIN CONTAINER ===
        backFrame = ctk.CTkFrame(self,
        fg_color="#ECF4FF",
        width=10,
        height=520,
        corner_radius=20,
        )
        backFrame.pack(expand=True, fill="both")
        backFrame.pack_propagate(False)
       
       
    # === LEFT PANEL ===
        leftFrame = ctk.CTkFrame(
        backFrame,
        fg_color="#ECF4FF",
        corner_radius=0,
        )
        leftFrame.place(relx=0.0, rely=0.5, relheight=1.0, relwidth=0.68, anchor="w")
       
        # background image
        original_img = Image.open(resource_path("assets/images/bg.png"))
        bg_image = ctk.CTkImage(light_image=original_img, size=(1280, 900))
        bg_label = ctk.CTkLabel(leftFrame, text="", image=bg_image)
        bg_label.place(relx=0.5, rely=0.5, anchor="center")


    # === RIGHT PANEL ===


        rightFrame = ctk.CTkFrame(
        backFrame,
        fg_color="#ffffff",
        border_width=2,
        border_color="#9D9D9D",
        corner_radius=45,
        )
        rightFrame.place(relx=0.97, rely=0.61, relheight=1.0, relwidth=0.33, anchor="e")


    # === TITLE ===
        tk.Label(
        rightFrame,
        text="Welcome!",
        bg="#ffffff",
        font=("Ubuntu", 30, "bold"),
        fg="#2d3748",
        ).place(relx=0.30, rely=0.12)


        tk.Label(
        rightFrame,
        text="Sign in to continue",
        bg="#ffffff",
        font=("Arial", 15),
        fg="#718096",
        ).place(relx=0.33, rely=0.19)


        self.notif_label = ctk.CTkLabel(
        self,text="",
        fg_color='transparent',
        text_color="red",
        font=("Arial", 15, "bold"),
        )
        self.notif_label.place(relx=0.450, rely=0.373, anchor="e", y=10, x=600)
       
        # === USERNAME ENTRY ===
        tk.Label(
        rightFrame,
        text="Username",
        bg="#ffffff",
        font=("Ubuntu", 12, "bold"),
        fg="#4a5568",
         ).place(relx=0.19, rely=0.32)


        self.username_entry = ctk.CTkEntry(
        rightFrame,
        border_width=2,
        border_color="#d1d1d1",
        font=("Arial", 14, "italic"),
        placeholder_text="Enter Username",
        placeholder_text_color="#a8a8a8",
        text_color="black",
        fg_color="#ffffff",
        width=313,
        height=46,
        corner_radius=30,
        )
        self.username_entry.place(relx=0.19, rely=0.35)


        # === PASSWORD ENTRY ===
        tk.Label(
        rightFrame,
        text="Password",
        bg="#ffffff",
        font=("Ubuntu", 12, "bold"),
        fg="#4a5568",
        ).place(relx=0.19, rely=0.45)


        self.password_entry = ctk.CTkEntry(
        rightFrame,
        border_width=2,
        border_color="#d1d1d1",
        font=("Arial", 14, "italic"),
        placeholder_text="Enter Password",
        placeholder_text_color="#a8a8a8",
        text_color="black",
        fg_color="#ffffff",
        show="●",
        width=313,
        height=46,
        corner_radius=30,
        )
        self.password_entry.place(relx=0.19, rely=0.48)


        self.show = ctk.CTkImage(Image.open(resource_path("assets/images/frontpage_icons/eye.png")), size=(18, 18))
        self.close = ctk.CTkImage(Image.open(resource_path("assets/images/frontpage_icons/hidden.png")), size=(18, 18))


        # --- Eye icon button ---
        self.toggle_btn_reg = ctk.CTkButton(
            rightFrame,
            image=self.close,
            text="",
            width=35,
            height=35,
            fg_color="#ffffff",
            hover_color="#f0f0f0",
            corner_radius=30,
            command=lambda: self.toggle_password_visibility(self.password_entry, self.toggle_btn_reg),
        )
        self.toggle_btn_reg.place(relx=0.68, rely=0.487)


    # === Forgot Password ===
        forgot_label = tk.Label(
        rightFrame,
        text="Forgot Password?",
        bg="#ffffff",
        fg="#354eab",
        font=("Arial", 9, "bold"),
        cursor="hand2")
        forgot_label.place(relx=0.555, rely=0.537)


        forgot_label.bind("<Enter>", lambda e: forgot_label.config(font=("Arial", 9, "bold", "underline")))
        forgot_label.bind("<Leave>", lambda e: forgot_label.config(font=("Arial", 9, "bold")))


        forgot_label.bind("<Button-1>", lambda e: self.show_forgot_password())  


    # === REGISTER BUTTON ===
        ctk.CTkButton(
        rightFrame,
        command=self.handle_login,
        text="Login",
        text_color="white",
        font=("Arial", 15),
        hover_color="#00145d",
        width=170,
        height=45,
        fg_color="#354eab",
        cursor="hand2",
        corner_radius=35,
        ).place(relx=0.33, rely=0.58)


        tk.Label(
        rightFrame,
        text="Don't have an account?",
        bg="#ffffff",
        fg="#718096",
        font=("Arial", 10),
        ).place(relx=0.30, rely=0.70)


        signuplabel = tk.Label(
        rightFrame,
        text="Sign Up",
        bg="#ffffff",
        fg="#354eab",
        font=("Arial", 9, "bold"),
        cursor="hand2")
        signuplabel.place(relx=0.58, rely=0.70)


        signuplabel.bind("<Enter>", lambda e: signuplabel.config(font=("Arial", 9, "bold", "underline")))
        signuplabel.bind("<Leave>", lambda e: signuplabel.config(font=("Arial", 9, "bold")))


        signuplabel.bind("<Button-1>", self.switch_to_register)


        self.username_entry.bind("<Return>", self.handle_login)
        self.password_entry.bind("<Return>", self.handle_login)


        self.master.bind("<Escape>", lambda e: self.switch_to_register())


        self.current_frame = backFrame

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 
    def show_forgot_password(self):
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
            size=(287, 110)
        )
        img_label = ctk.CTkLabel(rightFrame, text="", image=logo, fg_color="transparent")
        img_label.place(relx=0.5, rely=0.11, anchor="center")

        # === TITLE ===
        tk.Label(
            rightFrame,
            text="Forgot Password",
            bg="#ffffff",
            font=("Ubuntu", 25, "bold"),
            fg="#2d3748",
        ).place(relx=0.28, rely=0.17)

        tk.Label(
            rightFrame,
            text="Reset your password",
            bg="#ffffff",
            font=("Arial", 14),
            fg="#718096",
        ).place(relx=0.36, rely=0.22)

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
            width=313,
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
            width=313,
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
            width=313,
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
            command=self.handle_forgot_password,
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
        back_to_login.place(relx=0.59, rely=0.78)
        back_to_login.bind("<Enter>", lambda e: back_to_login.config(font=("Arial", 10, "bold", "underline")))
        back_to_login.bind("<Leave>", lambda e: back_to_login.config(font=("Arial", 10, "bold")))
        back_to_login.bind("<Button-1>", self.switch_to_login)

        self.master.bind("<Escape>", lambda e: self.switch_to_login())
        self.current_frame = backFrame


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # def show_change_password(self):
    #     self.clear_frame()


    #     # === BACKGROUND FRAME ===
    #     backFrame = ctk.CTkFrame(self, fg_color="#ECF4FF", width=10, height=520, corner_radius=20)
    #     backFrame.place(relx=0.97, rely=0.60)
    #     backFrame.pack(expand=True, fill="both")
    #     backFrame.pack_propagate(False)


    #     leftFrame = ctk.CTkFrame(backFrame, fg_color="#ECF4FF", corner_radius=0)
    #     leftFrame.place(relx=0.0, rely=0.5, relheight=1.0, relwidth=0.999, anchor="w")


    #     original_img = Image.open(resource_path("assets/images/bg1.png"))
    #     bg_image = ctk.CTkImage(light_image=original_img, size=(1500, 900))
    #     bg_label = ctk.CTkLabel(leftFrame, text="", image=bg_image)
    #     bg_label.place(relx=0.5, rely=0.5, anchor="center")


    #     def resize_bg(event):
    #         new_w, new_h = event.width, event.height
    #         resized = original_img.resize((new_w, new_h))
    #         new_ctk_img = ctk.CTkImage(light_image=resized, size=(new_w, new_h))
    #         bg_label.configure(image=new_ctk_img)
    #         bg_label.image = new_ctk_img


    #     leftFrame.bind("<Configure>", resize_bg)


    #     # === RIGHT FRAME (Change Password) ===
    #     rightFrame = ctk.CTkFrame(
    #         backFrame,
    #         fg_color="#ffffff",
    #         border_width=2,
    #         border_color="#9D9D9D",
    #         corner_radius=45,
    #     )
    #     rightFrame.place(relx=0.71, rely=0.60, relheight=1.0, relwidth=0.40, anchor="e")


    #     # === HEADINGS ===
    #     tk.Label(
    #         rightFrame,
    #         text="Change Password",
    #         bg="#ffffff",
    #         font=("Ubuntu", 30, "bold"),
    #         fg="#2d3748",
    #     ).place(relx=0.20, rely=0.15)


    #     tk.Label(
    #         rightFrame,
    #         text="Update your account credentials",
    #         bg="#ffffff",
    #         font=("Arial", 15),
    #         fg="#718096",
    #     ).place(relx=0.26, rely=0.22)


    #     # === CURRENT PASSWORD ===
    #     tk.Label(
    #         rightFrame,
    #         text="Current Password",
    #         bg="#ffffff",
    #         font=("Ubuntu", 12, "bold"),
    #         fg="#4a5568",
    #     ).place(relx=0.26, rely=0.30)


    #     current_pw_frame = ctk.CTkFrame(
    #         rightFrame,
    #         fg_color="#ffffff",
    #         border_width=2,
    #         border_color="#d1d1d1",
    #         corner_radius=30,
    #         width=313,
    #         height=45,
    #     )
    #     current_pw_frame.place(relx=0.24, rely=0.33)


    #     self.current_password_entry = ctk.CTkEntry(
    #         current_pw_frame,
    #         border_width=0,
    #         font=("Arial", 14, "italic"),
    #         placeholder_text="Enter Current Password",
    #         placeholder_text_color="#a8a8a8",
    #         text_color="black",
    #         fg_color="#ffffff",
    #         show="●",
    #         width=275,
    #         height=45,
    #         corner_radius=30,
    #     )
    #     self.current_password_entry.place(x=0, y=0)


    #     self.toggle_btn_current = ctk.CTkButton(
    #         current_pw_frame,
    #         text="👁",
    #         width=30,
    #         height=30,
    #         fg_color="#ffffff",
    #         text_color="#4a5568",
    #         font=("Arial", 14),
    #         hover_color="#f0f0f0",
    #         corner_radius=30,
    #         command=lambda: self.toggle_password_visibility(self.current_password_entry, self.toggle_btn_current),
    #     )
    #     self.toggle_btn_current.place(relx=0.85, rely=0.14)


    #     # === NEW PASSWORD ===
    #     tk.Label(
    #         rightFrame,
    #         text="New Password",
    #         bg="#ffffff",
    #         font=("Ubuntu", 12, "bold"),
    #         fg="#4a5568",
    #     ).place(relx=0.26, rely=0.42)


    #     new_pw_frame = ctk.CTkFrame(
    #         rightFrame,
    #         fg_color="#ffffff",
    #         border_width=2,
    #         border_color="#d1d1d1",
    #         corner_radius=30,
    #         width=313,
    #         height=45,
    #     )
    #     new_pw_frame.place(relx=0.24, rely=0.45)


    #     self.new_password_entry = ctk.CTkEntry(
    #         new_pw_frame,
    #         border_width=0,
    #         font=("Arial", 14, "italic"),
    #         placeholder_text="Enter New Password",
    #         placeholder_text_color="#a8a8a8",
    #         text_color="black",
    #         fg_color="#ffffff",
    #         show="●",
    #         width=275,
    #         height=45,
    #         corner_radius=30,
    #     )
    #     self.new_password_entry.place(x=0, y=0)


    #     self.toggle_btn_new = ctk.CTkButton(
    #         new_pw_frame,
    #         text="👁",
    #         width=30,
    #         height=30,
    #         fg_color="#ffffff",
    #         text_color="#4a5568",
    #         font=("Arial", 14),
    #         hover_color="#f0f0f0",
    #         corner_radius=30,
    #         command=lambda: self.toggle_password_visibility(self.new_password_entry, self.toggle_btn_new),
    #     )
    #     self.toggle_btn_new.place(relx=0.85, rely=0.14)


    #     # === CONFIRM NEW PASSWORD ===
    #     tk.Label(
    #         rightFrame,
    #         text="Confirm New Password",
    #         bg="#ffffff",
    #         font=("Ubuntu", 12, "bold"),
    #         fg="#4a5568",
    #     ).place(relx=0.26, rely=0.54)


    #     confirm_pw_frame = ctk.CTkFrame(
    #         rightFrame,
    #         fg_color="#ffffff",
    #         border_width=2,
    #         border_color="#d1d1d1",
    #         corner_radius=30,
    #         width=313,
    #         height=45,
    #     )
    #     confirm_pw_frame.place(relx=0.24, rely=0.57)


    #     self.confirm_password_entry = ctk.CTkEntry(
    #         confirm_pw_frame,
    #         border_width=0,
    #         font=("Arial", 14, "italic"),
    #         placeholder_text="Confirm New Password",
    #         placeholder_text_color="#a8a8a8",
    #         text_color="black",
    #         fg_color="#ffffff",
    #         show="●",
    #         width=275,
    #         height=45,
    #         corner_radius=30,
    #     )
    #     self.confirm_password_entry.place(x=0, y=0)


    #     self.toggle_btn_confirm = ctk.CTkButton(
    #         confirm_pw_frame,
    #         text="👁",
    #         width=30,
    #         height=30,
    #         fg_color="#ffffff",
    #         text_color="#4a5568",
    #         font=("Arial", 14),
    #         hover_color="#f0f0f0",
    #         corner_radius=30,
    #         command=lambda: self.toggle_password_visibility(self.confirm_password_entry, self.toggle_btn_confirm),
    #     )
    #     self.toggle_btn_confirm.place(relx=0.85, rely=0.14)


    #     # === SUBMIT BUTTON ===
    #     ctk.CTkButton(
    #         rightFrame,
    #         command=self.handle_change_password,
    #         text="Update Password",
    #         text_color="white",
    #         font=("Arial", 15),
    #         hover_color="#00145d",
    #         width=170,
    #         height=45,
    #         fg_color="#354eab",
    #         cursor="hand2",
    #         corner_radius=35,
    #     ).place(relx=0.36, rely=0.72)


    #     # === GO BACK TO DASHBOARD OR LOGIN ===
    #     tk.Label(rightFrame, text="Want to go back?", bg="#ffffff", fg="#718096", font=("Arial", 10)).place(relx=0.34, rely=0.78)
    #     back_label = tk.Label(rightFrame, text="Cancel", bg="#ffffff", fg="#354eab", font=("Arial", 10, "bold"), cursor="hand2")
    #     back_label.place(relx=0.54, rely=0.78)
    #     back_label.bind("<Enter>", lambda e: back_label.config(font=("Arial", 10, "bold", "underline")))
    #     back_label.bind("<Leave>", lambda e: back_label.config(font=("Arial", 10, "bold")))
    #     back_label.bind("<Button-1>", self.switch_to_dashboard)


    #     self.confirm_password_entry.bind("<Return>", self.handle_change_password)
    #     self.master.bind("<Escape>", lambda e: self.switch_to_dashboard())


    #     self.current_frame = backFrame


	
