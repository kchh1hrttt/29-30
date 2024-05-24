import gui
from PIL import Image
from customtkinter import *


def switch_theme():
    theme = get_appearance_mode()
    if theme == 'Light':
        next_theme = 'Dark'
        icon_name = 'sun.png'
    else:
        next_theme = 'Light'
        icon_name = 'moon.png'
    gui.switch_theme_btn.configure(image=CTkImage(Image.open(f'./icons/{icon_name}')))
    set_appearance_mode(next_theme)


def test():
    theme = get_appearance_mode()
    if theme == 'Light:':
        icon_name = 'moon.png'
    else:
        icon_name = 'sun.png'
    image = CTkImage(Image.open(f'./icons/{icon_name}'))
    print(theme)
    return image


def switch_to_reg_frame():
    gui.main_frame.pack_forget()
    gui.reg_frame.pack(fill=BOTH, expand=True)


def switch_to_main_frame():
    gui.reg_frame.pack_forget()
    gui.main_frame.pack(fill=BOTH, expand=True)


def reg_clck():
    gui.main_frame.pack_forget()
    gui.reg_frame.pack(fill=BOTH, expand=True)


def done_reg_clck():
    pass


# fill=BOTH, expand=True
