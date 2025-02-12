import tkinter as tk

hundreds = {
    "сто": 100,
    "двести": 200,
    "триста": 300,
    "четыреста": 400,
    "пятьсот": 500,
    "шестьсот": 600,
    "семьсот": 700,
    "восемьсот": 800,
    "девятьсот": 900
}

teens = {
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19
}

tens = {
    "десять": 10,
    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90
}

ones = {
    "ноль": 0,
    "один": 1,
    "два": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9
}


def normalize_input(s):
    return s.lower().strip()


def convert_text_to_number():
    input_text = entry.get()
    words = normalize_input(input_text).split()
    total = 0
    last_number_type = None
    has_hundreds = False
    has_tens = False
    has_teens = False
    has_ones = False

    for word in words:
        if word in hundreds:
            if has_ones:
                result_label.config(text="Ошибка: После единиц не могут идти сотни.")
                return
            if has_tens:
                result_label.config(text="Ошибка: После десятков не могут идти сотни.")
                return
            if has_hundreds:
                result_label.config(text="Ошибка: Две сотни не могут идти подряд.")
                return
            if has_teens:
                result_label.config(text="Ошибка: После чисел от 11 до 19 не могут идти сотни.")
                return
            total += hundreds[word]
            has_hundreds = True
            last_number_type = "hundreds"

        elif word in teens:
            if has_teens:
                result_label.config(text="Ошибка: Нельзя использовать два числа от 11 до 19 подряд.")
                return
            if has_tens or has_ones:
                result_label.config(text="Ошибка: Числа от 11 до 19 должны быть самостоятельными или идти после сотен.")
                return
            total += teens[word]
            has_teens = True
            last_number_type = "teens"

        elif word in tens:
            if has_ones:
                result_label.config(text="Ошибка: После единиц не могут идти десятки.")
                return
            if has_tens:
                result_label.config(text="Ошибка: Два десятичных формата не могут идти подряд.")
                return
            if has_teens:
                result_label.config(text="Ошибка: После чисел от 11 до 19 не может идти десятичный формат.")
                return
            total += tens[word]
            has_tens = True
            last_number_type = "tens"

        elif word in ones:
            # Проверка: если идет первая единица
            if has_ones:
                result_label.config(text="Ошибка: Два единичных формата не могут идти подряд.")
                return
            if has_teens:
                result_label.config(text="Ошибка: После чисел от 11 до 19 не может идти едичный формат.")
                return
            has_ones = True
            last_number_type = "ones"
            total += ones[word]

        else:
            result_label.config(text=f"Ошибка: '{word}' не распознано.")
            return

    if total > 0 or (len(words) == 1 and words[0] == "ноль"):
        result_label.config(text=f"Число: {total}")
    else:
        result_label.config(text="Ошибка: Число не найдено.")

# Инициализация графического интерфейса
root = tk.Tk()
root.title("Преобразование русских чисел в числа")
root.geometry("600x200")

entry_label = tk.Label(root, text="Введите строку:", font=15)
entry_label.pack()
entry = tk.Entry(root, width=50)
entry.pack()
process_button = tk.Button(root, text="Преобразовать", command=convert_text_to_number, font=15)
process_button.pack()
result_label = tk.Label(root, text="Число: ", font=20)
result_label.pack()

root.mainloop()
