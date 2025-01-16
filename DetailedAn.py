# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 09:28:31 2017

@author: u04102916
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FormatStrFormatter

# Read in stored experimental data
# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the data files
# Experimental Data
data_csv_path = os.path.join(current_dir, 'Data.csv')
# Physical Properties
pnk_csv_path = os.path.join(current_dir, 'PnK.csv')

# Load the data
rawdata = np.genfromtxt(data_csv_path, comments="#", delimiter=",")
n = np.shape(rawdata)[0]
PnK = np.genfromtxt(pnk_csv_path, comments="#", delimiter=",")

# Process data and generate plots for different sections of the publication paper

## Plots commented when not in use



##All fit final
##Combo par/ser for UC and 1.5 for compr (enh>15) Using all same assumed k's

fig, ax = plt.subplots()
for i in range(0,n):
    plotvar2=rawdata[i,4]
    kc=PnK[int(rawdata[i,3]),3]
#    if np.isnan(rawdata[i,9]):
#        kc=PnK[int(rawdata[i,3]),2]
#    else:
#        kc=rawdata[i,9]

    if rawdata[i,11]>15:
        kc=kc*10
        korig=kc*(rawdata[i,6]/100)**1.5
#    if rawdata[i,11]>15:
#        kc=kc*10
#        fact=0.00000000001
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
    elif rawdata[i,11]>2.5:
        kc=15.0
        fact=0.01
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
        ks=(((rawdata[i,6]/100)/kc)+((1-rawdata[i,6]/100)/rawdata[i,7]))**(-1)
        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
        korig=((fact/ks)+(1-fact)/kp)**(-1)
    else:
        kc=10.0
        fact=0.4#65
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
        ks=(((rawdata[i,6]/100)/kc)+((1-rawdata[i,6]/100)/rawdata[i,7]))**(-1)
        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
        korig=((fact/ks)+(1-fact)/kp)**(-1)


    plotvar1=korig


    msize=50
    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
        plt.scatter(plotvar1,plotvar2, color='b',marker='o',s=msize)
    elif (rawdata[i,3]==4):
        plt.scatter(plotvar1,plotvar2, color='g',marker='v',s=msize)
    elif (rawdata[i,3]==5):
        plt.scatter(plotvar1,plotvar2, color='r',marker='^',s=msize)
    elif (rawdata[i,3]==6):
        plt.scatter(plotvar1,plotvar2, color='c',marker='<',s=msize)
    elif (rawdata[i,3]==7):
        plt.scatter(plotvar1,plotvar2, color='m',marker='>',s=msize)
    elif (rawdata[i,3]==8):
        plt.scatter(plotvar1,plotvar2, color='y',marker='*',s=msize)
    elif (rawdata[i,3]==9):
        plt.scatter(plotvar1,plotvar2, color='k',marker='d',s=msize)

plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
plt.legend(loc=4, fontsize=15, scatterpoints=1)
plt.yscale('log')
plt.xscale('log')
plt.xlim(0.1,10000)
plt.ylim(0.1,10000)
kPred=np.linspace(0.01,10000,50)
plt.plot(kPred,kPred)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='x', which='major', size=8, width=2)
plt.tick_params(axis='x', which='minor', size=4, width=2)
plt.tick_params(axis='y', which='major', size=8, width=2)
plt.tick_params(axis='y', which='minor', size=4, width=2)
plt.ylabel('Actual $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20, wrap=True)
plt.xlabel('Predicted $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20)
plt.tight_layout()


## Plot raw data

#fig, ax = plt.subplots()
##plt.figure()
#for i in range(0,n):
#    msize=50
#    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,4], color='b',marker='o',s=msize)
#    elif (rawdata[i,3]==4):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,4], color='g',marker='v',s=msize)
#    elif (rawdata[i,3]==5):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,4], color='r',marker='^',s=msize)
#    elif (rawdata[i,3]==6):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,4], color='c',marker='<',s=msize)
#    elif (rawdata[i,3]==7):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,4], color='m',marker='>',s=msize)
#    elif (rawdata[i,3]==8):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,4], color='y',marker='*',s=msize)
#    elif (rawdata[i,3]==9):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,4], color='k',marker='d',s=msize)
#
#plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
#plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
#plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
#plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
#plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
#plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
#plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
#plt.legend(loc=4, fontsize=15, scatterpoints=1)
#
#plt.yscale('log')
##plt.xscale('log')
##for axis in [ax.yaxis, ax.xaxis]:
##    axis.set_major_formatter(ScalarFormatter())
#ax.yaxis.set_major_formatter(ScalarFormatter())
#ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#plt.show()
#plt.xlim(0.001,0.8)
#plt.ylim(0.1,300)
#plt.tick_params(axis='y', labelsize=15)
#plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=10, width=2)
#plt.tick_params(axis='x', which='minor', size=5, width=2)
#plt.tick_params(axis='y', which='major', size=10, width=2)
#plt.tick_params(axis='y', which='minor', size=5, width=2)
#plt.ylabel('Enhancement Factor [-]', fontsize=20, wrap=True)
#plt.xlabel('Carbon mass fraction [-]', fontsize=20)
#plt.tight_layout()




## Test curve for data

#fig, ax = plt.subplots()
##plt.figure()
#n=np.shape(rawdata)[0]
#for i in range(0,n):
#    msize=50
#    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='b',marker='o',s=msize)
#    elif (rawdata[i,3]==4):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='g',marker='v',s=msize)
#    elif (rawdata[i,3]==5):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='r',marker='^',s=msize)
#    elif (rawdata[i,3]==6):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='c',marker='<',s=msize)
#    elif (rawdata[i,3]==7):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='m',marker='>',s=msize)
#    elif (rawdata[i,3]==8):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='y',marker='*',s=msize)
#    elif (rawdata[i,3]==9):
#        plt.scatter(rawdata[i,6]/100,rawdata[i,11], color='k',marker='d',s=msize)
#
#plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
#plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
#plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
#plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
#plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
#plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
#plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
#
#xfrac=np.linspace(0.01,1,50)
#enh=1000*xfrac**1.5
#plt.plot(xfrac,enh,label='$1000x^{1.5}$')
#
#plt.legend(loc=4, fontsize=15, scatterpoints=1)
#plt.yscale('log')
##plt.xscale('log')
#ax.yaxis.set_major_formatter(ScalarFormatter())
#ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#plt.show()
##plt.annotate('Increasing Heat', xy=(265, 90), xytext=(235, 70), fontsize=20)
#plt.xlim(0.001,1)
#plt.ylim(50,1000)
#plt.tick_params(axis='y', labelsize=15)
#plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=8, width=2)
#plt.tick_params(axis='x', which='minor', size=4, width=2)
#plt.tick_params(axis='y', which='major', size=8, width=2)
#plt.tick_params(axis='y', which='minor', size=4, width=2)
#plt.ylabel('Enhancement Factor [-]', fontsize=20, wrap=True)
#plt.xlabel('Carbon mass fraction [-]', fontsize=20)
#plt.tight_layout()


## Plot non-unified with high conductivity

#fig, ax = plt.subplots()
#for i in range(0,n):
#    plotvar2=rawdata[i,11]
#    plotvar1=(PnK[int(rawdata[i,3]),1]*rawdata[i,6]/100+(1-rawdata[i,6]/100)*1)/((1-rawdata[i,6]/100)*1)
#
#
#    msize=50
#    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
#        plt.scatter(plotvar1,plotvar2, color='b',marker='o',s=msize)
#    elif (rawdata[i,3]==4):
#        plt.scatter(plotvar1,plotvar2, color='g',marker='v',s=msize)
#    elif (rawdata[i,3]==5):
#        plt.scatter(plotvar1,plotvar2, color='r',marker='^',s=msize)
#    elif (rawdata[i,3]==6):
#        plt.scatter(plotvar1,plotvar2, color='c',marker='<',s=msize)
#    elif (rawdata[i,3]==7):
#        plt.scatter(plotvar1,plotvar2, color='m',marker='>',s=msize)
#    elif (rawdata[i,3]==8):
#        plt.scatter(plotvar1,plotvar2, color='y',marker='*',s=msize)
#    elif (rawdata[i,3]==9):
#        plt.scatter(plotvar1,plotvar2, color='k',marker='d',s=msize)
#
#plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
#plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
#plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
#plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
#plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
#plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
#plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
#plt.legend(loc=1, fontsize=15, scatterpoints=1)
#plt.yscale('log')
#plt.xscale('log')
#
#ax.yaxis.set_major_formatter(ScalarFormatter())
#ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
#
#plt.xlim(1,10000)
#plt.ylim(0.8,1000)
#plt.tick_params(axis='y', labelsize=15)
#plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=8, width=2)
#plt.tick_params(axis='x', which='minor', size=4, width=2)
#plt.tick_params(axis='y', which='major', size=8, width=2)
#plt.tick_params(axis='y', which='minor', size=4, width=2)
#plt.ylabel('Enhancement Factor [-]', fontsize=20, wrap=True)
#plt.xlabel('Incremental Cost Factor [-]', fontsize=20)
#plt.tight_layout()




##Klett parallel using diff assumed k's

#fig, ax = plt.subplots()
#for i in range(0,n):
#    plotvar2=rawdata[i,4]
#    kc=PnK[int(rawdata[i,3]),2]
##    if np.isnan(rawdata[i,9]):
##        kc=PnK[int(rawdata[i,3]),2]
##    else:
##        kc=rawdata[i,9]
#    plotvar1=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#    plotvar1=kc*(rawdata[i,6]/100)**1.5
#
#
#    msize=50
#    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
#        plt.scatter(plotvar1,plotvar2, color='b',marker='o',s=msize)
#    elif (rawdata[i,3]==4):
#        plt.scatter(plotvar1,plotvar2, color='g',marker='v',s=msize)
#    elif (rawdata[i,3]==5):
#        plt.scatter(plotvar1,plotvar2, color='r',marker='^',s=msize)
#    elif (rawdata[i,3]==6):
#        plt.scatter(plotvar1,plotvar2, color='c',marker='<',s=msize)
#    elif (rawdata[i,3]==7):
#        plt.scatter(plotvar1,plotvar2, color='m',marker='>',s=msize)
#    elif (rawdata[i,3]==8):
#        plt.scatter(plotvar1,plotvar2, color='y',marker='*',s=msize)
#    elif (rawdata[i,3]==9):
#        plt.scatter(plotvar1,plotvar2, color='k',marker='d',s=msize)
#
#plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
#plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
#plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
#plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
#plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
#plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
#plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
#plt.legend(loc=2, fontsize=15, scatterpoints=1)
#plt.yscale('log')
#plt.xscale('log')
#plt.xlim(0.1,10000)
#plt.ylim(0.1,10000)
#kPred=np.linspace(0.01,10000,50)
#plt.plot(kPred,kPred)
#plt.tick_params(axis='y', labelsize=15)
#plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=8, width=2)
#plt.tick_params(axis='x', which='minor', size=4, width=2)
#plt.tick_params(axis='y', which='major', size=8, width=2)
#plt.tick_params(axis='y', which='minor', size=4, width=2)
#plt.ylabel('Actual $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20, wrap=True)
#plt.xlabel('Predicted $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20)
#plt.tight_layout()




##PURE parallel using all same assumed k's

#fig, ax = plt.subplots()
#for i in range(0,n):
#    plotvar2=rawdata[i,4]
#    kc=PnK[int(rawdata[i,3]),3]
##    if np.isnan(rawdata[i,9]):
##        kc=PnK[int(rawdata[i,3]),2]
##    else:
##        kc=rawdata[i,9]
#    plotvar1=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
##    plotvar1=300*(rawdata[i,6]/100)**1.5
#
#
#    msize=50
#    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
#        plt.scatter(plotvar1,plotvar2, color='b',marker='o',s=msize)
#    elif (rawdata[i,3]==4):
#        plt.scatter(plotvar1,plotvar2, color='g',marker='v',s=msize)
#    elif (rawdata[i,3]==5):
#        plt.scatter(plotvar1,plotvar2, color='r',marker='^',s=msize)
#    elif (rawdata[i,3]==6):
#        plt.scatter(plotvar1,plotvar2, color='c',marker='<',s=msize)
#    elif (rawdata[i,3]==7):
#        plt.scatter(plotvar1,plotvar2, color='m',marker='>',s=msize)
#    elif (rawdata[i,3]==8):
#        plt.scatter(plotvar1,plotvar2, color='y',marker='*',s=msize)
#    elif (rawdata[i,3]==9):
#        plt.scatter(plotvar1,plotvar2, color='k',marker='d',s=msize)
#
#plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
#plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
#plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
#plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
#plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
#plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
#plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
#plt.legend(loc=4, fontsize=15, scatterpoints=1)
#plt.yscale('log')
#plt.xscale('log')
#plt.xlim(0.1,10000)
#plt.ylim(0.1,10000)
#kPred=np.linspace(0.01,10000,50)
#plt.plot(kPred,kPred)
#plt.tick_params(axis='y', labelsize=15)
#plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=8, width=2)
#plt.tick_params(axis='x', which='minor', size=4, width=2)
#plt.tick_params(axis='y', which='major', size=8, width=2)
#plt.tick_params(axis='y', which='minor', size=4, width=2)
#plt.ylabel('Actual $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20, wrap=True)
#plt.xlabel('Predicted $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20)
#plt.tight_layout()




###Low fit
###Combo par/ser for UC and 1.5 for compr (enh>20) Using all same assumed k's

#fact=0.35
#fig, ax = plt.subplots()
#for i in range(0,n):
#    plotvar2=rawdata[i,4]
#    kc=PnK[int(rawdata[i,3]),3]
##    if np.isnan(rawdata[i,9]):
##        kc=PnK[int(rawdata[i,3]),2]
##    else:
##        kc=rawdata[i,9]
#
#    if rawdata[i,11]>20:
#        korig=kc*(rawdata[i,6]/100)**1.5
#    else:
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#
#
#    plotvar1=korig
#
#
#    msize=50
#    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
#        plt.scatter(plotvar1,plotvar2, color='b',marker='o',s=msize)
#    elif (rawdata[i,3]==4):
#        plt.scatter(plotvar1,plotvar2, color='g',marker='v',s=msize)
#    elif (rawdata[i,3]==5):
#        plt.scatter(plotvar1,plotvar2, color='r',marker='^',s=msize)
#    elif (rawdata[i,3]==6):
#        plt.scatter(plotvar1,plotvar2, color='c',marker='<',s=msize)
#    elif (rawdata[i,3]==7):
#        plt.scatter(plotvar1,plotvar2, color='m',marker='>',s=msize)
#    elif (rawdata[i,3]==8):
#        plt.scatter(plotvar1,plotvar2, color='y',marker='*',s=msize)
#    elif (rawdata[i,3]==9):
#        plt.scatter(plotvar1,plotvar2, color='k',marker='d',s=msize)
#
#plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
#plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
#plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
#plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
#plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
#plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
#plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
#plt.legend(loc=4, fontsize=15, scatterpoints=1)
#plt.yscale('log')
#plt.xscale('log')
#plt.xlim(0.1,10000)
#plt.ylim(0.1,10000)
#kPred=np.linspace(0.01,10000,50)
#plt.plot(kPred,kPred)
#plt.tick_params(axis='y', labelsize=15)
#plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=8, width=2)
#plt.tick_params(axis='x', which='minor', size=4, width=2)
#plt.tick_params(axis='y', which='major', size=8, width=2)
#plt.tick_params(axis='y', which='minor', size=4, width=2)
#plt.ylabel('Actual $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20, wrap=True)
#plt.xlabel('Predicted $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20)
#plt.tight_layout()



###High fit
###Combo par/ser for UC and 1.5 for compr (enh>20) Using all same assumed k's

#fact=0.1
#fig, ax = plt.subplots()
#for i in range(0,n):
#    plotvar2=rawdata[i,4]
#    kc=PnK[int(rawdata[i,3]),3]*10
##    if np.isnan(rawdata[i,9]):
##        kc=PnK[int(rawdata[i,3]),2]
##    else:
##        kc=rawdata[i,9]
#
#    if rawdata[i,11]>20:
#        korig=kc*(rawdata[i,6]/100)**1.5
#    else:
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#
#
#    plotvar1=korig
#
#
#    msize=50
#    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
#        plt.scatter(plotvar1,plotvar2, color='b',marker='o',s=msize)
#    elif (rawdata[i,3]==4):
#        plt.scatter(plotvar1,plotvar2, color='g',marker='v',s=msize)
#    elif (rawdata[i,3]==5):
#        plt.scatter(plotvar1,plotvar2, color='r',marker='^',s=msize)
#    elif (rawdata[i,3]==6):
#        plt.scatter(plotvar1,plotvar2, color='c',marker='<',s=msize)
#    elif (rawdata[i,3]==7):
#        plt.scatter(plotvar1,plotvar2, color='m',marker='>',s=msize)
#    elif (rawdata[i,3]==8):
#        plt.scatter(plotvar1,plotvar2, color='y',marker='*',s=msize)
#    elif (rawdata[i,3]==9):
#        plt.scatter(plotvar1,plotvar2, color='k',marker='d',s=msize)
#
#plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
#plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
#plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
#plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
#plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
#plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
#plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
#plt.legend(loc=4, fontsize=15, scatterpoints=1)
#plt.yscale('log')
#plt.xscale('log')
#plt.xlim(0.1,10000)
#plt.ylim(0.1,10000)
#kPred=np.linspace(0.01,10000,50)
#plt.plot(kPred,kPred)
#plt.tick_params(axis='y', labelsize=15)
#plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=8, width=2)
#plt.tick_params(axis='x', which='minor', size=4, width=2)
#plt.tick_params(axis='y', which='major', size=8, width=2)
#plt.tick_params(axis='y', which='minor', size=4, width=2)
#plt.ylabel('Actual $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20, wrap=True)
#plt.xlabel('Predicted $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20)
#plt.tight_layout()




###Mid fit
###Combo par/ser for UC and 1.5 for compr (enh>20) Using all same assumed k's

#fact=0.1
#fig, ax = plt.subplots()
#for i in range(0,n):
#    plotvar2=rawdata[i,4]
#    kc=PnK[int(rawdata[i,3]),3]
##    if np.isnan(rawdata[i,9]):
##        kc=PnK[int(rawdata[i,3]),2]
##    else:
##        kc=rawdata[i,9]
#
#    if rawdata[i,11]>20:
#        korig=kc*(rawdata[i,6]/100)**1.5
#    else:
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#
#
#    plotvar1=korig
#
#
#    msize=50
#    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
#        plt.scatter(plotvar1,plotvar2, color='b',marker='o',s=msize)
#    elif (rawdata[i,3]==4):
#        plt.scatter(plotvar1,plotvar2, color='g',marker='v',s=msize)
#    elif (rawdata[i,3]==5):
#        plt.scatter(plotvar1,plotvar2, color='r',marker='^',s=msize)
#    elif (rawdata[i,3]==6):
#        plt.scatter(plotvar1,plotvar2, color='c',marker='<',s=msize)
#    elif (rawdata[i,3]==7):
#        plt.scatter(plotvar1,plotvar2, color='m',marker='>',s=msize)
#    elif (rawdata[i,3]==8):
#        plt.scatter(plotvar1,plotvar2, color='y',marker='*',s=msize)
#    elif (rawdata[i,3]==9):
#        plt.scatter(plotvar1,plotvar2, color='k',marker='d',s=msize)
#
#plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
#plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
#plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
#plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
#plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
#plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
#plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
#plt.legend(loc=4, fontsize=15, scatterpoints=1)
#plt.yscale('log')
#plt.xscale('log')
#plt.xlim(0.1,10000)
#plt.ylim(0.1,10000)
#kPred=np.linspace(0.01,10000,50)
#plt.plot(kPred,kPred)
#plt.tick_params(axis='y', labelsize=15)
#plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=8, width=2)
#plt.tick_params(axis='x', which='minor', size=4, width=2)
#plt.tick_params(axis='y', which='major', size=8, width=2)
#plt.tick_params(axis='y', which='minor', size=4, width=2)
#plt.ylabel('Actual $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20, wrap=True)
#plt.xlabel('Predicted $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20)
#plt.tight_layout()




###All fit kcarb only, pure par??
###Combo par/ser for UC and 1.5 for compr (enh>15) Using all same assumed k's

#fig, ax = plt.subplots()
#fact=0
#for i in range(0,n):
#    plotvar2=rawdata[i,4]
#    kc=PnK[int(rawdata[i,3]),3]
##    if np.isnan(rawdata[i,9]):
##        kc=PnK[int(rawdata[i,3]),2]
##    else:
##        kc=rawdata[i,9]
#
#    if rawdata[i,11]>15:
#        kc=kc*10
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#    elif rawdata[i,11]>4:
#        kc=kc*0.6
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#    else:
#        kc=kc*0.1
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#
#
#    plotvar1=korig
#
#
#    msize=50
#    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
#        plt.scatter(plotvar1,plotvar2, color='b',marker='o',s=msize)
#    elif (rawdata[i,3]==4):
#        plt.scatter(plotvar1,plotvar2, color='g',marker='v',s=msize)
#    elif (rawdata[i,3]==5):
#        plt.scatter(plotvar1,plotvar2, color='r',marker='^',s=msize)
#    elif (rawdata[i,3]==6):
#        plt.scatter(plotvar1,plotvar2, color='c',marker='<',s=msize)
#    elif (rawdata[i,3]==7):
#        plt.scatter(plotvar1,plotvar2, color='m',marker='>',s=msize)
#    elif (rawdata[i,3]==8):
#        plt.scatter(plotvar1,plotvar2, color='y',marker='*',s=msize)
#    elif (rawdata[i,3]==9):
#        plt.scatter(plotvar1,plotvar2, color='k',marker='d',s=msize)
#
#plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
#plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
#plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
#plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
#plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
#plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
#plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
#plt.legend(loc=4, fontsize=15, scatterpoints=1)
#plt.yscale('log')
#plt.xscale('log')
#plt.xlim(0.1,10000)
#plt.ylim(0.1,10000)
#kPred=np.linspace(0.01,10000,50)
#plt.plot(kPred,kPred)
#plt.tick_params(axis='y', labelsize=15)
#plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=8, width=2)
#plt.tick_params(axis='x', which='minor', size=4, width=2)
#plt.tick_params(axis='y', which='major', size=8, width=2)
#plt.tick_params(axis='y', which='minor', size=4, width=2)
#plt.ylabel('Actual $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20, wrap=True)
#plt.xlabel('Predicted $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20)
#plt.tight_layout()




###All fit f,n only
###Combo par/ser for UC and 1.5 for compr (enh>15) Using all same assumed k's

#fig, ax = plt.subplots()
#for i in range(0,n):
#    plotvar2=rawdata[i,4]
#    kc=PnK[int(rawdata[i,3]),3]
##    if np.isnan(rawdata[i,9]):
##        kc=PnK[int(rawdata[i,3]),2]
##    else:
##        kc=rawdata[i,9]
#
#    if rawdata[i,11]>15:
##        korig=kc*(rawdata[i,6]/100)**1.5
#        fact=0.0
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#    elif rawdata[i,11]>4:
#        fact=0.1
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#    else:
#        fact=0.35
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#
#
#    plotvar1=korig
#
#
#    msize=50
#    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
#        plt.scatter(plotvar1,plotvar2, color='b',marker='o',s=msize)
#    elif (rawdata[i,3]==4):
#        plt.scatter(plotvar1,plotvar2, color='g',marker='v',s=msize)
#    elif (rawdata[i,3]==5):
#        plt.scatter(plotvar1,plotvar2, color='r',marker='^',s=msize)
#    elif (rawdata[i,3]==6):
#        plt.scatter(plotvar1,plotvar2, color='c',marker='<',s=msize)
#    elif (rawdata[i,3]==7):
#        plt.scatter(plotvar1,plotvar2, color='m',marker='>',s=msize)
#    elif (rawdata[i,3]==8):
#        plt.scatter(plotvar1,plotvar2, color='y',marker='*',s=msize)
#    elif (rawdata[i,3]==9):
#        plt.scatter(plotvar1,plotvar2, color='k',marker='d',s=msize)
#
#plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
#plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
#plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
#plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
#plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
#plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
#plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
#plt.legend(loc=4, fontsize=15, scatterpoints=1)
#plt.yscale('log')
#plt.xscale('log')
#plt.xlim(0.1,10000)
#plt.ylim(0.1,10000)
#kPred=np.linspace(0.01,10000,50)
#plt.plot(kPred,kPred)
#plt.tick_params(axis='y', labelsize=15)
#plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=8, width=2)
#plt.tick_params(axis='x', which='minor', size=4, width=2)
#plt.tick_params(axis='y', which='major', size=8, width=2)
#plt.tick_params(axis='y', which='minor', size=4, width=2)
#plt.ylabel('Actual $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20, wrap=True)
#plt.xlabel('Predicted $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20)
#plt.tight_layout()




###All fit
###Combo par/ser for UC and 1.5 for compr (enh>15) Using all same assumed k's

#fig, ax = plt.subplots()
#for i in range(0,n):
#    plotvar2=rawdata[i,4]
#    kc=PnK[int(rawdata[i,3]),3]
##    if np.isnan(rawdata[i,9]):
##        kc=PnK[int(rawdata[i,3]),2]
##    else:
##        kc=rawdata[i,9]
#
#    if rawdata[i,11]>15:
#        if (rawdata[i,3]==4):
#            kc=kc*10
#        else:
#            kc=kc*4
#            
##        korig=kc*(rawdata[i,6]/100)**1.5
#        fact=0.0
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#    elif rawdata[i,11]>4:
#        fact=0.025
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#    else:
#        fact=0.35
#        ks=((kc*(rawdata[i,6]/100))**(-1)+((1-rawdata[i,6]/100)*rawdata[i,7])**(-1))**(-1)
#        kp=kc*rawdata[i,6]/100+(1-rawdata[i,6]/100)*rawdata[i,7]
#        korig=((fact/ks)+(1-fact)/kp)**(-1)
#
#
#    plotvar1=korig
#
#
#    msize=50
#    if (rawdata[i,3]==1)or(rawdata[i,3]==2)or(rawdata[i,3]==3):
#        plt.scatter(plotvar1,plotvar2, color='b',marker='o',s=msize)
#    elif (rawdata[i,3]==4):
#        plt.scatter(plotvar1,plotvar2, color='g',marker='v',s=msize)
#    elif (rawdata[i,3]==5):
#        plt.scatter(plotvar1,plotvar2, color='r',marker='^',s=msize)
#    elif (rawdata[i,3]==6):
#        plt.scatter(plotvar1,plotvar2, color='c',marker='<',s=msize)
#    elif (rawdata[i,3]==7):
#        plt.scatter(plotvar1,plotvar2, color='m',marker='>',s=msize)
#    elif (rawdata[i,3]==8):
#        plt.scatter(plotvar1,plotvar2, color='y',marker='*',s=msize)
#    elif (rawdata[i,3]==9):
#        plt.scatter(plotvar1,plotvar2, color='k',marker='d',s=msize)
#
#plt.scatter(-1,-1, color='b',marker='o',s=msize, label='G')
#plt.scatter(-1,-1, color='g',marker='v',s=msize, label='GF')
#plt.scatter(-1,-1, color='r',marker='^',s=msize, label='FIB')
#plt.scatter(-1,-1, color='c',marker='<',s=msize, label='EG')
#plt.scatter(-1,-1, color='m',marker='>',s=msize, label='GNP')
#plt.scatter(-1,-1, color='y',marker='*',s=msize, label='GRF')
#plt.scatter(-1,-1, color='k',marker='d',s=msize, label='CNT')
#plt.legend(loc=4, fontsize=15, scatterpoints=1)
#plt.yscale('log')
#plt.xscale('log')
#plt.xlim(0.1,10000)
#plt.ylim(0.1,10000)
#kPred=np.linspace(0.01,10000,50)
#plt.plot(kPred,kPred)
#plt.tick_params(axis='y', labelsize=15)
#plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=8, width=2)
#plt.tick_params(axis='x', which='minor', size=4, width=2)
#plt.tick_params(axis='y', which='major', size=8, width=2)
#plt.tick_params(axis='y', which='minor', size=4, width=2)
#plt.ylabel('Actual $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20, wrap=True)
#plt.xlabel('Predicted $k$ $[W.m^{-2}.K^{-1}$]', fontsize=20)
#plt.tight_layout()




plt.show()