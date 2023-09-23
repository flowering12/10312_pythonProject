numbers = [1, 2, 3, 4, 5, 6, 7, 8]
strings = ["hello", "world"]

anys = [1, "hello", True, [1,2,3,4]]

print( numbers[0])
print( strings[0])

print(anys[3][2])

scores = [84, -5, 65, 79, 105, 100, 91, 50, -32, 80, 54, 23, 58, 64, 95, 90, 39, 84, 67, 82, 99, 91]

print(scores[3:])
print(scores[1:4])
print(scores[:3])

#점수 평균
sum = 0
# for i in scores:
#     if 0 < i < 100:
#         sum = sum+i
for i if scores:
    if i >100 or 1 < 0:
        print("skip", i)
        continue
        sum = sum + i

for i in scores:
    sum = sum + i
    average = sum / len(scores) # 이 경우 정상적이지 않은 평균값, 별도로 처리해주기
    print("점수 합:", sum)
    print("점수 평균:", average)

for i in range(0,11):
 print(i)