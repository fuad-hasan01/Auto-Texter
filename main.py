import pyautogui
import time

# ইউজার থেকে ইনপুট নেওয়া
b = input("Type the text you want to type automatically: ")

# কয়বার চালাবে সেটা নেওয়া
loop_count = int(input("How many times do you want to run the loop: "))

print("You have 5 seconds to switch to your typing window...")
time.sleep(5)  # 5 সেকেন্ড অপেক্ষা করবে

# লুপ চালু
for a in range(1, loop_count + 1):  # 1 থেকে শুরু করলাম যাতে numbering 1 হয়
    text_to_type = f"{b} {a}"  # টেক্সটের শেষে সংখ্যা যোগ করা
    pyautogui.typewrite(text_to_type)
    # time.sleep(0.5)  # সামান্য delay যাতে টাইপিং স্পষ্ট হয়
    pyautogui.press("enter")
    # time.sleep(1)  # সামান্য delay যাতে smooth চলে
