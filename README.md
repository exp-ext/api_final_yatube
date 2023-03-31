<h2>API YaTube, cоциальная сеть для авторов и подписчиков (Яндекс Практикум)</h2>

![статус](https://github.com/exp-ext/api_final_yatube/actions/workflows/api_yatube_workflow.yml/badge.svg?event=push)

<p align="center">
<img src="https://trafopedia.ru/storage/app/uploads/public/5f7/07d/ff7/5f707dff7011b583558647.jpg" width="1200">
</p>
<p>Социальная сеть для авторов и подписчиков. Пользователи могут подписываться на избранных авторов, оставлять и удалять комментарии к постам, оставлять новые посты на главной странице и в тематических группах, прикреплять изображения к публикуемым постам. Авторизация реализованна через JWT-токен.
</p>
<hr />
<h3>Стек технологий</h3>
<ul>
<li>Python</li>
<li>Django</li>
<li>Pytest</li>
<li>djangorestframework</li>
<li>PyJWT</li>
<li>PostgreSQL</li>
<li>Docker</li>
<li>Github Actions</li>
</ul>
<hr />
<h3>Зависимости</h3>
<ul>
<li>Перечислены в файле yatube_api/requirements.txt</li>
</ul>
<hr />
<h3>Особенности реализации</h3>
<ul>
<li>Проект запускается в Docker контейнерах;</li>
<li>Образ yatube запушен на DockerHub;</li>
<li>Реализован CI/CD;</li>
</ul>
<hr />
<h3>Развертывание на сервере c получением сертификата</h3>
<ul>
<li>Установите на сервере docker и docker-compose-plugin;</li>
<li>Клонируйте на локальный компьютер репозиторий;</li>
<li>Создайте файл /infra/.env. Шаблон для заполнения файла находится в /infra/.env.example;</li>
<li>В файле ./infra/nginx/default.conf закомментируйте строки 12:16 для получения сертификата.</li>
<li>Скопируйте папку infra со всем содержимым на сервер `scp -r ~/yatube_api/infra name@IP.ad.re.ss:~/`
</li>
<li>На сервере, перейдите в папку infra/ и получите сертификаты в Let's Encrypt запустив скрипт `sudo ./init-letsencrypt.sh`</li>
<li>Остановите сервер `docker compose down` </li>
<li>Раскомментируйте строки 14:18 в файле ./infra/nginx/default.conf и впишите имя своего домена вместо `grandmasrecipes.fun`</li>
<li>В папке infra выполните команду `docker compose up -d --build`;</li>
<li>Создайте суперюзера `docker compose exec web python manage.py createsuperuser`</li>
<br /><br />
</ul>
<hr />
<h3>Автор проекта:</h3>
<p>Борокин Андрей</p>

GITHUB: [exp-ext](https://github.com/exp-ext)

[![Join Telegram](https://img.shields.io/badge/My%20Telegram-Join-blue)](https://t.me/Borokin)
