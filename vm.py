class VM:
    def __init__(self, client):
        self.client = client

    def create(self, config: dict):
        return self.client.request("POST", "vm/create/", json=config)

    def list(self):
        return self.client.request("GET", "/vps/")

    def delete(self, vm_id: str):
        return self.client.request("DELETE", f"vm/{vm_id}/")
