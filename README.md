# 🧠 Iotamine Python SDK

**Iotamine** is a powerful and easy-to-use cloud platform designed for developers and startups. This Python SDK allows you to interact with the Iotamine Cloud API to programmatically deploy, manage, and monitor Virtual Private Servers (VPS) and core resources.

---

## 🚀 Features

- Create and manage VPS instances
- Start, stop, restart, power off VMs
- Add or remove disks and IPs
- Set reverse DNS
- Take and restore from snapshots
- Configure firewall rules
- List OS templates and Points of Presence (PoPs)

---

## 📦 Installation

```bash
pip install iotamine
```

## 🔑 Authentication

All requests require an API key. You can obtain this from your Iotamine dashboard.

## 🛠️ Usage Example

```
from iotamine import Iotamine

# Initialize client
client = Iotamine("your-api-key")

# List available OS and POPs
os_list = client.core.list_os()
pop_list = client.core.list_pop()

# Create a new VM
vm = client.vm.create(
    hostname="test-server",
    password="strongpassword123",
    operating_system=os_list[0]['id'],
    pop=pop_list[0]['id'],
    cores=2,
    ram=4096,
    disk=80
)

print("VM Created:", vm)

# List all VMs
print(client.vm.list())
```
