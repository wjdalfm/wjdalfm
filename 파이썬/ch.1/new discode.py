import random

# 학생 변수 선언
students = ["강기연", "곽예린", "감예진", "김효은", "내한성",
            "박솔비", "서백걸", "유효종", "이가을", "이정제",
            "임홍민", "정미르", "조성옥"]

# 그룹 변수 순언
groups = {
    'group1': [],
    'group2': [],
    'group3': [],
    'group4': [],
    'group5': []
}

# 그룹별 인원 수를 위한 변수 선언
group_sizes = {
    'group1': 3,
    'group2': 3,
    'group3': 3,
    'group4': 2,
    'group5': 2
}

# 학생들을 랜덤으로 섞기
random.shuffle(students)

# 학생을 그룹에 배정하는 함수
def health_check():

    # 학생리스트의 인덱스번호로 사용할 변수 선언 (초기화 한다.)
    student_index = 0

    # group_sizes 변수(딕셔너리)의 아이템(키, 벨류)를 이용한 반복문
    for group, size in group_sizes.items():

        # 반복문 내부 변수 size를 이용한 반복분
        for _ in range(size):

            # 그룹변수의 group에 해당하는 키에 students 변수의 student_index에 해당하는 인덱스 번호를 가진 항목을 추가한다.
            groups[group].append(students[student_index])

            # 학생리스트의 인덱스번호로 사용할 변수에 1을 더해서 재선언
            student_index += 1

    # 추가 해놓은 그룹과 아이템을 터미널로 확인해보기
    for group, members in groups.items():
        print(group, " : ", members)

# 그룹 배정 실행
health_check()
