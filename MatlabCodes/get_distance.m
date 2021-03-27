function distance = get_distance(c1,c2)
    [~,~,raw] = xlsread('Distances.xlsx');
    vec = raw(2:end,1);
    if ~(any(strcmp(vec, c1)) && any(strcmp(vec, c2)))
        distance = -1;
    else
        indexx = find(strcmp(vec, c1)) + 1;
        indexy = find(strcmp(vec, c2)) + 1;
        distance = raw{indexx, indexy};
    end
end