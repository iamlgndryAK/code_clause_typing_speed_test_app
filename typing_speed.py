from tkinter import Tk, Frame, Label, Entry, Button, END
from time import sleep
from random import choice
from threading import Thread

default_speed = "Speed: \n0.00 Characters Per Second\n0.00 Characters Per Minute\n" \
                "0.00 Words Per Second\n 0.00 Words Per Minute"


class AppGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Speed Test")
        self.window.geometry("800x600")
        self.window.config(background="pink")

        self.frame = Frame(self.window)

        self.text_list = ["He turned Random back and headed for the camp",
                          "So you just made a random deal with Darkyn",
                          "He nudged Random into motion and Carmen stepped back"]

        self.text_label = Label(self.frame, text=choice(self.text_list), font=("Helvetica", 18))
        self.text_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.entry = Entry(self.frame, width=40, font=("Helvetica", 24))
        self.entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.entry.bind("<KeyRelease>", self.start)

        self.speed_label = Label(self.frame, text=default_speed, font=("Helvetica", 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = Button(self.frame, text="Reset", command=self.reset, font=("Helvetica", 24), background='red')
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.count = 0
        self.is_running = False

        self.window.mainloop()

    def time_thread(self):
        while self.is_running:
            self.count = self.count + 0.1
            sleep(0.1)
            cps = len(self.entry.get()) / self.count
            cpm = cps * 60
            wps = len(self.entry.get().split(" ")) / self.count
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} Characters Per Second\n"
                                         f"{cpm:.2f} Characters Per Minute\n"
                                         f"{wps:.2f} Words Per Second\n"
                                         f"{wpm:.2f} Words per Minute")

    def start(self, event):
        if not self.is_running:
            if event.keycode not in [16, 17, 18]:
                self.is_running = True
                thread = Thread(target=self.time_thread)
                thread.start()
        if not self.text_label.cget("text").startswith(self.entry.get()):
            self.entry.config(fg="red")
        else:
            self.entry.config(fg="green")
        if self.entry.get() == self.text_label.cget("text"):
            self.is_running = False

    def reset(self):
        self.is_running = False
        self.count = 0
        self.speed_label.config(text=default_speed)
        self.text_label.config(text=choice(self.text_list))
        self.entry.delete(0, END)


AppGUI()