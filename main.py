import tkinter as tk
from utils.center_window import center_window
from authActivity.backend.UserAccount import UserAccount
from authActivity.frontend.auth import Auth
from authActivity.frontend.bar import Bar
# from authActivity.frontend.main_content.page_content import PageContent

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Schedule Management System")
        center_window(self, 1500, 900)
        self.user_account = UserAccount()
        # Create both frames, but only show one at a time
        self.auth_frame = Auth(self, user_account=self.user_account, on_login_success=self.show_dashboard)
        self.bar_frame = Bar(self, backend=self.user_account, on_logout=self.show_auth)


    def show_dashboard(self):
        self.auth_frame.pack_forget()
        self.bar_frame.destroy()
        self.bar_frame = Bar(self, backend=self.user_account, on_logout=self.show_auth)
        self.bar_frame.pack(fill="both", expand=True)
        self.bar_frame.bar_topFrame() # if you want sidebar content


    def show_auth(self):
        self.bar_frame.pack_forget()
        self.auth_frame.destroy()
        self.auth_frame = Auth(self, user_account=self.user_account, on_login_success=self.show_dashboard)
        self.auth_frame.pack(fill="both", expand=True)

def main():
    app = MyApp()
    app.mainloop()

if __name__ == "__main__":
    main()
