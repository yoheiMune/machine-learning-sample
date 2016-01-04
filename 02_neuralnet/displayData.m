%
% Display Images.
%
function [] = displayData(X, n_col, n_row)

    % num_of_display
    display_rows = 10;
    display_cols = 10;
    num_of_display = display_rows * display_cols;

    % Setup blank display
    image_width = display_rows * n_row;
    image_height = display_cols * n_col;
    display_array = zeros(image_height, image_width);

    % Copy image to display_array
    for i = 1:num_of_display
        row_start = mod(i - 1, display_rows) * n_row + 1;
        col_start = floor((i - 1) / display_cols) * n_col + 1;
        row_end   = row_start + n_row - 1;
        col_end   = col_start + n_col - 1;
        x = reshape(X(i,:), n_col, n_row)';
        display_array(col_start:col_end, row_start:row_end) = x;
    endfor

    % Display Image
    imshow(display_array)

endfunction