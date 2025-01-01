import tkinter as tk  # Importing the tkinter library
from time import strftime

# Create the main window
window = tk.Tk()
window.title("Time Display")

# Remove default window borders and title bar
window.overrideredirect(True)

# Set window size and position it in center
window.geometry("400x200")
window.resizable(False, False)
window.configure(bg='#2E2E2E')  # Dark background

# Add a close button
close_button = tk.Button(
    window,
    text="×",
    font=('Helvetica', 16, 'bold'),
    bg='#2E2E2E',
    fg='#FFFFFF',  # Brighter color for better visibility
    bd=0,
    cursor='hand2',  # Hand cursor on hover
    command=window.quit,
    activebackground='#FF4444',
    activeforeground='white',
    width=2,
    height=1,
    highlightthickness=0  # Remove highlight border
)
close_button.place(x=360, y=2)  # Moved slightly higher

# Add creator label
creator_label = tk.Label(
    window,
    text="Created By Gustov",
    font=('Helvetica', 10),
    bg='#2E2E2E',
    fg='#888888'  # Subtle gray color
)
creator_label.place(x=10, y=5)

def on_enter(e):
    close_button.config(bg='#FF4444', fg='white')

def on_leave(e):
    close_button.config(bg='#2E2E2E', fg='#FFFFFF')

# Bind hover events
close_button.bind('<Enter>', on_enter)
close_button.bind('<Leave>', on_leave)

# Variables to keep track of window dragging
x, y = 0, 0

def start_move(event):
    global x, y
    x = event.x
    y = event.y

def stop_move(event):
    global x, y
    x = None
    y = None

def do_move(event):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    new_x = window.winfo_x() + deltax
    new_y = window.winfo_y() + deltay
    window.geometry(f"+{new_x}+{new_y}")

# Bind mouse events for window dragging
window.bind("<Button-1>", start_move)
window.bind("<ButtonRelease-1>", stop_move)
window.bind("<B1-Motion>", do_move)

# Center the window on screen
window_width = 400
window_height = 200
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Create frames for better organization
main_frame = tk.Frame(window, bg='#2E2E2E')
main_frame.pack(expand=True, fill='both', padx=20, pady=(45, 20))  # Increased top padding even more

# Create a label to display time
time_label = tk.Label(
    main_frame,
    font=('Helvetica', 48, 'bold'),
    bg='#2E2E2E',
    fg='#00FF9F'  # Modern neon green color
)
time_label.pack(anchor='center', pady=10)

# Create a label for the date
date_label = tk.Label(
    main_frame,
    font=('Helvetica', 14),
    bg='#2E2E2E',
    fg='#888888'  # Subtle gray color
)
date_label.pack(anchor='center')

# Function to display time and date
def display_time():
    current_time = strftime('%I:%M:%S %p')  # %I for 12-hour format, %p for AM/PM
    current_date = strftime('%B %d, %Y')    # Month Day, Year
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    window.after(1000, display_time)  # Update every 1000ms (1 second)

# Call display_time function
display_time()

# Run the tkinter event loop
window.mainloop()
