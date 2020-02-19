# Random dice game
We should check if we have a good chance of winning in a game with two dice. The values of
the dice are added. We start the game with 50c. The profit is computed with the following table

| Sum | Payback | Profit 
| --- | ------- | ------ 
| 12 | 4x input | +1,50 Euro
| 11 | 3x input | +1,00 Euro
| 10 | 2x input | +0,50 Euro
| 7,8,9 | input back | +0,00 Euro
| 2,3,4,5,6 | none | -0,50 Euro

Is it good to take part in this game? Try in a loop with 1000 iterations, if you lose or
win in the long run. You can simulate the dice with random numbers.

## How to run
Simply run using ``python main.py`` 

You can change the number of rounds (default=1000), 
cost of each game (0.5 EUR), number of die in the game (default=2)
