import pandas as pd
import numpy as np

def sample():
    data = {
        "Column1": np.random.randint(1, 100, 5),  # Random integers between 1 and 100
        "Column2": np.random.choice(["A", "B", "C", "D", "E"], 5),  # Random selection from a list
        "Column3": np.random.uniform(0, 1, 5),  # Random floats between 0 and 1
    }
    sample_df = pd.DataFrame(data)

    print(sample_df.head())

if __name__ == "__main__":
    sample()