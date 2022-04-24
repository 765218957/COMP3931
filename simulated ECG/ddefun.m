function [ dxdt ] = ddefun( t,x,Z )

dxdt=zeros(6,1);
v_SA1=1;
v_SA2=-1.9;
d_SA=1.9;
e_SA=0.55;
alpha_SA=3;
rho_SA=8;
w_SA=2.1;
alpha_AV=7;
v_AV1=0.5;
v_AV2=-0.5;
d_AV=4;
e_AV=0.67;
w_AV=0;
rho_AV=0;
alpha_HP=7;
v_HP1=1.65;
v_HP2=-2;
d_HP=7;
e_HP=0.67;
rho_HP=0;
w_HP=0;
k_AV_SA=0;
k_AV_SA_t=0;
t_AV_SA=0;
k_HP_SA=0;
k_HP_SA_t=0;
t_HP_SA=0;
k_SA_AV=0.66;
k_SA_AV_t=0.09;
t_SA_AV=0.8;
k_HP_AV=0;
k_HP_AV_t=0;
t_HP_AV=0;
k_SA_HP=0;
k_SA_HP_t=0;
t_SA_HP=0;
k_AV_HP=14;
k_AV_HP_t=38;
t_AV_HP=0.1;

F_SA=rho_SA*sin(w_SA*t);
F_AV=rho_AV*sin(w_AV*t);
F_HP=rho_HP*sin(w_HP*t);

xlag1=Z(:,1);
xlag2=Z(:,2);
dxdt(1)=x(2);
dxdt(2)=F_SA-alpha_SA*x(2)*(x(1)-v_SA1)*(x(1)-v_SA2)-x(1)*(x(1)+d_SA)*(x(1)+e_SA)/d_SA/e_SA...
    -k_AV_SA*x(1)-k_HP_SA*x(1);
dxdt(3)=x(4);
dxdt(4)=F_AV-alpha_AV*x(4)*(x(3)-v_AV1)*(x(3)-v_AV2)-x(3)*(x(3)+d_AV)*(x(3)+e_AV)/d_AV/e_AV...
    -k_SA_AV*x(3)+k_SA_AV_t*xlag1(1)-k_HP_AV*x(3);
dxdt(5)=x(6);
dxdt(6)=F_HP-alpha_HP*x(6)*(x(5)-v_HP1)*(x(5)-v_HP2)-x(5)*(x(5)+d_HP)*(x(5)+e_HP)/d_HP/e_HP...
    -k_SA_HP*x(5)-k_AV_HP*x(5)+k_AV_HP_t*xlag2(3);


end

