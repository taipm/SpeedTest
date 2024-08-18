# Sử dụng Python image cơ bản
FROM python:3.10-slim

# Cài đặt các gói phụ thuộc
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy mã nguồn vào Docker container
COPY internet_speed_test.py /app/internet_speed_test.py

# Đặt thư mục làm việc
WORKDIR /app

# Chạy chương trình
CMD ["python", "internet_speed_test.py"]
