function[J grad] = nnCostFunction(nn_params, ...
    input_layer_size, ...
    hidden_layer_size, ...
    num_labels, X, y, lambda)

    
    % Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
    % for out 2 layer NN.
    Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
        hidden_layer_size, (input_layer_size + 1));
    Theta2 = reshape(nn_params(1 + (hidden_layer_size * (input_layer_size + 1)):end), ...
        num_labels, (hidden_layer_size + 1));


    % Num of dataset.
    m = size(X, 1);


    % Objectives.
    J = 0;
    Theta1_grad = zeros(size(Theta1));
    Theta2_grad = zeros(size(Theta2));


    % Compute cost J.
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    y2 = zeros(m, num_labels); % 400 x 10
    for i = 1:m
        y2(i, y(i)) = 1;
    end
    z2 = [ones(m, 1) X] * Theta1';
    a2 = sigmoid(z2);
    z3 = [ones(m, 1) a2] * Theta2';
    a3 = sigmoid(z3);
    pred = a3;

    cost1 = -1 * y2 .* log(pred);
    cost2 = -1 * (1 - y2) .* log(1 - pred);
    J = (1 / m) * sum(sum(cost1 + cost2));

    Theta1_j = sum(sum(Theta1(:,2:end) .^ 2));
    Theta2_j = sum(sum(Theta2(:,2:end) .^ 2));
    reg_cost = (lambda / 2 / m) * (Theta1_j + Theta2_j);
    J = J + reg_cost;


    % Compute Gradients.
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    delta1 = zeros(size(Theta1));
    delta2 = zeros(size(Theta2));
    for t = 1:m

        % Step1: feedforward
        a_1 = X(t, :);
        z_2 = [ones(1,1), a_1] * Theta1';
        a_2 = sigmoid(z_2);
        z_3 = [ones(1,1), a_2] * Theta2';
        a_3 = sigmoid(z_3);

        % Step2: compute delta of layer 3
        d_3 = a_3;
        d_3(y(t)) = d_3(y(t)) - 1;
        d_3 = d_3';

        % Step3: compute delta of layer 2.
        d_2 = Theta2' * d_3;
        d_2 = d_2(2:end);
        d_2 = d_2 .* sigmoidGradient(z_2)';

        % Step4: Accumulate the gradients
        delta1 = delta1 + d_2 * [ones(1,1), a_1];
        delta2 = delta2 + d_3 * [ones(1,1), a_2];

    end

    % Step5
    Theta1_grad = delta1 / m;
    Theta2_grad = delta2 / m;

    % Step6: Regularized Gradient
    Theta1_reg = Theta1;
    Theta2_reg = Theta2;
    Theta1_reg(:,1) = zeros(size(Theta1, 1), 1);
    Theta2_reg(:,1) = zeros(size(Theta2, 1), 1);
    Theta1_grad = Theta1_grad + (lambda / m * Theta1_reg);
    Theta2_grad = Theta2_grad + (lambda / m * Theta2_reg);


    % Unroll gradients.
    grad = [Theta1_grad(:); Theta2_grad(:)];

end