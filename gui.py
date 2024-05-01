from customtkinter import *
import func

root = CTk()
root.title('Hello World!!!')
root.geometry('700x500')
root.resizable(width=False, height=False)

main_frame = CTkFrame(root)
main_frame.pack(fill=BOTH, expand=True)

hello_lbl = CTkLabel(main_frame, text='Привет, аноним!', font=('Montserrat', 55), text_color='#7B68EE')
hello_lbl.pack(anchor=CENTER, pady=125)

log_in_btn = CTkButton(main_frame, text='Войти', width=250, height=50)
log_in_btn.pack()

reg_btn = CTkButton(main_frame, text='Зарегистрироваться', width=200, height=35, command=func.reg_clck)
reg_btn.pack(pady=12)

reg_frame = CTkFrame(root)

btn = CTkButton(reg_frame, text='qq')
btn.pack()





# fill=BOTH, expand=True