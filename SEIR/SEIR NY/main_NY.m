y0 = [8390000, 10, 10, 0]'; % initial data
tspan = [0,200]; % integration interval
h = 0.0001; % constant step size
[tout,yout] = rk4_NY(@SEIR_NY,tspan,y0,h);
plot(tout, yout(2, :), "y", tout, yout(3, :), "r", tout, yout(4, :), "g");
hold on
plot(Real)
legend({'Exposed','Infected','Removed', 'Real Data'});
M = readtable('NY 2.csv', 'format', '%s%f') % read excel
imported = table2array(M(:, 2));
n = length(imported);
m = yout(2, :)+yout(3, :)+yout(4, :);
m0 = m(1:91);
for i = 2:n
    imported(i) = imported(i)+imported(i-1);
    imported(i) = imported(i)*0.3;
    m0(i) = m0(i)-imported(i);
end
t0 = t(1:91);
figure(2);
plot(t0, imported, "r", t0, m0, "g");
legend({'Imported Case','Community Spread'});
xlabel('Time (Days)');
ylabel('Number Of People');