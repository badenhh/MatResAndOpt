# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:44:23 2019

@author: Games
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate as integ
from math import log10, floor

Qtot = 0.2*0.1*0.1*1*2720*870*100+(1-0.2)*0.1*0.1*1*990*(2800*100+204700) 

#Data1 = np.loadtxt('QoutCarbThinFin.csv', delimiter=',', skiprows=5)
#Integral1 = integ.cumulative_trapezoid(Data1[:,1],Data1[:,0])
#IntegralSc1 = Integral1/Qtot
#
#plt.figure()
#plt.plot(Data1[:-1,0],Integral1)
#
#plt.figure()
#plt.plot(Data1[:,0],Data1[:,1])
#
#plt.figure()
#plt.plot(IntegralSc1,Data1[1:,1])
#

Data2 = np.loadtxt('QoutThinFins.csv', delimiter=',', skiprows=5)
Integral2 = integ.cumulative_trapezoid(Data2[:,1],Data2[:,0])
IntegralSc2 = Integral2/Qtot

#plt.figure()
#plt.plot(Data2[:-1,0],Integral2)
#
#plt.figure()
#plt.plot(Data2[:,0],Data2[:,1])
#
#plt.figure()
#plt.plot(IntegralSc2,Data2[1:,1])


Data3 = np.loadtxt('QoutThinFoam.csv', delimiter=',', skiprows=5)
Integral3 = integ.cumulative_trapezoid(Data3[:,1],Data3[:,0])
IntegralSc3 = Integral3/Qtot
#
#plt.figure()
#plt.plot(Data3[:-1,0],Integral3)
#
#plt.figure()
#plt.plot(Data3[:,0],Data3[:,1])
#
#plt.figure()
#plt.plot(IntegralSc3,Data3[1:,1])


Data4 = np.loadtxt('QoutTree.csv', delimiter=',', skiprows=5)
Integral4 = integ.cumulative_trapezoid(Data4[:,1],Data4[:,0])
IntegralSc4 = Integral4/Qtot

#plt.figure()
#plt.plot(Data4[:-1,0],Integral4)
#
#plt.figure()
#plt.plot(Data4[:,0],Data4[:,1])
#
#plt.figure()
#plt.plot(IntegralSc4,Data4[1:,1])


#plt.figure()
#plt.plot(Data2[:-1,0]/60,Integral2)
#plt.plot(Data3[:-1,0]/60,Integral3)
#plt.plot(Data4[:-1,0]/60,Integral4)

#plt.figure()
#plt.plot(IntegralSc2,Data2[1:,1])
#plt.plot(IntegralSc3,Data3[1:,1])
#plt.plot(IntegralSc4,Data4[1:,1])

plt.rcParams.update({'font.size': 15})

fig, ax1 = plt.subplots()

label1 = 'Foam'
ax1.plot(Data2[0,0]/60,Integral3[0]/50000,'sk')
ax1.plot(Data2[500:-1,0]/60,Integral3[500::]/50000,'*k', label=label1, markevery = 50)
ax1.plot(Data2[:-1,0]/60,Integral3/50000,'k')
ax1.set_ylabel('Discharge [%]')
ax1.set_xlabel('Time [min]')
ax1.set_ylim(0,100)

plt.xlim(0,150)


label1 = 'Fins'
ax1.plot(Data2[500:-1,0]/60,Integral2[500::]/50500,'dk', label=label1, markevery = 50)
ax1.plot(Data2[:-1,0]/60,Integral2/50500,'k')
ax1.set_ylabel('Discharge [%]')
ax1.set_xlabel('Time [min]')
ax1.set_ylim(0,100)

label1 = 'Tree'
ax1.plot(Data2[500:-1,0]/60,Integral4[500::]/60000,'sk', label=label1, markevery = 50)
ax1.plot(Data2[:-1,0]/60,Integral4/60000,'k')
ax1.set_ylabel('Discharge [%]')
ax1.set_xlabel('Time [min]')
ax1.set_ylim(0,100)

plt.legend(loc=4, prop={'size': 17})
plt.tight_layout()

plt.style.use('default')


fig, ax = plt.subplots(figsize=(5, 5))

