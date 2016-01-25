%
% Linear Regression
% 
% Data: https://archive.ics.uci.edu/ml/datasets/Housing

% Initialize
clear; close all; clc


%% ============================================
%% 01. Linear Regression with a Single Value.
%% ============================================


% Load Data and Plot them.
% -----------------------------
fprintf('\nLoad Data and Plot them.\n')
data = load('ex1data1.txt');
X = data(:, 1);
y = data(:, 2);
m = length(y);
plotData(X, y);


% Gradient Descent.
% -----------------------------
fprintf('\nRunning Gradient Descent ...\n')

X = [ones(m,1), X];
theta = zeros(2, 1);

iterations = 150;
alpha = 0.01;

% compute and display initial cost.
initialcost = computeCost(X, y, theta)

% run gradient descent.
[theta, J_history] = gradientDescent(X, y, theta, alpha, iterations);
fprintf('\n theta is %f %f\n', theta);

% Plot the linear fit.
hold on;
plot(X(:,2), X*theta, '-');
legend('Training data', 'Linear regression');
hold off;
pause;


% Plot Cost.
iter = zeros(iterations, 1);
for i = 1:iterations
    iter(i) = i;
end
plot(iter, J_history, '-');
legend('Iterations', 'Cost');
pause;

% Predict values.
% -----------------------------
predict1 = [1, 3.5] * theta;
fprintf('\nFor population=35,000, we predict a profit of %f\n', predict1 * 10000);
predict2 = [1, 7] * theta;
fprintf('\nFor population=70,000, we predict a profit of %f\n', predict2 * 10000);


% fprinf('Program paused. Press enter to continue.\n')
% pause;


% Visualizing J(theta_0, theta_1)
% -----------------------------
fprintf('Visualizing J(Theta_0, theta_1)...\n');

% Grid over which we will calculate J.
theta0_vals = linspace(-10, 10, 100);
theta1_vals = linspace(-1, 4, 100);

% Initialize J_vals to a matrix of 0's.
J_vals = zeros(length(theta0_vals), length(theta1_vals));

% Fill out J_vals.
for i = 1:length(theta0_vals)
    for j = 1:length(theta1_vals)
        t = [theta0_vals(i); theta1_vals(j)];
        J_vals(i,j) = computeCost(X, y, t);
    end
end

% Because of the way meshgrids work in the surf command, we need to
% transpose J_vals before calling surf, or else the axes will be flipped.
J_vals = J_vals';
% Surface plot.
figure;
surf(theta0_vals, theta1_vals, J_vals)
xlabel('\theta_0');
ylabel('\theta_1');
pause;

% Contour plot
figure;
% Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100.
contour(theta0_vals, theta1_vals, J_vals, logspace(-2, 3, 20))
xlabel('\theta_0');
ylabel('\theta_1');
hold on;
plot(theta(1), theta(2), 'rx', 'MarkerSize', 10, 'LineWidth', 2);





