function [t,z] = rk4_NC(f,tspan,y0,h)
% initial value ODE y¡¯ = f(t,y), y(a) = y0,
% using the classical 4-stage Runge-Kutta method
% with a fixed step size h.
% tspan = [a b] is the integration interval.
% Note that y and f can be vector functions
M = readtable('NC 2.csv', 'format', '%s%f') % read excel
imported = table2array(M(:, 2));
n = length(imported);
m = length(y0); % problem size
t = tspan(1):h:tspan(2); % output abscissae
N = length(t)-1; % number of steps
y = zeros(m,N+1);
y(:,1) = y0; % initialize
% Integrate
for i=1:min(n/h, N)
% Calculate the four stages
if mod(i, 10000) == 0 
   y(2, i) = y(2, i)+imported(i/10000)*0.3;
end
K1 = feval(f, t(i),y(:,i) );
K2 = feval(f, t(i)+.5*h, y(:,i)+.5*h*K1);
K3 = feval(f, t(i)+.5*h, y(:,i)+.5*h*K2);
K4 = feval(f, t(i)+h, y(:,i)+h*K3 );
% Evaluate approximate solution at next step
y(:,i+1) = y(:,i) + h/6 *(K1+2*K2+2*K3+K4)';
end
for i = min(n/h, N):N
%predict future trend
K1 = feval(f, t(i),y(:,i) );
K2 = feval(f, t(i)+.5*h, y(:,i)+.5*h*K1);
K3 = feval(f, t(i)+.5*h, y(:,i)+.5*h*K2);
K4 = feval(f, t(i)+h, y(:,i)+h*K3 );
% Evaluate approximate solution at next step
y(:,i+1) = y(:,i) + h/6 *(K1+2*K2+2*K3+K4)';
end
for i = 1:N
    if mod(i, 10000)==0
        z(:, i/10000) = y(:, i);
    end
end