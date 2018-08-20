import os.path
import pandas as pd
import numpy as np


dir_path = os.path.dirname(os.path.realpath(__file__))


# File names for stored dataframes
VISITOR_CSV = os.path.join(dir_path, 'data.csv')
UNIQUE_VISITS_PKL = os.path.join(dir_path, 'unique_visitors.pkl')


def init_unique_visitor_dataframe():
    # Check if dataframe has been cached
    if os.path.isfile(UNIQUE_VISITS_PKL):
        return pd.read_pickle(UNIQUE_VISITS_PKL)

    # Load csv into dataframe
    visitors = pd.read_csv(VISITOR_CSV,
                           header=None,
                           names=['time', 'id', 'os', 'device'],
                           usecols=['id', 'os', 'device'],
                           dtype={'id': np.int64,
                                  'os': np.int8,
                                  'device': np.int8})

    # Add a column for number of visits
    visitors['visits'] = pd.Series(1, index=visitors.index)

    # Group into unique visits
    visitors = visitors.groupby(['id', 'os', 'device']).count()

    # Cache dataframe
    visitors.to_pickle(UNIQUE_VISITS_PKL)

    return visitors


class VisitorData():
    # Panda dataframes containing visitor information
    uniqueVisitors = init_unique_visitor_dataframe()


    def get_unique_users_count(self, os=[], device=[]):
        if not os and not device:
            return self.uniqueVisitors.index.get_level_values('id').nunique()

        return (self.uniqueVisitors
                    .loc[self.uniqueVisitors.index.get_level_values('os').isin(os) |
                         self.uniqueVisitors.index.get_level_values('device').isin(device)]
                    .index.get_level_values('id').nunique())


if __name__ == '__main__':
    data = VisitorData()
    print(data.get_unique_users_count())
    print(data.get_unique_users_count(os=[1,2], device=[1,2]))