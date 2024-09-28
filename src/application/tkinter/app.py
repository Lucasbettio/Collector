import os
import sys
import tkinter as tk
import customtkinter
from customtkinter import CTkButton

from src.application.tkinter.components.login.login import Login
from src.application.tkinter.components.menu.menu import Menu

class Application:
    def __init__(self):
        self.tela_principal = customtkinter.CTk()
        self.tela_principal.protocol("WM_DELETE_WINDOW", self.close_window)
        self._create_components()
        
    def _create_components(self):
        self._login_component = Login()
        self._menu_component = Menu()

    def center_window(self, window, width=568, height=588):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")
    
    def close_window(self):
        self.tela_principal.destroy()
    
    def _set_screen(self):
        self.tela_principal.title("Automatized Collect")
        self.tela_principal.configure(background="#333333")
        self.tela_principal.geometry("568x588")
        self.center_window(self.tela_principal)
        self.tela_principal.resizable(False, False)
        customtkinter.set_default_color_theme("green")

    def _destroy_children(self):
        for i in self.tela_principal.winfo_children():
            i.destroy()

    def _login_screen(self):
        self._destroy_children()
        self._login_component.create_menu_screen(self._menu_screen)
        self._login_component.create_login_screen(self.tela_principal)
    
    def _menu_screen(self):
        self._destroy_children()
        self._menu_component.create_menu_screen(self.tela_principal)

    def run_app(self):
        self._set_screen()
        self._login_screen()
        self.tela_principal.mainloop() 