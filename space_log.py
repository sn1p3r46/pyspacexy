import matplotlib.pyplot as plt

crm = [
234,
234,
233,
234,
234,
233,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234,
234
]

msc = [
2381,
2377,
1510,
1222,
2315,
2261,
2292,
2251,
2363,
1486,
1208,
2434,
2314,
2303,
2270,
2389,
1492,
1293,
2362,
2342,
2338,
2325,
2448,
1578,
1271,
2410,
2263,
2288,
2282,
2335,
1734
]

ngprs = [
15492,
16218,
13516,
11941,
15260,
15332,
15070,
15109,
15346,
12880,
11371,
14251,
14261,
14380,
14529,
15068,
12828,
11340,
14386,
14602,
14725,
14911,
15415,
13021,
11328,
14296,
14586,
15070,
14989,
15457,
13677
]

x = range(1,32)
plt.plot(x,msc)


plt.xlabel('Day Number')
plt.ylabel('MSC - Size of Daily Logs in MB')
plt.title('MSC - Size of Daily Logs Over Time')

# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
plt.grid(True)
axes = plt.gca()
axes.set_xlim([1,31])
plt.show()


plt.plot(x,ngprs)


plt.xlabel('Day Number')
plt.ylabel('NGPRS - Size of Daily Logs in MB')
plt.title('NGPRS - Size of Daily Logs Over Time')

# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
plt.grid(True)
axes = plt.gca()
axes.set_xlim([1,31])
plt.show()


plt.plot(x,crm)


plt.xlabel('Day Number')
plt.ylabel('CRM - Size of Daily Logs in MB')
plt.title('CRM - Size of Daily Logs Over Time')

# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
plt.grid(True)
axes = plt.gca()
axes.set_xlim([1, 31])
axes.set_ylim([230, 236])
plt.show()
