import tkinter.messagebox
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------READING FILE--------------------------#
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
    to_learn = pandas.DataFrame.to_dict(data, orient="records")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/250_spanish_words.csv")
    to_learn = pandas.DataFrame.to_dict(original_data, orient="records")
finally:

    # --------------------------FUNCTIONS---------------------------#
    def next_card():
        global timer, card
        card = random.choice(to_learn)
        window.after_cancel(timer)
        current_card = card["English"]
        canvas.itemconfig(background_card, image=image_front_card)
        canvas.itemconfig(card_word, text=current_card, fill="black")
        canvas.itemconfig(card_title, text="English", fill="black")
        timer = window.after(3000, flip)


    def flip():
        canvas.itemconfig(background_card, image=image_back_card)
        translate_card = card["Spanish"]
        canvas.itemconfig(card_word, text=translate_card, fill="white")
        canvas.itemconfig(card_title, text="Spanish", fill="white")


    def learned():
        to_learn.remove(card)
        if len(to_learn) > 0:
            words_to_learn = pandas.DataFrame(to_learn)
            words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
            next_card()
        else:
            canvas.itemconfig(card_word, text="That´s all", fill="red")
            canvas.itemconfig(card_title, text="Congratulations", fill="red")
            window.after_cancel(timer)
            end = window.after(3000, func=end_study)

    def end_study():
        end = tkinter.messagebox.showinfo(title="No words to learn left.", message="You have learned all the words! "
                                                                                   "Program will be terminated")
        window.destroy()


# --------------------------UI---------------------------#
window = Tk()
window.config(width=900, height=626, bg=BACKGROUND_COLOR, pady=50, padx=50)
window.title("FlashCards")

timer = window.after(3000, flip)

# front card canvas
canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)

# card images
image_front_card = PhotoImage(file="./images/card_front.png")
image_back_card = PhotoImage(file="./images/card_back.png")

background_card = canvas.create_image(400, 270, image=image_front_card)
canvas.grid(column=0, row=0, columnspan=2)

# texts in canvas
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

# buttons
cross_image = PhotoImage(file="./images/wrong.png")
check_image = PhotoImage(file="./images/right.png")

cross_button = Button(image=cross_image, command=next_card)
cross_button.grid(column=0, row=1)

check_button = Button(image=check_image, command=learned)
check_button.grid(column=1, row=1)

next_card()

window.mainloop()
