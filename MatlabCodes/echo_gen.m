function output = echo_gen(input, fs, delay, amp)
    dt = 1/fs;
    start = round(delay / dt);
    if ~delay
       output = input * (amp + 1);
    elseif start > length(input)
       output = [input; zeros(start - length(input),1) ; amp * input];
    else
        output = [input(1:start) ; [input(start+1:end); zeros(start,1)] + amp * input];
    end
    if any( abs(output) > 1 )
        output = output / max(output);
    end
end