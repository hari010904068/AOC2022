import random
import time

def random_char():
    return chr(random.randint(33, 127))

def main():
    while True:
        row = ''
        for i in range(80):
            row += random_char()
        print("\033[32m" + row + "\033[0m")  # Green text
        time.sleep(0.1)

if __name__ == '__main__':
    main()
