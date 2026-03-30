import numpy as np

# ================================
# 1. Tạo ma trận doanh thu 5 sản phẩm trong 7 ngày
# ================================
sales = np.array([
    [120, 150, 130, 140, 160],
    [125, 145, 128, 142, 158],
    [130, 155, 135, 150, 162],
    [135, 160, 140, 152, 168],
    [140, 165, 145, 155, 170],
    [138, 162, 142, 153, 169],
    [145, 170, 150, 160, 175]
])

# 1. Tổng doanh thu theo ngày
daily_total = sales.sum(axis=1)
print("1. Tổng doanh thu theo từng ngày:")
print(daily_total)

# 2. Tổng và trung bình theo sản phẩm
product_total = sales.sum(axis=0)
product_mean = sales.mean(axis=0)

print("\n2. Tổng doanh thu từng sản phẩm:")
print(product_total)

print("\nDoanh thu trung bình từng sản phẩm:")
print(product_mean)

# 3. Ngày cao nhất & sản phẩm bán tốt nhất
best_day = np.argmax(daily_total)
best_product = np.argmax(product_total)

print("\n3. Ngày có doanh thu cao nhất (1–7):", best_day + 1)
print("Sản phẩm bán tốt nhất (1–5):", best_product + 1)

# 4. Tăng doanh số sản phẩm 2 và 5 thêm 8%
new_sales = sales.astype(float).copy()
new_sales[:, [1, 4]] *= 1.08

print("\n4. Doanh thu sau điều chỉnh (tăng 8% SP2 và SP5):")
print(new_sales)

# 5. So sánh tổng tuần trước và sau điều chỉnh
before_total = sales.sum()
after_total = new_sales.sum()

print("\n5. Tổng doanh thu trước điều chỉnh:", before_total)
print("Tổng doanh thu sau điều chỉnh:", after_total)
print("Chênh lệch tăng:", after_total - before_total)

# 6. Lọc ngày doanh thu > trung bình tuần
high_days = np.where(daily_total > daily_total.mean())[0]

print("\n6. Các ngày có doanh thu cao hơn mức trung bình:")
print(high_days + 1)

# 7. Sản phẩm ổn định nhất (σ nhỏ nhất)
stable_product = np.argmin(sales.std(axis=0))

print("\n7. Sản phẩm ổn định nhất (độ lệch chuẩn nhỏ nhất):", stable_product + 1)

# 8. Nhận xét
print("\n8. Nhận xét:")
print("- Sản phẩm", best_product + 1, "có doanh thu cao nhất, nên ưu tiên quảng bá.")
print("- Sản phẩm", stable_product + 1, "có doanh số ổn định nhất, ít biến động theo ngày.")
print("- Tăng doanh số SP2 và SP5 giúp tổng doanh thu tuần tăng đáng kể.")
