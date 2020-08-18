# Cellular Automata

In this repository there are 2 command line scripts. `CellularAutomata.py` is a script I wrote that can be run from the command line to see the different patterns that each rule can generate in 1-D. `GameOfLife.py` is another command line script that can be run to emulate [Conways Game Of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). As described in [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/cellular-automata/) cellular automata is a process in which discrete units (cells) will interact with one another to form the next automaton based on an extremely simple rule. Starting from a single living cell for `CellularAutomata.py` or a few living cells for `GameOfLife.py`, extremely intricate patterns can be made from applying many iterations.

## My Motivations
Very early in my days of computing I came along cellular automata but didn't quite understand it. A few years later I listened to a podcast interviewing Lex Fridman who talked about Nick Bostrom's famous simulation hypothesis. Lex went on to explain how the idea of having something so simple generate very complex patterns can be one way that reality could have potentially been simulated. Obviously Lex was not suggesting that something like the script I wrote can be used to simulate reality, but just the idea its self that having something so simple like a single decimal value between 0-255 can generate such sophisticated patterns was very intriguing and I decided to dig deeper. From the outside the concept of this project seemed extremely easy and to be completely honest it wasn't the hardest project I have ever worked on. However, I thoroughly enjoyed learning about cellular automata and the different contributions its has made to the scientific world. To me, it seemed that the more I dig into this idea, the more I uncovered or learned.

## Conway's Game of Life
In `GameOfLife.py` there are 3 main rules. Each cell is evaluated based on its neighbourhood (the surrounding 8 cells).
  1. Any live cell with two or three live neighbours survives.
  2. Any dead cell with three live neighbours becomes a live cell.
  3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
  [Rules were taken from Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

### Running the Script
Prior to running this script please ensure that you have ```pygame``` installed. This script can be run from the command line or from any IDE. To run from command line simply write the follwing and specify the parameter:
``` GameOfLife.py -w <# of cells wide> -h <# of cells high> -p <present> -s <sleep>```
By default ```width = 101```, ```height = 50```, ```preset='glider'``` and ```sleep = false```. 
The available presets are ```glider```, ```blinker```, ```toad```, ```random```. (random works best for default screen size)
To enable a delay between state changes add ```-s 1``` at the end for your command line call.

### Sample Runs
```python GameOfLife.py -p random```
![Random](https://github.com/aivan6842/CellularAutomata/blob/master/Images/GameOfLife1.PNG)
```python GameOfLife.py```
![Glider](https://github.com/aivan6842/CellularAutomata/blob/master/Images/Glider.PNG)


## CellularAutomata 1-D
In `CellularAutomata.py` the rule is given by a single 8-bit binary value, thus having 256 rules (0-255). For example, for rule 30 this corresponds to the following: 
![Rule 30](https://github.com/aivan6842/CellularAutomata/blob/master/Images/Rule30Explain.PNG)

### Running the Script
Prior to running this script please ensure that you have ```pygame``` installed. This script can be run from the command line or from any IDE. To run from command line simply write the follwing and specify the parameter:
``` main.py -w <# of cells wide> -h <# of cells high> -r <rule #>```
By default ```width = 101```, ```height = 50``` and ```rule = 30```

### Sample Runs
```CellularAutomata.py -r 90```
![Rule 90](https://github.com/aivan6842/CellularAutomata/blob/master/Images/Rule90.PNG)
```CellularAutomata.py -r 30```
![Rule 30](https://github.com/aivan6842/CellularAutomata/blob/master/Images/Rule30.PNG)
```CellularAutomata.py -r 147```
![Rule 147](https://github.com/aivan6842/CellularAutomata/blob/master/Images/Rule147.PNG)


