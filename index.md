Добро пожаловать в блог Doprax!

Здесь мы собираем практические руководства, туториалы, сравнения и свежие новости от команды Doprax.

Что вас ждет:

- Пошаговые гайды по деплою (например, Node.js, Django, Telegram-боты, настройка V2Ray/Xray)

- Честные сравнения инфраструктуры (ProVM против сторонних провайдеров, App Spaces против управляемых PaaS)

- Бенчмарки, разбор стоимости и полезные советы из реальной практики

- Обзоры open-source инструментов, которые мы любим и поддерживаем

Есть вопросы или идеи? Пишите в issues.

Удачного билда!

## Статьи в блоге

## Ежедневные новости DevOps

<!-- NEWS START -->
### Свежее — 2026-07-31

- **n8n Sandbox Escape Lets Workflow Editors Run OS Commands as the n8n Process - The Hacker News**
  Уязвимость с выходом из песочницы в n8n позволяет пользователям с правами на редактирование рабочих процессов выполнять произвольные команды ОС от имени основного процесса. Для команд, разворачивающих n8n в мультитенантном режиме или предоставляющих доступ разработчикам без прав администратора, это полностью нарушает изоляцию. Если инструмент запущен в продакшене, немедленно изолируйте среду выполнения в жестко ограниченных контейнерах и закройте сетевой egress.
  [Read more](https://news.google.com/rss/articles/CBMie0FVX3lxTE80cFJDS2J5QjZkQ2lDTm56U3pxZE5vWm56NDRzZGxxelJFanhibDR6WVhub1RIdTR0RUl3cXo3bkdvQ19GekhQNmI2cUQtSUhSWjVsbFJBMEJidXRoZEI5RUZwSVdmaHBXZm00dGRUa2lPY0oySWtoUXhvbw?oc=5)

- **Nginx 1.29.8 and FreeNginx Released With Critical Security Updates - CyberSecurityNews**
  Критические патчи безопасности для Nginx и FreeNginx устраняют уязвимости работы с памятью, которые могут привести к отказу в обслуживании или удаленному выполнению кода. Поскольку Nginx работает на периферии большинства современных инфраструктур, непротравленные прокси становятся первой мишенью для автоматических сканеров. Обновление периферийных узлов стоит провести в приоритетном порядке через стандартный rolling update, не дожидаясь планового окна обслуживания.
  [Read more](https://news.google.com/rss/articles/CBMidEFVX3lxTE0tWVRPaG9lTlJMZFVyVGFNb2VKZ1g5WlAyQzlzMUVrWHZRSkRoSklKTzNSV184eWg5ZUNrS2wzX1VTVklacjJDZjZGSHY4NElReHhpcHI3WnI0VWNyUUZJb0ktY1V6c1NIS082SXVDMF9vUHFB0gF6QVVfeXFMTlpQZnZsRWlzLWJvSUFqUkY1a0RxMHlodFJXRzNGY2lZWnItMjFmU0hiNXN2MXplaTAtdlNSb0dZVWI2MHp6U1M2ZmVNeXptWlpsQTB5N09zaU12OGVnNTRFZ0diZ2w2cWl1UTU2YzlHY1BPTmxoLXpoc0E?oc=5)

- **macOS 26: Native container support delights developers – and not just them - heise online**
  Нативная поддержка контейнеров непосредственно в macOS снижает зависимость от виртуальных машин вроде QEMU или HyperKit при локальной разработке. Отказ от прослойки виртуализации существенно уменьшает нагрузку на ЦП и задержки файлового ввода-вывода при монтировании локальных директорий. Это дает ощутимый прирост скорости сборки и снижает нагрев на устройствах Apple Silicon.
  [Read more](https://news.google.com/rss/articles/CBMitAFBVV95cUxQZlM4SDNiNGVTM05pWE1QSFE0Q1BrZENVMlNJMVdPVjNxVkstZHBBQ19GZHN5VzByMUdfOGJOeG5OWUN4dW95dWo2ZTBFaGpUbjZ4dHpLQ3J5OXVZb3lON1ZSMUF4cHFTZWFlMVgwNnl2TGtIdXE0eHA4WWNOdUViTmZxR08zejRVYUw4M3BBMXc5UlhMdk82MHRrSFVQTnhuUE1HcEdyUHJVWHlVaWFFXzh4anc?oc=5)

- **Enhancing Developer Productivity: Finch’s Support for Development Containers and the Finch Daemon - Amazon Web Services (AWS)**
  AWS расширяет возможности Finch, добавляя фоновый демон и улучшенную поддержку спецификации Dev Container, позиционируя его как полностью открытую альтернативу Docker Desktop. Стандартизация на открытых спецификациях контейнеров позволяет командам избежать проприетарного лицензирования без потери единообразия сред. Появление демона также упрощает интеграцию с локальными конвейерами CI.
  [Read more](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNUEJ4S280bmpMT3M1SElkU2w3MVZpU25zTE1TNXRYNHVBVHY3UUtKYWJyTjF4cGhYUzFqSWQxcGFscEZsOXRVaEVRak5wYWpCR0NBNHNaaWZ1aGNrVVhDX0JpVE5hQ1NtWTRuN0s3dmp2ZXF2MkdjZXFPeFVEbFNPU2pnRnRsdWRDUzVJMGdsMEExMGc2blZsUm4xd3o4S0wzb0ZRXzI2WFpsWVhqb25MRGVHWkE2UnZfdUdPRVh2V21VeTM2Qmthd2UwLVJJLVdCZFE?oc=5)

- **NanoClaw integrates with Docker to bring trust to AI agents - Techzine Global**
  Интеграция автономных ИИ-агентов с Docker создает четкие границы во время выполнения недетерминированного кода, сгенерированного языковыми моделями. Запуск агентских процессов без строгой изоляции через cgroups и namespaces создает риск несанкционированного изменения файловой системы или сканирования хостовой сети. Такой подход позволяет применять к сгенерированному ИИ коду модель нулевого доверия, аналогично неизолированным мультитенантным нагрузкам.
  [Read more](https://news.google.com/rss/articles/CBMipgFBVV95cUxOaEg1RGJrZWtiTVlSbk5JZnlRd2xVV2tEVjBHODI1cW1SQUFDdFVzSE5VQUkxcE55OGFqTEZNM3VXUFRHRFg3VzVXWUk2MWlaRjhDaERUamVYclhyTVdPSVJKeF9Cb2FFcG95dnlyeUhNSU9OV1RNZ19CbGpkUVdpMGxLOTZfT0FudXplbU9PVGJLUUgwbjNjYXhMTl93YTlqc21DRTd3?oc=5)

## Архив

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
