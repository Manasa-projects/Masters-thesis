import matplotlib.pyplot as plt

costPercent=[10,20,30,40,50,60,70,80,90,100]
p1=[0, 0.425, 0.432, 0.475, 0.568, 0.566, 0.596, 0.719, 0.705, 0.780]
p2=[0, 0, 0.552, 0.628, 0.669, 0.666, 0.896, 0.788, 0.736, 0.860]
p3=[0, 0, 0.662, 0.660, 0.663, 0.689, 0.870, 0.788, 0.775, 0.895]
p4=[0, 0.430, 0.471, 0.480, 0.555, 0.586, 0.596, 0.606, 0.705, 0.745]
p5=[0, 0.635, 0.699, 0.746, 0.729, 0.814, 0.906, 0.908, 0.918, 0.920]
p6=[0, 0.330, 0.454, 0.480, 0.495, 0.523, 0.546, 0.646, 0.712, 0.743]
p7=[0, 0, 0.652, 0.780, 0.783, 0.795, 0.870, 0.872, 0.870, 0.871]
p8=[0, 0.645, 0.699, 0.780, 0.782, 0.804, 0.806, 0.815, 0.818, 0.932]
p9=[0, 0, 0.672, 0.690, 0.663, 0.789, 0.842, 0.756, 0.772, 0.879]
p10=[0, 0.330, 0.351, 0.480, 0.564, 0.568, 0.592, 0.665, 0.734, 0.791]
p11=[0, 0.308, 0.451, 0.482, 0.583, 0.566, 0.546, 0.716, 0.725, 0.745]
p12=[0, 0.645, 0.689, 0.770, 0.775, 0.814, 0.900, 0.902, 0.913, 0.918]
p13=[0, 0.645, 0.689, 0.770, 0.775, 0.814, 0.900, 0.902, 0.913, 0.918]
p14=[0, 0, 0.470, 0.670, 0.689, 0.880, 0.891, 0.891, 0.899, 0.888]
p15=[0, 0, 0.470, 0.670, 0.689, 0.880, 0.891, 0.891, 0.899, 0.888]

plt.plot(costPercent,p1)
plt.plot(costPercent,p2)
plt.plot(costPercent,p3)
plt.plot(costPercent,p4)
plt.plot(costPercent,p5)
plt.plot(costPercent,p6)
plt.plot(costPercent,p7)
plt.plot(costPercent,p8)
plt.plot(costPercent,p9)
plt.plot(costPercent,p10)
plt.plot(costPercent,p11)
plt.plot(costPercent,p12)
plt.plot(costPercent,p13)
plt.plot(costPercent,p14)
plt.plot(costPercent,p15)

plt.legend(["[M1,M4]", "[M2,M4]","[M3,M4]","[M1,M2,M4]","[M2,M1,M4]","[M1,M3,M4]","[M3,M1,M4]","[M2,M3,M4]","[M3,M2,M4]","[M1,M2,M3,M4]","[M1,M3,M2,M4]","[M2,M1,M3,M4]","[M2,M3,M1,M4]","[M3,M1,M2,M4]","[M3,M2,M1,M4]"])

plt.axvline(x=10, ymin=0, ymax=1540,color="black", linestyle=":")
plt.axvline(x=20, ymin=0, ymax=1540,color="black", linestyle=":")
plt.axvline(x=30, ymin=0, ymax=1540,color="black", linestyle=":")
plt.axvline(x=40, ymin=0, ymax=1540,color="black", linestyle=":")
plt.axvline(x=50, ymin=0, ymax=1540,color="black", linestyle=":")
plt.axvline(x=60, ymin=0, ymax=1540,color="black", linestyle=":")
plt.axvline(x=70, ymin=0, ymax=1540,color="black", linestyle=":")
plt.axvline(x=80, ymin=0, ymax=1540,color="black", linestyle=":")
plt.axvline(x=90, ymin=0, ymax=1540,color="black", linestyle=":")
plt.axvline(x=100, ymin=0, ymax=1540,color="black", linestyle="--")

plt.axhline(y=0.95, xmin=-10, xmax=130,color="black",linestyle="--")

plt.xlim(-10,130)
plt.ylim(-0.5,1)

plt.xlabel('Total Computational Budget')
plt.ylabel('F1 score of number of potential candidates')
#plt.plot(x,y)

plt.grid()
plt.show()
