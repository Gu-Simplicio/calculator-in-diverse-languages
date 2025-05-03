import customtkinter as ctk #import the library required for the project

window = ctk.CTk() #create the window

def show_calc():
    result = eval(output.cget("text"))
    output.configure(text=result)

ctk.set_appearance_mode("dark") #set the appearence to dark

window.title("Simple calculator in python!") #set the title of the window
window.geometry("600x290") #set the size of the window

#Create the label that show the result
output = ctk.CTkLabel(master=window, width=666, height=20, text="", anchor="sw", font=('Arial', 35, 'bold')) #create the label wich show the result
#insert the label on grid
output.grid(column=0, row=0, columnspan=5, pady=20, padx=5)

#create a label with the number 7
label_num7 = ctk.CTkButton(master=window, width=70, height=20, text="7", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "7"))
#insert the label on grid
label_num7.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)

#Create a label with the number 8
label_num8 = ctk.CTkButton(master=window, width=70, height=20, text="8", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "8"))
#insert the label on grid
label_num8.grid(column=1, row=1, sticky="nsew", padx=5, pady=5)

#Create a label with the number 9
label_num9 = ctk.CTkButton(master=window, width=70, height=20, text="9", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "9"))
#insert the label on grid
label_num9.grid(column=2, row=1, sticky="nsew", padx=5, pady=5)

#Create a label with the sum character
label_sum = ctk.CTkButton(master=window, width=70, height=20, text="+", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "+"))
#insert the label on grid
label_sum.grid(column=3, row=1, sticky="nsew", padx=5, pady=5)

#Create a label with the number 4
label_num4 = ctk.CTkButton(master=window, width=70, height=20, text="4", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "4"))
#insert the label on grid
label_num4.grid(column=0, row=2, sticky="nsew", padx=5, pady=5)

#Create a label with the number 5
label_num5 = ctk.CTkButton(master=window, width=70, height=20, text="5", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "5"))
#insert the label on grid
label_num5.grid(column=1, row=2, sticky="nsew", padx=5, pady=5)

#Create a label with the number 6
label_num6 = ctk.CTkButton(master=window, width=70, height=20, text="6", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "6"))
#insert the label on grid
label_num6.grid(column=2, row=2, sticky="nsew", padx=5, pady=5)

#Create a label with the sub character
label_sub = ctk.CTkButton(master=window, width=70, height=20, text="-", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "-"))
#insert the label on grid
label_sub.grid(column=3, row=2, sticky="nsew", padx=5, pady=5)

#Create a label with the number 1
label_num1 = ctk.CTkButton(master=window, width=70, height=20, text="1", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "1"))
#insert the label on grid
label_num1.grid(column=0, row=3, sticky="nsew", padx=5, pady=5)

#Create a label with the number 2
label_num2 = ctk.CTkButton(master=window, width=70, height=20, text="2", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "2"))
#insert the label on grid
label_num2.grid(column=1, row=3, sticky="nsew", padx=5, pady=5)

#Create a label with the number 3
label_num3 = ctk.CTkButton(master=window, width=70, height=20, text="3", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "3"))
#insert the label on grid
label_num3.grid(column=2, row=3, sticky="nsew", padx=5, pady=5)

#Create a label with the mult character
label_mult = ctk.CTkButton(master=window, width=70, height=20, text="*", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "*"))
#insert the label on grid
label_mult.grid(column=3, row=3, sticky="nsew", padx=5, pady=5)

#Create a label with the number 0
label_num0 = ctk.CTkButton(master=window, width=70, height=20, text="0", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "0"))
#insert the label on grid
label_num0.grid(column=0, row=4, sticky="nsew", padx=5, pady=5)

#Create a label with the clear character
label_clear = ctk.CTkButton(master=window, width=70, height=20, text="C", font=("Arial", 30, "bold"), command=lambda: output.configure(text=""))
#insert the label on grid
label_clear.grid(column=1, row=4, sticky="nsew", padx=5, pady=5)

#Create a label with the result character
label_result = ctk.CTkButton(master=window, width=70, height=20, text="=", font=("Arial", 30, "bold"), command=show_calc)
#insert the label on grid
label_result.grid(column=2, row=4, sticky="nsew", padx=5, pady=5)

#Create a label with the div character 
label_div = ctk.CTkButton(master=window, width=70, height=20, text="/", font=("Arial", 30, "bold"), command=lambda: output.configure(text=output.cget("text") + "/"))
#insert the label on grid
label_div.grid(column=3, row=4, sticky="nsew", padx=5, pady=5)


window.mainloop() #start the main loop