#plt.scatter(1.1,0.95, color='k',marker='o', label='G')
#plt.scatter(5.7,3.37, color='k',marker='o', label='G')
#plt.scatter(17,9.5, color='k',marker='o', label='G')
#plt.scatter(30,34, color='k',marker='o', label='G')
plt.scatter(1.1,0.96, color='k',marker='^', label='$\Delta T_{PCM}$', s=125)
plt.scatter(5.7,3.39, color='k',marker='^', s=125)
plt.scatter(17,9.65, color='k',marker='^', s=125)
plt.scatter(30,35.9, color='k',marker='^', s=125)
plt.scatter(1.1,0.76, color='k',marker='o', s=80, label='$\Delta T_{GR}$')
plt.scatter(1.9,1.56, color='k',marker='o', s=80)
plt.scatter(6.4,3.19, color='k',marker='o', s=80)
plt.scatter(7,5, color='k',marker='o', s=80)
plt.scatter(12.75,11, color='k',marker='o', s=80)
plt.scatter(18,21.2, color='k',marker='o', s=80)
plt.show()
plt.xlim(0,37)
plt.ylim(0,37)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=10, width=2)
#plt.tick_params(axis='x', which='minor', size=5, width=2)
#plt.tick_params(axis='y', which='major', size=10, width=2)
#plt.tick_params(axis='y', which='minor', size=5, width=2)
plt.ylabel('Predicted [K]', fontsize=20, wrap=True)
plt.xlabel('Actual [K]', fontsize=20)
plt.legend(loc=4, fontsize=20)
plt.tight_layout()


xfrac=np.linspace(0,37,500)
plt.plot(xfrac,xfrac,'k')


DataXfrac1 = np.loadtxt('Xfrac_1.csv', delimiter=',', skiprows=5)
DataXfrac2 = np.loadtxt('Xfrac_2_5.csv', delimiter=',', skiprows=5)
DataXfrac3 = np.loadtxt('Xfrac_5.csv', delimiter=',', skiprows=5)
DataXfrac4 = np.loadtxt('Xfrac_10.csv', delimiter=',', skiprows=5)

plt.style.use('default')
plt.rcParams.update({'font.size': 15})
fig, ax2 = plt.subplots()

label1 = '$x_{GR}=1$%'
label2 = '$x_{GR}=2.5$%'
label3 = '$x_{GR}=5$%'
label4 = '$x_{GR}=10$%'
ax2.plot(DataXfrac1[:,0],DataXfrac1[:,1],'*k', label=label1, markevery = 2)
ax2.plot(DataXfrac2[:,0],DataXfrac2[:,1],'ok', label=label2, markevery = 2)
ax2.plot(DataXfrac3[:,0],DataXfrac3[:,1],'vk', label=label3, markevery = 2)
ax2.plot(DataXfrac4[:,0],DataXfrac4[:,1],'^k', label=label4, markevery = 2)
ax2.set_ylabel('Melt fraction [%]')
ax2.set_xlabel('Time [s]')
ax2.set_ylim(0,1)
plt.xlim(0,11)

plt.plot([0,3.9],[1,0],'--k')
plt.plot([0,4.4],[1,0],'--k')
plt.plot([0,5.9],[1,0],'--k')
plt.plot([0,9],[1,0],'--k')

plt.legend(loc=1)
plt.tight_layout()



plt.style.use('default')
plt.rcParams.update({'font.size': 15})


fig, ax = plt.subplots()

DTgrDT = np.array([1.1,1.9,6.4,7,12.75,18])
DTgrQ = np.array([105200,102620,100200,96720,87050,75130])
DTpcmDT = np.array([1.1,5.7,17,30])
DTpcmQ = np.array([105200,98694,72351,44080])
plt.scatter(DTgrDT,DTgrQ/1000, color='k',marker='o', label='$\Delta T_{GR}$')
plt.scatter(DTpcmDT,DTpcmQ/1000, color='k',marker='^', label='$\Delta T_{PCM}$')
plt.show()
#plt.xlim(0,35)
#plt.ylim(0,35)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
#plt.tick_params(axis='x', which='major', size=10, width=2)
#plt.tick_params(axis='x', which='minor', size=5, width=2)
#plt.tick_params(axis='y', which='major', size=10, width=2)
#plt.tick_params(axis='y', which='minor', size=5, width=2)
plt.ylabel('Ave disch rate [kW]', fontsize=20, wrap=True)
plt.xlabel('Temp gradient [K]', fontsize=20)
plt.tight_layout()
plt.legend(loc=3)

