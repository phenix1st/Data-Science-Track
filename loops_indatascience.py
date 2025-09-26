import numpy as np

for x, y in my_dictionnairy.items() : 
    print(" this {x} and {y}") # this way it will print the content of a dictionnairy 
    # my_dic = { jacl : jkds , ksjds : jjdsk }


means = np.array([np_1darray , np2_1darray])
for x in np.nditer(means) :
    print(x) # it will print each element in the the 2d array rather than printing the whole first array in the
    # in the first iteration and the whole second array in the second iteration


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() : 
    cars.loc[lab,"COUNTRY"] = row["country"].upper()


# Print cars
print(cars)