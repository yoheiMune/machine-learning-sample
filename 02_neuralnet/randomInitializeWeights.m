function W = randomInitializeWeights(L_in, L_out)
    % RANDOMINITIALIZEWEIGHTS provides weight parameter for NN using random initializing.
    % W     : wight parameter
    % L_in  : in-layer size
    % L_out : out-layer size
    epsilon = 0.12;
    W = rand(L_out, 1 + L_in) * 2 * epsilon - epsilon;
endfunction