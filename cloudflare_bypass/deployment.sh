source .venv/bin/activate
mkdir /etc/scrapyd
cp scrapyd.conf.example /etc/scrapyd/scrapyd.conf
scrapyd > /tmp/scrapyd.log 2>&1 &
scrapyd-deploy localhost -p cloudflare_bypass
