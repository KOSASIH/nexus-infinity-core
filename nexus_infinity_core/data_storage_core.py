import pandas as pd
from sqlalchemy import create_engine

class DataStorageCore:
    """
    Data Storage Core for efficient data management and retrieval.

    Attributes:
    -----------
    database : sqlalchemy.Engine
        Database engine for data storage.
    """

    def __init__(self, database_url):
        self.database = create_engine(database_url)

    def store_data(self, data):
        """
        Store data in the database.

        Parameters:
        -----------
        data : pandas.DataFrame
            Data to store.

        Returns:
        -------
        None
        """
        data.to_sql('data', con=self.database, if_exists='replace', index=False)

    def retrieve_data(self):
        """
        Retrieve data from the database.

        Returns:
        -------
        data : pandas.DataFrame
            Retrieved data.
        """
        data = pd.read_sql_table('data', con=self.database)
        return data

    def query_data(self, query):
        """
        Query data from the database.

        Parameters:
        -----------
        query : str
            SQL query to execute.

        Returns:
        -------
        results : pandas.DataFrame
            Query results.
        """
        results = pd.read_sql_query(query, con=self.database)
        return results
