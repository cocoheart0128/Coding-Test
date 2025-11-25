def solution(dots):
    # 두 점 사이의 기울기
    def slope(a, b):
        if b[0] - a[0] == 0:   # x가 같으면 세로선
            return float('inf')
        return (b[1] - a[1]) / (b[0] - a[0])

    # 가능한 선 조합 3가지
    pairs = [
        ((0, 1), (2, 3)),
        ((0, 2), (1, 3)),
        ((0, 3), (1, 2))
    ]

    # 각 조합의 기울기 비교
    for (a, b), (c, d) in pairs:
        if slope(dots[a], dots[b]) == slope(dots[c], dots[d]):
            return 1

    return 0
