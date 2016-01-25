function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
% GRADIENTDESCENT performs gradient descent to learn theta.

    m = length(y);
    J_history = zeros(num_iters, 1);

    for iter = 1:num_iters

        h = X * theta;
        delta = X' * (h - y);
        theta = theta - (alpha / m) * delta;
        J_history(iter) = computeCost(X, y, theta);

    end

end