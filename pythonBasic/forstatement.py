numbers = [1, 2, 3, 4, 5, 6, 7, 8]
strings = ["hello", "world"]

anys = [1, "hello", True, [1,2,3,4]]

print( numbers[0])
print( strings[0])

print(anys[3][2])

scores = [84, 65, 79, 91, 50, 80, 54, 23, 58, 64, 95, 90, 39, 84, 67, 82, 99, 91]

print(scores[3:])
print(scores[1:4])
print(scores[:3])

#점수 평균
sum = 0

for i in scores:
    sum = sum + i
    average = sum / len(scores)
    print("점수 합:", sum)
    print("점수 평균:", average)