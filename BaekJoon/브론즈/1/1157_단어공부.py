# 입력 받는 문자열 대문자로 치환
# 중복을 제거한 리스트 하나 생성
# 알파벳 센 숫자를 저장할 빈 리스트 하나 생성
# 중복 제거된 리스트 알파벳을 입력받은 문자열에서 카운트
# cnt_list에 cnt를 append
# 가장 많이 카운트 된 수가 1 이상 이면 ? 출력
# 아니면 가장 많이 카운트된 수의 idx를 얻어와서 S_list에서 찾는다.
S = input().upper()
S_list = list(set(S))

cnt_list = []
for i in S_list:
    cnt = S.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_idx = cnt_list.index(max(cnt_list))
    print(S_list[max_idx])
