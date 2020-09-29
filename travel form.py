from tkinter import *
root = Tk()

root.geometry("455x245")
root.title("Rathi Travels")


l= Label(root, text="Travel form", fg="black", font="verdana 13 bold", pady=15)
l.grid(row=0, column=11)     #grid() me pack() vale attributes like "side, anchor, etc" nhi aa sakte. grid() ke attributes "row and column" hote h
#The above code in one line can also be written as:
#Label(root, text="Travel form", bg="grey", fg="white", font="verdana 13 bold", relief=SUNKEN).grid(row=0, column=1)



def button():
    print("Submitting form....")
    print("The entered information is:- ", name_value.get())
    print("The entered information is:- ", age_value.get())
    print("The entered information is:- ", phone_value.get())
    print("The entered information is:- ", gender_value.get())
    print("The entered information is:- ", payment_mode_value.get())
    print("Box checked or not:- ", food_service_value.get())


#The above 6 lines can also be written as this one below:
    print("The entered information is:- ", name_value.get(),"\n",  "The entered information is:- ", age_value.get(), "\n", "The entered information is:- ", phone_value.get(), "\n", "The entered information is:- ", gender_value.get(), "\n", "The entered information is:- ", payment_mode_value.get(), "\n", "The entered information is:- ", food_service_value.get())
    

    with open("records of tkinter.txt", "a") as f:          #Note:"a" for append, "w" for write, "r" for read
    #You cannot write new 2 attributes in f.write()     #agar hum file ko append mode ki jagah write mode m kholte to vo ek ke baad ek na hoke overwrite karta rehta use baar baar
        
        f.write(f"{name_value.get(), age_value.get(), phone_value.get(), gender_value.get(), payment_mode_value.get()}\n" )
        
        

name = Label(root, text="Name")
age = Label(root, text="Age")
phone = Label(root, text="Phone No.")
emergency = Label(root, text="Emergency")
gender = Label(root, text="Gender")
payment_mode= Label(root, text="Payment Mode")


name.grid(row=2, column=10)
age.grid(row=3, column=10)
phone.grid(row=4, column=10)
emergency.grid(row=5, column=10)
gender.grid(row=6, column=10)
payment_mode.grid(row=7, column=10)




name_value = StringVar()
age_value = StringVar()
phone_value = StringVar()
emergency_value = StringVar()
gender_value = StringVar()
payment_mode_value = StringVar()
food_service_value = IntVar()           #IntVar() bas 0 ya 1 leta h and hence it can be used to make checkbox


name_entry = Entry(root, textvariable=name_value)
age_entry = Entry(root, textvariable=age_value)
phone_entry = Entry(root, textvariable=phone_value)
emergency_entry = Entry(root, textvariable=emergency_value)
gender_entry = Entry(root, textvariable=gender_value)
payment_entry = Entry(root, textvariable=payment_mode_value)
food_service = Checkbutton(text="Want to prebook your meal", variable=food_service_value)

name_entry.grid(row=2, column=14)
age_entry.grid(row=3, column=14)
phone_entry.grid(row=4, column=14)
emergency_entry.grid(row=5, column=14)
gender_entry.grid(row=6, column=14)
payment_entry.grid(row=7, column=14)
food_service.grid(row=8, column=14)

Button(root, text="Submit", bg="green", fg="yellow", command=button).grid(row=8, column=10)



root.mainloop()