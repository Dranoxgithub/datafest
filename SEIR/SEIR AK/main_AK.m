y0 = [731500, 0, 0, 0]'; % initial data
tspan = [0,200]; % integration interval
tspan1 = [1, 200];
h = 0.0001; % constant step size
[tout,yout] = rk4_AK(@SEIR_AK,tspan,y0,h);
t = tspan1(1):tspan1(2);
figure(1);
plot(t, yout(2, :), "y", t, yout(3, :), "r", t, yout(4, :), "g");
legend({'Exposed','Infected','Removed'});
xlabel('Time (Days)');
ylabel('Number Of People');
M = readtable('AK 2.csv', 'format', '%s%f') % read excel
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