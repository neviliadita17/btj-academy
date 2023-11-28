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


## Result

    PLAY [Menjalankan container Docker - Neviii] ******************************************************
  
    TASK [Gathering Facts] ****************************************************************************
    Enter passphrase for key '/home/nevilliaditaberthilydia/.ssh/id_rsa': 
    ok: [btj-academy]
    
    TASK [Pull Docker Image] **************************************************************************
    [DEPRECATION WARNING]: The value of the "source" option was determined to be "pull". Please set 
    the "source" option explicitly. Autodetection will be removed in community.general 2.0.0. This 
    feature will be removed from community.general in version 2.0.0. Deprecation warnings can be 
    disabled by setting deprecation_warnings=False in ansible.cfg.
    ok: [btj-academy]
    
    TASK [Run Docker container] ***********************************************************************
    [DEPRECATION WARNING]: The container_default_behavior option will change its default value from 
    "compatibility" to "no_defaults" in community.general 3.0.0. To remove this warning, please 
    specify an explicit value for it now. This feature will be removed from community.general in 
    version 3.0.0. Deprecation warnings can be disabled by setting deprecation_warnings=False in 
    ansible.cfg.
    changed: [btj-academy]
    
    TASK [Create a test file] *************************************************************************
    changed: [btj-academy]
    
    PLAY RECAP ****************************************************************************************
    btj-academy                : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
