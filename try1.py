# coding: utf-8
INFO = INFO.sort_values("MATH_MEAN")    
INFO.iloc[0:22]["MATH_MEAN"] = 1
# INFO.loc[0:22,"MATH_MEAN"] = 1
INFO.iloc[22:45]["MATH_INDEX"] = 2
INFO.iloc[45:67]["MATH_INDEX"] = 3

INFO = INFO.sort_values("strength", ascending=False)
INFO.iloc[45:67]["RELATION_INDEX"] = 3
INFO.iloc[22:45]["RELATION_INDEX"] = 2
INFO.iloc[0:22]["RELATION_INDEX"] = 1
len(INFO[INFO["RELATION_INDEX"] == 2])
len(INFO[INFO["RELATION_INDEX"] == 1])
len(INFO[INFO["RELATION_INDEX"] == 3])
INFO.to_csv("INFO_PISA2012.csv")
