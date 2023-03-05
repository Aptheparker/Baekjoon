testcase = int(input())

for i in range(testcase):
    n, m = map(int, input().split())
    p = list(map(int,input().split()))

    # 문서위치 확인용 리스트 생성
    target = [0] * n
    target[m] = 1
    
    
    res = 0
    
    while True:
        # 첫번째 원소가 가장 큰 우선순위를 가진다면
        if p[0] == max(p):
            res += 1
            # 해당 원소가 타켓 원소라면
            if target[0] == 1:
                print(res)
                break
            else:
                # 인쇄
                del p[0]
                del target[0]
                
        # 우선순위가 가장 크지 않다면
        else:
            # 그 값을 리스트 가장 뒤로 재배치
            p.append(p[0])
            target.append(target[0])
            # 맨 앞에 있는 값은 즉시 삭제
            del p[0]
            del target[0]