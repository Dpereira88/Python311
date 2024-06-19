import tkinter as tk
import socket
import threading

def update_text_widget(data):
    text_widget.insert(tk.END, data)
    text_widget.see(tk.END)


class AsyncReceive(threading.Thread):
    def __init__(self, host, port, text_widget):
        super().__init__()
        self.host = host
        self.port = port
        self.text_widget = text_widget
        self.should_stop = False

    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            self.text_widget.insert(tk.END, f"Connected to {self.host} on port {self.port}\n")
            self.text_widget.see(tk.END)

            while not self.should_stop:
                data = s.recv(1024).decode('utf-8')
                if data:
                    root.after(0, update_text_widget, data)
                    self.text_widget.insert(tk.END, f"{data.strip()}\n")
                    self.text_widget.see(tk.END)
            s.close()
        except ConnectionRefusedError:
            self.text_widget.insert(tk.END, "Connection refused. Please check the server settings.\n")
            self.text_widget.see(tk.END)
        except Exception as e:
            self.text_widget.insert(tk.END, f"An error occurred: {e}\n")
            self.text_widget.see(tk.END)
    
    def stop(self):
        self.should_stop = True

def close_window():
    # Stop all threads when closing the window
    for thread in threads:
        thread.stop()
    root.destroy()


def send_message():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host_ip, int(entries[0].get())))
        s.sendall(entry1.get().encode('utf-8') + b"\n")
        response = s.recv(1024).decode('utf-8')
        text_widgets[0].insert(tk.END, f"Sent command: {entry1.get()}\nReceived response: {response}\n\n")
        text_widgets[0].insert(tk.END)
        s.close()
    except ConnectionRefusedError:
        text_widgets[0].insert(tk.END, "Connection refused. Please check the server settings.\n")
        text_widgets[0].insert(tk.END)
    except Exception as e:
        text_widgets[0].insert(tk.END, f"An error occurred: {e}\n")
        text_widgets[0].insert(tk.END)

def start_receiving():
    global threads

    ports = [entry.get() for entry in entries]

    for idx, port in enumerate(ports):
        text_widgets[idx].delete(1.0, tk.END)
        if idx == 0:
            continue
        receiver = AsyncReceive(host_ip, int(port), text_widgets[idx])
        receiver.start()
        threads.append(receiver)

# Replace '192.168.1.1' with the desired IP address
host_ip = '192.168.200.22'

root = tk.Tk()
root.title("Send and Receive Messages")
root.resizable(False, False)  # Disable resizing
# Disable maximize button
root.attributes('-topmost', True)
root.attributes('-topmost', False)
root.attributes('-toolwindow', True)

frames = []
text_widgets = []
entries = []
threads = []


# Define fonts (type and size)
label_font = ("Arial", 11)
entry_font = ("Arial", 8)
button_font = ("Arial", 11)
entry_frame_font = ("Arial", 11)

frames = []
text_widgets = []
text_widget_width = 50
entries = []
default_values_port = ["7000", "7010", "7020"]

for i in range(3):
    frame = tk.Frame(root)
    frame.grid(row=i, column=0, padx=10, pady=10)

    label = tk.Label(frame, text=f"Port {i+1}:", font=label_font)
    label.grid(row=0, column=0)

    entry = tk.Entry(frame, font=entry_font)
    entry.insert(0, default_values_port[i])
    entry.grid(row=1, column=0)
    entries.append(entry)

    text_widget = tk.Text(frame, width=text_widget_width, height=10, font=entry_font)
    text_widget.grid(row=2, column=0)
    text_widgets.append(text_widget)

column1_frame = tk.Frame(root)
column1_frame.grid(row=0, column=1, padx=10)

label_port1 = tk.Label(column1_frame, text="Port 1 Message:", font=label_font)
label_port1.grid(row=0, column=0)

entry1_frame = tk.Frame(column1_frame)
entry1_frame.grid(row=1, column=0)

entry1 = tk.Entry(entry1_frame, font=entry_frame_font)
entry1.pack()

send_button = tk.Button(column1_frame, text="Send Message", command=send_message,
                        font=button_font)
send_button.grid(row=2, column=0)

start_button = tk.Button(root, text="Start Receiving", command=start_receiving,
                         font=button_font)
start_button.grid(row=2, column=1)

exit_button = tk.Button(root, text="Exit", padx=10, command=close_window)
exit_button.grid(row=3, column=1, padx=10, pady=15, ipadx=10)

# Bind closing window event to stop threads
root.protocol("WM_DELETE_WINDOW", close_window)

# Start the receiving data function in a separate thread
receive_thread = threading.Thread(target=start_receiving)
receive_thread.start()

root.mainloop()