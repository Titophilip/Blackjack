from random import choice
from compare import CompareCards

deck: list[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
visible_deck: list[str] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits: list[str] = ["♣", "♦", "♠", "♥"]


class Dealer(CompareCards):

    def __init__(self):
        super().__init__()
        self.user_dealt_cards: list = []
        self.comp_dealt_cards: list = []
        self.user_cards_value: list = []
        self.comp_cards_value: list = []
        self.user_sum: int = 0
        self.comp_sum: int = 0
        self.deck: list = []
        self.create_deck()

    def create_deck(self):
        for card in visible_deck:
            for suit in suits:
                self.deck.append(card + suit)

    def deal(self):
        for i in range(2):
            user_card: str = choice(self.deck)
            self.deck.remove(user_card)
            if len(user_card) == 2:
                user_value: int = deck[visible_deck.index(user_card[0])]
            elif len(user_card) == 3:
                user_value: int = deck[visible_deck.index(user_card[0] + user_card[1])]

            comp_card: str = choice(self.deck)
            self.deck.remove(comp_card)
            if len(comp_card) == 2:
                comp_value: int = deck[visible_deck.index(comp_card[0])]
            elif len(comp_card) == 3:
                comp_value: int = deck[visible_deck.index(comp_card[0] + comp_card[1])]

            self.user_dealt_cards.append(user_card)
            self.user_cards_value.append(user_value)

            self.comp_dealt_cards.append(comp_card)
            self.comp_cards_value.append(comp_value)
        self.user_sum = sum(self.user_cards_value)
        self.comp_sum = sum(self.comp_cards_value)

        if self.user_sum == 21 or self.comp_sum == 21:
            print(f"Your hand: {self.user_dealt_cards}. Your sum: {self.user_sum}\n"
                  f"Computer hand: {self.comp_dealt_cards}. Computer sum: {self.comp_sum}.")
            if self.user_sum == self.comp_sum == 21:
                self.compare(self.user_sum, self.comp_sum)
            else:
                print("BLACKJACK!")
                self.compare(self.user_sum, self.comp_sum)
            self.reset()
        else:
            self.calculate('user', self.user_cards_value)
            self.calculate('comp', self.comp_cards_value)

            print(f"Your hand: {self.user_dealt_cards}. Your sum: {self.user_sum}\n"
                  f"Computer hand: {self.comp_dealt_cards[0]}, ?.")
            self.game_on = True

    def deal_again(self, player: str, dealt_cards: list[str], cards_value: list[int]):
        card: str = choice(self.deck)
        self.deck.remove(card)
        if len(card) == 2:
            value: int = deck[visible_deck.index(card[0])]
        if len(card) == 3:
            value: int = deck[visible_deck.index(card[0] + card[1])]

        dealt_cards.append(card)
        cards_value.append(value)

        self.calculate(player, cards_value)

    def player_deal_again(self):
        while self.game_on:
            print("*************************************************************")
            question = input("<hit> or <stand>: ").lower().strip()
            if question == "hit":
                self.deal_again('user', self.user_dealt_cards, self.user_cards_value)
                if self.user_sum < 21:
                    print(f"Your hand: {self.user_dealt_cards}. Your sum: {self.user_sum}\n"
                          f"Computer hand: {self.comp_dealt_cards[0]}, ?.")
                elif self.user_sum >= 21:
                    print(f"Your hand: {self.user_dealt_cards}. Your sum: {self.user_sum}\n"
                          f"Computer hand: {self.comp_dealt_cards}. Computer sum: {self.comp_sum}.")
                    self.compare(self.user_sum, self.comp_sum)
            elif question == "stand":
                while self.comp_sum < 17:
                    self.deal_again('comp', self.comp_dealt_cards, self.comp_cards_value)
                print(f"Your hand: {self.user_dealt_cards}. Your sum: {self.user_sum}\n"
                      f"Computer hand: {self.comp_dealt_cards}. Computer sum: {self.comp_sum}.")
                self.compare(self.user_sum, self.comp_sum)
        self.reset()

    def calculate(self, player: str, cards_value: list[int]):
        if player == "user":
            if sum(cards_value) > 21:
                for i in range(len(cards_value)):
                    if cards_value[i] == 11:
                        cards_value[i] = 1

            self.user_sum: int = sum(cards_value)

        elif player == "comp":
            for i in range(1, len(cards_value)):
                if cards_value[i] == 11:
                    cards_value[i] = 1

            if sum(cards_value) > 21:
                if cards_value[0] == 11:
                    cards_value[0] = 1

            self.comp_sum: int = sum(cards_value)

    def reset(self):
        self.__init__()
