def solution(A):
    B = A[0]
    C = A[1]    
    return C+B

def test():
    assert(solution("12") == "21")
    assert(solution("32") == "23")

def main():


    A = input()
    ans= solution(A)
    print(ans)
if __name__ == "__main__":
    main()