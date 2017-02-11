import pandas as pa
import numpy as np


col1 = [i for i in range(4)]
col2 = [float(i**2) for i in range(4) ]
col3 = ['cat1', 'cat2', 'cat3', 'cat1']

MyDataframe = pa.DataFrame({'INDEX':col1,
                  'DATE':pa.Timestamp('20130102'),
                  'SQUARED':col2,
                  'THREE':np.array([3]*4, dtype='int32'),
                  'SET':pa.Categorical(["test", "train",
                                        "test", "train"]),
                  'CAT':col3})


# print entire data frame
#print(MyDataframe)

# print only first 2 rows
#print(MyDataframe.head(2))

# print last 3 rows
#print(MyDataframe.tail(3))

# print the datatypes of the columns
#print(MyDataframe.dtypes)

# print columnames
#print(MyDataframe.columns)

# print the index
#print(MyDataframe.index)

# give a summary of the dataframe
#print(MyDataframe.describe)

# access a specific column
#print(MyDataframe['DATE'])
#rint(MyDataframe.DATE)

# access subset of rows
#print(MyDataframe[0:2])

# selecting by row and column
#print(MyDataframe.iloc[3,3])

# selecting by row and column
#print(MyDataframe.ix[3,'SQUARED'])

# filtering on a certain condition
#print(MyDataframe[MyDataframe['SET'] == 'test'])


# combining multiple conditions
# notice that unlike regular conditionals
# where you have to use 'and' or 'or'
# here you need the byte operators here &, |, != , etc.
# Also bracket your conditionals to avoid ambiguity
#print(MyDataframe[(MyDataframe['CAT'] == 'cat1') | (MyDataframe['SET'] != 'test')])


# add a column
MyDataframe['VALUES'] = [2,5,1,0.1]
MyDataframe['NUM_CAT'] = [1,1,2,3]
#print(MyDataframe)

# drop a column (two ways)
#MyDataframe.pop('THREE')
#MyDataframe = MyDataframe.drop('CAT',  axis=1)
#print(MyDataframe)

# vectorised operations on columns
#MyDataframe['DIVIDED'] = MyDataframe['VALUES']/MyDataframe['SQUARED']
#MyDataframe['VALUES'] = MyDataframe['VALUES'] * 100
#print(MyDataframe)


# column wide calcutions
#print(MyDataframe['VALUES'].median())
#print(MyDataframe['VALUES'].max())

# Apply a function for every columns
#print(MyDataframe.apply(max))

# Use a function on all rows in a column
def addset(string):
    return string + 'set'

MyDataframe['SET'] = MyDataframe['SET'].map(addset)
#print(MyDataframe)


# we can also use lambda functions
#MyDataframe['SET'] = MyDataframe['SET'].map(lambda x: x.upper())
#print(MyDataframe)

# we can also use lambda functions
#MyDataframe['SET'] = MyDataframe['SET'].map(lambda x: x.lower())
#print(MyDataframe)



# sorting on a column
MyDataframe= MyDataframe.sort_values(by='VALUES')
print(MyDataframe)

# sorting on multiple columns
MyDataframe= MyDataframe.sort_values(['NUM_CAT', 'VALUES'],
                                     ascending=[True, False])
print(MyDataframe)

MyDataframe.rename(columns={'INDEX':'PERSON'}, inplace = True)
## merging with other data frames
MyDataframe2 = pa.DataFrame({'PERSON':[2,3,1,0],
                             'VALUE2':[11,22,33,44]
                             })

# other options for how are 'inner', 'outer', 'right'
MyDataframe3 = pa.merge(MyDataframe, MyDataframe2,
                        how='left', on='PERSON')

print(MyDataframe3)

# notice that unlike R subsetting a dataframe
# does not reset rownumbers!!!!
Trainset = MyDataframe3[MyDataframe3['SET'] != 'trainset']
print(Trainset)

# resetting rownumbers
Trainset = Trainset.reset_index()
print(Trainset)

# notice the index has now become a column
# not to be confused with INDEX
# so columns in pandas case sensitive
# we can drop it
Trainset.pop("index")
print(Trainset)

