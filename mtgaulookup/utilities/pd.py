import pandas as pd
import os, re, time
from mtgaulookup.scrape import guf, goodgames, mtgmate


def run(file):
    
    df = pd.read_csv(file, header= None, names= ['Cards'])
    for i in range(len(df['Cards'])):
        card = re.sub(r'^[\d]+x[\s]+', '', df.iloc[i]['Cards'])

        df.loc[i, ('GUF')] = guf.lookup(card)
        df.loc[i, ('MTGMate')] = mtgmate.lookup(card)
        df.loc[i, ('GoodGames')] = goodgames.lookup(card)

    df.to_csv(file + '--ouput.csv', index= None)
    return True

