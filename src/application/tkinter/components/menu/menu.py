import tkinter as tk
import re
from functools import partial
from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkFont

class Menu():
    def create_settings_screen(self, callback):
        self._create_menu = callback

    def create_menu_screen(self, tela_principal):
        CTkLabel(
            tela_principal,
            text="Menu Screen!",
            text_color="#F2F2F2",
            font=("Roboto", 25, "bold")
        ).pack(side="top", pady=(60, 0))
