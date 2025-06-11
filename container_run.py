"""
Name: container_run.py

Description:
A Python utility script for managing Docker containers with an interactive command-line interface. 
This script simplifies container deployment and management operations for developers and DevOps engineers.

Pre-requisites:
    1. Docker Desktop installed and running (daemon process)
    2. Python 3.x
    3. Docker Python SDK: `pip3 install docker`

Features:
1. List all currently running containers
2. Deploy new containers with customizable options:
   - Custom image selection
   - Port mapping configuration
   - Detached mode operation
3. Stop running containers by ID

Use Cases:
1. Development environment setup
2. Quick container deployment for testing
3. Container management in local environments
4. Learning Docker operations through Python

Input Parameters:
1. For Container Deployment:
   - Image name (e.g., 'nginx:latest', 'redis:6')
   - Port publishing preference (Y/N)
   - Port mapping (format: container_port/protocol:host_port)
     Example: 80/tcp:8080 
     Supported protocols: tcp, udp, sctp
   - Detach mode preference (True/False)

2. For Container Stop:
   - Container ID

Steps to Run:
1. Install required dependencies:
   pip3 install docker 

2. Run the script:
   python3 container_run.py

3. Choose operation:
   - Enter 'Deploy' for container deployment
   - Enter 'Stop' to stop a container
4. Follow the interactive prompts

Error Handling:
- Validates port mapping format
- Handles Docker daemon connection errors
- Validates container existence before operations
"""

import docker

# client to connect to host docker environment
client= docker.from_env()

true=['Y','y',True,'yes','Yes','YES']
false=['n','N',False,'no','NO','no']
choice= ['Deploy','stop']

# list the already existing containers
def existing_containers():
    try:
        existing_containers= client.containers.list()
        return f"List of Existing containers: {existing_containers}"
    except Exception as e:
        print(f"Error:\n{e}")

# deploy the new conatiners based on image given as input
def deploy_containers():
    container_image= input("Image name to deploy\t")
    port_enabled= input("Need port publishing? (Y for yes, N for no)\t")
    detach_mode= input("Detached or not! (True for yes, False for no)\t")
    try:
        if port_enabled in true:
            ports= input("1111/tcp:1234 where the protocol is either tcp, udp, or sctp\t")
            # Convert port string input to proper dictionary format
            try:
                container_port, host_port = ports.split(':')
                container_port=container_port.strip()
                host_port= int(host_port.strip())
                print("Container Port:",container_port)
                print("Host Port:",host_port)
                client.containers.run(container_image,ports={f'{container_port}': host_port}, detach=detach_mode)
                print("deeBUG")
                running_containers= client.containers.list()
                return f"List of the containers running after deployment:\t{running_containers}"
            except ValueError:
                raise ValueError("Port mapping should be in format 'container_port/protocol:host_port'")
    except Exception as e:
        return f"Deploying Container failed due to: \n{e}"
    
# stop any container via container ID
def stop_container():
    running_containers= existing_containers()
    print(f"Current running containers:\t{running_containers}" )
    container_id= input("Enter the container ID\t")
    """This will stop the container only if it existis in the list of the existing containers"""
    container= client.containers.get(container_id=container_id)
    try:
        if container_id in running_containers:
            container.stop()
            running_containers = existing_containers()
            return f"Container killed with id {container_id} \n List of latest running containers \t {running_containers}"
    except Exception as e:
        return f"Function exited with error:\t{e}"

# main function
def main():
    choice= input("Do you want to deploy or stop container (Deploy for deploy, Stop for stop)\t")
    if choice== 'deploy':
        deploy_containers()
    elif choice== 'stop':
        stop_container()
    else:
        print("Oops! Invalid choice")

if __name__=="__main__":
    main()

