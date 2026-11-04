import numpy as np

from src.utils import data_splitting


def test_no_data_leakage():

    X = np.random.rand(100, 10)
    
    data_split_ratio = [0.3, 0.2, 0.2]
    
    indices = data_splitting(X.shape[0], *data_split_ratio)

    train_set = set(indices[0])
    val_set = set(indices[1])
    test_set = set(indices[2])
    
    # Assert pairwise intersections are completely empty
    assert train_set.isdisjoint(val_set), "Train and Val sets overlap!"
    assert train_set.isdisjoint(test_set), "Train and Test sets overlap!"
    assert val_set.isdisjoint(test_set), "Val and Test sets overlap!"