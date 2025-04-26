from rich.console import Console
from rich.table import Table
import subprocess
import gemfury.docker_cleanup.docker as docker

console = Console()

def main():
    docker.check_docker("docker --version")
    docker_images_list= docker.list_docker_images("docker images")
    console.print(f"[blue]{docker_images_list}[/blue]")
    docker.delete_images()

if __name__ == "__main__":
    main()
