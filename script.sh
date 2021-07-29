#!/bin/bash

# Kiểm tra có Docker hay chưa
# Kiểm tra có Docker Compose hay chưa

# Kiểm tra có chạy được Database server hay chưa
# Kiểm tra có chạy được Web server hay chưa

# sudo apt install zip -y
# sudo zip -r data.zip data

echo '### Log in to Docker ###'
cd docker
echo '### unzip data simple ###'
sudo unzip data.zip
# echo '### run docker compose ###'
# docker-compose up