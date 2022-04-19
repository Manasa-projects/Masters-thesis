import matplotlib.pyplot as plt

costPercent=[10,20,30,40,50,60,70,80,90,100]
p1=[0, 0.730, 0.741, 0.770, 0.754, 0.786, 0.796, 0.706, 0.805, 0.850]
p2=[0, 0, 0.852, 0.840, 0.863, 0.866, 0.896, 0.788, 0.775, 0.760]
p3=[0, 0, 0.862, 0.890, 0.863, 0.889, 0.870, 0.788, 0.775, 0.895]
p4=[0, 0.830, 0.871, 0.780, 0.855, 0.856, 0.896, 0.806, 0.705, 0.845]
p5=[0, 0.845, 0.799, 0.780, 0.720, 0.814, 0.806, 0.708, 0.818, 0.820]
p6=[0, 0.730, 0.754, 0.782, 0.764, 0.723, 0.746, 0.746, 0.712, 0.752]
p7=[0, 0, 0.772, 0.874, 0.863, 0.889, 0.870, 0.788, 0.765, 0.815]
p8=[0, 0.745, 0.799, 0.780, 0.720, 0.804, 0.806, 0.815, 0.818, 0.845]
p9=[0, 0, 0.752, 0.790, 0.763, 0.789, 0.842, 0.756, 0.772, 0.879]
p10=[0, 0.731, 0.751, 0.780, 0.764, 0.868, 0.892, 0.865, 0.734, 0.791]
p11=[0, 0.708, 0.751, 0.772, 0.783, 0.766, 0.736, 0.716, 0.825, 0.815]
p12=[0, 0.745, 0.789, 0.770, 0.725, 0.814, 0.844, 0.802, 0.813, 0.818]
p13=[0, 0.745, 0.789, 0.770, 0.725, 0.814, 0.844, 0.802, 0.813, 0.818]
p14=[0, 0, 0.770, 0.870, 0.823, 0.810, 0.801, 0.821, 0.819, 0.838]
p15=[0, 0, 0.770, 0.870, 0.823, 0.810, 0.801, 0.821, 0.819, 0.838]

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
plt.ylabel('Precision of number of potential candidates')
#plt.plot(x,y)

plt.grid()
plt.show()
