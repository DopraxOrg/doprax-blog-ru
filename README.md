# doprax-blog

Recent articles:

## Ежедневные новости DevOps

<!-- NEWS START -->
### Свежее — 2026-07-29

- **n8n Sandbox Escape Lets Workflow Editors Run OS Commands as the n8n Process - The Hacker News**
  Возможность обхода JS-песочницы позволяет редакторам сценариев выполнять системные команды с правами основного процесса n8n, полностью лишая изоляции рабочие задачи на хосте. Командам, использующим self-hosted инстансы n8n, следует ограничить права редакторов и изолировать сетевой доступ к сервису до установки обновлений. Запуск воркеров в непривилегированных одноразовых контейнерах остается надежным способом предотвратить захват сервера при исполнении вредоносных сценариев.
  [Read more](https://news.google.com/rss/articles/CBMie0FVX3lxTE80cFJDS2J5QjZkQ2lDTm56U3pxZE5vWm56NDRzZGxxelJFanhibDR6WVhub1RIdTR0RUl3cXo3bkdvQ19GekhQNmI2cUQtSUhSWjVsbFJBMEJidXRoZEI5RUZwSVdmaHBXZm00dGRUa2lPY0oySWtoUXhvbw?oc=5)

- **Nginx 1.29.8 and FreeNginx Released With Critical Security Updates - CyberSecurityNews**
  Устранение критических уязвимостей в основном дистрибутиве Nginx и форке FreeNginx требует оперативного обновления граничных прокси и ingress-контроллеров. Необновленные обратные прокси подвергают внутреннюю сеть рискам подмены запросов, переполнения буфера или атак на отказ в обслуживании на периметре. Инженерам рекомендуется проверить бинарные сигнатуры и протестировать новые образы на staging-контурах, чтобы исключить сбои в конфигурациях проксирования.
  [Read more](https://news.google.com/rss/articles/CBMidEFVX3lxTE0tWVRPaG9lTlJMZFVyVGFNb2VKZ1g5WlAyQzlzMUVrWHZRSkRoSklKTzNSV184eWg5ZUNrS2wzX1VTVklacjJDZjZGSHY4NElReHhpcHI3WnI0VWNyUUZJb0ktY1V6c1NIS082SXVDMF9vUHFB0gF6QVVfeXFMTlpQZnZsRWlzLWJvSUFqUkY1a0RxMHlodFJXRzNGY2lZWnItMjFmU0hiNXN2MXplaTAtdlNSb0dZVWI2MHp6U1M2ZmVNeXptWlpsQTB5N09zaU12OGVnNTRFZ0diZ2w2cWl1UTU2YzlHY1BPTmxoLXpoc0E?oc=5)

- **Enhancing Developer Productivity: Finch’s Support for Development Containers and the Finch Daemon - Amazon Web Services (AWS)**
  Добавление нативной поддержки dev-контейнеров и отдельного демона в Finch укрепляет позиции опенсорсной альтернативы Docker Desktop для рабочих станций. Интеграция упрощает настройку локального окружения при работе со сложными инструментами, сохраняя управление контейнерами открытым и бесплатным. Использование стандартизированных dev-контейнеров минимизирует расхождения между локальной разработкой и средой сборки в CI/CD.
  [Read more](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNUEJ4S280bmpMT3M1SElkU2w3MVZpU25zTE1TNXRYNHVBVHY3UUtKYWJyTjF4cGhYUzFqSWQxcGFscEZsOXRVaEVRak5wYWpCR0NBNHNaaWZ1aGNrVVhDX0JpVE5hQ1NtWTRuN0s3dmp2ZXF2MkdjZXFPeFVEbFNPU2pnRnRsdWRDUzVJMGdsMEExMGc2blZsUm4xd3o4S0wzb0ZRXzI2WFpsWVhqb25MRGVHWkE2UnZfdUdPRVh2V21VeTM2Qmthd2UwLVJJLVdCZFE?oc=5)

- **GitLab thrice sued for 'misleading' investors with AI hype - The Register**
  Коллективные иски из-за завышенных обещаний в сфере ИИ подсвечивают разрыв между маркетингом вендоров и реальным приростом производительности в DevOps-инструментах. Корпоративным командам, внедряющим ИИ в CI/CD, стоит оценивать генерацию кода и автоматическую триажирование по метрикам эффективности, а не по запевкам продавцов. Зависимость от непроверенных ИИ-функций рискует раздуть бюджеты на лицензии без ощутимого ускорения пайплайнов.
  [Read more](https://news.google.com/rss/articles/CBMisgFBVV95cUxONTBSSzB1MV9FUU9wX1ZBT2xFdVZCN0kwUWVGbVlSUmdaN1JMTUJpcjU5QmpEZW93V21CVkN0NHd2S3ZBbTZCNEpzYndyT0ZiQi1zMWRuUllNbFVvVVFXY05Da3I5R2pyRS0xUEFINS1obzkwei1SSnB4ZDZrbU9pc0VMeGNpNVk2d09GQm9lTUluRFd0SjRJVnVwQmt6TWhlY0w5UGVCRmV2Q2JMdlkwN1J3?oc=5)

- **NanoClaw integrates with Docker to bring trust to AI agents - Techzine Global**
  Изоляция автономных ИИ-агентов внутри контейнеров Docker создает необходимые границы выполнения при запуске непроверенного кода или команд оболочки. Без контейнерных ограничений инструменты автоматического написания кода могут случайно изменить конфигурацию хоста или скомпрометировать секреты. Применение жестких лимитов ресурсов и сетевых политик для контейнеров агентов предотвращает перерастание ошибок ИИ в инциденты на инфраструктурном уровне.
  [Read more](https://news.google.com/rss/articles/CBMipgFBVV95cUxOaEg1RGJrZWtiTVlSbk5JZnlRd2xVV2tEVjBHODI1cW1SQUFDdFVzSE5VQUkxcE55OGFqTEZNM3VXUFRHRFg3VzVXWUk2MWlaRjhDaERUamVYclhyTVdPSVJKeF9Cb2FFcG95dnlyeUhNSU9OV1RNZ19CbGpkUVdpMGxLOTZfT0FudXplbU9PVGJLUUgwbjNjYXhMTl93YTlqc21DRTd3?oc=5)

- **Moro Hub and Rafay team up for GPU PaaS in Dubai - Data Center Dynamics**
  Развертывание автоматизированной оркестрации Kubernetes для GPU-нагрузок на региональной инфраструктуре решает проблему управления аппаратными ИИ-ускорителями. Использование GPU PaaS снижает издержки на менеджмент драйверов, автомасштабирование кластеров и разделение ресурсов между командами. Размещение процессов дообучения моделей на управляемых GPU-кластерах обеспечивает контроль над данными и затратами по сравнению с публичными SaaS API.
  [Read more](https://news.google.com/rss/articles/CBMilwFBVV95cUxQSUNOMVNIS1l0Tnl0VHN2RmdjWnpfU25sVTN6WTMyODZTQWJ0NzdEaENsc09HVHRHTDRFMjR2UGRpbEp1ZElBUG5LTVNWd3UyTHZoa0c2YWRlQzh0Vm8wT3FNS1h4VmRVa2JaZktZczNzMVRXQS1ObHM5LUVLcG1TMFpEQzF1SzFhOUVmNjBtWTlwVlNOeS04?oc=5)

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
