produto = 0;
a = 1;
b = 2;
c = 3;
while (produto != 1000 and a < 1000 and b < 1000 and c < 1000)
  if (a < b)
      a += 1;
  else
    a = 1;
    if (b < c)
        b += 1;
    else
      b = 2;
      c += 1;
    end    
  end

  if ((a*a + b*b) == c*c)
    produto = (a+b+c)
  end
end

print (a*b*c)
