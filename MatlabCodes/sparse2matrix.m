function matrix = sparse2matrix(cellvec)
    matrix = cellvec{2} * ones(cellvec{1}(1), cellvec{1}(2));
    for i = 3:length(cellvec)
        if cellvec{i}(3) ~= cellvec{2}
            matrix(cellvec{i}(1), cellvec{i}(2)) = cellvec{i}(3);
        end
    end


end