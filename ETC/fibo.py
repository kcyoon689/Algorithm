
#1
# fibo

def fibo(n):  #피보나치 수열 함수
    a,b = 1, 1  # 변수 a, b에 각각 초기값 1 대입

    if n == 1 or n ==2:  # 피보나치 수열의 1항, 2항의 값은 1이므로,
        return 1         # 1,2항일 때 1을 반환

    for i in range(1, n): # 1부터 n-1번항 까지,
        a, b = b, a+b     # 변수 a와 b에 각각 (n-1)과 (n-2)+(n-1) 값들을 대입한다.

    return a   #n항 값 반환.


"""fibo-1) for 반복문과 range 함수를 통해 8번째 항까지 출력하기"""

for k in range (1, 9): # 1번째부터 8번까지
    print(fibo(k)) # 1부터 8항까지 fibo 함수를 통해 계산 후 n번 항을 출력함
    # print(k, "번째 항: ", fibo(k))