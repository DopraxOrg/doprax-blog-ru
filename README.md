# doprax-blog

Recent articles:

## Ежедневные новости DevOps

<!-- NEWS START -->
### Свежее — 2026-08-15

- **n8n Sandbox Escape Lets Workflow Editors Run OS Commands as the n8n Process - The Hacker News**
  Уязвимость с выходом из песочницы в n8n показывает риски использования одного инстанса автоматизации несколькими пользователями. Если n8n доступен не только доверенным администраторам, его необходимо изолировать на уровне отдельных контейнеров или виртуальных машин. Среду выполнения сценариев автоматизации следует изолировать так же строго, как и публичные CI-раннеры.
  [Read more](https://news.google.com/rss/articles/CBMie0FVX3lxTE80cFJDS2J5QjZkQ2lDTm56U3pxZE5vWm56NDRzZGxxelJFanhibDR6WVhub1RIdTR0RUl3cXo3bkdvQ19GekhQNmI2cUQtSUhSWjVsbFJBMEJidXRoZEI5RUZwSVdmaHBXZm00dGRUa2lPY0oySWtoUXhvbw?oc=5)

- **Trojanized ai-sdk-ollama Delivers Miasma, a Self-Replicating npm Worm via binding.gyp - Endor Labs**
  Внедрение вредоносного кода через binding.gyp остается эффективным вектором атак на цепочки поставок, поскольку сборка запускается сразу при установке пакета. На фоне массового внедрения сторонних оберток для локальных LLM вроде Ollama, аудит установочных скриптов в npm должен стать обязательным шагом в CI-пайплайнах. Отключение автоматического выполнения postinstall-скриптов — базовый шаг для минимизации подобных рисков.
  [Read more](https://news.google.com/rss/articles/CBMihAFBVV95cUxPSzdXaXZlNE1UR21NeDdsVlVXZm5BWDBqMGI0VzVvdHpkLV9IeHNjV2o3OXh2eWM3dXc2d0wxSmxYbEpsNWdXYU81T1BTWDdicVptRzJMRnN3cGxtaldELXpqbmVuanpIUExwQXlBSVJLRkpqOTRIOXRLSW5wZ3J3TzM0dkY?oc=5)

- **F5 releases out-of-band security updates for NGINX and BIG-IP products - Field Effect**
  Внеплановые обновления от F5 указывают на критические уязвимости, требующие срочной установки на пограничных прокси и балансировщиках нагрузки. Необновленные NGINX-инстансы и Ingress-контроллеры создают прямой риск компрометации внутреннего сетевого контура. Инфраструктурным командам стоит проверить версии проксирующих узлов и зависимости Ingress в кластерах Kubernetes.
  [Read more](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5JMkc1bEZSMVNyVkp2djRjazNOSVU2NnQ1V0Q2QlNKTXVnWS1aWW9qN1lWWm9JV2ctMEJvSzFhbmpZZFhWbW5DT2pqU0dQN09IYlB6ekplTGk1MmpWdy1QaHFn?oc=5)

- **Alarming runC Flaws Enable Hackers To Exploit Docker Containers For Root Access - HotHardware**
  Уязвимости побега из контейнера на уровне runC нивелируют стандартную изоляцию Docker и containerd, предоставляя атакующему root-доступ к хосту. Это подтверждает необходимость запуска процессов от непривилегированного пользователя и обязательного включения профилей seccomp. Обновление низкоуровневых сред исполнения на всех нодах и хостах контейнеризации должно быть в приоритете.
  [Read more](https://news.google.com/rss/articles/CBMijAFBVV95cUxOaTE0X1FvWGtLRDhBZXROVWUzcFdZN1hUSEZFNm0zSV9MajZUYm5vM0lDNVdKd0xfdHZpbWhFYnUtTUI5ckpsRHJMdnVjZl9Nb2NYd0dTeFY2bmZyZkNwbDU0S2Z3S3NxM1FpS1FrVVg1cnBFQlZrRzgzalZTWXliZjFfaHJqMTZJaXlCRA?oc=5)

- **Enhancing Developer Productivity: Finch’s Support for Development Containers and the Finch Daemon - Amazon Web Services (AWS)**
  Поддержка спецификации devcontainer и постоянного демона в AWS Finch устраняет главные препятствия для отказа от проприетарных сред контейнеризации на рабочих станциях. Для команд, стандартизирующих окружение разработки через devcontainer.json, это дает готовую open-source альтернативу на macOS и Linux. Новые возможности упрощают интеграцию с IDE без необходимости лицензирования коммерческого ПО.
  [Read more](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNUEJ4S280bmpMT3M1SElkU2w3MVZpU25zTE1TNXRYNHVBVHY3UUtKYWJyTjF4cGhYUzFqSWQxcGFscEZsOXRVaEVRak5wYWpCR0NBNHNaaWZ1aGNrVVhDX0JpVE5hQ1NtWTRuN0s3dmp2ZXF2MkdjZXFPeFVEbFNPU2pnRnRsdWRDUzVJMGdsMEExMGc2blZsUm4xd3o4S0wzb0ZRXzI2WFpsWVhqb25MRGVHWkE2UnZfdUdPRVh2V21VeTM2Qmthd2UwLVJJLVdCZFE?oc=5)

- **Google-Backed Software Developer GitLab Eyes Sale, Reuters Says - Bloomberg.com**
  Сообщения о возможной продаже GitLab отражают общую консолидацию на рынке инструментов для разработки и CI/CD. Смена владельца неизбежно повлияет на стратегию развития, ценообразование и поддержку редакции GitLab Community Edition. Инженерам, использующим self-hosted инстансы GitLab, стоит внимательно следить за изменениями в политике лицензирования платформы.
  [Read more](https://news.google.com/rss/articles/CBMiswFBVV95cUxPTUdBNmJQbXNrSENsUzNrRmFUZDNkTG1ZaUhsS2NEZTYtck42UkZpNkdTRTBSRzJTc2drdnlHWlpMTjhzcmZ3YlljbGVqWnJHenBVb0NHbTk5OE1tc3Q4cVpMamxWUlhJdGdPaElPckpHbGJHbzA5MzRNX0xXTkl5MXVPRzRrLWZkVjBueHp4TEJYOTRYU0lrSzNweE9lRDl5SnViYmpLRnJDakJrT01ha1g5MA?oc=5)

- **macOS 26: Native container support delights developers – and not just them - heise online**
  Появление нативной поддержки контейнеров в macOS снижает накладные расходы по памяти и процессору, характерные для промежуточных виртуальных машин Linux. Ускорение дискового ввода-вывода и запуск на уровне системы заметно упростят локальное тестирование и оркестрацию сервисов на рабочих станциях Mac. При этом ключевым фактором остается совместимость с бинарными сборками под Linux.
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
