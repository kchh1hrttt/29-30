import os
from gui import root
from CTkMessagebox import CTkMessagebox

if __name__ == '__main__':
    os.open('run.bat')
    CTkMessagebox(title='Сообщение', message='Открыть файл ReadMe?', icon='question',
                  option_1='Да', option_2='Нет', option_3='Да')
    root.mainloop()
