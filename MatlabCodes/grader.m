function gr = grader(stud,ref,varargin)
    p = zeros(1, length(varargin));
    
    for i = 1:length(varargin)
       if isequal(stud(varargin{i}), ref(varargin{i}))
           p(i) = true;
       end
    end
    if length(find(p)) == length(varargin)
        gr = true;
    else
        gr = false;
    end

end