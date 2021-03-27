function mx = recursive_max(v)
    if length(v) == 1
        mx = v(1);
    else
       a = recursive_max(v(2:end));  
       if v(1) >= a
           mx = v(1);
       else
           mx = a;        
       end  
    end
end