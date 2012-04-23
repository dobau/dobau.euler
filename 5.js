var num = 400;
var found = false;
while (!found) {
    var isCandidate = true;
    for (var i = 2;isCandidate && i <= 20;i+=1) {
        if (num % i != 0) {
            isCandidate = false;
        }
    }
    
    if (isCandidate) {
        found = true;
    } else {
        num++;
    }
}

console.log(num);