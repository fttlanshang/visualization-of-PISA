# coding: utf-8
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

pisa2012 = pd.read_csv('pisa2012.csv')
pisa2012 = pisa2012[["CNT","SUBNATIO","STRATUM","OECD","NC","SCHOOLID","STIDSTD",
	"ST04Q01", "ESCS", "PV1MATH","PV2MATH", "PV3MATH", "PV4MATH","PV5MATH",
	"W_FSTUWT"]]
# pisa2012_korea = pisa2012[pisa2012.CNT == "Korea"]
# pisa2012_japan = pisa2012[pisa2012.CNT == 'Japan']
# len(pisa2012_japan)
# pisa2012_macao = pisa2012[pisa2012.CNT == "Macao-China"]
# len(pisa2012_macao)
# pisa2012_hongkong = pisa2012[pisa2012.CNT == "Hong Kong-China"]
# len(pisa2012_hongkong)
# for cnt in pisa2012.CNT: # this is not consistent with the code book
#     if "Shang" in cnt:
#         print cnt
#         break  
# pisa2012_shanghai = pisa2012[pisa2012.CNT == "China-Shanghai"]
# len(pisa2012_shanghai)

# pisa2012_concerned_asian_countries = pd.concat([pisa2012_japan, pisa2012_korea, pisa2012_macao, pisa2012_hongkong, pisa2012_shanghai])
# len(pisa2012_concerned_asian_countries)

#thought boxplot is much more clear
# math_distribution = sns.violinplot(x="CNT", y = "PV1MATH", data = pisa2012_concerned_asian_countries)
# plt.show()
# math_distribution_whole = sns.violinplot(x="CNT", y = "PV1MATH", data = pisa2012)
# plt.show()
# pisa2012["CNT"].nunique() #68 countries

# draw math/read/science score relatively for three asian countries
# sns.boxplot(x="CNT", y = "PV1MATH", hue="ST04Q01", data = pisa2012_concerned_asian_countries)
# plt.show()
# sns.boxplot(x="CNT", y = "PV1READ", hue="ST04Q01", data = pisa2012_concerned_asian_countries)
# plt.show()
# sns.boxplot(x="CNT", y = "PV1SCIE", hue="ST04Q01", data = pisa2012_concerned_asian_countries)
# plt.show()

#########Thinks comparing only 3 contries is not enough###################################################




###############Below is for calculating mean for each country################
melted = pd.melt(pisa2012, 
	id_vars = ["CNT", "SUBNATIO","STRATUM","OECD","NC","SCHOOLID",
				"STIDSTD","ST04Q01", "ESCS", "W_FSTUWT"],
	var_name="PHASE", 
	value_name="SCORE")

def weighted_avg(group, avg_name, weight_name):
    d = group[avg_name]
    w = group[weight_name]
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return d.mean()
    
country_phase_math_means = melted.groupby(["CNT","PHASE"]).apply(weighted_avg, "SCORE","W_FSTUWT")
CNT_MATH_MEAN = country_phase_math_means.groupby("CNT").mean() # this is series data, not dataframe
CNT_MATH_MEAN = pd.DataFrame({
	"CNT": CNT_MATH_MEAN.index, 
	"MATH_MEAN": CNT_MATH_MEAN.values
})

CNT_MATH_MEAN.sort_values("MATH_MEAN", ascending=False)

pisa2012["MATH"] = (pisa2012["PV1MATH"] + pisa2012["PV2MATH"] + pisa2012["PV3MATH"] + pisa2012["PV4MATH"] + pisa2012["PV5MATH"]) / 5
countries = CNT_MATH_MEAN["CNT"]
slopes = []
strengths  = []

def cal_linear_regression():
    for country in countries:
        country_escs_math_data = pisa2012[pisa2012["CNT"] == country][["MATH", "ESCS"]] 
        country_escs_math_data = country_escs_math_data.dropna() # need to draw nan values!!
        x = np.array(country_escs_math_data["ESCS"])
        y = np.array(country_escs_math_data["MATH"])
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        slopes.append(slope)
        strengths.append(r_value**2)
          
