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
pred = predict(Theta1, Theta2, X_test);
good = 0;
m_test = size(X_test, 1)
for i = 1:m_test
    if pred(i) == Y_test(i)
        good = good + 1;
    end
end
% [pred, Y_test](1:10,:) % show results
fprintf('precision: %f%%\n', (good * 100 / m_test));


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



% Gradient check 1
fprintf('\nChecking Backpropagation... \n')
checkNNGradients;





























