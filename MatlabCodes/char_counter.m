function charnum = char_counter(fname, character)
    charnum = 0; 
    fid = fopen(fname, 'rt');
    if fid < 0 || ~ischar(character)
       charnum = -1; 
       return
    end
    oneline = fgets(fid);
    while ischar(oneline)
        charnum = charnum + length(strfind(oneline, character)) ;
        oneline = fgets(fid);
    end
    fclose(fid);
end