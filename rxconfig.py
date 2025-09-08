import os, reflex as rx
PROXY_CONTENT = os.getenv("PROXY_CONTENT", "TRUE").upper() == "TRUE"   # <- TRUE by default now
SOCKS5 = os.getenv("SOCKS5", "")
API_URL = os.getenv("API_URL", "https://stepdaddylivehd-teal-moon.reflex.run")  # no trailing slash

config = rx.Config(
    app_name="StepDaddyLiveHD",
    api_url=API_URL,
    proxy_content=PROXY_CONTENT,
    socks5=SOCKS5,
    show_built_with_reflex=False,
    plugins=[rx.plugins.SitemapPlugin(), rx.plugins.TailwindV4Plugin()],
)
