def solution(n, m, section):
    answer = 1
    paint = section[0]
    for s in section:
        if s - paint >= m:
            answer += 1
            paint = s
        
    return answer

#n미터 벽(페인트 칠)
#1미터 길이의 구역 n개로 나눔
# 롤러의 길이 m - 벽나감x, 구역 모두 칠하기
