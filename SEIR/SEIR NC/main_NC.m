y0 = [10490000, 10, 10, 0]'; % initial data
tspan = [0,200]; % integration interval
h = 0.0001; % constant step size
[tout,yout] = rk4_NC(@SEIR_NC,tspan,y0,h);
plot(tout, yout(2, :), "y", tout, yout(3, :), "r", tout, yout(4, :), "g");
legend({'Exposed','Infected','Removed'})
xlabel('Time (Days)')
ylabel('Number Of People')