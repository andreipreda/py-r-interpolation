import pandas as pd
import numpy as np
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage
from rpy2.robjects import pandas2ri


def random_df() -> pd.DataFrame:
    return pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)),
                        columns=['a', 'b', 'c', 'd', 'e'])

def call_r(r_path: str) -> pd.DataFrame:
    """Using rpy2 to convert an R tibble data frame into a pandas data frame"""
    if not r_path:
        raise ValueError('r_path it is required')

    with open(r_path, 'r') as file:
        r_module = SignatureTranslatedAnonymousPackage(file.read(), 'r_module')

    # get_tibble it's known to exists 
    # otherwise an abstract class shall be done to ensure the contract
    rdf = r_module.get_tibble()
    return pandas2ri.rpy2py_dataframe(rdf)
