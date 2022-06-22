'''
dataset: matrix of positive floating point numbers
        Some parts of the data is missing and instead of actual value it's 0

Task:
    1. Replace each 0 with the mean of the non-zero values in its column
    2. Normalize the matric in such a way that:
        - the mean value of each column is zero
        - std of each column is 1

'''
import pandas as pd
import numpy as np

def transform_data(data):

    ## Task 1
    df = pd.DataFrame(data,
                    columns=['a', 'b', 'c'])

    zero_cols = []
    for col in df.columns:
        if df[df[col]==0].shape[0]>0:
            zero_cols.append(col)

    for col in zero_cols:
        # print(f'mean for col {col} is {df[df[col]!=0][col].mean()}')
        val_to_impute = df[df[col]!=0][col].mean()
        df.loc[df[col]==0, col] = val_to_impute  ## Imputation of zero values to mean of non-zeros -- the dataframe is being updated in place


    ## Task 2

    array = np.array(df)
    final_array = (array - array.mean(axis=0))/ array.std(axis=0) ## Normalizing the dataset to make mean=0 and std=1
    return (final_array)

if __name__ == '__main__':
    data = [[1, 2, 0],
            [0, 1, 1],
            [5, 6, 5]]
    print(transform_data(data))
    