import sys, os
from mtgaulookup.utilities import pd


if __name__ == '__main__':

    try:
        sys.argv[1]
    except:
        print('Please specify input file.')

    if os.path.isfile(sys.argv[1]):
        file = os.path.abspath(sys.argv[1])
        pd.run(file)
    else:
        print('File doesn\'t exist.')
        sys.exit()

