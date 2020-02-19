from models import Game, Wallet

if __name__ == '__main__':
    player_wallet = Wallet()
    game = Game(player_wallet, rounds=1)
    game.start_game()
    if game.is_profitable():
        print("Profitable!")
    else:
        print("Not profitable!")
