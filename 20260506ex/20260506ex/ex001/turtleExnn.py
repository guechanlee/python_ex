# 회전하는 각도(angle)와 전진하는 길이(length)를 입력 받아 정육각형을 그려 봅시다.
# 정오각형의 내각은 60도입니다.

import turtle

t = turtle.Turtle()

angle = int(input('각도를 입력하세요'))
length = int(input('길이를 입력하세요'))

t.left(angle)       # 왼쪽으로 60도 회전
t.forward(length)      # 100픽셀 실선 그리기

t.left(angle)       # 왼쪽으로 60도 회전
t.forward(length)      # 100픽셀 실선 그리기

t.left(angle)       # 왼쪽으로 60도 회전
t.forward(length)      # 100픽셀 실선 그리기

t.left(angle)       # 왼쪽으로 60도 회전
t.forward(length)      # 100픽셀 실선 그리기

t.left(angle)       # 왼쪽으로 60도 회전
t.forward(length)      # 100픽셀 실선 그리기

t.left(angle)       # 왼쪽으로 60도 회전
t.forward(length)      # 100픽셀 실선 그리기