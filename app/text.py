from os import getenv

from func_outline import TestLimit


my_user_link = {
    "username": "@StrunkGroove"
}

menu_commands = {
    "about": {
        "key": "about",
        "value": "Узнать о проекте",
        "message": (
            "Почему Outline? 🤔\n\n"
            "Outline имеет ряд значительных преимуществ:\n\n"
            "🔒 Его трудно обнаружить и остановить, в отличие от OpenVPN или Wireguard, которые могут отключаться по щелчку пальцев.\n\n"
            "🛡️ Outline не собирает информацию о посещаемых страницах и имеет открытый исходный код! "
            "Каждый желающий может прочитать и модифицировать его по своему усмотрению.\n\n"
            "🚀 Также Outline почти не снижает скорость интернета, в отличие от AmneziaVPN.\n\n"
            "PS. Все выводы основаны на личном опыте. 😉\n\n"
        )
    },
    "full_access_key": {
        "key": "getvpn",
        "value": "Получить ключ для VPN без ограничений",
        "on_bad_message": (
            "🚀 Чтобы получить полный доступ к VPN, свяжитесь со мной: {user_link}.\n\n"
            "💰 Цена всего {price} ₽ в месяц — символическая для такого уровня комфорта и безопасности!\n\n"
            "🤔 Интроверт? Не верите, что это работает? Думаете, что 50 ₽ — это много? Или просто лень заморачиваться?\n\n"
            "🌟 Попробуйте демо-версию прямо сейчас и убедитесь сами в качестве моего сервиса!"
        ).format(user_link=my_user_link["username"], price=getenv("PRICE")),
        "message": (
            "<b>Ваш ключ доступа к VPN Outline:</b>\n\n"
            "<code>{key}</code>\n\n"
            "<b>Чтобы начать использовать VPN, выполните следующие шаги:</b>\n\n"
            "1️⃣ <a href=\"https://getoutline.org/get-started/#step-3\">Скачать приложение Outline</a> с официального сайта\n"
            "2️⃣ В правом верхнем углу экрана нажмите <b>+</b>\n"
            "3️⃣ Вставьте ключ доступа\n"
            "4️⃣ Разрешите приложению Outline добавлять VPN конфигурации\n\n"
            "<b>PS:</b> Время наслаждаться безграничностью!"
        )
    },
    "demo_access_key": {
        "key": "getdemovpn",
        "callback": "callback_demo_access_key",
        "value": "Получить демо-ключ для подключения к VPN",
        "message": (
            "<b>Ваш ключ доступа к VPN Outline:</b>\n\n"
            "<code>{key}</code>\n\n"
            "<b>Чтобы начать использовать VPN, выполните следующие шаги:</b>\n\n"
            "1️⃣ <a href=\"https://getoutline.org/get-started/#step-3\">Скачать приложение Outline</a> с официального сайта\n"
            "2️⃣ В правом верхнем углу экрана нажмите <b>+</b>\n"
            "3️⃣ Вставьте ключ доступа\n"
            "4️⃣ Разрешите приложению Outline добавлять VPN конфигурации\n\n"
            "<b>PS:</b> Демо-версия ключа имеет ограничение <b>{test_limit}</b> в месяц. 🕒"
        )
    },
    "stastitics": {
        "key": "stastitics",
        "value": "Получить статистику использования",
        "message": "Вы израсходовали {transferred_data}/{limit} (Gb)",
        "message_without_limit": "Вы израсходовали {transferred_data} (Gb)",
        "on_bad_message": (
            "❌ К сожалению, у вас еще нет активных ключей.\n\n"
            "🔑 Вы можете попробовать демоверсию или сразу получить полный доступ за всего {price} ₽ в месяц.\n\n"
            "🔗 Для этого свяжитесь со мной {user_link}"
        ).format(
            user_link=my_user_link["username"], price=getenv("PRICE")
        )
    },
    "get_tg_id": {
        "key": "getid",
        "value": "Узнать id",
        "message": (
            "Пользователь: {username} имеет id: <code>{id}</code>"
        )
    },
}

additional_commands = {
    "what_next": {
        "key": "what_next",
        "value": "Что будет дальше?",
        "message": (
            "Для начала я сосредоточусь на создании небольшой базы пользователей и решении следующих задач:\n\n"
            "- 🔐 Обеспечение безопасности\n"
            "- 🚀 Расширяемость системы\n"
            "- 📈 Управление пиковыми нагрузками\n\n"
            "Пока я занимаюсь настройкой и оптимизацией, все пользователи могут бесплатно воспользоваться VPN. 🌟"
            "Это даст мне возможность выявить и устранить возможные проблемы, а вам — насладиться надежностью, скоростью и безопасностью. 🌐✨"
        ),
    },
}

admin_commands = {
    "update": {
        "key": "update",
        "value": "Обновить",
        "inline_button": "Обновить",
        "callback_key": "admin_update_callback_key",
        "on_exceptions": "Нет доступа",
        "message": (
            "Обновлено!"
        ),
    },
    "set_user_vip": {
        "key": "set_user_vip",
        "value": "Сделать пользователя VIP",
        "callback": "set_user_vip_callback_key",
        "callback_text": "Введите id пользователя",
        "on_exceptions": "Нет доступа",
        "callback_statisticks": "Количество пользователей: {count}",
        "message": (
            "Пользователь {user} стал VIP!"
        ),
    },
    "statistics": {
        "key": "statistics",
        "value": "Получить статистику",
        "callback": "get_admin_statistics_callback_key",
        "message": (
            "Всего пользователей: {count}"
        ),
    },
}

start_message = {
    "message": (
        "Привет! 👋\n\n"
        "Добро пожаловать в нашего бота, который поможет вам получить доступ к VPN-сервису. 🌐🔐\n\n"
        "С его помощью вы сможете безопасно и анонимно путешествовать по просторам интернета, обходя любые блокировки и защищая свои данные. "
        "Просто отправьте команду (/{command}), и бот выдаст вам уникальный ключ для подключения к VPN. Всё просто, быстро и удобно! 🚀\n\n"
        "Если возникнут вопросы, я всегда готов помочь! {link}\n\n"
        "Ваше безопасное интернет-путешествие начинается здесь! 🌍✨"
    ).format(
        command=menu_commands["full_access_key"]["key"], 
        test_limit=TestLimit.name, 
        link=my_user_link["username"]
    )
}

text = {
    "exceptions": (
        "Произошла непридвиденная ошибка. Просьба попробовать попозже.\n"
        "Exceptions token: {exceptions_token}"
    )
}