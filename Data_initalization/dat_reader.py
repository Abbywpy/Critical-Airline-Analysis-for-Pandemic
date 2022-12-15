# import numpy as np
# c = np.fromfile('airlines.dat')
import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf)
df = pd.read_table('./routes.dat', sep=',', header=None, engine='python')

#df.columns = (['user_id', 'item_id', "rating", "timestamp"])
# flight_category = np.array(df[8].tolist())
#
# for index,i in enumerate(flight_category):
#     if len(i.split(' '))>1:
#         #print()
#         flight_category[index]=list(i.split(' '))[0]
# print(np.unique(flight_category))
#
