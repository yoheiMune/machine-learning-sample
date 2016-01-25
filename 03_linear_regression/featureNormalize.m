function [X_norm, mu, sigma] = featureNormalize(X)
% FEATURENORMALIZE normalizes the feature in X.
    
    mu = mean(X);
    sigma = std(X);
    X_norm = (X - mu) ./ sigma;

end