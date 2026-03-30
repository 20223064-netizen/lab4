import numpy as np

scores = np.array([
    [8.0, 7.5, 8.5, 7.0],
    [6.5, 6.0, 7.0, 6.5],
    [9.0, 8.5, 9.0, 8.5],
    [5.0, 5.5, 6.0, 5.5],
    [7.5, 7.0, 8.0, 7.5],
    [4.5, 5.0, 5.5, 5.0],
    [8.5, 9.0, 8.0, 9.0],
    [6.0, 6.5, 6.0, 6.5],
    [7.0, 7.5, 7.0, 8.0],
    [9.5, 9.0, 9.5, 9.0]
])

weights = np.array([0.1, 0.2, 0.3, 0.4])

# 1. Thông tin mảng
print("Shape:", scores.shape)
print("ndim:", scores.ndim)
print("dtype:", scores.dtype)

# 2. Điểm tổng kết
final_score = scores @ weights
print("\nFinal scores:", final_score)

# 3. Xếp loại ABCD
grades = np.where(final_score >= 8.5, "A",
         np.where(final_score >= 7.0, "B",
         np.where(final_score >= 5.5, "C", "D")))
print("\nGrades:", grades)

# 4. Cao nhất & thấp nhất
print("\nHighest:", np.max(final_score), " - Student:", np.argmax(final_score)+1)
print("Lowest:", np.min(final_score), " - Student:", np.argmin(final_score)+1)

# 5. Lọc >= 7.0
print("\nStudents >= 7.0:", np.where(final_score >= 7.0)[0] + 1)

# 6. SV có điểm < 5.0
low_component = np.any(scores < 5.0, axis=1)
print("\nStudents with component < 5.0:", np.where(low_component)[0] + 1)

# 7. Top 3
rank_idx = np.argsort(final_score)[::-1]
top3 = rank_idx[:3] + 1
print("\nTop 3 students:", top3)

# 8. Z-score điểm cuối kỳ
z_final = (scores[:, 3] - scores[:, 3].mean()) / scores[:, 3].std()
print("\nZ-score Final Exam:", z_final)
