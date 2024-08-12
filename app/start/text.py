from shared.text import my_user_link, TestLimit
from menu.text import full_access_text


start_message = {
    "message": (
        "Привет! 👋\n\n"
        "Добро пожаловать в нашего бота, который поможет вам получить доступ к VPN-сервису. 🌐🔐\n\n"
        "С его помощью вы сможете безопасно и анонимно путешествовать по просторам интернета, обходя любые блокировки и защищая свои данные.\n"
        "Просто отправьте команду (/{command}), и бот выдаст вам уникальный ключ для подключения к VPN. Всё просто, быстро и удобно! 🚀\n\n"
        "Если возникнут вопросы, я всегда готов помочь! {link}\n\n"
        "Ваше безопасное интернет-путешествие начинается здесь! 🌍✨"
    ).format(
        command=full_access_text["key"], 
        test_limit=TestLimit.name, 
        link=my_user_link["username"]
    )
}

