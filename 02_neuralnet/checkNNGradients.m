function checkNNGradients(lambda)
% CHECKNNGRADIENTS creates a small neural network to check the
% backpropagation gradients.


    if ~exist('lambda', 'var') || isempty(lambda)
        lambda = 0;
    end


    input_layer_size = 3;
    hidden_layer_size = 5;
    num_labels = 3;
    m = 5;


    % We generate some 'random' test data.
    Theta1 = debugInitializeWeights(hidden_layer_size, input_layer_size);
    Theta2 = debugInitializeWeights(num_labels, hidden_layer_size);

    % Reusing debugInitializeWeights to generate X.
    X = debugInitializeWeights(m, input_layer_size - 1);
    y = 1 + mod(1:m, num_labels);

    % Unroll parameters.
    nn_params = [Theta1(:) ; Theta2(:)];

    % Short hand for cost function
    costFunc = @(p) nnCostFunction(p, input_layer_size, hidden_layer_size, ...
        num_labels, X, y, lambda)

    [cost, grad] = costFunc(nn_params);
    numgrad = computeNumericalGradient(costFunc, nn_params);

    idx = zeros(size(nn_params));
    for i = 1:size(nn_params, 1)
        idx(i) = i;
    end

    % Visually examine the two gradient computations. The two columns
    % you get should be very similar;
    disp([idx numgrad grad]);

    % Evaluate the norm of the difference between two solutions.
    diff = norm(numgrad-grad)/norm(numgrad+grad);
    fprintf('evaluate the norm of the difference: %g\n', diff);








end