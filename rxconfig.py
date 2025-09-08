import os
import reflex as rx

# Safe defaults
PROXY_CONTENT = os.getenv("PROXY_CONTENT", "FALSE").upper() == "TRUE"
SOCKS5 = os.getenv("SOCKS5", "")

# Cloud URL fallback (no trailing slash)
API_URL = os.getenv("API_URL", "https://stepdaddylivehd-teal-moon.reflex.run")

config = rx.Config(
    app_name="StepDaddyLiveHD",
    api_url=API_URL,                # <-- IMPORTANT: tell frontend where the API lives
    proxy_content=PROXY_CONTENT,    # default FALSE for safe testing
    socks5=SOCKS5,
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
