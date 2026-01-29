import time
import tkinter as tk

# ================= WINDOW =================
root = tk.Tk()
root.title("SAUMYA SINGH | Smart Digital Clock")
root.geometry("600x300")
root.config(bg="black")

is_24_hour = False
dark_mode = True

# ================= FUNCTIONS =================
def current_time():
    if is_24_hour:
        time_string = time.strftime('%H:%M:%S')
    else:
        time_string = time.strftime('%I:%M:%S %p')

    date_string = time.strftime('%A, %d %B %Y')
    label.config(text=f"{time_string}\n{date_string}")
    label.after(1000, current_time)

def toggle_format():
    global is_24_hour
    is_24_hour = not is_24_hour

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        root.config(bg="black")
        label.config(bg="black", fg="cyan")
    else:
        root.config(bg="white")
        label.config(bg="white", fg="black")

# ================= LABEL =================
label = tk.Label(
    root,
    font=('calibri', 40, 'bold'),
    bg="black",
    fg="cyan",
    pady=20
)
label.pack()

# ================= BUTTONS =================
btn_frame = tk.Frame(root, bg=root["bg"])
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="12 / 24 Hour",
    font=("Arial", 12, "bold"),
    command=toggle_format,
    cursor="hand2"
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="Dark / Light Mode",
    font=("Arial", 12, "bold"),
    command=toggle_theme,
    cursor="hand2"
).grid(row=0, column=1, padx=10)

# ================= START =================
current_time()
root.mainloop()
