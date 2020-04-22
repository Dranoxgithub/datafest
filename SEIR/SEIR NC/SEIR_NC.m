function f = SEIR_NC(t,y, a, b)
% assume a natural birth-death rate balance
birthRate = 0.0000021; %if do not assume such balance
deathRate = 0.000002;
emigRate = 0.00205;
incubationPeriod = 6.2; 
awareness = (1/(1+exp(-0.32*t))-0.5)*1.98; % awareness is modeled by shifted and rescaled logistic function
contactRate = 1.68*(1-awareness);% contactRate¡Ê[0.5944, 1.68] 
recoveryRate = 0.04;
totalPopulation = 10490000;
f(1) = (birthRate-deathRate)*y(1)-contactRate*(y(2)+y(3))*y(1)/totalPopulation;
f(2) = contactRate*(y(2)+y(3))*y(1)/totalPopulation-(emigRate+1/incubationPeriod)*y(2);
f(3) = (1/incubationPeriod)*y(2)-(recoveryRate+emigRate)*y(3);
f(4) = recoveryRate*y(3)-deathRate*y(4);