%% Load data of MNIST, and convert to matrix.
%
% ref: http://yann.lecun.com/exdb/mnist/
% ref: http://nnet.dogrow.net/?p=31

function [X, Y, X_test, Y_test, n_col, n_row] = loaddata ()

    % training label.
    fid = fopen('data/train-labels-idx1-ubyte', 'r', 'b');
    magic_number = fread(fid, 1, 'int32');
    n_item = fread(fid, 1, 'int32');
    Y = fread(fid, [n_item 1], 'uchar');
    % size(Y)
    fclose(fid);

    % sampling.
    Y = Y(1:400,:);


    % training data.
    fid = fopen('data/train-images-idx3-ubyte', 'r', 'b');
    magic_number = fread(fid, 1, 'int32');
    n_item = fread(fid, 1, 'int32');
    n_row = fread(fid, 1, 'int32');
    n_col = fread(fid, 1, 'int32');
    X = fread(fid, [n_row*n_col n_item], 'uchar')';
    % size(X)
    % v = uint8(reshape(X(1,:), 28, 28)');
    % size(v)
    % imshow(v)
    fclose(fid);


    % sampling.
    X = X(1:400,:);


    % test label.
    fid = fopen('data/t10k-labels-idx1-ubyte', 'r', 'b');
    magic_number = fread(fid, 1, 'int32');
    n_item = fread(fid, 1, 'int32');
    Y_test = fread(fid, [n_item 1], 'uchar');
    % size(Y_test)
    fclose(fid);


    % sampling.
    Y_test = Y_test(1:400,:);



    % test data.
    fid = fopen('data/t10k-images-idx3-ubyte', 'r', 'b');
    magic_number = fread(fid, 1, 'int32');
    n_item = fread(fid, 1, 'int32');
    n_row = fread(fid, 1, 'int32');
    n_col = fread(fid, 1, 'int32');
    X_test = fread(fid, [n_row*n_col n_item], 'uchar')';
    % size(X)
    % v = uint8(reshape(X_test(1,:), 28, 28)');
    % size(v)
    % imshow(v)
    fclose(fid);

    % sampling
    X_test = X_test(1:400,:);

endfunction