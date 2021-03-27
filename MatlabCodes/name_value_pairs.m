function db = name_value_pairs(varargin)
    if rem(nargin, 2) || ~iscellstr(varargin(1:2:end)) || nargin == 0
        db = {};
    else
        db = cell(0.5 * length(varargin), 2);
        n = 1;
        for i = 1:2:length(varargin) - 1
           db(n,:) = {varargin{i}, varargin{i+1}};
           n = n + 1; 
        end 
    end    
end