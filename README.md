# 🔋 BESS Monitoring & Management System

A comprehensive system for monitoring Battery Energy Storage Systems (BESS) using a distributed architecture.

## 🛠️ Tech Stack & Tools

### 💻 Operating Systems
- ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
- ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

### ☁️ Virtualization & Containers
- ![LXC](https://img.shields.io/badge/LXC-003566?style=for-the-badge&logo=lxc&logoColor=white)
- ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

### ⚙️ Automation & Scripts
- ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### 📡 Protocols & Frameworks
- ![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)
- ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

---

## 📂 Project Structure

- **`bess_node/`**: Contains the battery simulation logic (`bess_sim.py`).
- **`ems_node/`**: The Energy Management System dashboard and controller.
- **`scripts/`**: Automation tools for deployment (`deploy.sh`).

## 🚀 How to Run
1. Ensure your MQTT broker is active.
2. Run the BESS simulation: `python3 bess_node/bess_sim.py`
3. Launch the dashboard: `python3 ems_node/app.py`
