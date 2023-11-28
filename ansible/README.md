# Ansible Docker Container Playbook

## Prerequisites
- Ansible installed on the machine running the playbook.
- Docker installed on the target host.

## 1. Buatlah sebuah inventory, pada inventory tersebut mendefinisikan daftar variables dan hosts
(File inventory.yaml)
    all:
      vars:
        docker_image: nginx
        docker_port: 8080
        docker_tag: latest
        docker_env_var1: "VAR1_VALUE"
        docker_env_var2: "VAR2_VALUE"
      hosts:
        btj-academy:
          ansible_host: 10.184.0.100


## 2. Buatlah satu playbook dengan task menjalankan sebuah docker container dengan kriteria yaitu terdapat image, port dan environment variables
(File playbook.yaml)
  ---
  - name: Menjalankan container Docker-Nevi
    hosts: btj-academy
    become: true
  
    vars:
      docker_tag: latest
  
    tasks:
      - name: Pull Docker image
        docker_image:
          name: "ubuntu:{{ docker_tag }}"
          state: present
  
      - name: Run Docker container
        docker_container:
          name: my_container
          image: "{{ docker_image }}:{{ docker_tag }}"
          ports:
            - "{{ docker_port }}:80"
          env:
            VAR1: "{{ docker_env_var1 }}"
            VAR2: "{{ docker_env_var2 }}"
          state: started
  
      - name: Create a test file
        ansible.builtin.file:
          path: /tmp/testing
          state: touch

## Running
ansible-playbook -i inventory.yaml playbook.yaml
