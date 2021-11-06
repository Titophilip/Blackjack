class CompareCards:
    def __init__(self):
        self.game_on = False

    def compare(self, user_sum, comp_sum):
        if user_sum == comp_sum == 21:
            print("PUSH!\nIt's a draw!!")
            self.game_on = False
        elif user_sum == 21:
            print("You win!!")
            self.game_on = False
        elif comp_sum == 21:
            print("You lose!!")
            self.game_on = False
        elif user_sum > 21:
            print("BUST! You lose!!")
            self.game_on = False
        elif user_sum == comp_sum < 21:
            print("PUSH!\nIt's a draw!!")
            self.game_on = False
        elif user_sum < 21 < comp_sum:
            print("You win!!")
            self.game_on = False
        elif comp_sum < user_sum < 21:
            print("You win!!")
            self.game_on = False
        elif user_sum < comp_sum < 21:
            print("You lose!!")
            self.game_on = False
        print("*************************************************************")
