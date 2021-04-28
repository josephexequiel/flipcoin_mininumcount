def looper(baseval, tempval):
    if baseval == 0:
        if tempval == 1:
            return True;
        else:
            return False;
    elif baseval == 1:
        if tempval == 0:
            return True;
        else:
            return False;
    else:
        return False;

def countflip(A):
    i = 0;
    count = 0;
    baseval = A[0];
    print("Iteration:");
    while i < len(A):
        print(baseval, A[i]);
        if looper(baseval, A[i]) == False:
            count = count + 1;
            if baseval == 0:
                baseval = 1;
            elif baseval == 1:
                baseval = 0;
        else:
            baseval = A[i];
        i = i + 1;
    dataset1 = len(A) - count;
    if dataset1 < count:
        result = dataset1;
    else:
        result = count;
    return result;

def solution(A):
    finaloutput = countflip(A);
    print("Minimum Flip Needed: ", finaloutput);
    return finaloutput;

A = [1, 1, 0, 1, 1];
solution(A);
A = [1, 1, 1, 1, 1, 1, 1];
solution(A);
A = [1, 0, 1, 1, 1, 1, 1];
solution(A);
A = [1, 1, 0, 0, 0, 1, 1];
solution(A);
A = [1, 1, 0, 1, 1];
solution(A);

