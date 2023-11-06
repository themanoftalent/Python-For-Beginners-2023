dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}

import pandas as pd

brics = pd.DataFrame (dict)
print (brics)
print('-'*48)
newDict = {'Ulke': ['Turkiye', 'Rusya', 'Afgan', 'Irak'],
           'Baskent': ['Istanbuk', 'Moskova', 'kabil', 'Bagdat'],
           'Nufus': [80000, 123000, 45000, 34000],
           'yuzolcum': [784, 12356, 345, 125]}
import pandas as pd

devam=pd.DataFrame(newDict)
devdam=pd.datetools

print(devam)
print('-'*48)
print(devdam)