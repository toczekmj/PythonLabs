import tkinter as tk
from tkinter import StringVar, Button, Entry
import tkinter.font as font
okno = tk.Tk()
okno.title("Calculator")

myFont = font.Font(family='Arial', size=20, weight='bold')

ans_entry =  Entry(okno, bd=5, width=20, font=myFont, bg="gray", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)

# przykładowy pierwszy Button
btn_1 = Button(okno, text="1", padx=20, pady=10)
btn_1['font'] = myFont
btn_1.grid(row=1, column=0)

btn_2 = Button(okno, text="2", padx=20, pady=10)
btn_2['font'] = myFont
btn_2.grid(row=1, column=1)

btn_3 = Button(okno, text="3", padx=20, pady=10)
btn_3['font'] = myFont
btn_3.grid(row=1, column=2)

btn_4 = Button(okno, text="4", padx=20, pady=10)
btn_4['font'] = myFont
btn_4.grid(row=2, column=0)

btn_5 = Button(okno, text="5", padx=20, pady=10)
btn_5['font'] = myFont
btn_5.grid(row=2, column=1)

btn_6 = Button(okno, text="6", padx=20, pady=10)
btn_6['font'] = myFont
btn_6.grid(row=2, column=2)

btn_7 = Button(okno, text="7", padx=20, pady=10)
btn_7['font'] = myFont
btn_7.grid(row=3, column=0)

btn_8 = Button(okno, text="8", padx=20, pady=10)
btn_8['font'] = myFont
btn_8.grid(row=3, column=1)

btn_9 = Button(okno, text="9", padx=20, pady=10)
btn_9['font'] = myFont
btn_9.grid(row=3, column=2)

btn_0 = Button(okno, text="0", padx=20, pady=10)
btn_0['font'] = myFont
btn_0.grid(row=4, column=1)

btn_add = Button(okno, text="+", padx=20, pady=10)
btn_add['font'] = myFont
btn_add.grid(row=4, column=3)

btn_sub = Button(okno, text="-", padx=20, pady=10)
btn_sub['font'] = myFont
btn_sub.grid(row=3, column=3)

btn_sub = Button(okno, text="-=", padx=20, pady=10)
btn_sub['font'] = myFont
btn_sub.grid(row=3, column=4)

btn_mul = Button(okno, text="*", padx=20, pady=10)
btn_mul['font'] = myFont
btn_mul.grid(row=2, column=3)

btn_div = Button(okno, text="/", padx=20, pady=10)
btn_div['font'] = myFont
btn_div.grid(row=1, column=3)

btn_eq = Button(okno, text="=", padx=20, pady=10)
btn_eq['font'] = myFont
btn_eq.grid(row=4, column=2)

btn_C = Button(okno, text="C", padx=20, pady=10)
btn_C['font'] = myFont
btn_C.grid(row=4, column=0)

temp1 = None
temp2 = None
operation = None


def mouse_button_release(event):
    global temp1, temp2, operation
    widg = event.widget
    text = widg.cget("text")

    if text == "-=":
        t = ans_entry.get()
        ans_entry.delete(0, "end")
        ans_entry.insert(len(ans_entry.get()), str(int(t) * -1))
        temp1 = int(ans_entry.get())
        temp2 = None

    if text in "0123456789":
        ans_entry.delete(0, "end")
        ans_entry.insert(len(ans_entry.get()), text)

    if text in "+-*/":
        if len(ans_entry.get()) == 0:
            return
        if temp1 is None and temp2 is None:
            temp1 = ans_entry.get()
        else:
            temp2 = ans_entry.get()
        ans_entry.delete(0, "end")
        ans_entry.insert(len(ans_entry.get()), text)
        operation = text

    if text == "C":
        operation = None
        temp1 = None
        temp2 = None
        ans_entry.delete(0, "end")

    if text == "=":
        temp2 = int(ans_entry.get())
        temp1 = int(temp1)
        ans_entry.delete(0, "end")
        result = 0

        if operation == "" or operation is None:
            return
        elif operation == "+":
            result = temp1 + temp2
        elif operation == "-":
            result = temp1 - temp2
        elif operation == "*":
            result = temp1 * temp2
        elif operation == "/":
            result = temp1 / temp2
        ans_entry.insert(len(ans_entry.get()), str(result))
        temp1 = result
        temp2 = None


okno.bind("<ButtonRelease-1>", mouse_button_release)
okno.mainloop()
