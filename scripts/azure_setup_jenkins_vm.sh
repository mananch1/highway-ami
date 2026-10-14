#!/usr/bin/env bash
# ==============================================================================
# Setup Script for Azure VM 1 (Jenkins CI/CD & Ansible Controller)
# Target OS: Ubuntu 22.04 LTS (x64)
# ==============================================================================
set -euo pipefail

echo "==> [1/6] Configuring 4GB Swap Space for Memory Protection..."
if [ ! -f /swapfile ]; then
    fallocate -l 4G /swapfile || dd if=/dev/zero of=/swapfile bs=1M count=4096
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
    curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | gpg --dearmor --yes -o /etc/apt/keyrings/jenkins.gpg
    echo "deb [signed-by=/etc/apt/keyrings/jenkins.gpg] https://pkg.jenkins.io/debian-stable binary/" | tee /etc/apt/sources.list.d/jenkins.list > /dev/null
    apt-get update -y
    apt-get install -y jenkins
    systemctl enable jenkins
    systemctl start jenkins
else
    echo "Jenkins is already active."
fi

echo "==> [5/6] Generating SSH Keypair for Jenkins-to-Ansible deployments..."
mkdir -p /var/lib/jenkins/.ssh
if [ ! -f /var/lib/jenkins/.ssh/id_rsa ]; then
    ssh-keygen -t rsa -b 2048 -f /var/lib/jenkins/.ssh/id_rsa -N "" -C "jenkins@azure-ci"
fi
chown -R jenkins:jenkins /var/lib/jenkins/.ssh
chmod 700 /var/lib/jenkins/.ssh
chmod 600 /var/lib/jenkins/.ssh/id_rsa
chmod 644 /var/lib/jenkins/.ssh/id_rsa.pub

# Allow jenkins user to run sudo commands without password if needed
echo "jenkins ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/jenkins

echo "==> [6/6] Setup Complete!"
echo "------------------------------------------------------------------------"
echo "Jenkins URL: http://$(curl -s ifconfig.me):8080"
echo "Initial Admin Password:"
cat /var/lib/jenkins/secrets/initialAdminPassword
echo ""
echo "------------------------------------------------------------------------"
echo "IMPORTANT: Copy this Public Key to VM 2 (~/.ssh/authorized_keys):"
cat /var/lib/jenkins/.ssh/id_rsa.pub
echo "------------------------------------------------------------------------"
