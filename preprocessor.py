import pandas as pd 

df=pd.read_csv('noc_regions.csv')
region_df=pd.read_csv('athlete_events.csv')

def preprocess(df):
    df,region_df
    #filtering for summer olympics
    df=df[df['Season']=='Summer']
    #merge with region df
    df=df.merge(region_df,on='NOC',how='left')
    #drop duplicates
    df.drop_duplicates(inplace=True)
    #one hot encoding for medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
