# standard library
import tkinter as tk


# third-party
import customtkinter as ctk
from PIL import Image


# local imports
from utils.resource_path import resource_path
from authActivity.frontend.main_content.show_cpassword_page import ShowChangePasswordPage
from authActivity.frontend.main_content.show_dashboard_page import ShowDashboardPage
from authActivity.frontend.main_content.show_schedule_page import ShowSchedulePage
from authActivity.frontend.main_content.show_to_do_page import ShowToDoPage
from authActivity.frontend.main_content.show_calendar_page import ShowCalendarPage
from authActivity.frontend.main_content.about_us_page import ShowAboutUsPage




class Bar(tk.Frame):
    def __init__(self, master, backend, on_logout):
        super().__init__(master, bg="#f5f5f5")


        self.current_frame = None
        self.on_logout = on_logout
        self.backend = backend
        self.expand_left = 0
        self.change_btn = None


        # Background frame
        self.backFrame = tk.Frame(self, bg="#333333", borderwidth=1, relief="raised")
        self.backFrame.pack(fill="both", expand=True)


        # Topbar frame
        self.topbarFrame = tk.Frame(self.backFrame, bg="#ffffff", borderwidth=1, relief="raised", pady=5)
        self.topbarFrame.pack(fill="x", side="top")
        self.topbarFrame.pack_propagate(False)


        # Left sidebar frame
        self.left_sidebarFrame = tk.Frame(self.backFrame, bg="#ffffff", padx=10)
        self.left_sidebarFrame.pack(fill="y", side="left")
        self.left_sidebarFrame.pack_propagate(False)


        # Subtle shadow beside sidebar
        self.sidebar_shadow = ctk.CTkFrame(
            self.backFrame, fg_color="#979797", width=3, corner_radius=0, border_width=3, border_color="#979797"
        )
        self.sidebar_shadow.pack(fill="y", side="left")


        # Content frame
        self.contentFrame = tk.Frame(self.backFrame, bg="#e0e0e0")
        self.contentFrame.pack(fill="both", side="right", expand=True)


        # Pages
        self.show_dashboard_page = ShowDashboardPage(self.contentFrame, backend=backend, calendar_page=None)
        self.show_schedule_page = ShowSchedulePage(self.contentFrame, backend=backend)
        self.show_to_do_page = ShowToDoPage(self.contentFrame, backend=backend)
        self.show_calendar_page = ShowCalendarPage(self.contentFrame, backend=backend, show_notification=self.show_notification)
        self.about_us_page = ShowAboutUsPage(self.contentFrame, backend=backend)
        self.show_cpassword_page = ShowChangePasswordPage(self.contentFrame, backend=backend)


        self.active_page = self.show_dashboard_page
        self.active_page.pack(fill="both", expand=True)


    # Utility methods
    def clear_all(self):
        for widget in self.left_sidebarFrame.winfo_children():
            widget.destroy()
        for widget in self.topbarFrame.winfo_children():
            widget.destroy()
        self.show_dashboard_page.show_dashboard()
        self.current_frame = None


    def handle_logout(self):
        self.backend.logout_user()
        if self.on_logout:
            self.on_logout()


    def confirm_logout(self):
           
            # Background overlay
            overlay = tk.Frame(self.backFrame, bg="#ecf4ff", highlightthickness=0)
            overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
            overlay.attributes = {"alpha": 0.4}


            # Popup frame
            popup_frame = ctk.CTkFrame(
                overlay,
                fg_color="#FFFFFF",
                corner_radius=12,
                border_width=1,
                border_color="#CFCFCF"
            )
            popup_frame.place(relx=0.5, rely=0.5, anchor="center")


            # Popup message
            lbl = ctk.CTkLabel(
                popup_frame,
                text="Are you sure you want to log out?",
                text_color="black",
                font=("Ubuntu", 14, "bold")
            )
            lbl.pack(padx=30, pady=(20, 10))


            # Button frame
            btn_frame = ctk.CTkFrame(popup_frame, fg_color="transparent")
            btn_frame.pack(pady=(0, 15))


            # Confirm Button
            confirm_btn = ctk.CTkButton(
                btn_frame,
                text="Yes",
                fg_color="#354eab",
                hover_color="#2E3E8E",
                text_color="white",
                width=100,
                command=lambda: (self.handle_logout(), overlay.destroy())
            )
            confirm_btn.pack(side="left", padx=10)


            # Cancel Button
            cancel_btn = ctk.CTkButton(
                btn_frame,
                text="Cancel",
                fg_color="#b0b0b0",
                hover_color="#999999",
                text_color="black",
                width=100,
                command=lambda: overlay.destroy()
            )
            cancel_btn.pack(side="left", padx=10)


            # Close popup on click outside
            def close_on_click(event):
                if event.widget == overlay:
                    overlay.destroy()


            overlay.bind("<Button-1>", close_on_click)


    def expand_menu(self):
        self.expand_left = 1 - self.expand_left  # Toggle 0 <-> 1
        for widget in self.left_sidebarFrame.winfo_children():
            widget.destroy()
        self.bar_leftFrame()


    def change_header(self, title):
        self.header_title.configure(text=f"| {title}")


    def change_page(self, text, method_name):
        self.active_page.pack_forget()


        # Auto expand sidebar when a main page is clicked
        if self.expand_left == 0:
            self.expand_left = 1
        for widget in self.left_sidebarFrame.winfo_children():
            widget.destroy()
        self.bar_leftFrame()


        page_map = {
            "Dashboard": self.show_dashboard_page,
            "Schedule": self.show_schedule_page,
            "To Do": self.show_to_do_page,
            "Calendar": self.show_calendar_page,
            "About Us": self.about_us_page,
            "Change Password": self.show_cpassword_page,
        }


        page = page_map.get(text)
        if page:
            page.pack(fill="both", expand=True)
            page.show_page(method_name)
            self.active_page = page


    def change_topbar_btn(self, btn_name):
        if btn_name == "Dashboard":
            self.create_btn.configure(image=None, text="")
        elif btn_name == "Schedule":
            self.create_btn.configure(
                image=self.topbar_btn_icons[1],
                text="Add",
                command=lambda: self.show_schedule_page.show_popup_schedule(),
            )
        elif btn_name == "To Do":
            self.create_btn.configure(
                image=self.topbar_btn_icons[2],
                text="Task",
                command=lambda: self.show_to_do_page.create_task("create"),
            )
        elif btn_name == "Calendar":
            self.create_btn.configure(
                image=self.topbar_btn_icons[3],
                text="Task",
                command=lambda: self.show_calendar_page.create_add_event(),
            )
        elif btn_name == "About Us":
            self.create_btn.configure(image=None, text="")


    # Settings Dropdown
    def on_settings(self):
        if self.expand_left == 0:
            self.expand_left = 1
        for widget in self.left_sidebarFrame.winfo_children():
            widget.destroy()
        self.bar_leftFrame()


        if hasattr(self, "settings_visible") and self.settings_visible:
            if hasattr(self, "settingsFrame"):
                self.settingsFrame.place_forget()
            self.settings_visible = False
            return


        self.settings_visible = True


        try:
            logout_icon = Image.open(resource_path("assets/images/sidebar_icons/logout.png"))
            settings_icon = Image.open(resource_path("assets/images/sidebar_icons/settings.png"))
            logout = ctk.CTkImage(light_image=logout_icon, dark_image=logout_icon, size=(20, 20))
            settings_img = ctk.CTkImage(light_image=settings_icon, dark_image=settings_icon, size=(20, 20))
        except Exception as e:
            print("Icon load error:", e)
            logout, settings_img = None, None


        self.settingsFrame = ctk.CTkFrame(self.backFrame, fg_color="#ffffff", bg_color="#ffffff", corner_radius=12)
        self.settingsFrame.place(relx=0.011, rely=0.81, anchor="nw")


        ctk.CTkButton(
            self.settingsFrame,
            image=settings_img,
            text=" Change Password",
            text_color="black",
            fg_color="#f5f5f5",
            border_width=1,
            corner_radius=10,
            font=("Ubuntu", 12, "bold"),
            anchor="w",
            cursor="hand2",
            hover_color="#E7E7E7",
            width=180,
            height=40,
            command=self.handle_change_password,
        ).pack(padx=1, pady=(6, 4))


        ctk.CTkButton(
            self.settingsFrame,
            image=logout,
            text=" Logout",
            text_color="black",
            fg_color="#f5f5f5",
            border_width=1,
            corner_radius=10,
            font=("Ubuntu", 12, "bold"),
            anchor="w",
            cursor="hand2",
            hover_color="#E7E7E7",
            width=180,
            height=40,
            command=self.confirm_logout,
        ).pack(padx=1, pady=(4, 8))


    def handle_change_password(self):
        self.change_page("Change Password", "show_cpassword")
        self.change_header("Change Password")
        self.change_topbar_btn("Change Password")


    # Topbar + Sidebar
    def bar_topFrame(self):
        self.clear_all()
        btn_color = "#ffffff"
        hover = "#E7E7E7"


        menu_icon = Image.open(resource_path("assets/images/topbar_icons/menu.png"))
        picture = ctk.CTkImage(light_image=menu_icon, dark_image=menu_icon, size=(20, 20))


        menu_btn = ctk.CTkButton(
            self.topbarFrame,
            image=picture,
            text="",
            fg_color=btn_color,
            height=30,
            width=30,
            hover_color=hover,
            cursor="hand2",
            command=lambda: self.after(100, self.expand_menu),
        )
        menu_btn.grid(row=0, column=0, padx=(15, 0), pady=10)


        logo = ctk.CTkImage(
            light_image=Image.open(resource_path("assets/images/smslogo1.png")), size=(114, 40)
        )
        design_logo = ctk.CTkLabel(self.topbarFrame, image=logo, text="", fg_color=btn_color)
        design_logo.grid(row=0, column=1, padx=(15, 20))


        self.header_title = ctk.CTkLabel(
            self.topbarFrame, text="| Dashboard", text_color="black", font=("Ubuntu", 20, "bold")
        )
        self.header_title.grid(row=0, column=2, padx=13)


        # Icons
        openf_pencil = Image.open(resource_path("assets/images/main_contents/personal_information_icons/create1.png"))
        openf_to_do = Image.open(resource_path("assets/images/main_contents/schedule_icons/clock.png"))
        openf_clock = Image.open(resource_path("assets/images/main_contents/to_do_icons/check_list.png"))
        openf_plan = Image.open(resource_path("assets/images/main_contents/calendar_icons/planner.png"))


        self.topbar_btn_icons = [
            ctk.CTkImage(light_image=openf_pencil, size=(25, 25)),
            ctk.CTkImage(light_image=openf_to_do, size=(28, 28)),
            ctk.CTkImage(light_image=openf_clock, size=(28, 28)),
            ctk.CTkImage(light_image=openf_plan, size=(28, 28)),
        ]


        notify_icon = Image.open(resource_path("assets/images/topbar_icons/notification.png"))
        picture1 = ctk.CTkImage(light_image=notify_icon, dark_image=notify_icon, size=(28, 28))


        notify_btn = ctk.CTkButton(
            self.topbarFrame,
            image=picture1,
            text="",
            fg_color=btn_color,
            height=40,
            width=30,
            hover_color=hover,
            cursor="hand2",
            command=self.expand_notification,
        )
        notify_btn.pack(side="right", padx=(0, 20))


        self.create_btn = ctk.CTkButton(
            self.topbarFrame,
            image=None,
            text="",
            text_color="black",
            fg_color=btn_color,
            height=40,
            width=30,
            hover_color=hover,
            font=("Ubuntu", 15, "bold"),
            cursor="hand2",
            compound="right",
            command=None,
        )
        self.create_btn.pack(side="right", padx=(0, 7))


        self.bar_leftFrame()


    # Sidebar
    def bar_leftFrame(self):
        btn_color = "#ffffff"
        hover = "#E7E7E7"


        design = ctk.CTkLabel(self.left_sidebarFrame, text="", height=1)
        design.grid(row=0, column=0)


        settings_icon = Image.open(resource_path("assets/images/sidebar_icons/settings1.png"))
        sett_icon = ctk.CTkImage(light_image=settings_icon, dark_image=settings_icon, size=(20, 20))


        button_names = [
            ("Dashboard", "show_dashboard"),
            ("Schedule", "show_schedule"),
            ("To Do", "show_to_do"),
            ("Calendar", "show_calendar"),
            ("About Us", "show_about_us"),
        ]


        icons = [
            "assets/images/sidebar_icons/home1.png",
            "assets/images/sidebar_icons/schedule2.png",
            "assets/images/sidebar_icons/to-do-list1.png",
            "assets/images/sidebar_icons/calendar1.png",
            "assets/images/sidebar_icons/about_us.png",
        ]


        for i, (text, method_name) in enumerate(button_names):
            icon_img = Image.open(resource_path(icons[i]))
            picture = ctk.CTkImage(light_image=icon_img, dark_image=icon_img, size=(20, 20))
            btn_text = "" if self.expand_left == 0 else f" {text}"


            btn = ctk.CTkButton(
                self.left_sidebarFrame,
                image=picture,
                text=btn_text,
                text_color="black",
                hover_color=hover,
                width=185 if self.expand_left else 40,
                height=40,
                cursor="hand2",
                fg_color=btn_color,
                anchor="w",
                command=lambda m=method_name, t=text: (
                    self.change_page(t, m),
                    self.change_header(t),
                    self.change_topbar_btn(t),
                ),
            )
            btn.grid(row=i + 1, column=0, padx=5, pady=(0, 10))


        # Settings button (bottom)
        if self.expand_left == 0:
            ctk.CTkButton(
                self.left_sidebarFrame,
                image=sett_icon,
                text="",
                fg_color=btn_color,
                hover_color=hover,
                width=40,
                height=40,
                anchor="w",
                cursor="hand2",
                command=self.on_settings,
            ).pack(padx=5, pady=20, side="bottom")
        else:
            ctk.CTkButton(
                self.left_sidebarFrame,
                image=sett_icon,
                text=" Settings",
                text_color="black",
                fg_color=btn_color,
                hover_color=hover,
                width=180,
                height=40,
                cursor="hand2",
                anchor="w",
                command=self.on_settings,
            ).pack(padx=5, pady=20, side="bottom")


        self.current_frame = self.backFrame


    # Notifications
    def expand_notification(self):
        color0 = "#E7E7E7"


        if hasattr(self, "notification_visible") and self.notification_visible:
            self.notificationFrame.place_forget()
            self.notification_visible = False
        else:
            if not hasattr(self, "notificationFrame") or self.notificationFrame is None:
                self.notificationFrame = ctk.CTkFrame(
                    self.backFrame,
                    fg_color=color0,
                    bg_color="#ffffff",
                    corner_radius=10,
                    border_color="#8B8989",
                    border_width=1,
                )


                ctk.CTkLabel(
                    self.notificationFrame,
                    text="Notifications",
                    text_color="black",
                    font=("Ubuntu", 15, "bold"),
                    width=350,
                    anchor="w",
                ).pack(padx=(20, 5), pady=5)


                notification_scrl = ctk.CTkScrollableFrame(
                    self.notificationFrame, fg_color=color0, width=346, height=400
                )
                notification_scrl.pack(side="top", expand=True)


                ctk.CTkLabel(
                    notification_scrl,
                    text="No Notifications",
                    text_color="#8B8989",
                    font=("Ubuntu", 12),
                ).pack(pady=100)


            self.notificationFrame.place(relx=1.0, rely=0.0, anchor="ne", y=55, x=-20)
            self.notification_visible = True


    def show_notification(self, message):
        if not hasattr(self, "notificationFrame") or self.notificationFrame is None:
            self.notificationFrame = ctk.CTkFrame(
                self.backFrame,
                fg_color="#E7E7E7",
                bg_color="#ffffff",
                corner_radius=10,
                border_color="#8B8989",
                border_width=1,
            )


            ctk.CTkLabel(
                self.notificationFrame,
                text="Notifications",
                text_color="black",
                font=("Ubuntu", 15, "bold"),
                width=350,
                anchor="w",
            ).pack(padx=(20, 5), pady=5)


            self.notification_scrl = ctk.CTkScrollableFrame(
                self.notificationFrame, fg_color="#E7E7E7", width=346, height=400
            )
            self.notification_scrl.pack(side="top", expand=True)


        for child in getattr(self, "notification_scrl", []).winfo_children():
            if isinstance(child, ctk.CTkLabel) and child.cget("text") == "No Notifications":
                child.destroy()


        notif_label = ctk.CTkLabel(
            self.notification_scrl,
            text=message,
            fg_color="#FFFFFF",
            text_color="#000000",
            corner_radius=6,
            wraplength=300,
            justify="left",
            anchor="w",
        )
        notif_label.pack(pady=5, padx=10, fill="x")


        if not getattr(self, "notification_visible", False):
            self.notificationFrame.place(relx=1.0, rely=0.0, anchor="ne", y=55, x=-20)
            self.notification_visible = True


    def clear_frame(self):
        for widget in self.contentFrame.winfo_children():
            widget.destroy()



