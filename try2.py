# coding: utf-8
get_ipython().magic(u'run get_concerned_countries.py')
INFO = INFO.sort_values("MATH_MEAN", ascending = False)
get_ipython().magic(u'paste')
pisa2012
america_pisa = pisa2012[pisa2012["CNT"] == "United States of America"]
america_pisa
plt.scatter(x = "ESCS", y = "MATH", data = america_pisa)
plt.show()
america_pisa = america_pisa.sample(n = 500)
america_pisa
plt.scatter(x = "ESCS", y = "MATH", data = america_pisa)
plt.show()
america_pisa = america_pisa[["ESCS", "MATH"]]
america_pisa
