# General

This Python tool is created to parse a list of MTG Cards and retrieve its minimum (cheapest) available price from three Australian TCG stores:

- GUF (https://guf.com.au/)
- MTGMate (https://www.mtgmate.com.au/)
- GoodGames (https://tcg.goodgames.com.au/)

# Instructions

## Input (`inputfile`)

An acceptable input is a plain-text file that contains a list of MTG singles in one of the following formats:

- Card Names only
```
Llanowar Elves
Sol Ring
Mana Crypt
Mana Confluence
```
- {Quantity}x Card Names
```
50x Llanowar Elves
20x Sol Ring
20x Mana Crypt
30x Mana Confluence
```
*(Note that the tool only checks for availability for **a single card**. The quantity is simply disregarded.)*

## Output (`inputfile--output.csv`)

```
Cards,GUF,MTGMate,GoodGames
Llanowar Elves,0.4,1.0,0.5
Sol Ring,7.1,6.0,20.0
Mana Crypt,299.0,228.0,
Mana Confluence,42.1,41.0,
```

## How-to Use

1. First, install dependencies by:
   ```
   pip install requirements.txt
   ```

2. Then:
   ```
   python -m mtgaulookup {inputfile}
   ```

# Version

## v1.0 2020/05/25 

- init version

# Future Improvements & To-Do

- [ ] Star City Games (SCG) scraping
- [ ] MTG Mint scraping
- [ ] Concurrency | Asynchronous Processing to increase performance