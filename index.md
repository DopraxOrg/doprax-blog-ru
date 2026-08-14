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
### Свежее — 2026-08-14

- **n8n Sandbox Escape Lets Workflow Editors Run OS Commands as the n8n Process - The Hacker News**
  Уязвимость с выходом из песочницы в n8n позволяет любому пользователю с правами редактирования сценариев выполнять произвольные команды от имени основного процесса. При самостоятельном хостинге это фактически приравнивает доступ к веб-интерфейсу к шелл-доступу, если сервис не изолирован в rootless-контейнерах или отдельных виртуальных машинах. Инсталляциям с общим доступом к сценариям необходимо срочно накатить патч или ограничить права контейнера на уровне хостовой ОС.
  [Read more](https://news.google.com/rss/articles/CBMie0FVX3lxTE80cFJDS2J5QjZkQ2lDTm56U3pxZE5vWm56NDRzZGxxelJFanhibDR6WVhub1RIdTR0RUl3cXo3bkdvQ19GekhQNmI2cUQtSUhSWjVsbFJBMEJidXRoZEI5RUZwSVdmaHBXZm00dGRUa2lPY0oySWtoUXhvbw?oc=5)

- **Trojanized ai-sdk-ollama Delivers Miasma, a Self-Replicating npm Worm via binding.gyp - Endor Labs**
  Пакет ai-sdk-ollama распространял самореплицирующийся npm-червь через хуки сборки binding.gyp на этапе установки. Поскольку скрипты жизненного цикла запускаются автоматически, фиксации версий в lock-файлах недостаточно для защиты локальных сред и CI-пайплайнов. Командам, разрабатывающим локальные ИИ-сервисы, стоит по умолчанию использовать флаг --ignore-scripts и внимательно проверять нативные зависимости.
  [Read more](https://news.google.com/rss/articles/CBMihAFBVV95cUxPSzdXaXZlNE1UR21NeDdsVlVXZm5BWDBqMGI0VzVvdHpkLV9IeHNjV2o3OXh2eWM3dXc2d0wxSmxYbEpsNWdXYU81T1BTWDdicVptRzJMRnN3cGxtaldELXpqbmVuanpIUExwQXlBSVJLRkpqOTRIOXRLSW5wZ3J3TzM0dkY?oc=5)

- **F5 releases out-of-band security updates for NGINX and BIG-IP products - Field Effect**
  F5 выпустила внеплановые исправления критических уязвимостей для систем BIG-IP и дистрибутивов NGINX. Непропатченные пограничные прокси и ingress-контроллеры остаются частой целью для автоматизированных атак на периметр и расщепления HTTP-запросов. Администраторам важно своевременно обновить граничные сервисы и проверить корректность конфигураций перед перезагрузкой.
  [Read more](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5JMkc1bEZSMVNyVkp2djRjazNOSVU2NnQ1V0Q2QlNKTXVnWS1aWW9qN1lWWm9JV2ctMEJvSzFhbmpZZFhWbW5DT2pqU0dQN09IYlB6ekplTGk1MmpWdy1QaHFn?oc=5)

- **Alarming runC Flaws Enable Hackers To Exploit Docker Containers For Root Access - HotHardware**
  Уязвимости в runC позволяют вредоносному коду внутри контейнера перезаписывать бинарники рантайма на хосте или перехватывать файловые дескрипторы при запуске. Это нарушает базовые гарантии изоляции в мультитенантных кластерах даже без использования привилегированного режима. Администраторам инфраструктуры необходимо обновить рантайм на всех нодах и настроить user namespaces там, где это поддерживается.
  [Read more](https://news.google.com/rss/articles/CBMijAFBVV95cUxOaTE0X1FvWGtLRDhBZXROVWUzcFdZN1hUSEZFNm0zSV9MajZUYm5vM0lDNVdKd0xfdHZpbWhFYnUtTUI5ckpsRHJMdnVjZl9Nb2NYd0dTeFY2bmZyZkNwbDU0S2Z3S3NxM1FpS1FrVVg1cnBFQlZrRzgzalZTWXliZjFfaHJqMTZJaXlCRA?oc=5)

- **Enhancing Developer Productivity: Finch’s Support for Development Containers and the Finch Daemon - Amazon Web Services (AWS)**
  AWS добавила в свой опенсорсный контейнерный CLI Finch поддержку спецификации Dev Containers и фоновый демон. Это упрощает отказ от Docker Desktop, избавляя от необходимости переписывать конфигурации IDE и процессы локальной разработки. Наличие демона также выравнивает поведение утилиты между средами macOS и Linux.
  [Read more](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNUEJ4S280bmpMT3M1SElkU2w3MVZpU25zTE1TNXRYNHVBVHY3UUtKYWJyTjF4cGhYUzFqSWQxcGFscEZsOXRVaEVRak5wYWpCR0NBNHNaaWZ1aGNrVVhDX0JpVE5hQ1NtWTRuN0s3dmp2ZXF2MkdjZXFPeFVEbFNPU2pnRnRsdWRDUzVJMGdsMEExMGc2blZsUm4xd3o4S0wzb0ZRXzI2WFpsWVhqb25MRGVHWkE2UnZfdUdPRVh2V21VeTM2Qmthd2UwLVJJLVdCZFE?oc=5)

- **macOS 26: Native container support delights developers – and not just them - heise online**
  Apple внедряет нативную виртуализацию контейнеров прямо в macOS, что снижает накладные расходы по памяти и процессору по сравнению с использованием вспомогательных виртуальных машин Linux. Для инженеров на Apple Silicon это означает меньшую нагрузку на систему при сборке образов и запуске тяжелых локальных окружений. Разработчики инструментов для контейнеризации теперь могут опираться на стандартные системные API вместо проприетарных прослоек.
  [Read more](https://news.google.com/rss/articles/CBMitAFBVV95cUxQZlM4SDNiNGVTM05pWE1QSFE0Q1BrZENVMlNJMVdPVjNxVkstZHBBQ19GZHN5VzByMUdfOGJOeG5OWUN4dW95dWo2ZTBFaGpUbjZ4dHpLQ3J5OXVZb3lON1ZSMUF4cHFTZWFlMVgwNnl2TGtIdXE0eHA4WWNOdUViTmZxR08zejRVYUw4M3BBMXc5UlhMdk82MHRrSFVQTnhuUE1HcEdyUHJVWHlVaWFFXzh4anc?oc=5)

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
