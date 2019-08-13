Find Same orders
----------------

다음은 요기요로 주문을 한 사람들과 주문한 음식들의 목록입니다.
다음 중 같은 음식을 주문한 사람들을 묶으세요.


```
input type: dict[str(person name), list[str](order list)]

return type: list[list[str]] (people who have same orders)

example.

given:
[
    {
        'einstein': ['pizza', 'hamburger'],
        'bohr': ['pizza', 'chicken', 'cidar'],
        'curie': ['pizza', 'hamburger'],
    }
]

answer:
[['einstein', 'curie'], ['bohr']]
```
