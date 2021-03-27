function v = reversal(v1)
    if length(v1) == 1
       v = v1;    
    else
       v = [reversal(v1(2:end)) v1(1)];     
    end      
end