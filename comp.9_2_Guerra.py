# Guerra
# Da 1 a 7 players 

import cards, games     

class G_Card(cards.Card):
    """ A Guerra Carte. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = G_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class G_Deck(cards.Deck):
    """ Guerra Deck. """
    def populate(self):
        for suit in G_Card.SUITS: 
            for rank in G_Card.RANKS: 
                self.cards.append(G_Card(rank, suit))
    

class G_Hand(cards.Hand):
    """ A Guerra Hand. """
    def __init__(self, name):
        super(G_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(G_Hand, self).__str__()  
        if self.total:
            rep += "(" + str(self.total) + ")"        
        return rep

    @property     
    def total(self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None
        
         #add up card values, treat each Ace 
        t = 0
        for card in self.cards:
              t += card.value

        
        contains_ace = False
        for card in self.cards:
           if card.value == G_Card.ACE_VALUE:
                contains_ace = True
                
       # if ace < 11 add 10 
        if contains_ace and t <= 11:
            
            t += 10   
                
        return t

    def is_busted(self):
        return self.total > 21


class G_Player(G_Hand):
    """ A Guerra  Player. """
    

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def push(self):
        print(self.name, "pushes.")

        



class G_Game(object):
    """ A Guerra  Game. """
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = G_Player(name)
            self.players.append(player)

        

        self.deck = G_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            
                sp.append(player)
        return sp

   
           
    def play(self):
        # una carta per giocatore 
        self.deck.deal(self.players , per_hand = 1)
            
        for player in self.players:
            print(player)
       
                    
        # troviamo vincitore !    
        winner = []
        max_score = 0
        for player in self.players:
            if max_score < player.total:
                max_score = player.total
            
        for player in self.players:
            score = player.total
            if score == max_score:
                winner.append(player)

            
        for win in winner:
             print("\nWinner e, ", win)

        # canceliamo carte 
        for player in self.players:
            player.clear()
        

def main():
    print("\t\tWelcome to Guerra!\n")
    
    names = []
   
    number = games.ask_number("How many players? (1 - 7): ", low = 1, high = 8)
   
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()
        
    game = G_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")


main()
input("\n\nPress the enter key to exit.")



