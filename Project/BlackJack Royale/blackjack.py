import random
import pymongo

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Project"]  
collection = database["Game History"] 

def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image, ))

        # next the face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image, ))


def _deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)  # Use 0 to take card from top of deck
    # and add it back to the deck
    deck.append(next_card)
    # add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    # now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards in the list
    # Only one ace an have the value 11 and this will be reduce to 1 if the hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")
        print_card_history()  # Print card history when game ends
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
        print_card_history()  # Print card history when game ends
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
        print_card_history()  # Print card history when game ends
    else:
        result_text.set("Draw!")
        print_card_history()  # Print card history when game ends


def print_card_history():
    game_history = {
        "dealer_hand": [card[0] for card in dealer_hand],
        "player_hand": [card[0] for card in player_hand],
        "winner": result_text.get()
    }

    collection.insert_one(game_history)


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")


def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, bg="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    # embedded frame to hold the card images
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, bg="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set("")

    # Create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []
    initial_deal()


def shuffle():
    random.shuffle(deck)


def play():
    initial_deal()
    mainWindow.mainloop()


mainWindow = tkinter.Tk()

# Set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(bg="green")

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=0)
mainWindow.columnconfigure(4, weight=5)
mainWindow.columnconfigure(5, weight=0)


result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, bg="black")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", bg="black", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, bg="black", fg="white").grid(row=1, column=0)
# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, bg="black")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", bg="black", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, bg="black", fg="white").grid(row=3, column=0)
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, bg="black")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=1, columnspan=3, sticky='w')

player_button = tkinter.Button(button_frame, text="Hit", command=deal_player, padx=8)
player_button.grid(row=0, column=0)

dealer_button = tkinter.Button(button_frame, text="Stay", command=deal_dealer, padx=5)
dealer_button.grid(row=0, column=1)

reset_button = tkinter.Button(button_frame, text="New Game", command=new_game)
reset_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle, padx=2)
shuffle_button.grid(row=0, column=3)
# load cards
cards = []
load_images(cards)
print(cards)
# Create a new deck of cards and shuffle them
deck = list(cards) + list(cards) + list(cards)
shuffle()

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()
