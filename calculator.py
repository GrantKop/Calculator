import customtkinter as ctk

expression = ""

def on_button_click(char):
    global expression
    if char == 'C':
        expression = ""
        output.delete(0, ctk.END)
    elif char == '=':
        try:
            result = eval(expression)
            output.delete(0, ctk.END)
            if result == float('inf') or result == float('-inf'):
                output.insert(ctk.END, "Error: Overflow")
            else:
                output.insert(ctk.END, f"{result:.10g}")
        except ZeroDivisionError:
            output.delete(0, ctk.END)
            output.insert(ctk.END, "Error: Undefined")
            expression = ""
        except Exception:
            output.delete(0, ctk.END)
            output.insert(ctk.END, "Error")
            expression = ""
    else:
        expression += str(char)
        output.delete(0, ctk.END)
        output.insert(ctk.END, expression)
        

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Calc")

window.geometry("380x420")
window.resizable(False, False)

window.grid_columnconfigure((0, 1, 2, 3), weight=1)

output = ctk.CTkEntry(window, placeholder_text="0", width=360, height=70, font=("Arial", 30), justify="right")
output.grid(row=0, column=0, columnspan=4, pady=(15, 0), padx=(0, 0))

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "^", "+",
    "C", "(", ")", "="
]

row = 1
col = 0
for button in buttons:
    ctk.CTkButton(window, text=button, width=80, height=50, font=("Arial", 30),
                  command=lambda b=button: on_button_click(b)).grid(row=row, column=col, padx=(0, 0), pady=(15, 0))

    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
