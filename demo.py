import keyboard
import pyautogui
import time

SAMPLE_RATE = .1
positions = []

while True:
    print("Press 'n' to record a a new sequence,'r' to replay,  or q to quit:")
    key_event = keyboard.read_event() # keep KEY_DOWN event 
    keyboard.read_event() # catch and discard KEY_UP event
    if key_event.event_type == keyboard.KEY_DOWN:
        print(key_event.name)
        if  key_event.name == 'n':
            print("Hold space to record mouse positions")
            positions = []
            keyboard.wait('space')
            while keyboard.is_pressed('space'):        
                position=pyautogui.position()
                positions.append(position)
                print(position, end = "\r")
                time.sleep(SAMPLE_RATE)
        elif  key_event.name =='r':
            if positions:
                for position in positions:
                    pyautogui.moveTo(position[0],position[1], SAMPLE_RATE)
                    print(position, end = "\r")
            else:
                print("Nothing is recorded. Try recording something first.")
        elif  key_event.name == 'q':
            print("Goodbye!")
            break
        else:
            print("Input not recognized.")