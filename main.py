from tkinter import *
from tkinter import  ttk

#Задание №1 ->

window = Tk()
window.title("Регистрация")
window.geometry("800x400")
window.resizable(False, False)
window.configure(bg="black")

name = ""
email = ""
login = ""
phone = ""
password = ""

def get_data():
    name = full_name_entry.get()
    email = email_entry.get()
    login = login_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()

    print(f"Name -> {name}\nEmail -> {email}\nLogin -> {login}\nPhone -> {phone}\nPassword -> {password}")

full_name_label = ttk.Label(window, text="Full name", width=15, background='black',foreground='white')
full_name_label.place(x=50, y=10)

full_name_entry = ttk.Entry(window, width=98)
full_name_entry.place(x=50, y=40)

email_label = ttk.Label(window, text="E-mail", width=15, background='black',foreground='white')
email_label.place(x=50, y=90)

email_entry = ttk.Entry(window, width=48)
email_entry.place(x=50, y=120)

login_label = ttk.Label(window, text="Login", width=15, background='black',foreground='white')
login_label.place(x=50, y=170)

login_entry = ttk.Entry(window, width=48)
login_entry.place(x=50, y=200)

phone_label = ttk.Label(window, text="Phone", width=15, background='black',foreground='white')
phone_label.place(x=350, y=90)

phone_entry = ttk.Entry(window, width=48)
phone_entry.place(x=350, y=120)

password_label = ttk.Label(window, text="Password", width=15, background='black',foreground='white')
password_label.place(x=350, y=170)

password_entry = ttk.Entry(window, width=48, show="*")
password_entry.place(x=350, y=200)

submit_button = Button(window, text="Submit", command=get_data, bg="orange")
submit_button.place(x=50, y=250, width=190, height=40)

#Задание №2 ->

from tkinter import messagebox

def is_int(s):
    return s.lstrip('-+').isdigit()

def parse_array(s):
    s = s.strip()

    if s.startswith('[') and s.endswith(']'):
        s = s[1:-1].strip()

    if not s:
        return []

    parts = [p.strip() for p in s.split(',')]

    int_list = []

    for item in parts:
        if item == '':
            messagebox.showerror("Ошибка", "Пустой элемент в списке")
            return None

        if is_int(item):
            int_list.append(int(item))
        else:
            messagebox.showerror("Ошибка", f"Элемент '{item}' не является целым числом")
            return None
    return int_list

def calculate():
    array1 = parse_array(entry1.get())
    array2 = parse_array(entry2.get())

    if array1 is None or array2 is None:
        return

    if len(array1) != len(array2):
        messagebox.showerror("Ошибка", "Длины массивов должны совпадать")
        return

    result = []
    for i in range(len(array1)):
        result.append(array1[i] * array2[i])

    label_result.config(text=str(result))

root = Tk()
root.title("Произведение массивов")
root.geometry("800x400")
root.configure(bg="black")

label1 = Label(root, text="Первый массив:", bg="black", fg="white")
label1.grid(row=0, column=0, padx=10, pady=10, sticky='e')

entry1 = Entry(root, width=50, bg="gray20", fg="white", insertbackground="white")
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = Label(root, text="Второй массив:", bg="black", fg="white")
label2.grid(row=1, column=0, padx=10, pady=10, sticky='e')

entry2 = Entry(root, width=50, bg="gray20", fg="white", insertbackground="white")
entry2.grid(row=1, column=1, padx=10, pady=10)

btn = Button(root, text="Вычислить", command=calculate, bg="#FFA500", fg="black")
btn.grid(row=2, column=0, columnspan=2, pady=20, ipadx=100)

label_result_text = Label(root, text="Результат:", bg="black", fg="white")
label_result_text.grid(row=3, column=0, padx=10, pady=10, sticky='e')

label_result = Label(root, text="тут должен быть результат", bg="black", fg="white")
label_result.grid(row=3, column=1, padx=10, pady=10, sticky='w')

root.mainloop()
window.mainloop()