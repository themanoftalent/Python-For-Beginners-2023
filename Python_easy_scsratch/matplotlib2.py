import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_json('df.json')

df.to_html('fg.html')

print(df)

df.plot()
plt.show()
