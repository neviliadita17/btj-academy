# Tugas Docker

## 1. Membuat Image

Membuat image dari aplikasi sederhana `oddeven.py`, dengan perintah berikut:

docker build -t appoddeven:v1.0.0 .

## 2. Menjalankan Container
docker run -d -p 8081:8081 --name oddeven-nevii appoddeven:v1.0.0
179c587aca8b5dbfe9ca1fdc9658dd7c5b981f98da3cbd48cef1d76b5a1932c2

## 3. IP Docker Container whoami
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' whoami

172.17.0.2


## 4. Isi file Tersembunyi
### Docker ps >> Docker inspect container_id_whoami >> akan mendapatkan direktori :
cat /home/local/.docker/whoami

Oofooni1eeb9aengol3feekiph6fieve

## 5. Image yang digunakan pada Container
Docker container whoami menggunakan image dengan nama "secret" dan tag "aequaix9De6dii1ay4HeeW
