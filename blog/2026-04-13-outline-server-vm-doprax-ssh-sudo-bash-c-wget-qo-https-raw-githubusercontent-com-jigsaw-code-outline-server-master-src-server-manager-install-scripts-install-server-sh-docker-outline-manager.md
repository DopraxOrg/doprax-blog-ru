---
layout: post
title: 'Outline Server: Создайте VM на Doprax, подключитесь по SSH и выполните sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)" — скрипт сам установит Docker и сервер, после чего выдаст ключ для вставки в приложение Outline Manager.'
date: 2026-04-13 13:02:07
author: Doprax
---

**Как развернуть сервер Outline на Doprax за 90 секунд**

Outline — это open-source-решение для создания приватных, зашифрованных VPN-серверов. С Doprax вы получаете готовую VM с высокой пропускной способностью, нулевой конфигурацией и развертыванием меньше чем за минуту.

---

### Шаг 1. Создайте сервер  
Зайдите в [Doprax Dashboard](https://doprax.com), выберите **ProVM**, укажите регион и конфигурацию (рекомендуем: `2 vCPU / 4 GB RAM` — хватит для 5–10 активных пользователей), нажмите **Deploy**.  

Сервер появится в списке через ~45 секунд. Скопируйте его IP-адрес.

---

### Шаг 2. Подключитесь по SSH  
На вашей локальной машине выполните:

```bash
ssh root@ВАШ_IP_АДРЕС
```

(Пароль или приватный ключ доступны в интерфейсе Doprax при первом деплое.)

---

### Шаг 3. Запустите установку Outline  
Выполните одну команду — она скачает и запустит официальный скрипт от Jigsaw:

```bash
sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"
```

Скрипт:
- Автоматически установит Docker (если ещё не установлен),
- Развернёт контейнеры Outline Server,
- Настроит firewall и TLS (через Let’s Encrypt, если указан домен — иначе использует самоподписанный сертификат),
- Выведет **ключ доступа (Access Key)** в формате `ss://...` — его нужно скопировать.

> ⚠️ Ключ содержит все данные для подключения: адрес, порт, шифр, пароль и сертификат. Храните его в безопасности.

---

### Шаг 4. Используйте в Outline Manager  
Откройте [Outline Manager](https://getoutline.org) (десктоп или мобильное приложение), нажмите **Add server → Import from clipboard**, вставьте ключ — и сервер готов к использованию.

Готово. Ваш приватный, маскируемый, open-source VPN работает — без настройки nginx, certbot, docker-compose или системных зависимостей.

---

Хотите автоматизировать это? Добавьте свой собственный скрипт в `App Market` как one-click deploy — или используйте AI Agent в Doprax для генерации и запуска custom-инсталляторов.

[Развернуть Outline сейчас →](https://doprax.com)