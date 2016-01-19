%
% Hand Digit Recognization with Neural Network
% 
% Data: http://yann.lecun.com/exdb/mnist/


% Initialize
clear; close all; clc


% Setup the parameters for NN
input_layer_size  = 784; % 28x28;
hidden_layer_size = 25;
output_layer_size = 10;


% Load Data.
fprintf('Loading data ... \n')
[X, Y, X_test, Y_test, n_col, n_row] = loaddata();


% Show Data.
% displayData(X, n_col, n_row);


% Initialize NN's Parameters.
Theta1 = randomInitializeWeights(input_layer_size, hidden_layer_size);
Theta2 = randomInitializeWeights(hidden_layer_size, output_layer_size);
nn_params = [Theta1(:);Theta2(:)];


% Predict before training.
test_nn(Theta1, Theta2, X_test, Y_test);


% sigmoid gradient
fprintf('\nEvaluating sigmoid gradient...\n')
g = sigmoidGradient([1 -0.5 0 0.5 1]);
fprintf('%f ', g);
fprintf('\n\n');



% Weight regularization paramer
lambda = 1;


% Feedforward Neural Network
fprintf('Feedforward Neural Network ... \n')
J = nnCostFunction(nn_params, input_layer_size, hidden_layer_size, output_layer_size, X, Y, lambda);


% Gradient check
% fprintf('\nChecking Backpropagation... \n')
% checkNNGradients;
% lambda = 3;
% checkNNGradients(lambda);



%% ================== Training NN ======================
fprintf('\nTraining Neural Network... \n')

% Option for fmincg
options = optimset('MaxIter', 10);

% Weight for regularization.
lambda = 1;

% Create "short hand" for the cost function to be optimized.
costFunction = @(p) nnCostFunction(p, ...
    input_layer_size, hidden_layer_size, output_layer_size, X, Y, lambda);

% Training
[nn_params, cost] = fmincg(costFunction, nn_params, options);

% Obtain Theta1 and Theta2 back from nn_params.
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
    hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
    output_layer_size, (hidden_layer_size + 1));





%% ================== Test ======================
test_nn(Theta1, Theta2, X_test, Y_test);






















