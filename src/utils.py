import numpy as np


def data_splitting(length, train_ratio=0.6, val_ratio=0, test_ratio=0):
    """
    Split sample indices into train, validation, and test subsets.

    Parameters
    ----------
    length : int or array-like
        Total number of samples to split. Can be a scalar or array of lengths
        for multiple matrices.
    train_ratio : float, optional
        Fraction of samples assigned to the training split. Default is 0.6.
    val_ratio : float, optional
        Fraction of samples assigned to the validation split. Default is 0.
    test_ratio : float, optional
        Fraction of samples assigned to the test split. Default is 0.

    Returns
    -------
    tuple of ndarray or tuple of tuple of ndarray
        If length is scalar: A tuple ``(train_idx, val_idx, test_idx)`` containing 
        shuffled indices for each split.
        If length is array-like: A tuple of tuples, where each inner tuple contains 
        ``(train_idx, val_idx, test_idx)`` for the corresponding length.
        If the sum of ratios is less than 1, the remaining samples are not 
        included in any returned split.

    Raises
    ------
    ValueError
        If any ratio is negative, if the sum of ratios exceeds 1, or if
        ``train_ratio`` is zero.
    """
    ratios = np.array([train_ratio, val_ratio, test_ratio])

    if np.any(ratios < 0):
        raise ValueError("Ratios must be non-negative.")

    if np.sum(ratios) > 1:
        raise ValueError("Sum of ratios must not exceed 1.")

    if ratios[0] == 0:
        raise ValueError("At least the training split ratio must be greater than zero.")

    # Handle both scalar and array inputs
    lengths = np.atleast_1d(length)
    is_scalar = np.isscalar(length)

    all_indices = []
    seed = np.random.randint(0, 1000)
    for l in lengths:
        rng = np.random.default_rng(seed)  
        shuffled_indices = rng.permutation(l)

        train_end = int(ratios[0] * l)
        val_end = int((ratios[0] + ratios[1]) * l)
        test_end = int((ratios[0] + ratios[1] + ratios[2]) * l)

        train_idx = shuffled_indices[:train_end]
        val_idx = shuffled_indices[train_end:val_end]
        test_idx = shuffled_indices[val_end:test_end]

        all_indices.append((train_idx, val_idx, test_idx))

    # Return scalar result if input was scalar
    if is_scalar:
        return all_indices[0]
    else:
        return tuple(all_indices)