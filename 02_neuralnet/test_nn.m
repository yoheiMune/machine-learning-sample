function [accuraty, pred] = test_nn(Theta1, Theta2, X_test, Y_test)
% TEST_NN tests NN using X and y.
pred = predict(Theta1, Theta2, X_test);
good = 0;
m_test = size(X_test, 1);
for i = 1:m_test
    if pred(i) == Y_test(i)
        good = good + 1;
    end
end
% [pred, Y_test](1:10,:) % show results
accuraty = good / m_test;
fprintf('precision: %f%%\n', accuraty * 100);

end