# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas
import numpy



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pandas.read_csv('SalesTable.csv')
    print(df)
    SOLD = df[(df['Sold'] == "Y")].shape[0]
    MRCNT = df[(df['Moon Roof'] == "Y") * (df['Sold'] == "Y")].shape[0]
    PMRES = df[(df['Moon Roof'] == "Y") * (df['Sold'] == "Y")].shape[0]/df[(df['Sold'] == "Y")].shape[0]
    PMRNS = df[(df['Moon Roof'] == "Y") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "N")].shape[0]
    PMRNES = df[(df['Moon Roof'] == "N") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "Y")].shape[0]
    PMRNENS = df[(df['Moon Roof'] == "N") * (df['Sold'] == "N")].shape[0] / df[(df['Sold'] == "N")].shape[0]
    PMRNSE = df[(df['Sold'] == 'N') * (df['Moon Roof'] == "Y")].shape[0] /df[(df['Moon Roof'] == "Y")].shape[0]
    #-------------------------------
    SRCNT = df[(df['Spinning Rims'] == "Y") * (df['Sold'] == "Y")].shape[0]
    PSRES = df[(df['Spinning Rims'] == "Y") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "Y")].shape[0]
    PSRNS = df[(df['Spinning Rims'] == "Y") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "N")].shape[0]
    PSRNES = df[(df['Spinning Rims'] == "N") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "Y")].shape[0]
    PSRNENS = df[(df['Spinning Rims'] == "N") * (df['Sold'] == "N")].shape[0] / df[(df['Sold'] == "N")].shape[0]
    PSRNSE = df[(df['Sold'] == 'N') * (df['Spinning Rims'] == "Y")].shape[0] / df[(df['Spinning Rims'] == "Y")].shape[0]
    #-------------------------------
    DCNT = df[(df['Decals'] == "Y") * (df['Sold'] == "Y")].shape[0]
    PDES = df[(df['Decals'] == "Y") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "Y")].shape[0]
    PDNS = df[(df['Decals'] == "Y") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "N")].shape[0]
    PDNES = df[(df['Decals'] == "N") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "Y")].shape[0]
    PDNENS = df[(df['Decals'] == "N") * (df['Sold'] == "N")].shape[0] / df[(df['Sold'] == "N")].shape[0]
    PDNSE = df[(df['Sold'] == 'N') * (df['Decals'] == "Y")].shape[0] / df[(df['Decals'] == "Y")].shape[0]
    #-------------------------------
    TWCNT = df[(df['Tinted Windows'] == "Y") * (df['Sold'] == "Y")].shape[0]
    PTWES = df[(df['Tinted Windows'] == "Y") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "Y")].shape[0]
    PTWNS = df[(df['Tinted Windows'] == "Y") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "N")].shape[0]
    PTWNES = df[(df['Tinted Windows'] == "N") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "Y")].shape[0]
    PTWNENS = df[(df['Tinted Windows'] == "N") * (df['Sold'] == "N")].shape[0] / df[(df['Sold'] == "N")].shape[0]
    PTWNSE = df[(df['Sold'] == 'N') * (df['Tinted Windows'] == "Y")].shape[0] / df[(df['Tinted Windows'] == "Y")].shape[0]
    #-------------------------------
    BLCNT = df[(df['Body Lift'] == "Y") * (df['Sold'] == "Y")].shape[0]
    PBLES = df[(df['Body Lift'] == "Y") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "Y")].shape[0]
    PBLNS = df[(df['Body Lift'] == "Y") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "N")].shape[0]
    PBLNES = df[(df['Body Lift'] == "N") * (df['Sold'] == "Y")].shape[0] / df[(df['Sold'] == "Y")].shape[0]
    PBLNENS = df[(df['Body Lift'] == "N") * (df['Sold'] == "N")].shape[0] / df[(df['Sold'] == "N")].shape[0]
    PBLNSE = df[(df['Sold'] == 'N') * (df['Body Lift'] == "Y")].shape[0] / df[(df['Body Lift'] == "Y")].shape[0]
    
    Prediction1 = PMRES*PSRNES*PDNES*PTWNENS*PBLNES*SOLD
    print("P(Moon Roof|Sold), P(Moon Roof|Not Sold)")
    print(Prediction1, PMRNSE)
    print("P(Spinning Rims|Sold), P(Spinning Rims|Not Sold)")
    Prediction2 = PMRNSE*PSRES*PDNES*PTWNENS*PBLNES*SOLD
    print(Prediction2, PSRNSE)
    print("P(Decals|Sold), P(Decals|Not Sold)")
    Prediction3 = PMRNSE*PSRNES*PDES*PTWNENS*PBLNES*SOLD
    print(Prediction3,PDNSE)
    print("P(Tinted Windows|Sold), P(Tinted Windows|Not Sold)")
    Prediction4 = PMRNSE*PSRNES*PDNES*PTWNES*PBLNES*SOLD
    print(Prediction4,PTWNSE)
    print("P(Body Lift|Sold), P(Body Lift|Not Sold)")
    Prediction5 = PMRNSE*PSRNES*PDNES*PTWNENS*PBLES*SOLD
    print(Prediction5,PBLNSE)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
