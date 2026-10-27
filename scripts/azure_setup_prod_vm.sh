#!/usr/bin/env bash
# ==============================================================================
# Setup Script for Azure VM 2 (Production Server with Docker Compose)
# Target OS: Ubuntu 22.04 LTS (x64)
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
    echo "Docker installed successfully."
else
    echo "Docker is already installed."
fi

# Ensure docker service is running
systemctl enable --now docker

# Add current user (azureuser) to docker group
TARGET_USER="${SUDO_USER:-azureuser}"
usermod -aG docker "$TARGET_USER" || true

echo "==> [3/4] Creating application directory hierarchy..."
mkdir -p /opt/road-helper /opt/road-helper/backups /opt/road-helper/logs
chown -R "$TARGET_USER":docker /opt/road-helper
chmod -R 775 /opt/road-helper

echo "==> [4/4] Production Host Setup Complete!"
echo "------------------------------------------------------------------------"
echo "Public IP: $(curl -s ifconfig.me)"
echo "Docker version: $(docker --version)"
echo "Docker Compose version: $(docker compose version)"
echo ""
echo "Next step: Paste Jenkins VM's public key (id_rsa.pub) into:"
echo "  ~/.ssh/authorized_keys"
echo "------------------------------------------------------------------------"
