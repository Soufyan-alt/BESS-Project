#!/bin/bash

# Configuration - Colors for better visibility
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}>>> Starting Automated Deployment for BESS Project...${NC}"

# 1. Push Emulator Code to bess-server
echo "Deploying BESS Emulator..."
lxc file push ../bess_node/bess_sim.py bess-server/root/

# 2. Push Controller Code to ems-server
echo "Deploying EMS Controller..."
lxc file push ../ems_node/ems_controller.py ems-server/root/

# 3. Restart Background Services
echo "Restarting services in containers..."
lxc exec bess-server -- systemctl restart bess-sim.service

echo -e "${GREEN}>>> Success! Project is live.${NC}"
