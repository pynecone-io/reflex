from reflex.components.core.banner import (
    ConnectionBanner,
    ConnectionModal,
    ConnectionPulser,
    WebsocketTargetURL,
)
from reflex.components.radix.themes.typography.text import Text


def test_websocket_target_url():
    url = WebsocketTargetURL.create()
    _imports = url.get_imports(collapse=True)
    assert list(_imports.keys()) == ["/utils/state", "/env.json"]


def test_connection_banner():
    banner = ConnectionBanner.create()
    _imports = banner.get_imports(collapse=True)
    assert list(_imports.keys()) == [
        "react",
        "/utils/context",
        "/utils/state",
        "@radix-ui/themes@^2.0.0",
        "/env.json",
    ]

    msg = "Connection error"
    custom_banner = ConnectionBanner.create(Text.create(msg))
    assert msg in str(custom_banner.render())


def test_connection_modal():
    modal = ConnectionModal.create()
    _imports = modal.get_imports(collapse=True)
    assert list(_imports.keys()) == [
        "react",
        "/utils/context",
        "/utils/state",
        "@radix-ui/themes@^2.0.0",
        "/env.json",
    ]

    msg = "Connection error"
    custom_modal = ConnectionModal.create(Text.create(msg))
    assert msg in str(custom_modal.render())


def test_connection_pulser():
    pulser = ConnectionPulser.create()
    _custom_code = pulser.get_custom_code()
    _imports = pulser.get_imports(collapse=True)
