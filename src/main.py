import os
import sys
import tkinter as tk
import math_lib

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_all()
        text_result.insert(1.0, "Error")


def clear_all():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def delete_last_char():
    pass

root = tk.Tk()
root.title('Calculator')
root.geometry("365x420")

text_result = tk.Text(root, height=3, width=20, font=("Arial", 24), fg="white", bg="gray")
text_result.grid(columnspan=5)

btn_sin = tk.Button(root, text="sin", command=lambda: add_to_calculation("sin("), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_sin.grid(row=4, column=0, padx=0, pady=2)
btn_cos = tk.Button(root, text="cos", command=lambda: add_to_calculation("cos("), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_cos.grid(row=4, column=1, padx=0, pady=2)
btn_tan = tk.Button(root, text="tan", command=lambda: add_to_calculation("tan("), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_tan.grid(row=4, column=2, padx=0, pady=2)
btn_log = tk.Button(root, text="log", command=lambda: add_to_calculation("log("), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_log.grid(row=4, column=3, padx=0, pady=2)
btn_ln = tk.Button(root, text="ln", command=lambda: add_to_calculation("ln("), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_ln.grid(row=4, column=4, padx=0, pady=2)

btn_x2 = tk.Button(root, text="x^2", command=lambda: add_to_calculation("x"), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_x2.grid(row=5, column=0, padx=0, pady=2)
btn_1x = tk.Button(root, text="1/x", command=lambda: add_to_calculation("x"), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_1x.grid(row=5, column=1, padx=0, pady=2)
btn_abs = tk.Button(root, text="|x|", command=lambda: add_to_calculation("x"), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_abs.grid(row=5, column=2, padx=0, pady=2)
btn_x3 = tk.Button(root, text="x^3", command=lambda: add_to_calculation("x"), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_x3.grid(row=5, column=3, padx=0, pady=2)
btn_10x = tk.Button(root, text="10^x", command=lambda: add_to_calculation("x"), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_10x.grid(row=5, column=4, padx=0, pady=2)

btn_sqrt = tk.Button(root, text="sqrt(x)", command=lambda: add_to_calculation("x"), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_sqrt.grid(row=6, column=0, padx=0, pady=2)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_open.grid(row=6, column=1, padx=0, pady=2)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_close.grid(row=6, column=2, padx=0, pady=2)
btn_mod = tk.Button(root, text="mod", command=lambda: add_to_calculation("x"), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_mod.grid(row=6, column=3, padx=0, pady=2)
btn_fact = tk.Button(root, text="n!", command=lambda: add_to_calculation("!"), width=5, font=("Arial", 14), fg="white", bg="#465657")
btn_fact.grid(row=6, column=4, padx=0, pady=2)


btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14), fg="white", bg="black")
btn_7.grid(row=7, column=0, padx=0, pady=2)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14), fg="white", bg="black")
btn_8.grid(row=7, column=1, padx=0, pady=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14), fg="white", bg="black")
btn_9.grid(row=7, column=2, padx=0, pady=2)
btn_clr = tk.Button(root, text="DEL", command=delete_last_char, width=5, font=("Arial", 14), fg="white", bg="#de7700")
btn_clr.grid(row=7, column=3, padx=0, pady=2)
btn_backspace = tk.Button(root, text="AC", command=clear_all, width=5, font=("Arial", 14), fg="white", bg="#de7700")
btn_backspace.grid(row=7, column=4, padx=0, pady=2)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14), fg="white", bg="black")
btn_4.grid(row=8, column=0, padx=0, pady=2)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14), fg="white", bg="black")
btn_5.grid(row=8, column=1, padx=0, pady=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14), fg="white", bg="black")
btn_6.grid(row=8, column=2, padx=0, pady=2)
btn_mul = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14), fg="white", bg="black")
btn_mul.grid(row=8, column=3, padx=0, pady=2)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14), fg="white", bg="black")
btn_div.grid(row=8, column=4, padx=0, pady=2)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14), fg="white", bg="black")
btn_1.grid(row=9, column=0, padx=0, pady=2)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14), fg="white", bg="black")
btn_2.grid(row=9, column=1, padx=0, pady=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14), fg="white", bg="black")
btn_3.grid(row=9, column=2, padx=0, pady=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14), fg="white", bg="black")
btn_plus.grid(row=9, column=3, padx=0, pady=2)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14), fg="white", bg="black")
btn_minus.grid(row=9, column=4, padx=0, pady=2)

btn_pi = tk.Button(root, text="PI", command=lambda: add_to_calculation(math_lib.pi), width=5, font=("Arial", 14), fg="white", bg="black")
btn_pi.grid(row=10, column=0, padx=0, pady=2)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14), fg="white", bg="black")
btn_0.grid(row=10, column=1, padx=0, pady=2)
btn_e = tk.Button(root, text="e", command=lambda: add_to_calculation(math_lib.e), width=5, font=("Arial", 14), fg="white", bg="black")
btn_e.grid(row=10, column=2, padx=0, pady=2)
btn_dot = tk.Button(root, text=".", command=lambda: add_to_calculation("x"), width=5, font=("Arial", 14), fg="white", bg="black")
btn_dot.grid(row=10, column=3, padx=0, pady=2)
btn_eval = tk.Button(root, text="=", command=evaluate, width=5, font=("Arial", 14), fg="white", bg="#17aee2")
btn_eval.grid(row=10, column=4, padx=0, pady=2)

root.mainloop()
