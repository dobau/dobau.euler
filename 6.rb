#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

a = 0
b = 0
for i in 0..100 do
  a += (i *i)
  b += i
end

b *= b

print b - a