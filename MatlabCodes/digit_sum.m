%Digit_Summation
function output = digit_sum(input)
    if ~isscalar(input) || input <= 0 || input ~= fix(input)
       error("not a positive number");
    end
    if input < 10
       output = input;
    else
       input = input / 10; 
       a = 10*rem(input,1); 
       output = a + digit_sum(fix(input));       
    end
end