DTgrF = np.polyfit(DTgrDT,DTgrQ/1000,1)
F1 = np.poly1d(DTgrF)
arr_DT = np.arange(0,25,5)
plt.plot(arr_DT, F1(arr_DT),'--k')

DTpcmF = np.polyfit(DTpcmDT,DTpcmQ/1000,1)
F2 = np.poly1d(DTpcmF)
arr_DT = np.arange(0,35,5)
plt.plot(arr_DT, F2(arr_DT),'--k')
plt.xlim(0,31)

plt.annotate("$y = -1.73x + 108$", xy=(17,84), fontsize=16)
plt.annotate("$y = -2.16x + 109$", xy=(12,51), fontsize=16)


TmPCM_H=334.0
TmPCM_L=69.0
ThtfIN=25.0
kGR=1750.0
rhoE_H=88*1000*2110.0 #kJ/kg*kg/m3
rhoE_L=187000000.0
tdis=12*3600.0
DTmax=7.0
Q_H=30000000.0
Q_L=10000.0
DTlm_H=54.0
DTlm_L=11.75
Ppcm_H=844.0
Ppcm_L=940.0
Palu=5400.0
Pgr=58916000.0

arr_xGR = np.arange(0.05,0.6,0.05)

h_HT = 1/(TmPCM_H-ThtfIN)*(3*arr_xGR*kGR*rhoE_H*DTmax/tdis)**(0.5)
A_HT = Q_H/h_HT/DTlm_H
Vpcm_HT = Q_H*tdis/rhoE_H
CpcmH = Vpcm_HT*Ppcm_H*arr_xGR/arr_xGR
CaluH = A_HT*1/1000*Palu
CgrH = Vpcm_HT/(1-arr_xGR)*arr_xGR*Pgr

plt.style.use('default')
plt.rcParams.update({'font.size': 15})
plt.rcParams.update({'legend.fontsize': 14})

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(arr_xGR,h_HT,'*k', markersize=10, label='$h_{max}$')
ax1.plot(arr_xGR,h_HT,'k')
ax1.set_ylabel('$h_{max}$  $[W.m^{-2}.K^{-1}]$')
ax1.set_xlabel('$x_{GR}$ [-]')
ax1.plot(0,-10,'ok', markersize=8, label='Fins')
ax1.plot(0,-10,'^k', markersize=8, label='Exchanger')
ax1.plot(0,-10,'vk', markersize=8, label='PCM')
plt.legend(loc=1, bbox_to_anchor=(0.99,0.85))

ax2 = fig1.add_subplot(111, sharex=ax1, frameon=False)
ax2.plot(arr_xGR,CgrH/1000000,'ok', markersize=8)
ax2.plot(arr_xGR,CgrH/1000000,'k')
ax2.plot(arr_xGR,CaluH/1000000,'^k', markersize=8)
ax2.plot(arr_xGR,CaluH/1000000,'k')
ax2.plot(arr_xGR,CpcmH/1000000,'vk', markersize=8)
ax2.plot(arr_xGR,CpcmH/1000000,'k')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
ax2.set_yscale('log')
ax2.set_ylabel('Cost [M$]')


ax1.set_ylim(0,100)
ax2.set_ylim(0.01,1000000)

plt.xlim(0,0.51)
plt.tight_layout()


h_LT = 1/(TmPCM_L-ThtfIN)*(3*arr_xGR*kGR*rhoE_L*DTmax/tdis)**(0.5)
A_LT = Q_L/h_LT/DTlm_L
Vpcm_LT = Q_L*tdis/rhoE_L
CpcmL = Vpcm_LT*Ppcm_L*arr_xGR/arr_xGR
CaluL = A_LT*1/1000*Palu
CgrL = Vpcm_LT/(1-arr_xGR)*arr_xGR*Pgr

plt.style.use('default')
plt.rcParams.update({'font.size': 15})
plt.rcParams.update({'legend.fontsize': 14})

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(arr_xGR,h_LT,'*k', markersize=10, label='$h_{max}$')
ax1.plot(arr_xGR,h_LT,'k')
ax1.set_ylabel('$h_{max}$  $[W.m^{-2}.K^{-1}]$')
ax1.set_xlabel('$x_{GR}$ [-]')
ax1.plot(0,-10,'ok', markersize=8, label='Fins')
ax1.plot(0,-10,'^k', markersize=8, label='Exchanger')
ax1.plot(0,-10,'vk', markersize=8, label='PCM')
plt.legend(loc=1, bbox_to_anchor=(0.99,0.72))

