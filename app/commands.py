commands = {
    "access_key": {
        "key": "get_demo_access_key",
        "value": "Получить демо-ключ для подключения к VPN",
        "message": (         
            "Ваш ключ доступа к VPN Outline:\n\n"
            "`{key}`\n\n"
            "Для продолжения необходимо:\n" 
            "1\) [Скачать приложение Outline](https://getoutline.org/get-started/#step-3) на свое устройство с официального сайта\n"
            "2\) В правом верхнем углу экрана нажать `+`\n"
            "3\) Вставить ключ доступа\n"
            "4\) Разрешить приложению Outline добавлять VPN конфигурации\n\n"
            "PS: Демо версия ключа имеет ограничение {limit} в мес\n"
        )
    },
    "stastitics": {
        "key": "get_stastitics",
        "value": "Получить статистику использования",
        "message": "Вы израсходовали {transferred_data}/{limit} (Gb)",
        "message_without_limit": "Вы израсходовали {transferred_data} (Gb)"
    }
}
