import pandas as pd



# def filtercolumnarguments(df, columnname, *columnAttributes):
#     if(len(columnAttributes)==1):
#         print(len(columnAttributes))
#         return df[(df.columnname==columnAttributes)]
#     elif(len(columnAttributes)==2):
#         return df[(df.columnname==columnAttributes[0]) | (df.columnname==columnAttributes[1])]
#     elif(len(columnAttributes)==3):
#         return df[(df.columnname==columnAttributes[0]) | (df.columnname==columnAttributes[1]) | (df.columnname==columnAttributes[2])]
#     elif(len(columnAttributes)==4):
#         return df[(df.columnname==columnAttributes[0]) | (df.columnname==columnAttributes[1]) | (df.columnname==columnAttributes[2]) | (df.columnname==columnAttributes[3])]
#     else: raise Exception("Sorry wrong number of column attributes")

#
#
df = pd.read_csv("/home/cedcoss/Music/file.csv")


def mycsv():
        print(df)
    # df2=filtercolumnarguments(df,"Jurisdiction_Level","State")
    # print(df2)
    # df2.to_csv("/home/cedcoss/Music/what.csv")
        df3 = df[(df.Jurisdiction_Level == "State")]
        print(df3)
    # df4 = df3[(df3.Jurisdiction_Name == "FL") | (df3.Jurisdiction_Name == "KS") | (df3.Jurisdiction_Name == "TN")]
    # print(df4)
        df3.to_csv('/home/cedcoss/Music/New1Csv.csv')

#

