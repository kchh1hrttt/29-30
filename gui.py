from CTkMessagebox import CTkMessagebox
from idlelib.tooltip import Hovertip
from customtkinter import *
import func
import os


root = CTk()
root.title('Hello World!!!')
root.geometry('700x500')
root.resizable(width=False, height=False)
lbl_font = 'Montserrat', 16
readme_msg = CTkMessagebox(title='Сообщение', message='Открыть файл ReadMe?', icon='question',
                           option_1='Да', option_2='Нет', option_3='Да')
if readme_msg.get() == 'Да':
    os.startfile('readme.txt')

main_frame = CTkFrame(root)
main_frame.pack(fill=BOTH, expand=True)

hello_lbl = CTkLabel(main_frame, text='Привет, аноним!', font=('Montserrat', 55), text_color='#7B68EE')
hello_lbl.pack(anchor=CENTER, pady=125)

log_in_btn = CTkButton(main_frame, text='Войти', width=250, height=50, state=DISABLED)
log_in_btn.pack()

reg_btn = CTkButton(main_frame, text='Зарегистрироваться', width=200, height=35, command=func.switch_to_reg_frame)
reg_btn.pack(pady=12)

reg_frame = CTkFrame(root)
root.configure(width=30, height=30)

email_lbl = CTkLabel(reg_frame, text='E-mail:', font=lbl_font)
email_lbl.place(x=17, y=20)
email_ent = CTkEntry(reg_frame, width=485)
email_ent.place(x=200, y=20)
Hovertip(email_ent, text='Ваша электронная почта, на которую будут приходить наши рассылки и коды подтверждений')

psw_lbl = CTkLabel(reg_frame, text='Пароль:', font=lbl_font)
psw_lbl.place(x=17, y=60)
psw_ent = CTkEntry(reg_frame, width=485)
psw_ent.place(x=200, y=60)
Hovertip(psw_ent, text='Секретное слово для защиты вашей учётной записи')

confirm_psw_lbl = CTkLabel(reg_frame, text='Повторите пароль:', font=lbl_font)
confirm_psw_lbl.place(x=17, y=100)
confirm_psw_ent = CTkEntry(reg_frame, width=485)
confirm_psw_ent.place(x=200, y=100)
Hovertip(confirm_psw_ent, text='Повторите ваше секретное слово')

legal_entity_lbl = CTkLabel(reg_frame, text='Юридическое лицо:', font=lbl_font)
legal_entity_lbl.place(x=17, y=140)
legal_entity_cbox = CTkCheckBox(reg_frame, text='', fg_color='green', hover_color='green')
legal_entity_cbox.place(x=200, y=143)
Hovertip(legal_entity_cbox, text='Ткните для подтверждения')

surname_lbl = CTkLabel(reg_frame, text='Фамилия:', font=lbl_font)
surname_lbl.place(x=17, y=180)
surname_ent = CTkEntry(reg_frame, width=485)
surname_ent.place(x=200, y=180)

first_name_lbl = CTkLabel(reg_frame, text='Имя:', font=lbl_font)
first_name_lbl.place(x=17, y=220)
first_name_ent = CTkEntry(reg_frame, width=485)
first_name_ent.place(x=200, y=220)

middle_name_lbl = CTkLabel(reg_frame, text='Отчество:', font=lbl_font)
middle_name_lbl.place(x=17, y=260)
middle_name_ent = CTkEntry(reg_frame, width=485)
middle_name_ent.place(x=200, y=260)

full_name_lbl = CTkLabel(reg_frame, text='Полное имя:', font=lbl_font)
full_name_lbl.place(x=17, y=300)
full_name_ent = CTkEntry(reg_frame, width=485)
full_name_ent.place(x=200, y=300)

reg_btn = CTkButton(reg_frame, text='Готово', width=140, height=60)
reg_btn.place(x=280, y=370)

back_btn = CTkButton(reg_frame, text='← Назад', width=10, height=30,
                     command=func.switch_to_main_frame)
back_btn.place(x=318, y=450)

switch_theme_btn = CTkButton(root, text='', fg_color='#708090', hover_color='#778899',
                             width=10, height=10,
                             image=func.test(), command=func.switch_theme)
switch_theme_btn.place(x=6, y=468)
# fill=BOTH, expand=True
