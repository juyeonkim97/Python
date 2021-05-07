def solution(w, h):
    # 최대공약수(gcd, Greatest Common Divisor) 구하는 함수
    def ucld_gcd(x, y):
        if y == 0:
            return x
        else:
            return ucld_gcd(y, x%y)
    gcd = ucld_gcd(w, h)
    sub_w = int(w / gcd)
    sub_h = int(h / gcd)
    # 패턴에서 사용못하는 사각형 개수 구하기
    sub_whiteblock = sub_w + sub_h - 1
    # 최종 사각형 개수 구하기
    answer = w * h - (gcd * sub_whiteblock)
    return answer

