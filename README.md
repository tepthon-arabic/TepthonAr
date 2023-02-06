<p align="center">
  <img src="./resources/extras/logo_readme.jpg" alt="Tepthone Logo">
</p>
<h1 align="center">
  <b> Tepthon - UserBot</b>
</h1>

<b>روبوت مستخدم Telegram ثابت وقابل للتوصيل + بوت موسيقي للمكالمات الصوتية والمرئية ، يعتمد على Telethon.</b>

[![](https://img.shields.io/badge/Ultroid-v0.7-darkgreen)](#)
[![Stars](https://img.shields.io/github/stars/tepthon-arabic/TepthonAr?style=flat-square&color=yellow)](https://github.com/tepthon-arabic/TepthonAr/stargazers)
[![Forks](https://img.shields.io/github/forks/tepthon-arabic/TepthonAr?style=flat-square&color=orange)](https://github.com/tepthon-arabic/TepthonAr/fork)
[![Size](https://img.shields.io/github/repo-size/tepthon-arabic/TepthonAr?style=flat-square&color=green)](https://github.com/tepthon-arabic/TepthonAr/)   
[![Python](https://img.shields.io/badge/Python-v3.10.3-blue)](https://www.python.org/)
[![CodeFactor](https://www.codefactor.io/repository/github/tepthon-arabic/TepthonAr/badge/main)](https://www.codefactor.io/repository/github/tepthon-arabic/TepthonAr/overview/main)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/tepthon-arabic/TepthonAr/graphs/commit-activity)
[![Docker Pulls](https://img.shields.io/docker/pulls/thetepthon-arabic/TepthonAr?style=flat-square)](https://img.shields.io/docker/pulls/thetepthon-arabic/TepthonAr?style=flat-square)   
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/tepthon-arabic/TepthonAr)
[![Contributors](https://img.shields.io/github/contributors/tepthon-arabic/TepthonAr?style=flat-square&color=green)](https://github.com/tepthon-arabic/TepthonAr/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/tepthon-arabic/TepthonAr/blob/main/LICENSE)   
[![Sparkline](https://stars.medv.io/tepthon-arabic/TepthonAr.svg)](https://stars.medv.io/tepthon-arabic/TepthonAr)
----

# Deploy
- [هيروكو](#deploy-to-heroku)
- [اوكيتو](#deploy-to-okteto)
- [لوكال ميجتال](#deploy-locally)

# Documentation 
[![Documentation](https://img.shields.io/badge/Documentation-Ultroid-blue)](http://ultroid.tech/)

# Tutorial 
- Full Tutorial - [![Full Tutorial](https://img.shields.io/badge/Watch%20Now-blue)](https://www.youtube.com/watch?v=0wAV7pUzhDQ)

- Tutorial to get Redis URL and password - [here.](./resources/extras/redistut.md)
---

## Deploy to Heroku
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://deploy.ultroid.tech)

## Deploy to Okteto
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/tepthon-arabic/TepthonAr)

## Deploy Locally
- [Traditional Method](#local-deploy---traditional-method)
- [Easy Method](#local-deploy---easy-method)
- [Ultroid CLI](#ultroid-cli)

### Local Deploy - Easy Method
- Linux - `wget -O locals.py https://git.io/JY9UM && python3 locals.py`
- Windows - `cd desktop ; wget https://git.io/JY9UM -o locals.py ; python locals.py`
- Termux - `wget -O install-termux https://tiny.ultroid.tech/termux && bash install-termux`

### Local Deploy - Traditional Method
- Get your [Necessary Variables](#Necessary-Variables)
- Clone the repository:    
`git clone https://github.com/tepthon-arabic/TepthonAr.git`
- Go to the cloned folder:    
`cd Ultroid`
- Create a virtual env:      
`virtualenv -p /usr/bin/python3 venv`
`. ./venv/bin/activate`
- Install the requirements:      
`pip(3) install -U -r re*/st*/optional-requirements.txt`
`pip(3) install -U -r requirements.txt`
- Generate your `SESSION`:
  - For Linux users:
    `bash sessiongen`
     or
    `wget -O session.py https://git.io/JY9JI && python3 session.py`
  - For Termux users:
    `wget -O session.py https://git.io/JY9JI && python session.py`
  - For Windows Users:
    `cd desktop ; wget https://git.io/JY9JI -o ultroid.py ; python ultroid.py`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/tepthon-arabic/TepthonAr/blob/main/.env.sample).
(You can either edit and rename the file or make a new file named `.env`.)
- Run the bot:
  - Linux Users:
   `bash startup`
  - Windows Users:
    `python(3) -m pyUltroid`
<details>
<summary><h3>[OUTDATED] Ultroid CLI</h3></summary>

[Ultroid CLI](https://github.com/BLUE-DEVIL1134/UltroidCli) is a command-line interface for deploying Ultroid.   

- **Installing** -    
Run the following code on a terminal, with curl installed.   
`ver=$(curl https://raw.githubusercontent.com/BLUE-DEVIL1134/UltroidCli/main/version.txt) && curl -L -o ultroid https://github.com/BLUE-DEVIL1134/UltroidCli/releases/download/$ver/ultroid.exe`
OR
Go to [UltroidCli](https://github.com/BLUE-DEVIL1134/UltroidCli) and install the version release from the Github Releases. Add the executable to your system path as specified in the [Readme](https://github.com/BLUE-DEVIL1134/UltroidCli#how-to-use-ultroidcli-).   

- **Documentation** -
Take a look at the [`docs`](https://blue-devil1134.github.io/UltroidCli/) for more detailed information.
</details>

---
## Necessary Variables
- `SESSION` - SessionString for your accounts login session. Get it from [here](#Session-String)

One of the following database:
- For **Redis** (tutorial [here](./resources/extras/redistut.md))
  - `REDIS_URI` - Redis endpoint URL, from [redislabs](http://redislabs.com/).
  - `REDIS_PASSWORD` - Redis endpoint Password, from [redislabs](http://redislabs.com/).
- For **MONGODB**
  - `MONGO_URI` - Get it from [mongodb](https://mongodb.com/atlas).
- For **SQLDB**
  - `DATABASE_URL`- Get it from [elephantsql](https://elephantsql.com).

## Session String
Different ways to get your `SESSION`:
* [![Run on Repl.it](https://replit.com/@Tepthoniq/StringSessionTepthon)
* Linux : `wget -O session.py https://git.io/JY9JI && python3 session.py`
* PowerShell : `cd desktop ; wget https://git.io/JY9JI ; python ultroid.py`
* Termux : `wget -O session.py https://git.io/JY9JI && python session.py`
* TelegramBot : [@SessionGeneratorBot](https://t.me/SessionGeneratorBot)

---

# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
Ultroid is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

---

# Credits
* [![Tepthone-Devs](https://img.shields.io/static/v1?label=Tepthone&message=devs&color=critical)](https://t.me/UltroidDevs)
* [Lonami](https://github.com/LonamiWebs/) for [Telethon.](https://github.com/LonamiWebs/Telethon)
* [MarshalX](https://github.com/MarshalX) for [PyTgCalls.](https://github.com/MarshalX/tgcalls)

> من [@Tepthon](https://t.me/Tepthon).    
# Dev hmd @PPF22
