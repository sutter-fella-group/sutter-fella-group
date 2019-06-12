function BE = binde(A,Z)
av = 15.56;
as = 17.23;
ac = 0.7;
aa = 23.285;
if rem(A,2) == 1
    delta = 0;
elseif rem(Z,2) == 1
    delta = -11/A^(1/2);
else
    delta = 11/A^(1/2);
end
BE = av*A - as*A^(2/3) - ac*Z^2/(A^(1/3))- aa*((A-2*Z)^2)/A + delta;
disp(ac*Z^2/(A^(1/3)));
disp(aa*((A-2*Z)^2)/A);
end