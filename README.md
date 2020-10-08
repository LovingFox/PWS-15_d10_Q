# PWS-15_e5_linux (на основе PWS-15_d10_Q)

## Доступен на виртуальном сервере в облаке Яндекс (до 2020.12.08) по адресу:
https://sf.rtru.tk

### Реализовано
- Django приложение, запущенное через gunicorn на сокете 127.0.0.0:8000
  - все критичные данные спрятаны в enviroment
- Описание самого приложения см. тут: https://github.com/LovingFox/PWS-15_d10_Q
- Web-сервер nginx (см. файл [sf.rtru.tk.conf](https://github.com/LovingFox/PWS-15_d10_Q/blob/e5/sf.rtru.tk.conf)):
  - http -> https
  - / -> proxy_pass 127.0.0.0:8000 (proxy_set_header, proxy_set_header)
  - /static -> директория с собранными (collectstatic) статическими файлами
  - /favicon.ico { access_log off; log_not_found off; }
- Локальный PostgreSQL сервер
- Домен через freenom.com
- SSL сертификат через letsencrypt.org
