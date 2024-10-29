# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer=[]
    other=[]
  
    shuffle_deck(deck)
     
    for i in range(len(deck)):
        if i%2!=0:
            dealer.append(deck[i])
        else:
            other.append(deck[i])
         
    return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[] 

    length=1
    l=sorted(l)
      
    for i in range(len(l)-1):
        firstcard=l[i]
        secondcard=l[i+1]
        if firstcard[:-1] == secondcard[:-1]:
            length=length+1
        else:
            if length==1:               
                no_pairs.append(l[i])
                length=1
                
            elif length%2!=0:
                no_pairs.append(l[i])
                
                
            elif length>1:
                length=1

    #IF LENGTH OF LIST IS ODD, ADD LAST ITEM

    if length%2!=0 or length==1:     
                no_pairs.append(l[-1])


    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    print("\n")
    for i in deck:
        print(i, end=" ")
    print("\n")

    
def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
    Precondition: n>=1
    '''

    print("I have " + str(n) + " cards. If 1 stands for my first card and " + str(n) + " for my last card, which of my cards would you like?")
    integer=int(input("Give me an integer between 1 and " + str(n) + ": ").strip())
    while integer<1 or integer>n:
        integer=int(input("Invalid number. Please enter integer between 1 and " + str(n) + ": ").strip())
    return integer
    
    
def add_card_human(integer,dealer,human):

    '''
    (int,str,str)->lst
    adds a card from dealers deck to humans deck and returns the new
    human deck
    '''   
    
    if integer==1:
        suffix="st"
    elif integer==2:
        suffix="nd"
    elif integer==3:
        suffix="rd"
    else:
        suffix="th"
    
    a=dealer[integer-1]   
    print("You asked for my " + str(integer) + suffix + " card.")
    print("Here it is. It is " + str(a))
    human.append(a)
    print("\nWith " + a + " added, your current deck is:\n")
    for i in human:
        print(i, end=" ")
    dealer.pop(integer-1)
    print("\nAnd after discarding pairs and shuffling, your deck is:\n")
    human=remove_pairs(human)
    for i in human:
        print(i, end=" ")

    return human

def add_card_dealer(integer,dealer,human):

    '''
    (int,str,str)->lst
    adds a card from humans deck to dealers deck and returns the new
    dealers deck
    '''
    

    if len(human)==1:
        integer=1
        suffix="st"
        a=human[integer-1]   
        print("I took your " + str(integer) + suffix + " card.")
        dealer.append(a)
        human.pop(integer-1)
        dealer=remove_pairs(dealer)
        
    else:
        integer=random.randrange(1,len(human))

        if integer==1:
            suffix="st"
        elif integer==2:
            suffix="nd"
        elif integer==3:
            suffix="rd"
        else:
            suffix="th"
            
        a=human[integer-1]   
        print("I took your " + str(integer) + suffix + " card.")
        dealer.append(a)
        human.pop(integer-1)
        dealer=remove_pairs(dealer)

    return dealer
            
def play_game():
    '''()->None
    This function plays the game'''
    
    deck=make_deck()
    shuffle_deck(deck)
    tmp=deal_cards(deck)

    dealer=tmp[0]
    human=tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
     
    dealer=remove_pairs(dealer)
    human=remove_pairs(human)

    while not((len(dealer)==1 and len(human)==0) or (len(dealer)==0 and len(human)==1)):
        print("*************************************************************************\nYour turn.\n\nYour current deck of cards is:\n")
        for i in human:
            print(i, end=" ")
        print()          
        print("\n")
        if not len(dealer)==0:
            integer=get_valid_input(len(dealer))    
            human=add_card_human(integer,dealer,human)
            print()
            wait_for_player()
        if not len(dealer)==0:
            print("*************************************************************************\nMy turn.\n")
            dealer=add_card_dealer(integer,dealer,human)      
            wait_for_player()

    if len(human)==1:
        print("*************************************************************************")
        print("Ups. I do not have any more cards\nYou lost! I, Robot, win")
    else:
        print("*************************************************************************")
        print("Ups. You do not have any more cards\nCongratulations! You, Human, win")

play_game()
