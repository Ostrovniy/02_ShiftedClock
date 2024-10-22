import re
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from datetime import datetime, timedelta

root = Tk()
root.geometry('408x390')
root.title('Сдвинутые часы')
root.configure(background='#1E1E1E')
root.resizable(False, False)

# Стиль Фрейма контейнера
frame_time_label_style = ttk.Style()
frame_time_label_style.configure("FrameTime.TLabel", font=("Arial", 72, "bold"), foreground="#F5F5F5", padding=6, background="#1E1E1E")

# Стиля Блок к часами
time_label_style = ttk.Style()
time_label_style.configure("Time.TLabel", font=("Arial", 72, "bold"), foreground="#F5F5F5", padding=6, background="#1E1E1E", relief='solid')

# Стиль заголовка времени   
time_label_style = ttk.Style()
time_label_style.configure("TitleTime.TLabel", font=("Arial", 10), foreground="#F5F5F5", background="#1E1E1E")

# Стиль Input времени
label_style = ttk.Style()
label_style.configure("Input.TLabel", foreground="#FFFFFF", background="#333333", padding=(5, 5, 5, 5), insertcolor="#00FF00")

# Стиль Кнопка
btn_style = ttk.Style()
btn_style.configure("BTN.TLabel", foreground="#FFFFFF", background="#333333", padding=(5, 5, 5, 5), relief='flat')


# Пременная в которой будет время когда человек проснулся
click_time = StringVar(value='7:00')

# Валидации времени по формату , "%H:%M"
def validate_time_string(str_time):
    # проверка по регулярному выражению
    pattern = r"^([01]?[0-9]|2[0-4]):([0-5]?[0-9])$"
    match = re.match(pattern, str_time)
    return bool(match)

# Функция обновления таймеров
def tick():
    # Запустить авто повторение каждую секунду
    now_time.after(1000, tick)
    # Получить текущее время
    current_time = datetime.now()
    # Отформатировать текущее время в формат 12:45:56
    formatted_time = current_time.strftime('%H:%M:%S')
    # Лейблу текущее время обновить текст
    now_time['text'] = formatted_time
    # Время когда человек проснулся через связанную переменную
    time_to_subtract = click_time.get()
    # Преобразовать строку в минуты и часы в фиде числа
    hours, minutes = map(int, time_to_subtract.split(':'))
    # Создание обьекта времени (Когда человек проснулся)
    time_delta = timedelta(hours=hours, minutes=minutes)
    # Вычиатния разницы во времени Текущее время - (Время когда проснулся - 7 утра)
    new_time_data = current_time - ( time_delta - timedelta(hours=7, minutes=0) )
    # Форматируем полученую разницу во времени
    formatted_new_time_data = new_time_data.strftime('%H:%M:%S')
    # Лейблу Со смещенным временем обновляем время
    sdwig_time['text'] = formatted_new_time_data

# Обработчик нажатия кнопки
def un_data_new_time():
    # Получить данные с поля ввода времени
    new_sdvig = input_entry.get()
    # Проверка что польвоматель ввел валиднове время
    if validate_time_string(new_sdvig):
        # Обновить связанную переменную, время когда человек проснулся
        click_time.set(new_sdvig)
    else:
        showinfo('Неверный формат времени', 'Введите время в формате "12:00" или "15:45"')

# Оболочка для всех компонентов borderwidth=1,
frame = ttk.Frame(borderwidth=0, style="FrameTime.TLabel")
frame.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

# Установка минимального размера для фрейма
frame.update_idletasks()
frame_width = frame.winfo_reqwidth()
frame_height = frame.winfo_reqheight()
frame.config(width=frame_width, height=frame_height)

# input фрейм для ввода и кнопки
input_frame = ttk.Frame(borderwidth=0, style="FrameTime.TLabel")
input_frame.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")


# Текущее время заголовок
now_time_title = ttk.Label(frame, text='Текущее время', style="TitleTime.TLabel")
now_time_title.pack(anchor="w")

# Текущее время
now_time = ttk.Label(frame, text='00:00:00', style="Time.TLabel")
now_time.pack(anchor="w")

# Заголовок Время со смещением
sdwig_time_title = ttk.Label(frame, text='Время если бы вы проснулись в 7:00 утра', style="TitleTime.TLabel")
sdwig_time_title.pack(anchor="w")

# Время со смещением
sdwig_time = ttk.Label(frame, text='00:00:01', style="Time.TLabel")
sdwig_time.pack(anchor="w")

# Текст для инпута времени
input_text = ttk.Label(input_frame, text='Время когда вы простулись: (12:45)', style="TitleTime.TLabel")
input_text.grid(column=0, row=0)

# Поле ввода времени когда человек проснулся
input_entry = ttk.Entry(input_frame, style='Input.TLabel', font=("Arial", 16))
input_entry.grid(column=0, row=1, padx=(5,0), columnspan=3, sticky='ew')

# Кнопка сохарнении времени когда человек проснулся
save_btn = ttk.Button(input_frame, text='Обновить часы', command=un_data_new_time, style='BTN.TLabel')
save_btn.grid(column=3, row=1, padx=8, sticky='ewns')

tick()

root.mainloop()