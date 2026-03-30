import numpy as np

# ==========================
# 1. Tạo ma trận chuyên cần
# ==========================
attendance = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,0,1,1],
    [1,0,0,1,1,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,1,1,0,1,1,1,0],
    [1,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1,0],
    [0,0,1,1,0,1,1,1],
    [1,1,1,0,1,1,1,1],
    [1,1,0,0,1,0,1,1],
    [1,1,1,1,1,0,1,1]
])

# 1. Tổng số buổi đi học
present_count = attendance.sum(axis=1)
print("1. Tổng số buổi đi học của từng sinh viên:")
print(present_count)

# 2. Tỉ lệ chuyên cần
rate = present_count / attendance.shape[1] * 100
print("\n2. Tỉ lệ chuyên cần (%):")
print(rate)

# 3. Sinh viên bị cảnh báo < 75%
warning_idx = np.where(rate < 75)[0]
print("\n3. Sinh viên bị cảnh báo (< 75%):")
print(warning_idx + 1)   # +1 để hiển thị đúng số SV

# 4. Buổi học có số lượng vắng nhiều nhất
absent_count_by_session = (attendance == 0).sum(axis=0)
worst_session = np.argmax(absent_count_by_session)
print("\n4. Số vắng theo từng buổi:")
print(absent_count_by_session)
print("Buổi vắng nhiều nhất:", worst_session + 1)

# 5. Sinh viên đi học đủ cả 8 buổi
full_attendance = np.where(np.all(attendance == 1, axis=1))[0]
print("\n5. Sinh viên đi học đầy đủ 8 buổi:")
print(full_attendance + 1)

# 6. Sinh viên có >= 2 buổi vắng liên tiếp
two_absent_in_row = np.where(
    np.any((attendance[:, :-1] == 0) & (attendance[:, 1:] == 0), axis=1)
)[0]
print("\n6. Sinh viên có từ 2 buổi vắng liên tiếp trở lên:")
print(two_absent_in_row + 1)

# 7. Nhận xét chung
print("\n7. Nhận xét:")
print(" - Có", len(warning_idx), "sinh viên bị cảnh báo.")
print(" - Chỉ có", len(full_attendance), "sinh viên đi học đủ 8 buổi.")
print(" - Nhiều sinh viên có vắng liên tiếp, ý thức chuyên cần chưa tốt.")
