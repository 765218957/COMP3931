clc;
clear all;
close all;
tspan=0:0.001:300;
y0=[-0.1;0.025;-0.6;0.1;-3.3;2/3];
t_AV_SA=0;
t_HP_SA=0;
t_SA_AV=0.8;
t_HP_AV=0;
t_SA_HP=0;
t_AV_HP=0.1;

lags=[t_SA_AV t_AV_HP];
sol=dde23(@ddefun,lags,@history,tspan);
X=sol.y;
T=sol.x;
b0=1;
b1=0.06;
b2=0.1;
b3=0.3;
y=b0+b1*X(1,:)+b2*X(3,:)+b3*X(5,:);
ySA=b0/3+b1*X(1,:);
yAV=b0/3+b2*X(3,:);
yHP=b0/3+b3*X(5,:);
figure;
subplot(411)
plot(T,y,'-r')
subplot(412)
plot(T,ySA,'-r')
subplot(413)
plot(T,yAV,'-r')
subplot(414)
plot(T,yHP,'-r')