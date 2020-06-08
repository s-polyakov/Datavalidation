# example of usage validate_dict function
import pandas as pd
from datavalidation import validate_dict

s1 = pd.Series(['a', 'b', 'c'])
s2 = pd.Series(['a2', 'b2', 'c2'])
d1 = {'1': s1, '2': s2}
r1 = validate_dict('', d1)
print('data', d1)
print('result', r1)

