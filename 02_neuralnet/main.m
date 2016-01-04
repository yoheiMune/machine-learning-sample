%
% Hand Digit Recognization with Neural Network
% 
% Data: http://yann.lecun.com/exdb/mnist/


% Initialize
clear; close all; clc


% Setup the parameters for NN
input_layer_size  = 784; % 28 * 28;
hidden_layer_size = 25;
output_layer_size = 10;


% Load Data.
fprintf('Loading data ... \n')
[X, Y, X_test, Y_test, n_col, n_row] = loaddata();


% Show Data.
displayData(X, n_col, n_row);
% fprintf('Program paused. Press enter to continue.\n')
% pause;


% Initialize NN's Parameters.
Theta1 = randomInitializeWeights(input_layer_size, hidden_layer_size);
Theta2 = randomInitializeWeights(hidden_layer_size, output_layer_size);
nn_params = [Theta1(:);Theta2(:)];
% size(nn_params)


% Weight regularization paramer
lambda = 0;


% Feedforward Neural Network
fprintf('Feedforward Neural Network ... \n')
J = nnCostFunction(nn_params, input_layer_size, hidden_layer_size, output_layer_size, X, Y, lambda);

































