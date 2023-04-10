#!/usr/bin/env python3

from tkinter import *
import webbrowser

links1 = {"RVCE": "https://google.com",
         "PESU": "https://en.wikipedia.org/wiki/Wikipedia",
         "BMS ": "https://stackoverflow.com/",
         "RNSIT":"https://www.rnsit.ac.in/"}
links2= {"PESU":"https://www.pesuacademy.com/Academy/sessionExpired"}
links3= {"PESU":"https://cs.pes.edu/programs/"}
links4= {"PES":"https://www.pes.edu/contact/"}


# Create new Tkinter instance
root = Tk()

# Creats a new page
page_home = Frame(root)

# Position Page
page_home.grid(row=0, column=0, sticky='news')

# Create new label with required text
l1 = Label(page_home, text="*****Enter college name*****")

# Positioning Label
l1.pack()

# Object to hold the value of selected option
college = StringVar(page_home)

# Sets default value of college
college.set("Default")


def clear_default(evt):
    if college.get() == "Default":
        evt.widget.delete(0, END)


ignore = False
vs = []


def process_input(evt):
    global ignore, vs

    print("EVT", evt)

    # Ignore keys entered by code
    if ignore:
        ignore = False
        return

    # For each college in colleges, check if college name is in input text
    vs = []
    curr_text = str.lower(college.get())
    college_list.delete(0, END)
    for c in links1.keys():
        if str.lower(c).startswith(curr_text):
            # If yes, then add it to the suggestions box
            college_list.insert(END, c)
            vs.append(c)

    # Dont run if backspace is pressed
    if evt.keycode not in [22, 50, 110]:

        # If any suggestions exist, then auto fill the first suggestion
        if len(vs):
            college_entry.delete(0, END)

            # Ignore keys pressed due to autofill for processing
            ignore = len(vs) != 1
            college_entry.insert(END, vs[0])

            # Select auto fill text
            college_entry.select_range(len(curr_text), END)

    # Enable Feature selection if a valid input is typed
    if len(vs) == 1:
        feature_option.configure(state="normal")
    else:
        feature_option.configure(state="disabled")


def select_item(evt):
    global vs
    if vs:
        # If selection is present, then change entry text to selected value
        sel = evt.widget.curselection()
        if sel:
            college_entry.delete(0, END)
            college_entry.insert(END, vs[sel[0]])
            feature_option.configure(state="normal")


# Creating an option menu in page_home
college_entry = Entry(page_home, textvariable=college)
college_entry.bind("<Button-1>", clear_default)
college_entry.bind("<KeyRelease>", process_input)

# Positioning option menu
college_entry.pack()

college_list = Listbox(page_home)
college_list.bind("<<ListboxSelect>>", select_item)
college_list.pack()

# Object to hold the value of selected option
features = StringVar(page_home)

# Default
features.set("Select Feature")


def next_callback(*args):
    # Get Feature
    if features.get() == "About College":
            # If featuer is show college, the show College link page
            page_linking.tkraise()

            # Set text to college link text
            lbl_link["text"] = "About College" + college.get()

            # Set Hyperlink to Required college link
            lbl_link.bind("<Button-1>", lambda x: webbrowser.open_new(links1[college.get()]))
    elif features.get() == "How to apply":
            # If featuer is show college, the show College link page
            page_linking.tkraise()

            # Set text to college link text
            lbl_link["text"] = "How to apply" + college.get()

            # Set Hyperlink to Required college link
            lbl_link.bind("<Button-1>", lambda x: webbrowser.open_new(links2[college.get()]))
    elif features.get() == "Syllabi and courses":
            # If featuer is show college, the show College link page
            page_linking.tkraise()

            # Set text to college link text
            lbl_link["text"] = "Syllabi and courses" + college.get()

            # Set Hyperlink to Required college link
            lbl_link.bind("<Button-1>", lambda x: webbrowser.open_new(links3[college.get()]))
    elif features.get() == "Contact the college":
            # If featuer is show college, the show College link page
            page_linking.tkraise()

            # Set text to college link text
            lbl_link["text"] = "Contact the college" + college.get()

            # Set Hyperlink to Required college link
            lbl_link.bind("<Button-1>", lambda x: webbrowser.open_new(links4[college.get()]))
    # elif features.get() == "feature 2":
    #   open feature 2 page
    #   customize feature 2 page
    # ...


# Creating an option menu in page_home
feature_option = OptionMenu(page_home, features, "About College", "How to apply", "Syllabi and courses","Contact the college",
                            command=next_callback)
feature_option.configure(state="disabled")

# Positioning option menu
feature_option.pack()



#############################################################################################
def prev_callback():
    """Run when previous button is pressed"""

    # Raise home page
    page_home.tkraise()


# Create linking page
page_linking = Frame(root)
page_linking.grid(row=0, column=0, sticky='news')

lbl_link = Label(page_linking, fg="blue", cursor="hand2")
lbl_link.pack()

linking_prev_btn = Button(page_linking, text="Prev", command=prev_callback)
linking_prev_btn.pack()

# Raise Home Page
page_home.tkraise()

# Run application loop
root.mainloop()
