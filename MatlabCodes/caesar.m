function coded = caesar(v, shift)
    a = shift * ones(1, length(v));
    for i = 1:length(v)
       while a(i) + v(i) < 31 || a(i) + v(i) > 126
           if a(i) + v(i) > 126
               a(i) = a(i) - (127 - v(i));
               v(i) = 32;
           elseif a(i) + v(i) < 32
               a(i) = a(i) + (v(i) - 31);
               v(i) = 126;
           end
       end
    end
    coded = char(a + v);
end