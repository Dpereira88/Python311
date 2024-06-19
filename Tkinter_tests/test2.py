import asyncio
import tkinter as tk

async def start_receiving_async(host_ip, ports, text_widgets):
    for idx, port in enumerate(ports):
        text_widgets[idx].delete(1.0, tk.END)
        if idx == 0:
            continue
        try:
            reader, _ = await asyncio.open_connection(host_ip, int(port))
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                text_widgets[idx].insert(tk.END, data.decode())
                text_widgets[idx].see(tk.END)
        except Exception as e:
            text_widgets[idx].insert(tk.END, f"An error occurred: {e}\n")
            text_widgets[idx].see(tk.END)



async def send_message_async(host_ip, port, message):
    try:
        reader, writer = await asyncio.open_connection(host_ip, port)
        writer.write(message.encode() + b"\n")
        await writer.drain()

        data = await reader.read(1024)
        response = data.decode().strip()
        writer.close()
        await writer.wait_closed()

        return response
    except Exception as e:
        return f"An error occurred: {e}"

async def main():
    # Your previous code for the GUI setup remains unchanged


    def close_window():
        # Stop all threads when closing the window
        for thread in threads:
            thread.stop()
        root.destroy()    
                
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

    # ip is host_ip
    # 7000 for port 1
    # 7010 for port 2
    # 7020 for port 3
    
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

    send_button = tk.Button(column1_frame, text="Send Message", command=lambda: asyncio.create_task(send_message_async(None)))
    send_button.grid(row=2, column=0)

    start_button = tk.Button(root, text="Start Receiving", command=lambda: asyncio.create_task(start_receiving_async(None)))
    start_button.grid(row=2, column=1)

    exit_button = tk.Button(root, text="Exit", padx=10, command=close_window)
    exit_button.grid(row=3, column=1, padx=10, pady=15, ipadx=10)

    # Bind closing window event to stop threads
    root.protocol("WM_DELETE_WINDOW", close_window)


    root.mainloop()

# Run the main event loop
asyncio.run(main())