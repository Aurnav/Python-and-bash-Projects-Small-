import subprocess
result = subprocess.run(
    ["rc-service", "--list"], capture_output=True, text=True
)
services = result.stdout.splitlines()
def add_service(service_name):
    if service_name not in services:
        print(f"Service {service_name} not found.")
        return
    subprocess.run(["rc-service", service_name, "add"])
    print(f"Service {service_name} added.")
def remove_service(service_name):
    if service_name in services:
        subprocess.run(["rc-service", service_name, "del"])
        print(f"Service {service_name} removed.")
def status_service(sevice_name):
    if sevice_name in services:
        result = subprocess.run(["rc-service", sevice_name, "status"], capture_output=True, text=True)
        print(result.stdout)
def start_service(service_name):
    if service_name in services:
        subprocess.run(["rc-service", service_name, "start"])
        print(f"Service {service_name} started.")
def stop_service(service_name):
    if service_name in services:
        subprocess.run(["rc-service", service_name, "stop"])
        print(f"Service {service_name} stopped.")   
def restart_service(service_name):
    if service_name in services:
        subprocess.run(["rc-service", service_name, "restart"])
        print(f"Service {service_name} restarted.")
def enable_at_boot(service_name):
    if service_name in services:
        subprocess.run(["rc-update", "add", service_name, "default"])
        print(f"Service {service_name} enabled at boot.")
def disable_at_boot(service_name):
    if service_name in services:
        subprocess.run(["rc-update", "del", service_name, "default"])
        print(f"Service {service_name} disabled at boot.")  
print("************ Service Management Menu **********")
if __name__ == "__main__":
    while True:
        print("\n1. Add Service")
        print("2. Remove Service")
        print("3. Check Service Status")
        print("4. Start Service")
        print("5. Stop Service")
        print("6. Restart Service")
        print("7. Enable Service at Boot")
        print("8. Disable Service at Boot")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service_name = input("Enter the service name to add: ")
            add_service(service_name)
        elif choice == "2":
            service_name = input("Enter the service name to remove: ")
            remove_service(service_name)
        elif choice == "3":
            service_name = input("Enter the service name to check status: ")
            status_service(service_name)
        elif choice == "4":
            service_name = input("Enter the service name to start: ")
            start_service(service_name)
        elif choice == "5":
            service_name = input("Enter the service name to stop: ")
            stop_service(service_name)
        elif choice == "6":
            service_name = input("Enter the service name to restart: ")
            restart_service(service_name)
        elif choice == "7":
            service_name = input("Enter the service name to enable at boot: ")
            enable_at_boot(service_name)
        elif choice == "8":
            service_name = input("Enter the service name to disable at boot: ")
            disable_at_boot(service_name)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")
