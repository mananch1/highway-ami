#!/usr/bin/env bash
# ==============================================================================
# Setup Script for AWS EC2 Node 2: Production Host (Docker Compose)
# Target OS: Ubuntu 24.04 LTS / 22.04 LTS (x86_64) on AWS EC2 (t3.small)
# Region: ap-south-1 (Mumbai)
# ==============================================================================
set -euo pipefail

echo "==> [1/4] Configuring 2GB Swap Space..."
if [ ! -f /swapfile ]; then
    fallocate -l 2G /swapfile || dd if=/dev/zero of=/swapfile bs=1M count=2048
    chmod 600 /swapfile
    mkswap /swapfile
    swapon /swapfile
    echo '/swapfile none swap sw 0 0' >> /etc/fstab
    echo "Swap configured successfully."
else
    echo "Swap file already exists."
fi

echo "==> [2/4] Installing Docker and Docker Compose plugin..."
export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y curl ca-certificates gnupg

if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    rm -f get-docker.sh
    echo "Docker Engine installed successfully."
else
    echo "Docker is already installed."
fi

systemctl enable --now docker

TARGET_USER="${SUDO_USER:-ubuntu}"
usermod -aG docker "$TARGET_USER" || true

echo "==> [3/4] Creating application directory hierarchy..."
mkdir -p /opt/road-helper /opt/road-helper/backups /opt/road-helper/logs
chown -R "$TARGET_USER":docker /opt/road-helper
chmod -R 775 /opt/road-helper

# Ensure strict SSH folder permissions
USER_HOME=$(eval echo "~$TARGET_USER")
mkdir -p "$USER_HOME/.ssh"
chmod 700 "$USER_HOME/.ssh"
if [ -f "$USER_HOME/.ssh/authorized_keys" ]; then
    chmod 600 "$USER_HOME/.ssh/authorized_keys"
fi

echo "==> [4/4] AWS Production Host Setup Complete!"
echo "------------------------------------------------------------------------"
echo "Host Private IP (Use this for Jenkins PROD_SERVER_IP):"
curl -s http://169.254.169.254/latest/meta-data/local-ipv4 || hostname -I | awk '{print $1}'
echo ""
echo "Host Public IP (For your browser demonstration):"
curl -s http://169.254.169.254/latest/meta-data/public-ipv4 || curl -s ifconfig.me
echo ""
echo "Docker version: $(docker --version)"
echo "Docker Compose version: $(docker compose version)"
echo "------------------------------------------------------------------------"
echo "NEXT STEP: Append the Jenkins VM public key to: $USER_HOME/.ssh/authorized_keys"
echo "------------------------------------------------------------------------"