ax2 = fig1.add_subplot(111, sharex=ax1, frameon=False)
ax2.plot(arr_xGR,CgrL/1000000,'ok', markersize=8)
ax2.plot(arr_xGR,CgrL/1000000,'k')
ax2.plot(arr_xGR,CaluL/1000000,'^k', markersize=8)
ax2.plot(arr_xGR,CaluL/1000000,'k')
ax2.plot(arr_xGR,CpcmL/1000000,'vk', markersize=8)
ax2.plot(arr_xGR,CpcmL/1000000,'k')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
ax2.set_yscale('log')
ax2.set_ylabel('Cost [M$]')


ax1.set_ylim(0,205)
ax2.set_ylim(0.00001,5000)

plt.xlim(0,0.51)
plt.tight_layout()







TmPCM_H=334.0
TmPCM_L=69.0
ThtfIN=25.0
kGR=3100.0
rhoE_H=2640000000.0
rhoE_L=683000000.0
tdis=1*3600.0
DTmax=7.0
Q_H=30000000.0
Q_L=10000.0
DTlm_H=54.0
DTlm_L=11.75
Ppcm_H=52800.0
Ppcm_L=52360.0
Palu=5400.0
Pgr=58916000.0

arr_xGR = np.arange(0.05,0.6,0.05)

h_HT = 1/(TmPCM_H-ThtfIN)*(3*arr_xGR*kGR*rhoE_H*DTmax/tdis)**(0.5)
A_HT = Q_H/h_HT/DTlm_H
Vpcm_HT = Q_H*tdis/rhoE_H
CpcmH = Vpcm_HT*Ppcm_H*arr_xGR/arr_xGR
CaluH = A_HT*1/1000*Palu
CgrH = Vpcm_HT/(1-arr_xGR)*arr_xGR*Pgr

plt.style.use('default')
plt.rcParams.update({'font.size': 15})
plt.rcParams.update({'legend.fontsize': 11})

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(arr_xGR,h_HT,'*k', markersize=10, label='$h_{max}$')
ax1.plot(arr_xGR,h_HT,'k')
ax1.set_ylabel('$h_{max}$  $[W.m^{-2}.K^{-1}]$')
ax1.set_xlabel('$x_{GR}$ [-]')
ax1.plot(0,-10,'ok', markersize=8, label='Fins')
ax1.plot(0,-10,'^k', markersize=8, label='Exchanger')
ax1.plot(0,-10,'vk', markersize=8, label='PCM')
plt.legend(loc=1, bbox_to_anchor=(0.99,0.4))

ax2 = fig1.add_subplot(111, sharex=ax1, frameon=False)
ax2.plot(arr_xGR,CgrH/1000000,'ok', markersize=8)
ax2.plot(arr_xGR,CgrH/1000000,'k')
ax2.plot(arr_xGR,CaluH/1000000,'^k', markersize=8)
ax2.plot(arr_xGR,CaluH/1000000,'k')
ax2.plot(arr_xGR,CpcmH/1000000,'vk', markersize=8)
ax2.plot(arr_xGR,CpcmH/1000000,'k')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
ax2.set_yscale('log')
ax2.set_ylabel('Cost [M$]')


ax1.set_ylim(0,600)
ax2.set_ylim(0.005,5000)

plt.xlim(0,0.51)
plt.tight_layout()


h_LT = 1/(TmPCM_L-ThtfIN)*(3*arr_xGR*kGR*rhoE_L*DTmax/tdis)**(0.5)
A_LT = Q_L/h_LT/DTlm_L
Vpcm_LT = Q_L*tdis/rhoE_L
CpcmL = Vpcm_LT*Ppcm_L*arr_xGR/arr_xGR
CaluL = A_LT*1/1000*Palu
CgrL = Vpcm_LT/(1-arr_xGR)*arr_xGR*Pgr

