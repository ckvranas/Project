function p = palindrome(v)
    if length(v) <= 1
        p = true;
    else
        if ~isequal(v(1),v(end))
            p = false;
        else
            p = palindrome(v(2:end-1));
        end
    end
end