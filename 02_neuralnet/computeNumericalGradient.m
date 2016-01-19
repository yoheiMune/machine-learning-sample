function numgrad = computeNumericalGradient(J, theta)
% COMPUTENUMERICALGRADIENT computes the gradient using "finite differences"
% and gives us a numerical estimate of the gradient.

    numgrad = zeros(size(theta));
    perturb = zeros(size(theta));
    e = 1e-4;
    for p = 1:numel(theta)
        % Set perturbation vector
        perturb(p) = e;
        loss1 = J(theta - perturb);
        loss2 = J(theta + perturb);
        % Compute Numerical Gradient
        numgrad(p) = (loss2 - loss1) / (2 * e);
        perturb(p) = 0;

        % fprintf('%f, %f, %f\n', (loss1, loloss1 - loss2));
    end


end