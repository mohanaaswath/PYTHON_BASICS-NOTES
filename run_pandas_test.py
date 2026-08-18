import sys
import os

# Remove any local folder named "Pandas" (case-insensitive) from sys.path so
# the installed third-party `pandas` package is imported instead of a local file/folder.
sys.path = [p for p in sys.path if not (p and os.path.basename(p).lower() == 'pandas')]

import pandas as pd

def main():
    print("Pandas version:", pd.__version__)
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
    print("DataFrame:")
    print(df)

if __name__ == '__main__':
    main()
