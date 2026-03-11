# Настройка сервера V2Ray/Xray на Doprax ProVM — Полный гайд 2026
> **Doprax: Практический хаб по деплою, архитектуре и оптимизации инфраструктуры для современных билдеров.**
**Безлимитный трафик + протокол REALITY (Hiddify или 3X-UI)**

Развертываем готовый к продакшену сервер Xray с протоколом **REALITY** меньше чем за 10 минут.  
Опыт в DevOps не требуется. Безлимитный канал, порты 1 Гбит/с, чистые выделенные IP и запуск инстанса менее чем за 60 секунд.
---

### Почему именно Doprax ProVM?
* **Реально безлимитный трафик** — никаких лимитов в ТБ и доплат за перерасход.
* **Современные процессоры + выделенные порты 1 Гбит/с**.
* **Чистые IP**, которые отлично подходят для прокси и VPN.
* **Посекундная тарификация + оплата криптой**.
* **Деплой полноценной инфраструктуры за минуты** — без лишней возни с администрированием.

В этом гайде используем **ProVM** (собственная инфраструктура Doprax). Конфига `P1` ($8.95/мес) или `P2` ($12.95/мес) хватит для большинства задач.

---

## Предварительные требования
* Аккаунт на Doprax → [doprax.com](https://www.doprax.com)
* Базовые навыки работы с SSH
* (Опционально) Свой домен для пущей скрытности (для REALITY не обязателен)

---

## Шаг 1: Создаем ProVM (пошагово в панели)

1. Логинимся в панель Doprax.
2. Идем в **My Virtual Machines** → **Create a Virtual Machine**.
3. **Provider**: Выбираем **ProVM**.
4. **Location**: Любая доступная локация (Германия, Франция, Польша и т.д.).
5. **OS Image**: **Ubuntu 24.04** (рекомендуется).
6. **Size**:  
   * `P1` (1 vCPU / 1 GB) — для личного использования.  
   * `P2` (1 vCPU / 2 GB) — если будете раздавать доступ друзьям.
7. **Access Method**: **SSH Key** (настоятельно рекомендую).
8. **Name**: например, `xray-reality-2026`.
9. Жмем **Create Virtual Machine**.

ВМ будет готова **меньше чем за 60 секунд**. Вы увидите IPv4 адрес и пользователя `root`.

---

## Шаг 2: Подключаемся к серверу

```bash
ssh root@ВАШ-IP-PROVM
```
Первым делом обновляем систему:

```bash
apt update && apt upgrade -y
```
## Шаг 3: Выбираем способ установки
### Вариант А: Панель Hiddify (Самый простой — Рекомендую)
Установка одной командой:
```
bash <(curl [https://i.hiddify.com/release](https://i.hiddify.com/release))
```
После установки:

Скрипт выдаст URL админки (обычно https://ВАШ-IP:9000).

В панели создайте нового юзера и выберите протокол Reality.

Всё настроится автоматически (VLESS + Reality + uTLS).
### Вариант Б: Панель 3X-UI (Больше контроля)
Установка одной командой:
```bash <(curl -Ls [https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh](https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh))```
Настройка:

Зайдите в панель (http://ВАШ-IP:порт).

Inbounds → Add new.

Protocol: vless, Port: 443, Security: reality.

Dest: www.microsoft.com:443, Fingerprint: chrome.

### Вариант В: Ручной Xray + REALITY (Advanced)
```bash -c "$(curl -L [https://github.com/XTLS/Xray-install/raw/main/install-release.sh](https://github.com/XTLS/Xray-install/raw/main/install-release.sh))" @ install```
Создайте /usr/local/etc/xray/config.json:
```{
  "log": { "loglevel": "warning" },
  "inbounds": [{
    "port": 443,
    "protocol": "vless",
    "settings": {
      "clients": [{ "id": "ВАШ-UUID", "flow": "xtls-rprx-vision" }],
      "decryption": "none"
    },
    "streamSettings": {
      "network": "tcp",
      "security": "reality",
      "realitySettings": {
        "show": false,
        "dest": "[www.microsoft.com:443](https://www.microsoft.com:443)",
        "xver": 0,
        "serverNames": ["[www.microsoft.com](https://www.microsoft.com)"],
        "privateKey": "ВАШ-PRIVATE-KEY",
        "shortIds": ["ВАШ-SHORT-ID"]
      }
    }
  }],
  "outbounds": [{ "protocol": "freedom" }]
}
```
Генерация ключей:
```
xray uuid
xray x25519
```
Запуск:
```
systemctl enable --now xray
```
## Шаг 4: Тестируем сервер
Используйте любой современный клиент:
- HiddifyNext (iOS/Android/Desktop)
- v2rayN (Windows)
- Nekobox (Android)

Импортируйте конфиг и проверяйте скорость. Ожидаемый результат: Full speed без троттлинга.

## Почему этот сетап выигрывает?
- Безлимит — качайте сколько угодно без доплат.
- 1 Gbps — реальные скорости до 900 Мбит/с.
- Чистые IP — высокий шанс, что REALITY заведется с полпинка.

## Траблшутинг
- Порт 443 закрыт? — На ProVM все порты открыты по дефолту.
- Не коннектит? — Проверьте статус: systemctl status xray.
- Медленно? — Смените домен в dest на другой популярный ресурс.
