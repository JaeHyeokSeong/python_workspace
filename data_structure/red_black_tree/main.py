#  reference [1]: https://code-lab1.tistory.com/62 - 이론 설명

# 새로운 노드는 항상 빨간색으로 삽입한다.
# insert 과정 발생할 수 있는 케이스들
# case1: 삼촌 노드가 검은색인 경우에는 -> restructuring 을 수행한다.
# case2: 삼촌 노드가 빨간색인 경우에는 -> recoloring 을 수행한다.

# restructuring 수행과정
# step1: 새로운 노드, 부모 노드, 조상 노드들을 오름차순으로 정렬한다.
# step2: 셋 중 중간값을 부모로 만들고 나머지 둘을 자식으로 만든다.
# step3: 새로 부모가 된 노드를 검은색으로 만들고 나머지 자식들을 빨간색으로 만든다

# recoloring 수행과정
# step1: 새로운 노드의 부모와 삼촌을 검은색으로 바꾸고 조상을 빨간색으로 바꾼다.
# step1-1: 이때 조상이 루트 노드이라면 검은색으로 바꾼다 (왜냐하면 규칙2에 의하면 루트 노드는 항상 검은색이다.)
# step1-2: 조상 노드를 빨간색으로 바꿨을 때 또다시 Double Red가 발생한다면 또다시 restructuring 혹은
# recoloring 을 진행해서 Double Red 문제가 발생하지 않을 때까지 반복한다.

# red black tree 에서는 검은색 노드가 2번 이상 나와도 상관 없다. 하지만 만약에 빨간색 노드가 2번 이상
# 나오게 된다면 이는 red black tree 의 case4 즉 doule red 가 발생하는 것이므로 규칙을 위반하게 된다.


# reference[2] https://8iggy.tistory.com/188 - 구현

