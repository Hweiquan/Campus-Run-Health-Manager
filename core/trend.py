import numpy as np


def moving_avg(data, window=3):
    if len(data) < window:
        return data
    return np.convolve(data, np.ones(window)/window, mode='valid')


def weight_trend(weights):
    if len(weights) < 2:
        return "stable"

    diff = weights[-1] - weights[0]

    if diff < -0.5:
        return "decreasing"
    elif diff > 0.5:
        return "increasing"
    else:
        return "stable"