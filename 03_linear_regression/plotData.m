function plotData(x, y)
% PLOTDATA plots the data points x and y into a new figure.

    % Open a new figure window.
    figure;

    % Plot Data.
    plot(x, y, 'r+', 'MarkerSize', 10);
    ylabel('Profit in 10,000s');
    xlabel('Population of City in 10,000s');

end