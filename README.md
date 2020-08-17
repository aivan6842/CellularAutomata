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
![Rule 30]()

```main.py -r 147```
![Rule 147]()
