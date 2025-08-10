import json
from typing import Any, Union


def try_json_load(v: Any) -> Any:
    if not isinstance(v, str):
        return v
    try:
        return json.loads(v)
    except json.JSONDecodeError:
        return v


def build_vpn_link(domain: str, inbound: dict, client: dict) -> str:
    s = inbound["streamSettings"]["realitySettings"]
    settings = s["settings"]

    return (
        f'{inbound["protocol"]}://{client["id"]}@{domain}:{inbound["port"]}'
        f'?type={inbound["streamSettings"]["network"]}'
        f'&security={inbound["streamSettings"]["security"]}'
        f'&pbk={settings["publicKey"]}'
        f'&fp={settings["fingerprint"]}'
        f'&sni={s["serverNames"][0]}'
        f'&sid={s["shortIds"][0]}'
        f'&spx={settings["spiderX"]}'
        f'&pqv={settings["mldsa65Verify"]}'
        f'&flow={client["flow"]}'
        f'#{inbound["remark"]}-{client["email"]}'
    )


def create_email(tg_id: int, email: str) -> str:
    return f"{email}|{tg_id}"


def get_vpn_link(tg_id: int) -> Union[str, None]:
    from api.x_ui_api import X_UI_API

    inbound = X_UI_API.get_inboud()
    client = next(
        (
            client
            for client in inbound["settings"]["clients"]
            if str(tg_id) == client["id"]
        ),
        None,
    )
    if not client:
        return None
    return build_vpn_link(X_UI_API.domain, inbound, client)


if __name__ == "__main__":
    get_vpn_link("mark")
