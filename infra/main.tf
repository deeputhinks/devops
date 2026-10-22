terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

# Resource 1: Pull the Nginx Image
resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

# Resource 2: Run the Container
resource "docker_container" "web" {
  image = docker_image.nginx.image_id
  name  = "terraform-prod-web"
  
  ports {
    internal = 80
    external = 8000
  }
}
