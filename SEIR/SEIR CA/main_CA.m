y0 = [39510000, 0, 0, 0]'; % initial data
tspan = [0,200]; % integration interval
tspan1 = [1, 200];
h = 0.0001; % constant step size
t = tspan1(1):tspan1(2);
[tout,yout] = rk4_CA(@SEIR_CA,tspan,y0,h);
M1 = readtable('California.csv', 'format', '%s%f') % read excel
imported1 = table2array(M1(:, 2));
n1 = length(imported1);
for i = 1
    p(i) = 0;
end
for i = 25:112
    p(i) = imported1(i-24);
end
t3 = t(1:112);
figure(1);
plot(t, yout(2, :), "y", t, yout(3, :), "r", t, yout(4, :), "g");
hold on;
plot(t3, p, "b");
legend({'Exposed','Infected','Removed', 'Real Data'});
hold off;
xlabel('Time (Days)');
ylabel('Number Of People');
M = readtable('CA 2.csv', 'format', '%s%f') % read excel
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