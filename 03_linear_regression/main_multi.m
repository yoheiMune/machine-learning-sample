%
% Linear Regression with Multiple Values.
%

%% Initialization
clear; close all; clc;
warning ('off', 'Octave:broadcast');


% Load Data.
% ------------------------------------------------
fprintf('\n Loading data ...\n');
data = load('ex1data2.txt');
X = data(:, 1:end-1);
y = data(:, end:end);
m = length(y);


% Normalization.
% ------------------------------------------------
fprintf('\nFeature Normailization ...\n')
[X mu sigma] = featureNormalize(X);


% Add intercept term to X.
X = [ones(m, 1) X];


% Gradient Descent.
% ------------------------------------------------
fprintf('\nRun Gradient Descent ...\n')

% Adjusted parameters.
alpha = 0.01;
num_iters = 500;

% Initialize theta.
theta = zeros(size(X, 2), 1);

% Run gradient descent.
[theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters);

% Plot the convergence graph.
figure;
plot(1:numel(J_history), J_history, '-b', 'LineWidth', 2);
xlabel('Number of iterations');
ylabel('Cost J');

fprintf('theta1:%f\n', theta(1));
fprintf('theta2:%f\n', theta(2));
fprintf('theta3:%f\n', theta(3));

