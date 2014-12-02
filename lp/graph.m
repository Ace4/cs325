x_in = [1,2,3,5,7,8,10];
y_in = [3,5,7,11,14,15,19];

figure(1);
plot(x_in, y_in, 'rx'); hold on;
plot(x_in, y_in, 'r'); hold on;

x = 1:10;
y = 1.7142857*x + 1.8571429;

figure(1); plot(x, y, 'b'); hold off;
legend('Data Points','Data Line', 'Solution');
print -dpng 'plot.png';