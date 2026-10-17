import tkinter as tk
import customtkinter as ctk
from PIL import Image
from utils.resource_path import resource_path  # Make sure this exists in your project

class ShowAboutUsPage(ctk.CTkFrame):
    def __init__(self, master, backend):
        super().__init__(master, fg_color="#f0f0f0")
        self.current_frame = None
        self.backend = backend

    def show_page(self, name):
        if name == "show_about_us":
            self.show_about_us()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.current_frame = None

    def show_about_us(self):
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
        leftFrame = ctk.CTkFrame(
            backFrame,
            fg_color="#ECF4FF",
            corner_radius=0,
        )
        leftFrame.place(relx=0.0, rely=0.5, relheight=1.0, relwidth=0.68, anchor="w")

        # Background image
        original_img = Image.open(resource_path("assets/images/bg.png"))
        bg_image = ctk.CTkImage(light_image=original_img, size=(1280, 900))
        bg_label = ctk.CTkLabel(leftFrame, text="", image=bg_image)
        bg_label.place(relx=0.5, rely=0.5, anchor="center")

        # Main frame (RIGHT SIDE)
        mainFrame = ctk.CTkFrame(backFrame, fg_color="#ecf4ff")
        mainFrame.place(relx=0.68, rely=0.5, relheight=1.0, relwidth=0.32, anchor="w")

        # Title
        about_label = ctk.CTkLabel(
            mainFrame, text="About Us",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        about_label.pack(padx=20, pady=(20, 10))

        # Info text (FIXED WITH TRIPLE QUOTES)
        info_text = """
The system is made for students at St. Michael’s College to help them stay organized, productive, and stress-free. Built using Python and Tkinter, our Schedule Management System simplifies planning by combining scheduling, task tracking, book monitoring, and weekly progress updates in one easy-to-use platform.

One key feature is the book borrowing tracker, which helps students keep track of the required 20 books per semester, ensuring they meet academic requirements without hassle. Another is the task management module, allowing students to add, organize, and prioritize tasks while receiving weekly accomplishment notifications to reflect on their progress.

At the core of the system is the schedule management module, where students can add schedules, mark events, and view all activities clearly in one place. Unlike the current SMC portal, this system offers a clean and organized view of both academic and personal commitments, making time management simple and effective.

In short, this system is designed to make student life easier, helping them manage responsibilities efficiently while staying motivated and on track.

Made with Love and Care in compliance for the subject:

Object Oriented Programming

Austria Candole Manginsay Connection
ScheduleManagementSystem © 2025
"""

        # Label for info text
        info_label = ctk.CTkLabel(
            mainFrame,
            text=info_text,
            font=ctk.CTkFont(size=14),
            justify="left",
            text_color="black",
            wraplength=350
        )
        info_label.pack(padx=20, pady=10)