# Ansible Docker Container Playbook

## Prerequisites
- Ansible installed on the machine running the playbook.
- Docker installed on the target host.

## 1. Buatlah sebuah inventory, pada inventory tersebut mendefinisikan daftar variables dan hosts
(File inventory1.yaml)
  ---
    all:
      vars:
        docker_tag: 1.0.0
        docker_image: suhu-nevi
    
      hosts:
        btj-academy:
          ansible_host: 10.184.0.100



## 2. Buatlah satu playbook dengan task menjalankan sebuah docker container dengan kriteria yaitu terdapat image, port dan environment variables
(File playbook.yaml)
  ---
    - name: Menjalankan container Docker - Neviii
      hosts: btj-academy
      become: true
    
      tasks:
        - name: Pull Docker Image
          docker_image:
            name: "{{ docker_image }}:{{ docker_tag }}"
    
        - name: Run Docker container
          docker_container:
            name: cont-suhu
            image: "{{ docker_image }}:{{ docker_tag }}"
            state: started
            ports:
             - "8083:8081"
    
        - name: Create a test file
          ansible.builtin.file:
            path: /tmp/testing
            state: touch



## Running
  `ansible-playbook -i inventory1.yaml playbook1.yaml`
