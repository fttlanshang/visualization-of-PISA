# coding: utf-8
get_ipython().magic(u'run get_concerned_countries.py')
math_distribution = sns.violinplot(x="CNT", y = "PV1MATH", data = pisa2012_concerned_asian_countries)
math_distribution.draw()
math_distribution
plt.show()
math_distribution_whole = sns.violinplot(x="CNT", y = "PV1MATH")
math_distribution_whole = sns.violinplot(x="CNT", y = "PV1MATH", data = pisa2012)
plt.show()
pisa2012["CNT"].nunique
pisa2012["CNT"].nunique()
sns.boxplot(x="CNT", y = "PV1MATH", data = pisa2012_concerned_asian_countries)
plt.show()
sns.boxplot(x="CNT", y = "PV1MATH", hue="ST04Q01", data = pisa2012_concerned_asian_countries)
plt.show()
sns.boxplot(x="CNT", y = "PV1READ", hue="ST04Q01", data = pisa2012_concerned_asian_countries)
plt.show()
sns.boxplot(x="CNT", y = "PV1SCIE", hue="ST04Q01", data = pisa2012_concerned_asian_countries)
plt.show()
sns.violinplot(x="CNT", y = "PV1SCIE", hue="ST04Q01", data = pisa2012_concerned_asian_countries)
plt.show()
sns.boxplot(x="CNT", y = "PV1SCIE", hue="ST04Q01", data = pisa2012_concerned_asian_countries)
plt.show()
get_ipython().magic(u'save try.py 1-22')
sns.violinplot(x="CNT", y = "PV1SCIE", hue="ST04Q01", data = pisa2012_concerned_asian_countries, palette="muted", split=True)
plt.show()
sns.boxplot(x="CNT", y = "PV1MATH", hue="ST04Q01", data = pisa2012_concerned_asian_countries, palette="muted", split=True)
plt.scatter(x = "ESCS", y = "PV1MATH", data = pisa2012)
plt.show()
plt.scatter(x = "ESCS", y = "PV1MATH", data = pisa2012, alpha = 1/20)
plt.show()
plt.scatter(x = "ESCS", y = "PV1MATH", data = pisa2012, alpha = 0.05)
plt.shjow()
plt.show()
plt.scatter(x = "ESCS", y = "PV1MATH", data = pisa2012[pisa2012["CNT"]=="China-Shanghai"], alpha = 0.05)
plt.show()
pisa2012_math_escs = pisa2012[["CNT", "SUBNATIO","STRATUM","OCED","NC","SCHOOLID","STIDSTD","PV1MATH","PV2MATH","PV3MATH","PV4MA","PV5MATH","W_FSTUWT"]]
pisa2012_math_escs = pisa2012[["CNT", "SUBNATIO","STRATUM","OECD","NC","SCHOOLID","STIDSTD","PV1MATH","PV2MATH","PV3MATH","PV4MATH","PV5MATH","W_FSTUWT"]]
pisa2012_math_escs
melted = pd.melt(pisa2012_math_escs, id_vars = ["CNT", "SUBNATIO","STRATUM","OECD","NC","SCHOOLID","STIDSTD","W_FSTUWT"], var_name="PHASE", value_name="SCORE")
melted
def weighted_avg(group, avg_name, weight_name):
    d = group[avg_name]
    w = group[weight_name]
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return d.mean()
    
country_phase_math_means = pisa2012_math_escs.groupby("CNT","PHASE").apply(weighted_avg, "SCORE","W_FSTUWT")
pisa2012_math_escs
country_phase_math_means = melted.groupby("CNT","PHASE").apply(weighted_avg, "SCORE","W_FSTUWT")
melted
type(melted)
melted["PHASE"]
country_phase_math_means = melted.groupby(["CNT","PHASE"]).apply(weighted_avg, "SCORE","W_FSTUWT")
country_phase_math_means
CNT_MATH_MEAN = country_phase_math_means.groupby("CNT").mean()
CNT_MATH_MEAN
get_ipython().magic(u'save cal_mean.py')
