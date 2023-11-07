import tkinter as tk
from tkinter import ttk

global giatri

def create_rounded_frame(canvas, x0, y0, x1, y1, radius, color):
    canvas.create_arc(x0, y0, x0 + 2 * radius, y0 + 2 * radius, start=90, extent=90, fill=color, outline=color)
    canvas.create_arc(x1 - 2 * radius, y0, x1, y0 + 2 * radius, start=0, extent=90, fill=color, outline=color)
    canvas.create_arc(x0, y1 - 2 * radius, x0 + 2 * radius, y1, start=180, extent=90, fill=color, outline=color)
    canvas.create_arc(x1 - 2 * radius, y1 - 2 * radius, x1, y1, start=270, extent=90, fill=color, outline=color)
    canvas.create_rectangle(x0 + radius, y0, x1 - radius, y1, fill=color, outline=color)
    canvas.create_rectangle(x0, y0 + radius, x1, y1 - radius, fill=color, outline=color)

def resize_rounded_frame(canvas,event):
    canvas.delete("all")  # Clear the canvas
    canvas_width = event.width
    canvas_height = event.height
    create_rounded_frame(canvas, 0, 0, canvas_width, canvas_height, 30, "white")

root = tk.Tk()
root.geometry("800x500")
root.title("Resizable Rounded Frame")
root.config(background="blue")

canvas1 = tk.Canvas(root, background="blue", highlightthickness=0)
canvas1.place(relx=0.01, rely=0.01, relwidth=0.49, relheight=0.48)
canvas2 = tk.Canvas(root, background="blue", highlightthickness=0)
canvas2.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.48)
canvas3 = tk.Canvas(root, background="blue", highlightthickness=0)
canvas3.place(relx=0.01, rely=0.51, relwidth=0.49, relheight=0.48)
canvas4 = tk.Canvas(root, background="blue", highlightthickness=0)
canvas4.place(relx=0.51, rely=0.51, relwidth=0.48, relheight=0.48)

giatri = ""
o1 = "Các cảm biến hiện có"
o2 = "Giá trị cảm biến"
o3 = f"Giá trị theo thời gian"
o4 = "lịch sử"

stringLabel1 = tk.Label(canvas1, text=f'{o1}', bg="white", anchor="w")
stringLabel1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
stringLabel2 = tk.Label(canvas2, text=f'{o2}', bg="white", anchor="w")
stringLabel2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
stringLabel3 = tk.Label(canvas3, text=f'{o3}', bg="white", anchor="w")
stringLabel3.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
stringLabel4 = tk.Label(canvas4, text=f'{o4}', bg="white", anchor="w")
stringLabel4.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

canvas1.bind("<Configure>", lambda event, canvas=canvas1: resize_rounded_frame(canvas, event))
canvas2.bind("<Configure>", lambda event, canvas=canvas2: resize_rounded_frame(canvas, event))
canvas3.bind("<Configure>", lambda event, canvas=canvas3: resize_rounded_frame(canvas, event))
canvas4.bind("<Configure>", lambda event, canvas=canvas4: resize_rounded_frame(canvas, event))
global selected_value2
def click_command():
    global giatri
    giatri = selected_value2.get()
    stringLabel3.config(text=f"Giá trị {giatri} theo thời gian")

def create_button():
    global selected_value2
    #create button in canvas2
    for widget in canvas2.winfo_children():
        widget.destroy()
    stringLabel2 = tk.Label(canvas2, text=f'{o2}', bg="white", anchor="w")
    stringLabel2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
    global giatri
    giatri = selected_value.get()
    selected_value2 = tk.StringVar(value="E")
    if giatri == "A":
        radiobutton1canvas2 = tk.Radiobutton(canvas2, text="E", variable=selected_value2, value="E", command=click_command, background="white",activebackground="white")
        radiobutton1canvas2.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)
        radiobutton2canvas2 = tk.Radiobutton(canvas2, text="F", variable=selected_value2, value="F", command=click_command, background="white", activebackground="white")
        radiobutton2canvas2.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)
        radiobutton3canvas2 = tk.Radiobutton(canvas2, text="G", variable=selected_value2, value="G", command=click_command, background="white", activebackground="white")
        radiobutton3canvas2.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.1)
    elif giatri =="B":
        radiobutton1canvas2 = tk.Radiobutton(canvas2, text="E", variable=selected_value2, value="E", command=click_command, background="white",activebackground="white")
        radiobutton1canvas2.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)
        radiobutton2canvas2 = tk.Radiobutton(canvas2, text="F", variable=selected_value2, value="F", command=click_command, background="white", activebackground="white")
        radiobutton2canvas2.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)
        radiobutton3canvas2 = tk.Radiobutton(canvas2, text="G", variable=selected_value2, value="G", command=click_command, background="white", activebackground="white")
        radiobutton3canvas2.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.1)
        radiobutton4canvas2 = tk.Radiobutton(canvas2, text="H", variable=selected_value2, value="H", command=click_command, background="white", activebackground="white")
        radiobutton4canvas2.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.1)
    elif giatri =="C":
        radiobutton1canvas2 = tk.Radiobutton(canvas2, text="E", variable=selected_value2, value="E", command=click_command, background="white",activebackground="white")
        radiobutton1canvas2.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)
        radiobutton2canvas2 = tk.Radiobutton(canvas2, text="F", variable=selected_value2, value="F", command=click_command, background="white", activebackground="white")
        radiobutton2canvas2.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)

    elif giatri =="D":
        radiobutton1canvas2 = tk.Radiobutton(canvas2, text="E", variable=selected_value2, value="E", command=click_command, background="white",activebackground="white")
        radiobutton1canvas2.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)
        radiobutton2canvas2 = tk.Radiobutton(canvas2, text="F", variable=selected_value2, value="F", command=click_command, background="white", activebackground="white")
        radiobutton2canvas2.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)
        radiobutton3canvas2 = tk.Radiobutton(canvas2, text="G", variable=selected_value2, value="G", command=click_command, background="white", activebackground="white")
        radiobutton3canvas2.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.1)





# Create a Treeview widget
tree = ttk.Treeview(canvas3)
tree["columns"] = ("Name", "Age")  # Define column names
# Create treeview columns
tree.column("#0", width=0, stretch=tk.NO)  # Hidden ID column
tree.column("Name", width=150, minwidth=50, anchor="center")
tree.column("Age", width=150, minwidth=50, anchor="center")

# Define column headings
tree.heading("#0", text="", anchor=tk.W)
tree.heading("Name", text="Thời Gian", anchor="center")
tree.heading("Age", text="Dữ Liệu", anchor="center")

# Insert data into the treeview
tree.insert("", "end", values=("John Doe", 30))
tree.insert("", "end", values=("Jane Smith", 25))

# Pack the treeview widget to add it to the window
tree.place(relx=0.1, rely=0.21, relwidth=0.8, relheight=0.77)

# Create Radio buttons
selected_value = tk.StringVar(value="A")

radiobutton1 = tk.Radiobutton(canvas1, text="A", variable=selected_value, value="A", command=create_button, background="white",activebackground="white")
radiobutton1.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)

radiobutton2 = tk.Radiobutton(canvas1, text="B", variable=selected_value, value="B", command=create_button, background="white", activebackground="white")
radiobutton2.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)

radiobutton3 = tk.Radiobutton(canvas1, text="C", variable=selected_value, value="C", command=create_button, background="white", activebackground="white")
radiobutton3.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.1)

radiobutton4 = tk.Radiobutton(canvas1, text="D", variable=selected_value, value="D", command=create_button, background="white", activebackground="white")
radiobutton4.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.1)

root.mainloop()
