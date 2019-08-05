import pandas as pd


# Define a Students Directory using "dictionary

class PandasFeatures:
    """
    Describing various pandas Features
    """
    def iterate_df_columns_index(self):
        """
        Args:

        Return:

        """

        # Define a dictionary containing students data
        data = {'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka'],
                'Age': [21, 19, 20, 18],
                'Stream': ['Math', 'Commerce', 'Arts', 'Biology'],
                'Percentage': [88, 92, 95, 70]}

        print(data)

        # Convert the dictionary into DataFrame
        df = pd.DataFrame(data, columns = ['Name', 'Age', 'Stream', 'Percentage'])

        print("Given Dataframe :\n{df.}")


if __name__ == "__main__":
    """
    Mani Functions
    """
    pandas_features = PandasFeatures()
    pandas_features.iterate_df_columns_index()
