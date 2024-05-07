#The psutil library in Python can be used to retrieve system information, including CPU usage. You can install it using pip install psutil.
#Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.

import psutil
import os
import time

user_input= True
#user_input= int(input("Hello, Please press 1 to check the cpu utilization level, Press 2 to exit:  "))
try:
    while user_input == True:
        i = (psutil.cpu_percent(2))
        print("*********Press Ctrl+C to exit********")
        print (f"\nTHE CPU UTILIZATION LEVEL IS: {i} %")
        if i > 1.5:
            
            print(f"\n*** Warning: Alert! CPU usage exceeds threshold: {i}%")
            time.sleep(2)
        time.sleep(2)
        os.system('cls')
except KeyboardInterrupt:
    print("\n***Program terminated by user.***")   
    
