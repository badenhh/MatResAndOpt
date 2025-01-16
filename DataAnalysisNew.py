# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 09:28:31 2017

@author: u04102916
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FormatStrFormatter

rawdata = np.genfromtxt('Data.csv', comments="#", delimiter=",")
n=np.shape(rawdata)[0]
PnK = np.genfromtxt('PnK.csv', comments="#", delimiter=",")

plt.rcParams["figure.figsize"] = (11.1,8.3)

fig, ax = plt.subplots()
#plt.figure()
for i in range(0,n):
    msize=50
    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='b',marker='o',s=msize)
    elif (rawdata[i,3]==4):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='g',marker='v',s=msize)
    elif (rawdata[i,3]==5):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='r',marker='^',s=msize)
    elif (rawdata[i,3]==6):
        if (rawdata[i,13]==1):
            plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='b',marker='<',s=msize)
        else:
            plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='c',marker='<',s=msize)
                
    elif (rawdata[i,3]==7):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='m',marker='>',s=msize)
    elif (rawdata[i,3]==8):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='y',marker='*',s=msize)
    elif (rawdata[i,3]==9):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='k',marker='d',s=msize)

plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
plt.legend(loc=0, fontsize=15, scatterpoints=1)

plt.yscale('log')
plt.xscale('log')
#for axis in [ax.yaxis, ax.xaxis]:
#    axis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.show()
plt.xlim(0.01,1)
plt.ylim(0.8,1000)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='x', which='major', size=10, width=2)
plt.tick_params(axis='x', which='minor', size=5, width=2)
plt.tick_params(axis='y', which='major', size=10, width=2)
plt.tick_params(axis='y', which='minor', size=5, width=2)
plt.ylabel('Enhancement Factor [-]', fontsize=20, wrap=True)
plt.xlabel('Carbon mass fraction [-]', fontsize=20)
plt.tight_layout()

x1 = np.linspace(0.009,0.7,500)
y1 = x1/x1
#y2 = 10*x1+1
y2 = 10*x1**0.5
ax.fill_between(x1, y1, y2, where=y2 >= y1, facecolor='red', alpha=0.5, interpolate=True)
#y1 = 11*x1+1
y1 = 10*x1**0.5
#y2 = 130*x1+0.4
y2 = 200*(x1)**1.1
ax.fill_between(x1, y1, y2, where=y2 >= y1, facecolor='blue', alpha=0.5, interpolate=True)
x1 = np.linspace(0.009,1.0,500)
#y1 = 110*x1+1
y1 = 200*(x1)**1.1
y2 = 2500*(x1)**1.5
ax.fill_between(x1, y1, y2, where=y2 >= y1, facecolor='green', alpha=0.5, interpolate=True)

plt.annotate("Porous", xy=(0.085,39), fontsize=20)
plt.annotate("Matrices", xy=(0.08,28), fontsize=20)
plt.annotate("Particulate", xy=(0.27,15), fontsize=20)
plt.annotate("Additives", xy=(0.29,11), fontsize=20)
plt.annotate("Particulates", xy=(0.29,2.56), fontsize=20)
plt.annotate("Poor", xy=(0.38,1.8), fontsize=20)
plt.annotate("Mixing", xy=(0.35,1.3), fontsize=20)






fig, ax = plt.subplots()
#plt.figure()
for i in range(0,n):
    msize=50
    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='b',marker='o',s=msize)
    elif (rawdata[i,3]==4):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='g',marker='v',s=msize)
    elif (rawdata[i,3]==5):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='r',marker='^',s=msize)
    elif (rawdata[i,3]==6):
        if (rawdata[i,13]==1):
            plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='b',marker='<',s=msize)
        else:
            plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='c',marker='<',s=msize)
                
    elif (rawdata[i,3]==7):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='m',marker='>',s=msize)
    elif (rawdata[i,3]==8):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='y',marker='*',s=msize)
    elif (rawdata[i,3]==9):
        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='k',marker='d',s=msize)

plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
plt.legend(loc=0, fontsize=15, scatterpoints=1)

