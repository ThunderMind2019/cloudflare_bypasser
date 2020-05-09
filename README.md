# cloudflare_bypasser
Scrapy project to bypass the cloudflare DDoS protection

# Prerequisite

1. Python3+
2. virtualenv installed (pip3 install virtualenv)
3. node >= 10


## Instructions

1. Go to project directory where scrapy.cfg file exist
2. Create python3 virtualenv using
```bash
virtualenv .venv -p python3
```
3. Activate Virtualenv
```bash
source .venv/bin/activate
```
4. install dependencies
```bash
pip install -r requirements.txt
```
6. Replace the \_\_init\_\_.py file as describe

5. Deploy project
```bash
sh deployment.sh
```

NOTE: You might need root access
