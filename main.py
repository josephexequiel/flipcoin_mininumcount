A = [1, 0, 1, 0, 1, 1, 1];

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

def solution(A):
    i = 0;
    count = 0;
    baseval = A[0];
    #print("Iteration:");
    while i < len(A):
        #print(baseval, A[i])
        if looper(baseval, A[i]) == False:
            count = count + 1;
            if baseval == 0:
                baseval = 1;
            elif baseval == 1:
                baseval = 0;
        else:
            baseval = A[i];
        i = i + 1;
    #print("Minimum Flip Count: ", len(A) - count);
    print(len(A) - count);

solution(A);
