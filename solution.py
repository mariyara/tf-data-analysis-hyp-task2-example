import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 558620654 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    p_val = anderson_ksamp([x, y])[2]
    return p_val < 0.09
   
