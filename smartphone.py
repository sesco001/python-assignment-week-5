# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Inheritance
        self.storage = storage
        self.battery = battery
    
    def call(self, contact):
        return f"Calling {contact} from {self.device_info()} 📞"
    
    def charge(self, amount):
        self.battery += amount
        return f"Battery charged to {self.battery}% 🔋"
    
    def install_app(self, app_name):
        return f"{app_name} installed on {self.device_info()} 📱"

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB", 60)
print(phone1.call("Alex"))
print(phone1.charge(20))
print(phone1.install_app("WhatsApp"))
