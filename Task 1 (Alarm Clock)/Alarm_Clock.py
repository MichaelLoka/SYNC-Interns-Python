import tkinter as tk
from tkinter import ttk
from datetime import datetime
from ttkthemes import ThemedStyle

alarms = []

def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    check_alarms()
    root.after(1000, update_time)

def set_alarm():
    alarm_time_str = alarm_time_entry.get()
    try:
        alarm_time = datetime.strptime(alarm_time_str, '%H:%M')
        alarms.append(alarm_time)
        alarm_label = ttk.Label(root, text=alarm_time.strftime(
            '%H:%M'), style="Alarm.TLabel")
        alarm_label.pack(pady=5)
        check_alarms()
    except ValueError:
        alarm_status.config(text="Invalid time format", style="Error.TLabel")

def check_alarms():
    current_time = datetime.now().time()
    for alarm_time in alarms:
        if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
            alarm_ring()

def alarm_ring():
    alarm_status.config(text="Alarm Activated", style="Activated.TLabel")
    alarms.clear()
    set_alarm_button.config(state=tk.NORMAL)
    turn_off_button.config(state=tk.NORMAL)

def turn_off_alarm():
    alarm_status.config(text="Alarm Deactivated", style="Deactivated.TLabel")
    set_alarm_button.config(state=tk.NORMAL)
    turn_off_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("24-Hour Alarm Clock")

# Apply the 'plastik' theme using ThemedStyle
style = ThemedStyle(root)
style.set_theme("plastik")

# Define custom styles
style.configure("Alarm.TLabel", foreground="blue", font=("Helvetica", 24),
                background="lightgray", padding=10, borderwidth=2, relief="raised")
style.configure("TButton", foreground="white", background="blue", font=(
    "Helvetica", 14), borderwidth=0, relief="flat", padding=10, borderRadius=10)
style.configure("Activated.TLabel", foreground="green", font=(
    "Helvetica", 18), background="lightgray", padding=10, borderwidth=2, relief="raised")
style.configure("Deactivated.TLabel", foreground="red", font=(
    "Helvetica", 18), background="lightgray", padding=10, borderwidth=2, relief="raised")
style.configure("Error.TLabel", foreground="red", font=("Helvetica", 18),
                background="lightgray", padding=10, borderwidth=2, relief="raised")

# Label to display the current time
time_label = ttk.Label(root, font=("Helvetica", 48))
time_label.pack(pady=20)

# Entry widget to set the alarm time
alarm_label = ttk.Label(
    root, text="Set Alarm Time (HH:MM):", font=("Helvetica", 18))
alarm_label.pack(pady=10)
alarm_time_entry = ttk.Entry(root, font=("Helvetica", 16))
alarm_time_entry.pack(pady=10)

# Button to set the alarm
set_alarm_button = ttk.Button(
    root, text="Set Alarm", command=set_alarm, style="TButton")
set_alarm_button.pack(pady=10)

# Button to turn off the alarm
turn_off_button = ttk.Button(root, text="Turn Off Alarm",
                             command=turn_off_alarm, style="TButton", state=tk.DISABLED)
turn_off_button.pack(pady=10)

# Label to display alarm status
alarm_status = ttk.Label(root, text="", font=("Helvetica", 18))
alarm_status.pack(pady=10)

update_time()
root.mainloop()
