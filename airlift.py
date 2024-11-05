import matplotlib.pyplot as plt 
import numpy as np

#H = Depth of Submergence 
#L = Length of pump 
#Ds = Internal diameter 
#K = Loss coefficient 
#g = Acceleration of Gravity 
#s = Slip Ratio 
#Qg = Volume flow rate of air 
#Qf = Volume flow rate of water 

def calculate_preformance(K,S,HDL, QgQf, i, j, k, l):
    return np.sqrt((HDL[k]-(1/(1+(1/S[j])*(QgQf[l]))))/(K[i]+1+(K[i]+2)*QgQf[l]))

def example_data(K,S,HDL,QgQf, i, j):
    return np.sqrt((HDL[i]-(1/(1+(1/S[i])*(QgQf[j]))))/(K[i]+1+(K[i]+2)*QgQf[j]))

#SI Units only 

#Keeping s and K values constant despite s and K values not actually being constant 
#is a good enough approximation to not be statistically significant 

#Plotting Water Volume Flow Rate (CFS), Qf vs Air Volume Flow Rate (CFS), Qg 

#F = np.arange(0.004, 0.005, 0.0001)
#L = 0.3048
#DS = 0.0204216

K = np.arange(4.0,6.1, 0.1) #Loss Coefficient 
S = np.arange(1.5, 2.6, 0.1) #Slip Ratio 
HDL = np.arange(0.1, 0.8333, 0.1) #H/L Submergence Ratio 

#Example Data:
#K = np.array([4.0,5.0,6.0,5.0])
#S = np.array([1.5, 1.5, 1.5, 2.0])
#HDL = np.array([0.700, 0.700, 0.700, 0.700])

QgQf = np.arange(0, 15, 0.01) #Qg/Qf
res = np.zeros(shape=(QgQf.shape))#V/sqrt(2gL)
gresarr = np.zeros(2000)
gQgQfarr = np.zeros(2000)
gres = 0
gQgQf = 0
cc = 0 #Counts Curves 

'''
for i in range(len(K)):
    for j in range(len(QgQf)):
        res[j] = example_data(K,S,HDL,QgQf, i, j)
    plt.plot(QgQf, res, label=f'Curve{cc+1}: K={K[i]} S={S[i]} H/L={HDL[i]}')
    cc+=1
'''
#fig, axs = plt.subplots(len(K), sharex=True, sharey=True) #Activates subplots 

for i in range(len(K)):
    for j in range(len(S)):
        for k in range(len(HDL)):
            for l in range(len(QgQf)):
                res[l] = calculate_preformance(K,S,HDL,QgQf, i, j, k, l)
                if res[l] > gres:
                    gres = res[l]
                    gQgQf = QgQf[l]
            gresarr[cc] = gres
            gQgQfarr[cc] = gQgQf
            print(f'Curve {cc+1}: K={K[i]} S={S[j]} H/L = {HDL[k]} Greatest V={gres} Greatest QgQf={gQgQf}')
            gres = 0
            gQgQf = 0
            plt.plot(QgQf, res)
            cc+=1

globmaxres = gresarr.max()
curveid = gresarr.argmax()
gQgQf = gQgQfarr[curveid]
print(f'Global Maximum = {globmaxres}, Curve # = {curveid}, Qg/Qf = {gQgQf}')


#plt.legend()
plt.xlabel('Qg/Qf')
plt.ylabel('V/Sqrt(2gL)')
plt.show()
