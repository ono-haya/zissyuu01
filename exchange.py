import ast
from collections import defaultdict

# ファイル読み込み（文字列として）
with open("system_sample_database.txt", "r", encoding="utf-8") as f:
    raw_data = f.read()

# 配列に変換（文字列をリストとして安全に評価）
students = ast.literal_eval(raw_data)

# 授業 → 生徒番号の対応辞書を作成
course_to_students = defaultdict(list)

for student_index, course_list in enumerate(students):
    for course in course_list:
        course_to_students[course].append(student_index)

# 転置：各科目に履修している生徒番号リストを追加
transposed = [[course] + course_to_students[course] for course in sorted(course_to_students)]

# 出力確認
for row in transposed:
    print(row)

