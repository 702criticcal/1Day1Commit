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

### 3. re 모듈

파이썬에서 정규표현식을 지원하기 위해 제공하는 기본 내장 모듈.
* re.compile()을 사용하여 정규표현식을 컴파일한다. 컴파일할 때, 특정 옵션을 주는 것도 가능하다.
```
# 다음 설명에도 계속 이 패턴을 사용하여 설명한다.
>>> import re
>>> p = re.compile('[a-z]+')
```

#### 정규식을 이용한 문자열 검색
1. match() : 문자열의 처음부터 정규식과 매치되는지 조사한다. 매치될 때는 match 객체 반환, 매치되지 않을 때는 None 반환.
* 매치되는 상황.
```
>>> m = p.match("python")
>>> print(m)
<_sre.SRE_Match object at 0x01F3F9F8>
```
* 매치되지 않는 상황. 처음에 나오는 문자 3이 정규식 [a-z]+에 부합하지 않으므로 None이 반환된다.
```
>>> m = p.match("3 python")
>>> print(m)
None
```
* 축약한 코드 형태.
```
# match 메소드 사용 시, 이 방법도 사용 가능.
>>> import re
>>> m = re.match('[a-z]+', "python")
```

1-1. match 객체의 메소드
- group() : 매치된 문자열을 돌려준다.
- start() : 매치된 문자열의 시작 위치를 돌려준다.
- end() : 매치된 문자열의 끝 위치를 돌려준다.
- span() : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
```
>>> m = p.match("python")
>>> m.group()
'python'
>>> m.start()
0
>>> m.end()
6
>>> m.span()
(0, 6)
```
2. search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사한다. 매치될 때는 match 객체 반환, 매치되지 않을 때는 None 반환.
```
>>> m = p.search("python")
>>> print(m)
<_sre.SRE_Match object at 0x01F3FA68>
```
* match와 다르게 문자열의 처음부터 검색하는 것이 아니라 전체를 검색하기 때문에 match 객체를 반환한다.
```
>>> m = p.search("3 python")
>>> print(m)
<_sre.SRE_Match object at 0x01F3FA30>
```
3. findall() : 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
* 문자열의 각 단어를 정규식 [a-z]+과 매치해서 리스트로 반환한다.
```
>>> result = p.findall("life is too short")
>>> print(result)
['life', 'is', 'too', 'short']
```
4. finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.
* findall과 동일하지만 그 결과로 반복 가능한 객체를 반환한다. 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.
```
>>> result = p.finditer("life is too short")
>>> print(result)
<callable_iterator object at 0x01F5E390>
>>> for r in result: print(r)
...
<_sre.SRE_Match object at 0x01F3F9F8>
<_sre.SRE_Match object at 0x01F3FAD8>
<_sre.SRE_Match object at 0x01F3FAA0>
<_sre.SRE_Match object at 0x01F3F9F8>
```

#### 백슬래시 문제

* \section 문자열을 찾기 위한 정규식을 만든다고 가정한다고 하면, \s는 whitespace로 인식되어 매치가 의도한대로 이루어지지 않는다.
* 그렇기 때문에 의도한 대로 매치하고 싶다면 \\section으로 변경해야 한다.
* 하지만, 실제 파이썬 정규식 엔진에는 파이썬 문자열 리터럴 규칙에 따라 \\이 \로 변경되어 문자열에 전달된다.
    * 이 문제는 \이 포함된 정규식을 **파이썬에서 사용할 때만 발생**한다.
* 결국 정규식 엔진에 \\ 문자를 전달하려면 파이썬은 \\\\처럼 백슬래시를 4개나 사용해야 한다.

**결론**
* \를 사용한 표현이 반복되는 정규식은 복잡해서 이해하기 힘들기 때문에 **Raw String** 규칙이 생겼다.
* **Raw String** : 컴파일해야 하는 정규식이 Raw String임을 알려 줄 수 있도록 파이썬 문법을 만든 것.
```
p = re.compile(r'\\section')
```
정규식 문자열 앞에 **r 문자를 삽입**하면 이 정규식은 Raw String 규칙에 의하여 백슬래시 2개 대신 1개만 써도 2개를 쓴 것과 같은 동일한 의미를 갖게 된다.