plt.style.use('default')
plt.rcParams.update({'font.size': 15})
plt.rcParams.update({'legend.fontsize': 11})

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(arr_xGR,h_LT,'*k', markersize=10, label='$h_{max}$')
ax1.plot(arr_xGR,h_LT,'k')
ax1.set_ylabel('$h_{max}$  $[W.m^{-2}.K^{-1}]$')
ax1.set_xlabel('$x_{GR}$ [-]')
ax1.plot(0,-50,'ok', markersize=8, label='Fins')
ax1.plot(0,-50,'^k', markersize=8, label='Exchanger')
ax1.plot(0,-50,'vk', markersize=8, label='PCM')
plt.legend(loc=1, bbox_to_anchor=(0.99,0.45))

ax2 = fig1.add_subplot(111, sharex=ax1, frameon=False)
ax2.plot(arr_xGR,CgrL/1000000,'ok', markersize=8)
ax2.plot(arr_xGR,CgrL/1000000,'k')
ax2.plot(arr_xGR,CaluL/1000000,'^k', markersize=8)
ax2.plot(arr_xGR,CaluL/1000000,'k')
ax2.plot(arr_xGR,CpcmL/1000000,'vk', markersize=8)
ax2.plot(arr_xGR,CpcmL/1000000,'k')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
ax2.set_yscale('log')
ax2.set_ylabel('Cost [M$]')


ax1.set_ylim(0,2000)
ax2.set_ylim(0.000001,10)

plt.xlim(0,0.51)
plt.tight_layout()






kPGS = np.array([400,1000,1750])
cPGS = np.array([6.1,14.7,26.0])
tPGS = np.array([0.2,0.07,0.017])
kC = 3200.0
tC = 0.0008

arr_k = np.arange(400,1900,50)
arr_k3 = np.arange(1900,3500,50)
f_t =-0.0018285*arr_k+6.0466
f_t2 =-0.0018285*arr_k3+6.0466
arr_k2 = np.arange(400,1800,50)
f_c =0.0148*arr_k2+0.1284

plt.style.use('default')
plt.rcParams.update({'font.size': 15})

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(kPGS,np.log(tPGS*1000),'vk', markersize=10, label='$t\,_{  Commercial}$')
ax1.plot(kC,np.log(tC*1000),'ok', markersize=10, label='$t\,_{Chalmers}$ [X]')
ax1.plot(arr_k,f_t,'k')
ax1.plot(arr_k3,f_t2,'--k')
ax1.set_ylabel('$ln\,(t)$ [μm]')
#ax1.set_ylabel('$ln\,(t)$ [XXm]')
ax1.set_xlabel('$k$  $[W.m^{-1}.K^{-1}]$')
ax1.plot(0,0,'^k', markersize=8, label='$Cost$')
plt.legend(loc=1)

ax2 = fig1.add_subplot(111, sharex=ax1, frameon=False)
ax2.plot(kPGS,cPGS,'^k', markersize=10, label='Cost')
ax2.plot(arr_k2,f_c,'k')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
ax2.set_ylabel('$Cost\,\,[\$.g^{-1}$]')

plt.annotate("$y = 0.0148*k+0.128$", xy=(660,7))
plt.annotate("$y = -0.00183*k$", xy=(1900,18.9))
plt.annotate("$+6.05$", xy=(3000,17))

#ax1.set_ylim(0,0.3)
ax2.set_ylim(5,30)

plt.xlim(200,3500)
plt.tight_layout()






