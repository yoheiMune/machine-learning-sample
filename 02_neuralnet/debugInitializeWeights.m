function W = debugInitializeWeights(fan_out, fan_in)
% DEBUGINITIALIZEWEIGHT initialize the weights of a layer with fan_in
% incoming connections and fan_out outgoing connections using a fixed
% strategy. this will help you layer in debugging


    % Set W to zeros
    W = zeros(fan_out, 1 + fan_in);

    % Initialize W using "sin", this ensures that W is always of the
    % values and will be useful for debugging.
    W = reshape(sin(1:numel(W)), size(W)) / 10;

end