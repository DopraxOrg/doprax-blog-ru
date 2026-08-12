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
### Свежее — 2026-08-12

- **n8n Sandbox Escape Lets Workflow Editors Run OS Commands as the n8n Process - The Hacker News**
  Побег из песочницы в n8n подчёркивает риски выполнения low-code автоматизаций с завышенными привилегиями. Предоставление пользователям прав на редактирование сценариев без жёсткой изоляции контейнера фактически равносильно выдаче доступа к терминалу. При самостоятельным хостинге n8n следует запускать в непривилегированных контейнерах с монтированием корневой файловой системы в режиме read-only и ограничением исходящего трафика.
  [Read more](https://news.google.com/rss/articles/CBMie0FVX3lxTE80cFJDS2J5QjZkQ2lDTm56U3pxZE5vWm56NDRzZGxxelJFanhibDR6WVhub1RIdTR0RUl3cXo3bkdvQ19GekhQNmI2cUQtSUhSWjVsbFJBMEJidXRoZEI5RUZwSVdmaHBXZm00dGRUa2lPY0oySWtoUXhvbw?oc=5)

- **Trojanized ai-sdk-ollama Delivers Miasma, a Self-Replicating npm Worm via binding.gyp - Endor Labs**
  Злоумышленники сместили фокус на вспомогательные библиотеки вокруг локальных LLM, используя сборочные скрипты вроде binding.gyp для доставки вредоносного кода. Поскольку процедуры npm install автоматически запускают нативную сборку, рабочие станции разработчиков и CI-раннеры оказываются под угрозой. Командам следует отключать выполнение жизненных скриптов npm по умолчанию и строго проверять lock-файлы.
  [Read more](https://news.google.com/rss/articles/CBMihAFBVV95cUxPSzdXaXZlNE1UR21NeDdsVlVXZm5BWDBqMGI0VzVvdHpkLV9IeHNjV2o3OXh2eWM3dXc2d0wxSmxYbEpsNWdXYU81T1BTWDdicVptRzJMRnN3cGxtaldELXpqbmVuanpIUExwQXlBSVJLRkpqOTRIOXRLSW5wZ3J3TzM0dkY?oc=5)

- **F5 releases out-of-band security updates for NGINX and BIG-IP products - Field Effect**
  Внеочередные обновления безопасности для NGINX и BIG-IP указывают на серьёзные уязвимости в ключевых точках маршрутизации входящего трафика. Граничные реверс-прокси служат приоритетной целью для атак, где возможность удалённого выполнения кода ставит под угрозу всю внутреннюю сеть. Инфраструктурным командам необходимо оперативно провести аудит используемых версий и запустить автоматическое пересоздание образов.
  [Read more](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5JMkc1bEZSMVNyVkp2djRjazNOSVU2NnQ1V0Q2QlNKTXVnWS1aWW9qN1lWWm9JV2ctMEJvSzFhbmpZZFhWbW5DT2pqU0dQN09IYlB6ekplTGk1MmpWdy1QaHFn?oc=5)

- **Alarming runC Flaws Enable Hackers To Exploit Docker Containers For Root Access - HotHardware**
  Уязвимости в низкоуровневой среде исполнения runC представляют прямую угрозу для мультитенантной контейнерной архитектуры, позволяя получить root-доступ к хостовой системе. Изоляция контейнеров напрямую зависит от стабильности runtime, поэтому отсутствие патчей делает хост уязвимым для повышения привилегий из ненадёжных контейнеров. Для защиты требуется немедленное обновление runC, а также принудительное включение user namespaces и профилей seccomp.
  [Read more](https://news.google.com/rss/articles/CBMijAFBVV95cUxOaTE0X1FvWGtLRDhBZXROVWUzcFdZN1hUSEZFNm0zSV9MajZUYm5vM0lDNVdKd0xfdHZpbWhFYnUtTUI5ckpsRHJMdnVjZl9Nb2NYd0dTeFY2bmZyZkNwbDU0S2Z3S3NxM1FpS1FrVVg1cnBFQlZrRzgzalZTWXliZjFfaHJqMTZJaXlCRA?oc=5)

- **Moro Hub and Rafay team up for GPU PaaS in Dubai - Data Center Dynamics**
  Запуск специализированных GPU PaaS в региональных дата-центрах упрощает эксплуатацию инфраструктуры под ресурсоёмкие задачи ИИ и машинного обучения. Использование Kubernetes-абстракций вроде Rafay облегчает распределение ресурсов и управление драйверами на bare-metal кластерах. Это позволяет инженерным командам предоставлять масштабируемые вычислительные мощности с соблюдением требований к локализации данных.
  [Read more](https://news.google.com/rss/articles/CBMilwFBVV95cUxQSUNOMVNIS1l0Tnl0VHN2RmdjWnpfU25sVTN6WTMyODZTQWJ0NzdEaENsc09HVHRHTDRFMjR2UGRpbEp1ZElBUG5LTVNWd3UyTHZoa0c2YWRlQzh0Vm8wT3FNS1h4VmRVa2JaZktZczNzMVRXQS1ObHM5LUVLcG1TMFpEQzF1SzFhOUVmNjBtWTlwVlNOeS04?oc=5)

- **Enhancing Developer Productivity: Finch’s Support for Development Containers and the Finch Daemon - Amazon Web Services (AWS)**
  Расширение возможностей AWS Finch за счёт поддержки спецификации Dev Containers и фонового демона усиливает его позиции как модульной альтернативы Docker Desktop. Стандартизация конфигураций окружения через Dev Containers снижает рассинхронизацию между локальной разработкой и продакшен-пайплайнами CI. Использование открытых CLI-инструментов позволяет командам избежать привязки к коммерческим лицензиям и снизить накладные расходы.
  [Read more](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNUEJ4S280bmpMT3M1SElkU2w3MVZpU25zTE1TNXRYNHVBVHY3UUtKYWJyTjF4cGhYUzFqSWQxcGFscEZsOXRVaEVRak5wYWpCR0NBNHNaaWZ1aGNrVVhDX0JpVE5hQ1NtWTRuN0s3dmp2ZXF2MkdjZXFPeFVEbFNPU2pnRnRsdWRDUzVJMGdsMEExMGc2blZsUm4xd3o4S0wzb0ZRXzI2WFpsWVhqb25MRGVHWkE2UnZfdUdPRVh2V21VeTM2Qmthd2UwLVJJLVdCZFE?oc=5)

- **GitLab thrice sued for 'misleading' investors with AI hype - The Register**
  Судебные иски против GitLab из-за завышенных показателей продуктивности ИИ отражают растущий скептицизм относительно реальной эффективности генеративных инструментов в DevOps. При оценке ИИ-функций в корпоративных платформах командам следует опираться на измеримую пропускную способность пайплайнов, а не на заявления вендоров. Внедрение должно оправдываться реальным сокращением времени цикла и качеством кода.
  [Read more](https://news.google.com/rss/articles/CBMisgFBVV95cUxONTBSSzB1MV9FUU9wX1ZBT2xFdVZCN0kwUWVGbVlSUmdaN1JMTUJpcjU5QmpEZW93V21CVkN0NHd2S3ZBbTZCNEpzYndyT0ZiQi1zMWRuUllNbFVvVVFXY05Da3I5R2pyRS0xUEFINS1obzkwei1SSnB4ZDZrbU9pc0VMeGNpNVk2d09GQm9lTUluRFd0SjRJVnVwQmt6TWhlY0w5UGVCRmV2Q2JMdlkwN1J3?oc=5)

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
