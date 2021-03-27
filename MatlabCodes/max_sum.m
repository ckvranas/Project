function [summa, index] = max_sum(v,n)
    if n > length(v)
        summa = 0;
        index = -1;
        return
    elseif n == length(v)
        summa = sum(v);
        index = 1;
        return
    end    
    temp = zeros(length(v) - n + 1, 2);
    for i = 1:length(v)-n+1
        temp(i, 2) = i;
        for d = i:i+n-1
            temp(i, 1) = temp(i, 1) + v(d);
        end           
    end
    [summa, index] = max(temp(:,1));
    index = temp(index, 2);
end
