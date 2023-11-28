# Task

## Pada example python app, tambahkan beberapa routing kemudia custom posrt yang di listen
  (File app.py)
    from flask import Flask

    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return 'Hello, Docker!'
    
    @app.route('/about')
    def about():
        return 'This is the About page.'
    
    @app.route('/contact')
    def contact():
        return 'This is the Contact page.'
    
    if __name__ == '__main__':
        # Ganti port menjadi 5001
        app.run(debug=True, host='0.0.0.0', port=5001)


- Menambahkan dua routing baru, yaitu /about dan /contact
- Mengganti port yang di-listen menjadi 5001.


## Buatlah satu playbook dengan beberapa task yaitu
### 1. Menyalin file dari local ke server btj-academy
     - name: Copy app.py to remote server
        copy:
          src: "./app.py"
          dest: "{{ remote_path }}/app.py"

### 2. Build docker image untuk aplikasi app.py diatas
### 3. Jalankan container yang sudah dibuild


