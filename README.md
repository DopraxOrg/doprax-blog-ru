# doprax-blog

Recent articles:

## Ежедневные новости DevOps

<!-- NEWS START -->
### Свежее — 2026-08-28

- **F5 releases out-of-band security updates for NGINX and BIG-IP products - Field Effect**
  F5 выпустила внеплановые патчи для уязвимостей в NGINX и устройствах BIG-IP. Командам, эксплуатирующим NGINX в продакшене, следует проверить конфигурации upstream и используемые модули, а затем оперативно обновиться. Уязвимости на уровне обратного прокси позволяют обойти стандартные сетевые экраны при компрометации самого шлюза.
  [Read more](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5JMkc1bEZSMVNyVkp2djRjazNOSVU2NnQ1V0Q2QlNKTXVnWS1aWW9qN1lWWm9JV2ctMEJvSzFhbmpZZFhWbW5DT2pqU0dQN09IYlB6ekplTGk1MmpWdy1QaHFn?oc=5)

- **n8n Sandbox Escape Lets Workflow Editors Run OS Commands as the n8n Process - The Hacker News**
  Уязвимость в n8n позволяет пользователям с правами редактирования сценариев обходить песочницу и выполнять произвольные команды ОС от имени процесса n8n. Self-hosted инсталляциям с многопользовательским доступом или открытыми вебхуками требуется срочное обновление либо жесткая изоляция процессов. Запуск систем автоматизации в rootless-контейнерах или изолированных VM остается базовым требованием безопасности.
  [Read more](https://news.google.com/rss/articles/CBMie0FVX3lxTE80cFJDS2J5QjZkQ2lDTm56U3pxZE5vWm56NDRzZGxxelJFanhibDR6WVhub1RIdTR0RUl3cXo3bkdvQ19GekhQNmI2cUQtSUhSWjVsbFJBMEJidXRoZEI5RUZwSVdmaHBXZm00dGRUa2lPY0oySWtoUXhvbw?oc=5)

- **Alarming runC Flaws Enable Hackers To Exploit Docker Containers For Root Access - HotHardware**
  Очередные уязвимости в runC показывают, как побег из контейнера может привести к получению root-доступа на уровне ядра хоста. Это напоминает, что контейнеры сами по себе не являются границей изоляции без включенных user namespaces и профилей seccomp. Обновление среды выполнения контейнеров на нодах Kubernetes и Docker-хостах имеет приоритет перед плановым деплоем приложений.
  [Read more](https://news.google.com/rss/articles/CBMijAFBVV95cUxOaTE0X1FvWGtLRDhBZXROVWUzcFdZN1hUSEZFNm0zSV9MajZUYm5vM0lDNVdKd0xfdHZpbWhFYnUtTUI5ckpsRHJMdnVjZl9Nb2NYd0dTeFY2bmZyZkNwbDU0S2Z3S3NxM1FpS1FrVVg1cnBFQlZrRzgzalZTWXliZjFfaHJqMTZJaXlCRA?oc=5)

- **Enhancing Developer Productivity: Finch’s Support for Development Containers and the Finch Daemon - Amazon Web Services (AWS)**
  AWS развивает Finch — открытую альтернативу Docker Desktop, добавив поддержку Dev Containers и фоновый демон. Паритет CLI с Docker на macOS и Linux практически достигнут, но скорость внедрения зависит от интеграции с локальными пайплайнами разработчиков. Для команд, оптимизирующих расходы на лицензии Docker Desktop, проект становится вполне жизнеспособной заменой.
  [Read more](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNUEJ4S280bmpMT3M1SElkU2w3MVZpU25zTE1TNXRYNHVBVHY3UUtKYWJyTjF4cGhYUzFqSWQxcGFscEZsOXRVaEVRak5wYWpCR0NBNHNaaWZ1aGNrVVhDX0JpVE5hQ1NtWTRuN0s3dmp2ZXF2MkdjZXFPeFVEbFNPU2pnRnRsdWRDUzVJMGdsMEExMGc2blZsUm4xd3o4S0wzb0ZRXzI2WFpsWVhqb25MRGVHWkE2UnZfdUdPRVh2V21VeTM2Qmthd2UwLVJJLVdCZFE?oc=5)

- **Building a detection-as-code pipeline with Sigma and CI/CD - Security Boulevard**
  Применение практик CI/CD к разработке правил Sigma позволяет тестировать и валидировать логику алертов до их релиза в SIEM. Подход Detection-as-Code снижает число ложных срабатываний и автоматизирует деплой правил в гетерогенных инфраструктурах. Основная практическая сложность здесь — поддержка качественных синтетических логов для регрессионного тестирования в пайплайне.
  [Read more](https://news.google.com/rss/articles/CBMingFBVV95cUxNbWJybGFKZ2g4VmtCcnAzTThoeE9OUHpaVVJQZDhreHYxVVVzVU43eDVTdUFiUExnVEFBOGFtSkVPaXE1T2xrQ1R1dGxQd2ZWVktNRUQ4VzJfTHlLdktfTWszaWJzdk5oOGNmc0R0Rk14SG1pNGV0WXR1TXdmUVhRUDd4S2tJbjVzWVJpMEZmQU85QWt1Q25OeXR1SlM4UQ?oc=5)

- **Deploying Containers on Specialized Flatcar OS - Virtualization Review**
  Использование легковесных неизменяемых ОС вроде Flatcar Container Linux упрощает управление нодами, исключая дрейф конфигураций и автоматизируя обновления системы. В кластерах Kubernetes и bare-metal инсталляциях immutable-дистрибутивы заметно снижают трудозатраты на патч-менеджмент. Обратная сторона — необходимость полностью перевести настройку хостов на Ignition-конфиги и cloud-init.
  [Read more](https://news.google.com/rss/articles/CBMipwFBVV95cUxOczRVRTdReHpkLURFZGJ3LUhIeDJKbTNoRUlpWDBKZ0VwLXExNWNkZTN4MFJiaWpxbVlaZzM1YWliOGl3eGt0aU5uMnJZS0VwT2Q4TV82UkkwNGpXVWNsOUVxSko5TC0zWnFVQzFPNkYwNk5QNlNuWjRVbUpnb191LTZzbEJadktUbktwX01pNnJFcUh1TS0yTFhFQ0pYa2R3ZS1meGY4RQ?oc=5)

## Архив

- [Август 2026](news/2026-08.md)
- [Июль 2026](news/2026-07.md)

<!-- NEWS END -->

<!-- BLOG START -->
- **2026-04-13** — ['Outline Server: Создайте VM на Doprax, подключитесь по SSH и выполните sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)" — скрипт сам установит Docker и сервер, после чего выдаст ключ для вставки в приложение Outline Manager.'](blog/2026-04-13-outline-server-vm-doprax-ssh-sudo-bash-c-wget-qo-https-raw-githubusercontent-com-jigsaw-code-outline-server-master-src-server-manager-install-scripts-install-server-sh-docker-outline-manager.md)
- **2026-04-13** — ["Свой VPN-сервер на VPS: обзор лучших open-source инструментов для развёртывания в 2026 году"](blog/2026-04-13-Open-Source-VPN.md)
- **2026-04-01** — [2026-04-01-internet-ports](blog/2026-04-01-internet-ports.md)
- **2026-03-30** — [2026-03-30-Install-Amnezia-VPN](blog/2026-03-30-Install-Amnezia-VPN.md)
- **2026-03-27** — ["Как обойти блокировки через DNS-туннель: Инструкция по dnstt"](blog/2026-03-27-dnstt-russia-setup.md)
- **2026-03-26** — ['What to Do When Your VPN Server Gets Blocked (IP Rotation Guide)'](blog/2026-03-26-what-to-do-when-your-vpn-server-gets-blocked-ip-rotation-guide.md)
- **2026-03-26** — ['VLESS, VMess, Trojan, Shadowsocks: Which Protocol Still Works in 2026?'](blog/2026-03-26-vless-vmess-trojan-shadowsocks-which-protocol-still-works-in-2026.md)
- **2026-03-26** — ["How to Run Your Own V2Ray Server in 5 Minutes with Doprax — "как поднять свой VPN на VPS""](blog/2026-03-26-how-to-run-your-own-v2ray-server-in-5-minutes-with-doprax-vpn-vps-.md)
- **2026-03-26** — ['3x-ui vs x-ui: Which XRay Panel to Choose and How to Deploy It'](blog/2026-03-26-3x-ui-vs-x-ui-which-xray-panel-to-choose-and-how-to-deploy-it.md)
- **2026-03-18** — [2026-03-18-Doprax-YAML](blog/2026-03-18-Doprax-YAML.md)
- **2026-03-11** — [2026-03-11-kak-oplatit-doprax-kriptovalyutoy-s-minimalnoy-komissiey](blog/2026-03-11-kak-oplatit-doprax-kriptovalyutoy-s-minimalnoy-komissiey.md)
- **2026-03-10** — [2026-03-10-v2ray-xray-2026-doprax](blog/2026-03-10-v2ray-xray-2026-doprax.md)
<!-- BLOG END -->
