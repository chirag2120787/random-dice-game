import random


class Wallet(object):
    def __init__(self):
        """
        Wallet of a player
        """
        self.profit = 0

    def pay(self, value):
        """
        Pay from wallet

        :param value: value of money to be paid
        :return:
        """
        self.profit -= value

    def add(self, value):
        """
        Add money to wallet

        :param value: value of money to be added
        :return:
        """
        self.profit += value


class Game(object):
    def __init__(self, wallet, cost=0.5, rounds=1000):
        """
        Dice game

        :param wallet: Player's wallet
        :param cost: Cost to enter a round of game
        :param rounds: Number of rounds in the game
        """
        self.wallet = wallet
        self.cost = cost
        self.rounds = rounds

    def start_game(self, num_dice=2):
        """
        Start playing

        :param num_dice: Number of die
        :return:
        """
        for i in range(self.rounds):
            self.wallet.pay(self.cost)
            result = self._roll_dice(num_dice)
            payback = self._get_money(result)
            self.wallet.add(payback)

    def is_profitable(self):
        """
        If game was profitable

        :return: profit in wallet is greater than 0
        """
        return self.wallet.profit > 0

    def _roll_dice(self, num_dice):
        """
        Roll the die and add the result

        :param num_dice: Number of die in the game
        :return: Sum of result of die
        """
        result = 0
        for dice in range(num_dice):
            result += random.randint(1, 6)
        return result

    def _get_money(self, result):
        """
        Get money back

        :param result: Result of die roll
        :return: Payback
        """
        if result < 7:
            return 0
        if 6 < result < 10:
            return self.cost
        if result == 10:
            return 2 * self.cost
        if result == 11:
            return 3 * self.cost
        return 4 * self.cost
