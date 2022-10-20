"""Project tests"""
import mltn
import numpy as np

def test_random_timeseries():
    ts_df = mltn.generate_random_timeseries('2022-09-01', '2022-10-01', 'option_a')

    assert not ts_df.empty

    assert 'date' in ts_df.columns
    assert ts_df.date.dtype == np.dtype('datetime64[ns]')
    
    assert 'quantity' in ts_df.columns
    assert ts_df.quantity.dtype == float
