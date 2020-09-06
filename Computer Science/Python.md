Python
=====================

### 1. collections 모듈

#### 1-1. Counter()
* 컨테이너에 동일한 값의 자료가 몇 개인지 파악하는데 사용하는 객체
* collections.Counter(데이터) 혹은 Counter(데이터) 형태로 사용한다.
* collections.Counter()의 결과값은 **딕셔너리 형태로 출력**된다.

1-1-1. Counter()의 입력값들

1. 리스트(List)
* 리스트 안의 각 요소들의 개수를 구하여 딕셔너리 형태로 반환한다.

```
from collections import Counter

lst = ['a', 'b', 'c', 'a']
print(Counter(lst))

# 예상 결과 값: Counter({'a': 2, 'b': 1, 'c': 1})
```

2. 딕셔너리(Dictionary)
* 딕셔너리의 요소의 개수가 많은 것부터 딕셔너리 형태로 반환한다.

```
from collections import Counter

dict = {'a': 1, 'b': 2, 'c': 3}
print(Counter(dict))

# 예상 결과 값: Counter({'c': 3, 'b': 2, 'a': 1})
```

3. 값 = 개수 형태

```
from collections import Counter

c = Counter(a=2, b=3, c=2)
print(Counter(c))
print(sorted(c.elements()))

'''
예상 결과 값: 
Counter({'b': 3, 'c': 2, 'a': 2})
['a', 'a', 'b', 'b', 'b', 'c', 'c']
'''
```

4. 문자열(String)
* 문자열을 입력했을 경우, {문자 : 개수}의 딕셔너리 형태로 반환해준다.

```
from collections import Counter

container = Counter()
container.update("aabcdeffgg")
print(container)

# 예상 결과 값 : Counter({'f': 2, 'g': 2, 'a': 2, 'e': 1, 'b': 1, 'c': 1, 'd': 1})
```

### 2. functools 모듈

#### 1-1. reduce()
* 여러 개의 데이터를 대상으로 주로 누적 집계를 내기 위해서 사용하는 함수
* functools.reduce(집계 함수, 데이터[, 초기값]) 혹은 reduce(집계 함수, 데이터[, 초기값])의 형태로 사용한다.

```
from functools import reduce

container = Counter()
container.update("aabcdeffgg")
print(container)

# 예상 결과 값 : Counter({'f': 2, 'g': 2, 'a': 2, 'e': 1, 'b': 1, 'c': 1, 'd': 1})
```

1-1-1. Counter()의 입력값들