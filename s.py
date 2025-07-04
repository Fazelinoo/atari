import random
import pyttsx3

poems = [
    "به یاد کسی همیشه در دل منی. تو آن گل سرخی که در چمن منی.",
    "زندگی زیباست ای زیبا پسند. زنده اندیشان به زیبایی رسند.",
    "به یاد کسی دل من تنگ است. در این شب تاریک، امیدم کم‌رنگ است.",
    "هر کسی کو دور ماند از اصل خویش. باز جوید روزگار وصل خویش."
]

def read_poem():
    poem = random.choice(poems)
    print("شعر امروز:\n")
    print(poem)
    engine = pyttsx3.init()
    engine.say(poem)
    engine.runAndWait()

if __name__ == "__main__":
    read_poem()