plt.yscale('log')
plt.xscale('log')
#for axis in [ax.yaxis, ax.xaxis]:
#    axis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.show()
plt.xlim(0.01,1)
plt.ylim(0.8,1000)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='x', which='major', size=10, width=2)
plt.tick_params(axis='x', which='minor', size=5, width=2)
plt.tick_params(axis='y', which='major', size=10, width=2)
plt.tick_params(axis='y', which='minor', size=5, width=2)
plt.ylabel('Enhancement Factor [-]', fontsize=20, wrap=True)
plt.xlabel('Carbon mass fraction [-]', fontsize=20)
plt.tight_layout()

x1 = np.linspace(0.009,0.7,500)
y1 = x1/x1
#y2 = 11*x1+1
y2 = 10*x1**0.5
ax.fill_between(x1, y1, y2, where=y2 >= y1, facecolor='white', alpha=1, interpolate=True)


xfrac=np.linspace(0.0009,1,500)
kc=250.0
kpcm=0.25
enh=kc/kpcm*xfrac**1.5
plt.plot(xfrac,enh,'g-.',label='$1000x^{1.5}$')

kc=250.0
kpcm=0.25
kp=kc*xfrac+(1-xfrac)*kpcm
enh=kp/kpcm
plt.plot(xfrac,enh,'g')

#kc=1750.0
#kpcm=0.25
#kp=kc*xfrac#+(1-xfrac)*kpcm
#enh=kp/kpcm
#plt.plot(xfrac,enh,'m')
#
#kc=3100.0
#kpcm=0.25
#kp=kc*xfrac+(1-xfrac)*kpcm
#enh=kp/kpcm
#plt.plot(xfrac,enh)

xfracp=np.linspace(0.0009,0.7,500)
kc=15.0
kpcm=0.25
ks=((xfracp/kc)+((1-xfracp)/kpcm))**(-1)
kp=kc*xfracp+(1-xfracp)*kpcm
fact=0.1
enh=((fact/ks)+(1-fact)/kp)**(-1)/kpcm
plt.plot(xfracp,enh,'b-.')

#xfrac=np.linspace(0.009,0.7,500)
#kc=10.0
#kpcm=0.25
#enh=40.0*xfrac**0.8
#plt.plot(xfrac,enh,'b')

kc=15.0
kpcm=0.25
kp=kc*xfracp+(1-xfracp)*kpcm
enh=kp/kpcm
plt.plot(xfracp,enh,'b')

#kc=10.0
#kpcm=0.25
#ks=((xfracp/kc)+((1-xfracp)/kpcm))**(-1)
#kp=kc*xfracp+(1-xfracp)*kpcm
#fact=0.65
#enh=((fact/ks)+(1-fact)/kp)**(-1)/kpcm
#plt.plot(xfracp,enh)

#plt.annotate("$k_{GR} = 1750\ W.m^{-1}.K^{-1}$", xy=(0.03,770), fontsize=16)
plt.annotate("$k_{GR} = 250\ W.m^{-1}.K^{-1}$", xy=(0.25,790), fontsize=16)
plt.annotate("$k_{GR} = 15\ W.m^{-1}.K^{-1}$", xy=(0.315,45), fontsize=16)

plt.annotate("$Eqn. (1)$", xy=(0.06,30), fontsize=16)
plt.annotate("$Eqn. (2)$", xy=(0.61,12), fontsize=16)
#plt.annotate("$Eqn. (3)$", xy=(0.02,230), fontsize=16)
plt.annotate("$Eqn. (3)$", xy=(0.04,67), fontsize=16)
plt.annotate("$Eqn. (3)$", xy=(0.61,29), fontsize=16)







fig, ax = plt.subplots()
#plt.figure()
for i in range(0,n):
    if i!=187:
        msize=50
        if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
            plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='b',marker='o',s=msize)
        elif (rawdata[i,3]==4):
            plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='g',marker='v',s=msize)
        elif (rawdata[i,3]==5):
            plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='r',marker='^',s=msize)
        elif (rawdata[i,3]==6):
            if (rawdata[i,13]==1):
                plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='b',marker='<',s=msize)
            else:
                plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='c',marker='<',s=msize)
                    
        elif (rawdata[i,3]==7):
            plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='m',marker='>',s=msize)
        elif (rawdata[i,3]==8):
            plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='y',marker='*',s=msize)
        elif (rawdata[i,3]==9):
            plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='k',marker='d',s=msize)

plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
plt.scatter(0.0338,140, color='orange',marker='o',s=msize+200, label='NEW')
#plt.scatter(0.04,280, color='orange',marker='o',s=msize+200)
#plt.scatter(0.1,650, color='orange',marker='o',s=msize+200)
plt.legend(loc=0, fontsize=15, scatterpoints=1)

#plt.scatter(0.01,60.5, color='None',marker='o',edgecolors='k',s=msize+300)
#plt.scatter(0.2,182, color='None',marker='o',edgecolors='k',s=msize+300)

plt.yscale('log')
plt.xscale('log')
#for axis in [ax.yaxis, ax.xaxis]:
#    axis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.show()
plt.xlim(0.009,1)
plt.ylim(0.8,1000)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='x', which='major', size=10, width=2)
plt.tick_params(axis='x', which='minor', size=5, width=2)
plt.tick_params(axis='y', which='major', size=10, width=2)
plt.tick_params(axis='y', which='minor', size=5, width=2)
plt.ylabel('Enhancement Factor [-]', fontsize=20, wrap=True)
plt.xlabel('Carbon mass fraction [-]', fontsize=20)
plt.tight_layout()

x1 = np.linspace(0.009,0.7,500)
y1 = x1/x1
#y2 = 11*x1+1
y2 = 10*x1**0.5
ax.fill_between(x1, y1, y2, where=y2 >= y1, facecolor='white', alpha=1, interpolate=True)


xfrac=np.linspace(0.0009,1,500)
kc=250.0
kpcm=0.25
enh=kc/kpcm*xfrac**1.5
plt.plot(xfrac,enh,'g-.',label='$1000x^{1.5}$')

#kc=250.0
#kpcm=0.25
#kp=kc*xfrac+(1-xfrac)*kpcm
#enh=kp/kpcm
#plt.plot(xfrac,enh,'g')

kc=1750.0
kpcm=0.25
kp=kc*xfrac#+(1-xfrac)*kpcm
enh=kp/kpcm
plt.plot(xfrac,enh,'m')

#kc=3100.0
#kpcm=0.25
#kp=kc*xfrac+(1-xfrac)*kpcm
#enh=kp/kpcm
#plt.plot(xfrac,enh)

#xfracp=np.linspace(0.0009,0.7,500)
#kc=15.0
#kpcm=0.25
#ks=((xfracp/kc)+((1-xfracp)/kpcm))**(-1)
#kp=kc*xfracp+(1-xfracp)*kpcm
#fact=0.1
#enh=((fact/ks)+(1-fact)/kp)**(-1)/kpcm
#plt.plot(xfracp,enh,'b-.')

#xfrac=np.linspace(0.009,0.7,500)
#kc=10.0
#kpcm=0.25
#enh=40.0*xfrac**0.8
#plt.plot(xfrac,enh,'b')

kc=15.0
kpcm=0.25
kp=kc*xfracp+(1-xfracp)*kpcm
enh=kp/kpcm
plt.plot(xfracp,enh,'b')

#kc=10.0
#kpcm=0.25
#ks=((xfracp/kc)+((1-xfracp)/kpcm))**(-1)
#kp=kc*xfracp+(1-xfracp)*kpcm
#fact=0.65
#enh=((fact/ks)+(1-fact)/kp)**(-1)/kpcm
#plt.plot(xfracp,enh)

plt.annotate("$k_{GR} = 1750\ W.m^{-1}.K^{-1}$", xy=(0.03,770), fontsize=16)
plt.annotate("$k_{GR} = 250\ W.m^{-1}.K^{-1}$", xy=(0.25,790), fontsize=16)
plt.annotate("$k_{GR} = 15\ W.m^{-1}.K^{-1}$", xy=(0.315,45), fontsize=16)

plt.annotate("$Eqn. (1)$", xy=(0.06,30), fontsize=16)
#plt.annotate("$Eqn. (2)$", xy=(0.61,12), fontsize=16)
plt.annotate("$Eqn. (3)$", xy=(0.02,230), fontsize=16)
#plt.annotate("$Eqn. (3)$", xy=(0.04,67), fontsize=16)
plt.annotate("$Eqn. (3)$", xy=(0.61,29), fontsize=16)



