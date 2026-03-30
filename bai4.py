import numpy as np

# ================================
# Dữ liệu kho hàng
# ================================
stock = np.array([35, 8, 12, 5, 40, 18, 7, 22, 9, 15])         # tồn kho hiện tại
min_stock = np.array([20, 15, 15, 10, 25, 20, 12, 18, 12, 15]) # mức tồn tối thiểu
price = np.array([30, 25, 28, 22, 35, 20, 18, 24, 19, 21])     # giá nhập dự kiến

# 1. Xác định mặt hàng đang thiếu
missing_idx = np.where(stock < min_stock)[0]
print("1. Các mặt hàng đang thiếu:", missing_idx + 1)

# 2. Số lượng cần nhập thêm
need_import = np.maximum(min_stock - stock, 0)
print("\n2. Số lượng cần nhập thêm:")
print(need_import)

# 3. Chi phí nhập thêm cho mặt hàng thiếu
cost = need_import * price
print("\n3. Chi phí nhập thêm từng mặt hàng:")
print(cost)

# 4. Tổng chi phí nhập hàng
total_cost = cost.sum()
print("\n4. Tổng chi phí nhập hàng:", total_cost)

# 5. Trạng thái từng mặt hàng
status = np.where(stock < min_stock, "Thiếu hàng", "Đủ hàng")
print("\n5. Trạng thái mặt hàng:")
print(status)

# 6. 3 mặt hàng thiếu nhiều nhất
top3_shortage = np.argsort(need_import)[::-1][:3]
print("\n6. 3 mặt hàng thiếu nhiều nhất:", top3_shortage + 1)

# 7. Giới hạn nhập tối đa 20 đơn vị
limited_need = np.clip(need_import, 0, 20)
print("\n7. Số lượng nhập sau khi giới hạn 20 đơn vị:")
print(limited_need)

# 8. Tổng chi phí sau giới hạn
limited_total_cost = (limited_need * price).sum()
print("\n8. Tổng chi phí sau giới hạn:", limited_total_cost)

# 9. Nhận xét
print("\n9. Nhận xét:")
print("- Có", len(missing_idx), "mặt hàng thiếu so với mức tối thiểu.")
print("- Các mặt hàng thiếu nhiều nhất là:", top3_shortage + 1)
print("- Tổng chi phí nhập khá lớn, cần cân nhắc ưu tiên nhập các mặt hàng thiếu nặng và tốc độ tiêu thụ cao.")
