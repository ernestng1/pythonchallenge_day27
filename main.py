from tkinter import *
#function
def miles_to_km():
    value = float(input.get())*1.609
    my_label4.config(text=str(value))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=50,height=50)
window.config(padx=20, pady=20)

#label, is equal to
my_label = Label(text="is equal to", font=("Arial",16))
my_label.grid(column=0, row=1)

#label, miles
my_label2 = Label(text="Miles", font=("Arial",16))
my_label2.grid(column=2, row=0)

#label, Km
my_label3 = Label(text="Km", font=("Arial",16))
my_label3.grid(column=2, row=1)

#label, reading
my_label4 = Label(text="0", font=("Arial",16))
my_label4.grid(column=1, row=1)

#button1
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

#entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()