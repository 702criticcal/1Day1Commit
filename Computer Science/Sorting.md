CS(Computer Science)
=====================
정렬 (Sorting)
------------------
목록의 요소를 특정 순서대로 넣는 알고리즘이다. 보통 숫자식 순서(Numerical Order)와 사전식 순서(Lexicographical Order)로 정렬한다.

### 1. 계수 정렬 (Counting Sort)
##### 원소간 비교하지 않고 각 원소가 몇 개 등장하는지 개수를 세서 정렬하는 방법.
* 조건 : 모든 원소는 양의 정수여야 한다.

시간복잡도는 O(n)으로, 시간복잡도가 O(nlogn)인 퀵정렬, 병합정렬보다도 빠르다!
1. 원소의 최댓값을 구한다.
2. 0부터 최댓값까지의 인덱스를 가지는 계수를 위한 배열을 할당한다.
3. 계수 배열의 원소는 모두 0으로 초기화한다.
4. 각 원소들의 개수를 계산하여 계수 배열에 담는다.
5. 계수 배열의 원소마다 **누적합을 계산**한다.
5-1. count[i] += count[i - 1]
6. 누적합을 이용하여 정렬한다. 누적합은 해당 원소의 자리를 만드는 것이라고 생각하면 이해하기 쉽다.
7. **입력 배열의 오른쪽에서 왼쪽으로 진행해야 안정 정렬(Stable Sort)이 가능하다.**
7-1. 왼쪽에서 오른쪽으로 해도 정렬은 가능하지만 안정 정렬이 불가능하다.
	* **안정 정렬** : 정렬 후에도 원래의 순서가 유지되는 정렬을 말한다.
8. 결과 배열에 넣을 때 계수 배열의 누적합 - 1을 하고 누적합 - 1 위치로 넣는다..

* Counting Sort 예제 코드
```
# 입력될 수 있는 숫자의 최대 크기 선언
MAX_NUM = 1000
# 입력된 숫자를 저장하는 배열
A = list(map(int, input().split()))
# 입력된 숫자의 개수
N = len(A)
# 0으로 초기화된 입력될 MAX_NUM+1 길이의 배열 count 생성
count =[0]*(MAX_NUM+1)
# countSum은 누적합을 저장하는 배열
countSum =[0]*(MAX_NUM+1)
# 숫자 등장 횟수 세기
for i in range(0, N): count[A[i]] += 1
# 숫자 등장 횟수 누적합 구하기
countSum[0] = count[0] for i in range(1, MAX_NUM+1): countSum[i] = countSum[i-1]+count[i];
# 정렬된 결과를 저장하는 배열
B = [0]*(N+1) for i in range(N-1, -1, -1): B[countSum[A[i]]] = A[i] countSum[A[i]] -= 1
# A를 정렬한 결과인 B를 출력
result = "" for i in range(1, N+1): result += str(B[i]) + " " print(result)
```

<hr/>

