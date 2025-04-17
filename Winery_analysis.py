import pandas as pd
import numpy as np 

DATA_PATH ="/home/user01/prac_python/Data_wine/winemag-data-130k-v2.csv"

def load_data(fpath):

    """ Load the  CSV  file  """
    try:
        df = pd.read_csv(fpath,index_col = 0)
        #df_clean = df.dropna()
        return df
    except FileNotFoundError:
        print(f" file not  found")

        return df


def data_cleaning(df):

    grp = df.groupby(['variety','province','winery'])
    v_grp = grp['points']
    v_mean = v_grp.mean()
    print("*******************************\n")
    print(v_mean)
    print("---------------------------------\n")
    grp1 = df.groupby(['country','taster_name'])
    v_grp1 = grp1['price']
    print(v_grp1.mean())


def Country_winery_price(df,cnty):

    print( df.loc[:,['country','winery','price']])

    print("=======================================")

    print(df.loc[df.country == cnty])


def Coutry_province_variety(df):
    print("=======================================")

    print(df.loc[:,['country','province','variety']])

def Data_Aggregation(df):

    grouped = df['price'].groupby(df['country'])

    print(grouped.mean())
   
    grouped_01 = df['price'].groupby([df['country'],df['variety'],df['winery']]).mean()
    grouped_001= df['price'].groupby([df['country'],df['variety'],df['winery']])
    

    grouped_02 = df['price'].groupby([df['country'],df['province'],df['region_1'],df['region_2']]).mean()
    print(grouped_02)
            
    grouped_03= df['price'].groupby([df['country'],df['province'],df['taster_name'],df['taster_twitter_handle']]).median()
    print(grouped_03)
    print(f"type: { type(grouped_03)}")
    

    quartiles = pd.cut(df['price'],4)

    print(" -----   Quattiles   ------")

    print(quartiles)
    
    


def print_data(dt):

    print(f" DataFrames \n {dt.info()}")
    print("\n-------------------------------")

    print(dt.head,4)
    print("//////////////////////////////////")
    lt_drop = ['description','designation','taster_name','taster_twitter_handle','title']
    dt_changed = dt.drop(lt_drop,axis =1)

    print(dt_changed.info())

    print(dt_changed['country'].is_unique)


def main():
    print("Loading  the  data ....")
    
    df = load_data(DATA_PATH)
    
    print_data(df )

    
    #Country_variety_price(df,'Italy')
    df_cleaned = df.dropna()
    
    print(" Cleaned  Data Frame: ")
    
    print(df.loc[:,['region_1']])

    print(df_cleaned.loc[:,['region_1']])
    print(df_cleaned.loc[:,['region_2']])
    
    Data_Aggregation(df)

    #Country_winery_price(df,'Italy')
    
    #Country_winery_price(df,'Mexico')
   
    
main()