#TmPCM_H=334.0
#TmPCM_L=69.0
#ThtfIN=25.0
#kGR=1750.0
#kPCM_H=11.3
#kPCM_L=0.6
#rhoE_H=2640000000.0
#rhoE_L=683000000.0
#tdis=1*3600.0
#DTmax=7.0
#Q_H=30000000.0
#Q_L=10000.0
#DTlm_H=54.0
#DTlm_L=11.75
#Ppcm_H=52800.0
#Ppcm_L=52360.0
#Palu=5400.0
#Pgr=58916000.0
#
#arr_xGR = np.arange(0.02,0.6,0.05)
#
#h_HT = 1/(TmPCM_H-ThtfIN)*(3*arr_xGR*kGR*rhoE_H*DTmax/tdis)**(0.5)
#A_HT = Q_H/h_HT/DTlm_H
#h_HT_nofin = 1/(TmPCM_H-ThtfIN)*(rhoE_H*DTmax*kPCM_H/tdis)**(0.5)
#A_HT_nofin = Q_H/h_HT_nofin/DTlm_H
#Vpcm_HT = Q_H*tdis/rhoE_H
#Vtot_HT = Vpcm_HT/(1-arr_xGR)
#CpcmH = Vpcm_HT*Ppcm_H*arr_xGR/arr_xGR
#BEgr = 1/1000.0*Palu/Vtot_HT/arr_xGR*(A_HT_nofin-A_HT)
#
#plt.style.use('default')
#plt.rcParams.update({'font.size': 15})
#plt.rcParams.update({'legend.fontsize': 11})
#
#fig1 = plt.figure()
#ax1 = fig1.add_subplot(111)
#ax1.plot(arr_xGR,Pgr/BEgr,'ok', markersize=10, label='k=1750 $[W.m^{-1}.K^{-1}]$')
#ax1.plot(arr_xGR,Pgr/BEgr,'k')
#ax1.set_ylabel('Cost reduction factor [-]')
#ax1.set_xlabel('$x_{GR}$ [-]')
#plt.xlim(0,0.51)
#ax1.set_yscale('log')
#
#
#kGR=1000.0
#Pgr=33310200.0
#
#h_HT = 1/(TmPCM_H-ThtfIN)*(3*arr_xGR*kGR*rhoE_H*DTmax/tdis)**(0.5)
#A_HT = Q_H/h_HT/DTlm_H
#h_HT_nofin = 1/(TmPCM_H-ThtfIN)*(rhoE_H*DTmax*kPCM_H/tdis)**(0.5)
#A_HT_nofin = Q_H/h_HT_nofin/DTlm_H
#Vpcm_HT = Q_H*tdis/rhoE_H
#Vtot_HT = Vpcm_HT/(1-arr_xGR)
#CpcmH = Vpcm_HT*Ppcm_H*arr_xGR/arr_xGR
#BEgr = 1/1000.0*Palu/Vtot_HT/arr_xGR*(A_HT_nofin-A_HT)
#ax1.plot(arr_xGR,Pgr/BEgr,'^k', markersize=10, label='k= 1000$[W.m^{-1}.K^{-1}]$')
#ax1.plot(arr_xGR,Pgr/BEgr,'k')
#
#
#
#kGR=400.0
#Pgr=13822600.0
#
#h_HT = 1/(TmPCM_H-ThtfIN)*(3*arr_xGR*kGR*rhoE_H*DTmax/tdis)**(0.5)
#A_HT = Q_H/h_HT/DTlm_H
#h_HT_nofin = 1/(TmPCM_H-ThtfIN)*(rhoE_H*DTmax*kPCM_H/tdis)**(0.5)
#A_HT_nofin = Q_H/h_HT_nofin/DTlm_H
#Vpcm_HT = Q_H*tdis/rhoE_H
#Vtot_HT = Vpcm_HT/(1-arr_xGR)
#CpcmH = Vpcm_HT*Ppcm_H*arr_xGR/arr_xGR
#BEgr = 1/1000.0*Palu/Vtot_HT/arr_xGR*(A_HT_nofin-A_HT)
#ax1.plot(arr_xGR,Pgr/BEgr,'vk', markersize=10, label='k= 400$[W.m^{-1}.K^{-1}]$')
#ax1.plot(arr_xGR,Pgr/BEgr,'k')
#
#plt.legend(loc=1, bbox_to_anchor=(0.99,0.4))
#plt.tight_layout()




# NB!!! H is actually L from here on

TmPCM_H=69.0
ThtfIN=25.0
kGR=1750.0
kGR=3100.0
kPCM_H=0.6
rhoE_H=683000000.0
tdis=1*3600.0
DTmax=7.0
Q_H=10000.0
DTlm_H=11.75
Ppcm_H=52360.0
Palu=5400.0
Pgr=58916000.0

arr_xGR = np.arange(0.05,0.6,0.05)

