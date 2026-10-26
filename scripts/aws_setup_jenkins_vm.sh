#!/usr/bin/env bash
# ==============================================================================
# Setup Script for AWS EC2 Node 1: Jenkins Controller & Ansible Engine
# Target OS: Ubuntu 24.04 LTS / 22.04 LTS (x86_64) on AWS EC2 (t3.small)
# Region: ap-south-1 (Mumbai)
# ==============================================================================
set -euo pipefail

echo "==> [1/6] Configuring 2GB Swap Space for Memory Protection..."
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

echo "==> [2/6] Updating system repositories and installing dependencies..."
export DEBIAN_FRONTEND=noninteractive
rm -f /etc/apt/sources.list.d/jenkins.list
apt-get update -y
apt-get install -y \
    curl \
    wget \
    gnupg \
    software-properties-common \
    git \
    openjdk-21-jdk \
    maven \
    ansible \
    fontconfig \
    unzip

echo "==> [3/6] Installing Google Chrome for Headless Selenium Testing..."
if ! command -v google-chrome &> /dev/null; then
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    apt-get install -y ./google-chrome-stable_current_amd64.deb
    rm -f google-chrome-stable_current_amd64.deb
    google-chrome --version
else
    echo "Google Chrome is already installed."
fi

echo "==> [4/6] Installing Jenkins LTS..."
if ! systemctl is-active --quiet jenkins; then
    mkdir -p /etc/apt/keyrings
    curl -fsSL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x7198F4B714ABFC68" | gpg --dearmor --yes -o /etc/apt/keyrings/jenkins.gpg
    chmod 644 /etc/apt/keyrings/jenkins.gpg
    echo "deb [signed-by=/etc/apt/keyrings/jenkins.gpg] https://pkg.jenkins.io/debian-stable binary/" | tee /etc/apt/sources.list.d/jenkins.list > /dev/null
    apt-get update -y
    apt-get install -y jenkins
    systemctl enable jenkins
    systemctl start jenkins
else
    echo "Jenkins is already active."
fi

echo "==> [5/6] Generating Dedicated SSH Deployment Keypair..."
mkdir -p /var/lib/jenkins/.ssh
if [ ! -f /var/lib/jenkins/.ssh/id_rsa ]; then
    ssh-keygen -t rsa -b 4096 -f /var/lib/jenkins/.ssh/id_rsa -N "" -C "jenkins@aws-mumbai-ci"
fi
chown -R jenkins:jenkins /var/lib/jenkins/.ssh
chmod 700 /var/lib/jenkins/.ssh
chmod 600 /var/lib/jenkins/.ssh/id_rsa
chmod 644 /var/lib/jenkins/.ssh/id_rsa.pub

# Initialize .env file for dynamic IP injection
if [ ! -f /var/lib/jenkins/.env ]; then
    cat << 'EOF' > /var/lib/jenkins/.env
# AWS Environment Configuration (Private & Confidential)
# Add your Prod EC2 Private IP below (e.g., PROD_SERVER_IP=172.31.x.x)
PROD_SERVER_IP=
SSH_USER=ubuntu
APP_PORT=80
EOF
    chown jenkins:jenkins /var/lib/jenkins/.env
    chmod 600 /var/lib/jenkins/.env
fi

echo "==> [6/6] AWS Jenkins Controller Setup Complete!"
echo "------------------------------------------------------------------------"
echo "Waiting for Jenkins to initialize..."
for i in {1..30}; do
    if [ -f /var/lib/jenkins/secrets/initialAdminPassword ]; then
        break
    fi
    sleep 2
done

echo "Jenkins Web UI URL: http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4 || curl -s ifconfig.me):8080"
echo "Initial Admin Password:"
if [ -f /var/lib/jenkins/secrets/initialAdminPassword ]; then
    cat /var/lib/jenkins/secrets/initialAdminPassword
else
    echo "(Jenkins is still generating password; view /var/lib/jenkins/secrets/initialAdminPassword shortly)"
fi
echo ""
echo "------------------------------------------------------------------------"
echo "ACTION REQUIRED: Copy this Public Key to EC2-Prod (~ubuntu/.ssh/authorized_keys):"
echo "------------------------------------------------------------------------"
cat /var/lib/jenkins/.ssh/id_rsa.pub
echo "------------------------------------------------------------------------"
