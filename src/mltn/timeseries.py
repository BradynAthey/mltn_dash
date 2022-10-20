import pandas as pd
import numpy as np
import time
import joblib

SEED_MAP = {'option_a': 0, 'option_b': 1, 'option_c': 2}

# in-memory cache for storing results of expensive computations
cache_memory = joblib.Memory('cache', verbose=True)

@cache_memory.cache
def generate_random_timeseries(start_date, end_date, option):

    # simulate time-intensive calculation
    time.sleep(2)
    dates = pd.date_range(start_date, end_date)
    # produce the same random outputs given the same inputs
    np.random.seed(SEED_MAP[option])
    quantities = np.random.randn(len(dates))
    return pd.DataFrame({'date': dates, 'quantity': quantities})