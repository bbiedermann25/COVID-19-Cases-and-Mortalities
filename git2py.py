import pandas as pd 

#In this file I will be using the github data and pandas to grab data from github.
#First thing we can do is use the read csv function in pandas to read the raw github
#data.

data = pd.read_csv("https://raw.githubusercontent.com/BroadStreet-Health/COVID-19-Cases-and-Mortalities/master/Coronavirus_by_County.csv", low_memory = False)

# data:
#                 region  state_fips  ... mort_022721 pbmort_022721
# 0            southeast         1.0  ...          81            10
# 1            southeast         1.0  ...         213            70
# 2            southeast         1.0  ...          34            17
# 3            southeast         1.0  ...          34            26
# 4            southeast         1.0  ...         107            20
# ...                ...         ...  ...         ...           ...
# 3267  u.s. territories        72.0  ...           0             0
# 3268  u.s. territories        72.0  ...           0             0
# 3269  u.s. territories        72.0  ...           0             0
# 3270  u.s. territories        72.0  ...           0             0
# 3271  u.s. territories        72.0  ...        1733           303

# [3272 rows x 2278 columns]

#formats:
#County: "Name County, State"
#State: "XX"
#date: "mmddyy"

County = 'DuPage County, Illinois'
State = 'IL'
date = '010121'

tstpos = 'tstpos_' + date
pbpos = 'pbpos_' + date
mort = 'mort_' + date
pbmort = 'pbmort_' + date

index = data.index[data['county'] == County].tolist()[0]
Statistics = [data.at[index, tstpos], data.at[index, pbpos], data.at[index, mort], data.at[index, pbmort]]
print(Statistics)
#[62300, 0, 974, 0]