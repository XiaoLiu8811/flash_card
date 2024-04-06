from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# -------------------Read words list------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)



def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    current_card = random.choice(to_learn)


def known_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


#--------------------UI SETUP------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# Create the canvas
canvas = Canvas(width=800, height=526)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
# Create buttons
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command= next_card)
wrong_button.grid(column=0, row=1)
check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, highlightthickness=0, command = known_card)
right_button.grid(column=1, row=1)

next_card()





window.mainloop()