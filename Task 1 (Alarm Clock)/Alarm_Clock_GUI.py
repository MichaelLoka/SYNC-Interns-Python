import tkinter as tk
from tkinter import ttk
from datetime import datetime
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes

# Global variables
alarms = []

# Function to update the label with the current time


def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    check_alarms()
    root.after(1000, update_time)

# Function to set the alarm


def set_alarm():
    alarm_time_str = alarm_time_entry.get()
    try:
        alarm_time = datetime.strptime(alarm_time_str, '%H:%M')
        alarms.append(alarm_time)
        alarm_label = ttk.Label(root, text=alarm_time.strftime('%H:%M'))
        alarm_label.pack()
        check_alarms()
    except ValueError:
        alarm_status.config(text="Invalid time format")

# Function to check the alarms


def check_alarms():
    current_time = datetime.now().time()
    for alarm_time in alarms:
        if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
            alarm_ring()

# Function to ring the alarm


def alarm_ring():
    alarm_status.config(text="Alarm Activated")
    alarms.clear()
    set_alarm_button.config(state=tk.NORMAL)
    turn_off_button.config(state=tk.NORMAL)

# Function to turn off the alarm


def turn_off_alarm():
    alarm_status.config(text="Alarm Deactivated")
    set_alarm_button.config(state=tk.NORMAL)
    turn_off_button.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("24-Hour Alarm Clock")

# Apply the 'plastik' theme using ThemedStyle
style = ThemedStyle(root)
style.set_theme("plastik")

# Label to display the current time
time_label = ttk.Label(root, font=("Helvetica", 48))
time_label.pack()

# Entry widget to set the alarm time
alarm_label = ttk.Label(root, text="Set Alarm Time (HH:MM):")
alarm_label.pack()
alarm_time_entry = ttk.Entry(root)
alarm_time_entry.pack()

# Button to set the alarm
set_alarm_button = ttk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack()

# Button to turn off the alarm
turn_off_button = ttk.Button(
    root, text="Turn Off Alarm", command=turn_off_alarm, state=tk.DISABLED)
turn_off_button.pack()

# Label to display alarm status
alarm_status = ttk.Label(root, text="")
alarm_status.pack()

# Update the time label initially and every second
update_time()

# Start the tkinter main loop
root.mainloop()
