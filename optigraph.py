import matplotlib.pyplot as plt

costPercent=[10,20,30,40,50,60,70,80,90,100]
p1=[0,230,451,658,864,1043,1206,1306,1405,1478]
p2=[0,0,178,422,666,910,1151,1374,1506,1522]
p3=[0,0,97,341,585,829,1073,1317,1517,1522]
p4=[0,200,410,620,828,1028,1215,1356,1433,1522]
p5=[0,161,383,604,825,1046,1263,1445,1516,1522]
p6=[0,171,358,549,732,918,1101,1256,1344,1432]
p7=[0,0,88,309,531,752,973,1194,1414,1522]
p8=[0,141,335,527,720,914,1106,1294,1467,1521]
p9=[0,0,86,303,519,735,952,1168,1385,1521]
p10=[0,162,333,504,675,845,1014,1177,1304,1418]
p11=[0,156,326,496,667,837,1004,1165,1283,1362]
p12=[0,130,309,487,668,845,1023,1203,1365,1479]
p13=[0,130,309,488,668,847,1025,1203,1365,1499]
p14=[0,0,79,277,476,674,873,1071,1270,1459]
p15=[0,0,79,277,476,674,873,1071,1270,1459]


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

plt.axhline(y=1522, xmin=-10, xmax=130,color="black",linestyle="--")

plt.xlim(-10,130)
plt.ylim(-5,1540)

plt.xlabel('Total Computational Budget')
plt.ylabel('The number of potential candidates')
#plt.plot(x,y)

plt.grid()
plt.show()
