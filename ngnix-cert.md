bkp@dev:~$ mkdir -p ~/nAIsrc/certs
bkp@dev:~$ 
bkp@dev:~$ ls -l nAIsrc/
total 40
drwxrwxr-x+ 8 bkp bkp 4096 Sep 19 12:58 apps
drwxrwxr-x  2 bkp bkp 4096 Sep 19 19:55 certs
drwxrwxr-x  2 bkp bkp 4096 Sep 16 17:56 config
drwxrwxr-x  2 bkp bkp 4096 Sep 16 20:39 database
-rw-rw-r--  1 bkp bkp  901 Sep 17 10:42 docker-compose.yml
drwxrwxr-x  6 bkp bkp 4096 Sep 16 23:39 infra
drwxrwxr-x  2 bkp bkp 4096 Sep 14 22:00 packages
-rw-rw-r--  1 bkp bkp  808 Sep 18 23:07 README.md
drwxrwxr-x  2 bkp bkp 4096 Sep 15 23:24 scripts
drwxrwxr-x  4 bkp bkp 4096 Sep 14 20:29 services
bkp@dev:~$ 
bkp@dev:~$ 
bkp@dev:~$ 
bkp@dev:~$ mkcert \
  -cert-file ~/nAIsrc/certs/nai.local.pem \
  -key-file ~/nAIsrc/certs/nai.local-key.pem \
  localhost 127.0.0.1 nai.local

Created a new certificate valid for the following names 📜
 - "localhost"
 - "127.0.0.1"
 - "nai.local"

The certificate is at "/home/bkp/nAIsrc/certs/nai.local.pem" and the key at "/home/bkp/nAIsrc/certs/nai.local-key.pem" ✅

It will expire on 19 December 2028 🗓

bkp@dev:~$ 
bkp@dev:~$ 
bkp@dev:~$ 
bkp@dev:~$ openssl verify \
  -CAfile /home/bkp/.local/share/mkcert/rootCA.pem \
  ~/nAIsrc/certs/nai.local.pem
/home/bkp/nAIsrc/certs/nai.local.pem: OK
bkp@dev:~$ 
bkp@dev:~$ 
bkp@dev:~$ openssl verify   -CAfile /home/bkp/.local/share/mkcert/rootCA.pem   ~/nAIsrc/certs/nai.local.pem
/home/bkp/nAIsrc/certs/nai.local.pem: OK
bkp@dev:~$ 
bkp@dev:~$ 
bkp@dev:~$ sudo cp ~/nAIsrc/certs/nai.local.pem \
    /etc/nginx/certs/nai.local.pem
bkp@dev:~$ 
bkp@dev:~$ 
bkp@dev:~$ sudo cp ~/nAIsrc/certs/nai.local-key.pem \
    /etc/nginx/certs/nai.local-key.pem
bkp@dev:~$ 
bkp@dev:~$ sudo chmod 600 /etc/nginx/certs/nai.local-key.pem
bkp@dev:~$ 
bkp@dev:~$ sudo nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
bkp@dev:~$ 
bkp@dev:~$ sudo systemctl reload nginx
bkp@dev:~$ 
bkp@dev:~$ 
bkp@dev:~$ curl https://nai.local
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>client</title>
    <script type="module" crossorigin src="/assets/index-ChvZUJaW.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-BLUv8c9M.css">
  <link rel="manifest" href="/manifest.webmanifest"><script id="vite-plugin-pwa:register-sw" src="/registerSW.js"></script></head>
  <body>
    <div id="root"></div>
  </body>
</html>
bkp@dev:~$ 
bkp@dev:~$ 
bkp@dev:~$ curl \
  --cacert /home/bkp/.local/share/mkcert/rootCA.pem \
  https://nai.local
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>client</title>
    <script type="module" crossorigin src="/assets/index-ChvZUJaW.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-BLUv8c9M.css">
  <link rel="manifest" href="/manifest.webmanifest"><script id="vite-plugin-pwa:register-sw" src="/registerSW.js"></script></head>
  <body>
    <div id="root"></div>
  </body>
</html>
bkp@dev:~$ 


## if the below is successful , things are set properly
bkp@dev:~$ curl https://nai.local
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>client</title>
    <script type="module" crossorigin src="/assets/index-ChvZUJaW.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-BLUv8c9M.css">
  <link rel="manifest" href="/manifest.webmanifest"><script id="vite-plugin-pwa:register-sw" src="/registerSW.js"></script></head>
  <body>
    <div id="root"></div>
  </body>
</html>
