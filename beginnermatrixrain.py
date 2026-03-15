import random
import time
import os

def matrix_rain():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&"
    width = os.get_terminal_size().columns
    
    try:
        while True:
            line = ""
            for i in range(width):
                line += random.choice(chars) + " "
            print(line)
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n[N.U.L.L. terminated]")

matrix_rain()
