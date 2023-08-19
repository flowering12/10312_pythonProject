score = float(input("이번 외국어 영역의 점수를 숫자만 입력해주세요. ex) 90 ::"))
#int 정수 float 실수
if score >100 or score <0:
    print("값이 이상함")

elif score >= 90:
        print("a반으로 가세요.")

elif score >= 80:
            print("b반으로 가세요.")
elif score >= 70:
                print("c반으로 가세요.")
elif score < 60:
                    print("d반으로 가세요.")

else:print("값이 이상함")







