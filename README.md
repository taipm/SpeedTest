# SpeedTest

# Khởi tạo môi trường ảo (nếu sử dụng)
python3 -m venv venv
source venv/bin/activate

# Cài đặt các dependency (ví dụ: sử dụng pip)
pip install -r requirements.txt

# Khởi tạo database (nếu sử dụng)



Để tạo một file `setup.sh` để cài đặt chương trình trên Docker và lưu kết quả ra ngoài thư mục `downloads` trên macOS, bạn có thể làm theo hướng dẫn sau.

### 1. Tạo file `setup.sh`

Tạo một tệp `setup.sh` với nội dung sau:

```bash
#!/bin/bash

# Tạo Docker image cho chương trình
docker build -t internet-speed-test .

# Tạo thư mục downloads nếu chưa tồn tại
mkdir -p ~/Downloads/internet_speed_results

# Chạy Docker container và mount thư mục downloads
docker run -d \
    --name internet-speed-test \
    -v ~/Downloads/internet_speed_results:/app/data \
    internet-speed-test

echo "Docker container 'internet-speed-test' is running."
echo "Results will be saved to ~/Downloads/internet_speed_results/internet_speed.csv"
```

### 2. Chi tiết về script `setup.sh`

- **docker build -t internet-speed-test .**: Lệnh này xây dựng Docker image từ `Dockerfile` với tên `internet-speed-test`.

- **mkdir -p ~/Downloads/internet_speed_results**: Lệnh này tạo thư mục `internet_speed_results` trong `~/Downloads` nếu nó chưa tồn tại.

- **docker run -d --name internet-speed-test -v ~/Downloads/internet_speed_results:/app/data internet-speed-test**: Lệnh này chạy Docker container trong chế độ nền (`-d`), gắn kết (`mount`) thư mục `~/Downloads/internet_speed_results` trên máy Mac với thư mục `/app/data` trong container. File CSV sẽ được lưu tại đây.

- **echo**: Lệnh này in thông báo ra màn hình để xác nhận rằng container đang chạy và nơi lưu kết quả.

### 3. Sử dụng `setup.sh`

Để sử dụng file `setup.sh`, thực hiện các bước sau:

1. Đảm bảo file `setup.sh` có quyền thực thi:
   ```bash
   chmod +x setup.sh
   ```

2. Chạy script `setup.sh`:
   ```bash
   ./setup.sh
   ```

Sau khi script này hoàn tất, Docker container sẽ bắt đầu chạy và lưu các kết quả đo tốc độ internet vào thư mục `~/Downloads/internet_speed_results/internet_speed.csv` trên máy của bạn.

### 4. Kiểm tra kết quả

Bạn có thể kiểm tra file `internet_speed.csv` trong thư mục `~/Downloads/internet_speed_results` để xem các kết quả đo được lưu lại.

### 5. Quản lý container

Bạn có thể dừng container bằng lệnh:
```bash
docker stop internet-speed-test
```

Và khởi động lại bằng lệnh:
```bash
docker start internet-speed-test
```

Với `setup.sh`, bạn sẽ dễ dàng cài đặt và quản lý chương trình đo tốc độ internet trên Docker, và lưu kết quả ra ngoài máy Mac của mình.