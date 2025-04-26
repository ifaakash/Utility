from main import subprocess
from main import console

# Check if docker is installed or not
def check_docker(command):
    try:
        docker_version= subprocess.run(command, shell=True,capture_output=True, text=True, check= True)
        console.print(f"[green]Docker is installed! \nVersion info: {docker_version.stdout}[/green]")
        return docker_version.stdout
    except subprocess.CalledProcessError as e:
        error_message = e.stderr if e.stderr else str(e)
        if "not found" in error_message.lower():
            console.print("[red]Docker is not installed![/red]")
        elif "permission denied" in error_message.lower():
            console.print("[yellow]Docker is installed, but you need to run the script with sudo.[/yellow]")
        else:
            console.print(f"[red]Error executing command: {e.stderr}[/red]")
        return None

def list_docker_images(command):
    try:
        docker_images= subprocess.run(command,shell=True,capture_output= True, check=True, text=True)
        console.print("[green]List of currently installed docker images:[/green]")
        return docker_images.stdout
    except subprocess.CalledProcessError as e:
        error_message= e.stderr if e.stderr else str(e)
        if "docker daemon" in error_message.lower():
            console.print("[red]Please start the docker daemon![/red]\n")
        return None

# user enter image ID, delete that image, then again ask for image id else skip this function
# else, write skip to skip the loop
def delete_images():
    while True:
        image_id= input("Enter the image ID to delete( or type skip to exit):\n").strip()
        if image_id.lower() == "skip":
            console.print("[green]Skipping image deletion[/green]")
            break
        try:
            subprocess.run(f"docker rmi {image_id}", shell=True,capture_output= True, check=True, text=True)
            console.print(f"{image_id} deleted successfully")
            docker_images=subprocess.run("docker images",shell=True,capture_output= True, check=True, text=True)
            console.print(f"[yellow]{docker_images}[/yellow]")
        except subprocess.CalledProcessError as e:
            error_message= e.stderr if e.stderr else str(e)
            console.print(f"Error deleting image {error_message}")
