import customtkinter as ctk

def format_output(number):
    print(number)
    if number.is_integer():
        number = int(number)
    if number > 1e6 or number < -1e6:
        number = f"{number:.2e}"
    elif number < 1e-6 and number != 0 and number > -1e-6:
        number = f"{number:.2e}"
    return number

def clear_output():
    output.delete(0, "end")
    output.configure(placeholder_text="0")

def calculate():
    output.insert("end", "\n")
    equation_string = output.get()
    num1 = None
    num2 = 0
    last_operator = None
    for char in equation_string:
        if char in "0123456789.":
            if num1 is None:
                num1 = char
            else:
                num1 += char
        elif char in "+-*/^\n":
            if last_operator is None:
                if num1 is not None:
                    num2 = float(num1)
                    num1 = None
                last_operator = char
            elif last_operator is not None and num1 is not None:
                if last_operator == "+":
                    num2 += float(num1)
                elif last_operator == "-":
                    num2 -= float(num1)
                elif last_operator == "*":
                    num2 *= float(num1)
                elif last_operator == "/":
                    if num1 == "0":
                        output.delete(0, "end")
                        output.configure(placeholder_text="Undefined")
                        return
                    num2 /= float(num1)
                elif last_operator == "^":
                    num2 **= float(num1)
        else:
            output.delete(0, "end")
            output.configure(placeholder_text="Invalid input")
            return
    
    output.delete(0, "end")

    num2 = format_output(num2)

    output.insert("end", num2)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Calc")

window.geometry("380x420")
window.resizable(False, False)

window.grid_columnconfigure((0, 1, 2, 3), weight=1)

output = ctk.CTkEntry(window, placeholder_text="0", width=360, height=70, font=("Arial", 30))
output.grid(row=0, column=0, columnspan=4, pady=(15, 0), padx=(0, 0))

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "^", "+",
    "C", "()", "del", "="
]

row = 1
col = 0
for button in buttons:
    if button == "C":
        ctk.CTkButton(window, text=button, width=80, height=50, font=("Arial", 30), command=clear_output).grid(row=row, column=col, padx=(0, 0), pady=(15, 0))
    elif button == "=":
        ctk.CTkButton(window, text=button, width=80, height=50, font=("Arial", 30), command=calculate).grid(row=row, column=col, padx=(0, 0), pady=(15, 0))
    elif button == "del":
        ctk.CTkButton(window, text=button, width=80, height=50, font=("Arial", 30), command=lambda: output.delete(len(output.get()) - 1, "end")).grid(row=row, column=col, padx=(0, 0), pady=(15, 0))
    elif button == "()":
        ctk.CTkButton(window, text=button, width=80, height=50, font=("Arial", 30)).grid(row=row, column=col, padx=(0, 0), pady=(15, 0))
    else:
        ctk.CTkButton(window, text=button, width=80, height=50, font=("Arial", 30), command=lambda x=button: output.insert("end", x)).grid(row=row, column=col, padx=(0, 0), pady=(15, 0))
        
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
