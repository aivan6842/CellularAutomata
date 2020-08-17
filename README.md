# Cellular Automata

## Description
This is script I wrote that can be run from the command line to see the different patterns that each rule can generate. As described in [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/cellular-automata/) cellular automata is a process in which discrete units (cells) will interact with one another to form the next automaton (row) based on an extremely simple rule. For this implementation I have chosen the rule to be a value that can be represented as a 8-bit binary number (0-255). Starting from a row with a single live cell, extremely intricate patterns can be made from applying many interations.

## Running the Script
Prior to running this script please ensure that you have ```pygame``` installed. This script can be run from the command line or from any IDE. To run from command line simply write the follwing and specify the parameter:
``` main.py -w <# of cells wide> -h <# of cells high> -r <rule #>```
By default ```width = 101```, ```height = 50``` and ```rule = 30```

### Sample Runs
```main.py -r 90```
![Rule 90](https://github.com/aivan6842/CellularAutomata/blob/master/Images/Rule90.PNG)
```main.py -r 30```
![Rule 30](https://github.com/aivan6842/CellularAutomata/blob/master/Images/Rule30.PNG)

```main.py -r 147```
![Rule 147](https://github.com/aivan6842/CellularAutomata/blob/master/Images/Rule147.PNG)

## My Motivations
Very early in my days of computing I came along cellular automata but didn't quite understand it. A few years later I listened to a podcast interviewing Lex Fridman who talked about Nick Bostrom's famous simulation hypothesis. Lex went on to explain how the idea of having something so simple generate very complex patterns can be one way that reality could have potentially been simulated. Obviously Lex was not suggesting that something like the script I wrote can be used to simulate reality, but just the idea its self that having something so simple like a single decimal value between 0-255 can generate such sophisticated patterns was very intriguing and I decided to dig deeper. From the outside the concept of this project seemed extremely easy and to be completely honest it wasn't the hardest project I have ever worked on. However, I thoroughly enjoyed learning about cellular automata and the different contributions its has made to the scientific world. To me, it seemed that the more I dig into this idea, the more I uncovered or learned. 
