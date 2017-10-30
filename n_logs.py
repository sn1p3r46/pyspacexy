import matplotlib.pyplot as plt

msc_nlog = [
32322009,
32071631,
20523653,
16554370,
31223705,
30699775,
30898270,
30582162,
31927218,
20157715,
16371842,
32904470,
31342864,
31139294,
30715679,
32343246,
20170505,
17516282,
32023860,
31677915,
31691740,
31445919,
33167091,
21393693,
17129135,
32697568,
30607875,
31012492,
30863566,
31589414,
23551233
]
 # 868316191 total

ngprs_nlog = [
200481896,
209846749,
175247554,
154912227,
197542920,
198589583,
195186950,
195684992,
198868669,
167326442,
147854951,
184870141,
184987337,
186549796,
188476745,
195436279,
166649923,
147448188,
186684693,
189522102,
191101557,
193500215,
199970865,
169183219,
147292943,
185573325,
189287809,
195457206,
194332921,
200351695,
177472802]

# 5715692694 total

crm_nlog = [
5606287,
5604649,
5603908,
5604849,
5604829,
5604263,
5604279,
5606520,
5607272,
5606615,
5609192,
5609193,
5609133,
5606724,
5606593,
5607163,
5606894,
5605676,
5605396,
5607755,
5610963,
5612214,
5612221,
5612176,
5612007,
5611825,
5609780,
5614661,
5616341,
5615248,
5614380]

# 173869006 total

x = range(1,32)
plt.plot(x,msc_nlog)


plt.xlabel('Day')
plt.ylabel('MSC - Number of Daily Logs')
plt.title('MSC - Number of Logs Over Time')

# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
plt.grid(True)
axes = plt.gca()
axes.set_xlim([1,31])
plt.show()


plt.plot(x,ngprs_nlog)


plt.xlabel('Day')
plt.ylabel('NGPRS - Number of Daily Logs')
plt.title('NGPRS - Number of Logs Over Time')

# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
plt.grid(True)
axes = plt.gca()
axes.set_xlim([1,31])
plt.show()


plt.plot(x,crm_nlog)


plt.xlabel('Day')
plt.ylabel('CRM - Number of Daily Logs')
plt.title('CRM - Number of Logs Over Time')

# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
plt.grid(True)
axes = plt.gca()
axes.set_xlim([1,31])
plt.show()