h_HT = 1/(TmPCM_H-ThtfIN)*(3*arr_xGR*kGR*rhoE_H*DTmax/tdis)**(0.5)
A_HT = Q_H/h_HT/DTlm_H
h_HT_nofin = 1/(TmPCM_H-ThtfIN)*(rhoE_H*DTmax*kPCM_H/tdis)**(0.5)
A_HT_nofin = Q_H/h_HT_nofin/DTlm_H
Vpcm_HT = Q_H*tdis/rhoE_H
Vtot_HT = Vpcm_HT/(1-arr_xGR)
CpcmH = Vpcm_HT*Ppcm_H*arr_xGR/arr_xGR
BEgr = 1/1000.0*Palu/Vtot_HT/arr_xGR*(A_HT_nofin-A_HT)
CFgr=Pgr/BEgr


dataCh=np.zeros((9,3))
dataCh[8,0]=round(h_HT[9],0)
dataCh[8,1]=round(CFgr[9], -int(floor(log10(abs(CFgr[9])))))
dataCh[8,2]=CFgr[9]
dataCh[7,0]=round(h_HT[3],0)
dataCh[7,1]=round(CFgr[3], -int(floor(log10(abs(CFgr[3])))))
dataCh[7,2]=CFgr[3]
dataCh[6,0]=round(h_HT[0],0)
dataCh[6,1]=round(CFgr[0], -int(floor(log10(abs(CFgr[0])))))
dataCh[6,2]=CFgr[0]

kGR=1000.0
Pgr=33310200.0

h_HT = 1/(TmPCM_H-ThtfIN)*(3*arr_xGR*kGR*rhoE_H*DTmax/tdis)**(0.5)
A_HT = Q_H/h_HT/DTlm_H
h_HT_nofin = 1/(TmPCM_H-ThtfIN)*(rhoE_H*DTmax*kPCM_H/tdis)**(0.5)
A_HT_nofin = Q_H/h_HT_nofin/DTlm_H
Vpcm_HT = Q_H*tdis/rhoE_H
Vtot_HT = Vpcm_HT/(1-arr_xGR)
CpcmH = Vpcm_HT*Ppcm_H*arr_xGR/arr_xGR
BEgr = 1/1000.0*Palu/Vtot_HT/arr_xGR*(A_HT_nofin-A_HT)
CFgr=Pgr/BEgr


dataCh[5,0]=round(h_HT[9],0)
dataCh[5,1]=round(CFgr[9], -int(floor(log10(abs(CFgr[9])))))
dataCh[5,2]=CFgr[9]
dataCh[4,0]=round(h_HT[3],0)
dataCh[4,1]=round(CFgr[3], -int(floor(log10(abs(CFgr[3])))))
dataCh[4,2]=CFgr[3]
dataCh[3,0]=round(h_HT[0],0)
dataCh[3,1]=round(CFgr[0], -int(floor(log10(abs(CFgr[0])))))
dataCh[3,2]=CFgr[0]


kGR=400.0
Pgr=13822600.0

h_HT = 1/(TmPCM_H-ThtfIN)*(3*arr_xGR*kGR*rhoE_H*DTmax/tdis)**(0.5)
A_HT = Q_H/h_HT/DTlm_H
h_HT_nofin = 1/(TmPCM_H-ThtfIN)*(rhoE_H*DTmax*kPCM_H/tdis)**(0.5)
A_HT_nofin = Q_H/h_HT_nofin/DTlm_H
Vpcm_HT = Q_H*tdis/rhoE_H
Vtot_HT = Vpcm_HT/(1-arr_xGR)
CpcmH = Vpcm_HT*Ppcm_H*arr_xGR/arr_xGR/1000
CaluH = A_LT*1/1000*Palu/1000
CgrH = Vpcm_LT/(1-arr_xGR)*arr_xGR*Pgr/1000
BEgr = 1/1000.0*Palu/Vtot_HT/arr_xGR*(A_HT_nofin-A_HT)
CFgr=Pgr/BEgr


dataCh[2,0]=round(h_HT[9],0)
dataCh[2,1]=round(CFgr[9], -int(floor(log10(abs(CFgr[9])))))
dataCh[2,2]=CFgr[9]
dataCh[1,0]=round(h_HT[3],0)
dataCh[1,1]=round(CFgr[3], -int(floor(log10(abs(CFgr[3])))))
dataCh[1,2]=CFgr[3]
dataCh[0,0]=round(h_HT[0],0)
dataCh[0,1]=round(CFgr[0], -int(floor(log10(abs(CFgr[0])))))
dataCh[0,2]=CFgr[0]



print(CgrH[0]/(CgrH[0]+CaluH[0]+CpcmH[0]))