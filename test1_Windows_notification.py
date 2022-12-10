"""
File: test1_Windows_notification.py
Project: Python311
File Created: Sat 10th Dec 2022 2:48:26 pm
Author: Dpereira88
"""



import time
from win10toast import ToastNotifier
# One-time initialization
toaster = ToastNotifier()

# Show notification whenever needed
toaster.show_toast("Notification!", "Alert!", threaded=True,
                   icon_path=None, duration=3)  # 3 seconds

# To check if any notifications are active,
# use `toaster.notification_active()`
while toaster.notification_active():
    time.sleep(0.1)