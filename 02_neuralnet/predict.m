function p = predict(Theta1, Theta2, X)
% PREDICT predicts the label of an input given a trained neural network.


    % Number of trainset.
    m = size(X, 1);
    num_labels = size(Theta2, 1);


    % Go Forward.
    z2 = [ones(m, 1) X] * Theta1';
    a2 = sigmoid(z2);
    z3 = [ones(m, 1) a2] * Theta2';
    a3 = sigmoid(z3);


    % Predict.
    [results, indexes] = max(a3, [], 2);
    p = indexes;

end