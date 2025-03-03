from tkinter import *

WINDOW_WIDTH = 300
WINDOWS_HEIGHT = 100
FONT = ("Ariel", 20)


window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=WINDOW_WIDTH, height=WINDOWS_HEIGHT)


# Labels
miles_text_label = Label(text="Miles", font=FONT)
miles_text_label.config(padx=20)
miles_text_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.config(padx=20)
is_equal_to_label.grid(row=1, column=0)

miles_num_label = Label(text="0", font=FONT)
miles_num_label.grid(row=1, column=1)

km_text_label = Label(text="Km", font=FONT)
km_text_label.grid(row=1, column=2)


# Entry
user_input = Entry(width=10)
user_input.insert(END, string="0")
user_input.grid(row=0, column=1)


# Button
def calculate_click():
    miles_converted = round(float(user_input.get())*1.6)
    miles_num_label.config(text=f"{miles_converted}")


calculate_button = Button(text="Calculate", command=calculate_click)
calculate_button.grid(row=2, column=1)


window.mainloop()
