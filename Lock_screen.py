import ctypes
def lock_screen():
    try:
        if ctypes.windll.user32.LockWorkStation():
            print("Locked screen")
        else:
            print("Screen not locked")
    except Exception as e:
        print(e)
lock_screen()
