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
