import tkinter as tk
import re
from functools import partial
from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkFont, CTkToplevel

class Login():
    def create_menu_screen(self, callback):
        self._create_menu = callback

    def create_login_screen(self, tela_principal):
        CTkLabel(
            tela_principal,
            text="Seja Bem Vindo ao Coletor!",
            text_color="#F2F2F2",
            font=("Roboto", 25, "bold")
        ).pack(side="top", pady=(60, 0))
        
        CTkLabel(
            tela_principal,
            text="Login",
            text_color="#F2F2F2",
            font=("Roboto", 20, "bold")
        ).pack(side="top", pady=(60, 20))
        
        self.login = CTkEntry(
            tela_principal,
            width=200,
            placeholder_text="E-mail",
            fg_color="#F2F2F2",
            text_color="#000"
        )
        self.login.pack(side="top", pady=(10, 10))
        
        self.password = CTkEntry(
            tela_principal,
            width=200,
            placeholder_text="Password",
            show="*",
            fg_color="#F2F2F2",
            text_color="#000"
        )
        self.password.pack(side="top", pady=0)
        
        CTkButton(
            tela_principal,
            text="LOGIN",
            width=150,
            font=CTkFont(weight="bold"),
            command=self._login
        ).pack(side="top", pady=(20, 0))
        
    def _login(self, event=None):
        (is_valid, self.email, password) = self._validate_login()
        if is_valid:
            self._create_menu()
        else:
            self.popup_error()

    def popup_error(self):
        message = "Wrong E-mail or Password!"
        popup = CTkToplevel()
        popup.title("Login Error")
        popup.configure(bg="#333333")
        popup.geometry("300x150")
        popup.protocol(
            "WM_DELETE_WINDOW",
            lambda: popup.destroy,
        )
        CTkLabel(popup, text=message, text_color="#F2F2F2", font=CTkFont(weight="bold")).pack(pady=(30, 20))
        CTkButton(
            popup,
            text="BACK TO LOGIN",
            width=150,
            command=popup.destroy
        ).pack(pady=20)

        self.center_popup(popup)
        popup.lift()
        popup.grab_set()
        popup.focus_force()
        
    def center_popup(self, window, width=300, height=200):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")
            
        
    def _validate_login(self):
        email_pattern = r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$'
        email = self.login.get()
        passwd = self.password.get()

        if not re.match(email_pattern, email) or not email:
            return False, None, None
        if not passwd:
            return False, None, None
        return True, email, passwd
    
    