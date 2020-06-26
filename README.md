# sample-lambda-selenium
AWS Lambda で Selenium を使うサンプル

## Requirements
- Node.js (10.16.3 LTS にて動作を確認)
- Python (3.8.3にて 動作を確認)
- Google Chrome (83.0.4103.106 にて動作を確認)

## Deploy AWS
### Install Serverless Framework
```bash
#e.g. Global mode
sudo npm install -g serverless
```
### Setting AWS-CLI
```bash
aws configure --profile serverless
#AWS Access Key ID [None]: XXXXXXXXXXXXXXXXXXXX
#AWS Secret Access Key [None]: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#Default region name [None]: ap-northeast-1
#Default output format [None]: json
```
### Get Chromium
```bash
cd /path_to_sample/layer/chrome/
curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-55/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip
unzip headless-chromium.zip
rm headless-chromium.zip
```
### Get Chromedriver
```bash
cd /path_to_sample/layer/chrome/
curl -SL https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip > chromedriver.zip
unzip chromedriver.zip
rm chromedriver.zip
```
### Get Selenium (with Docker)
```bash
cd /path_to_sample/layer/selenium/
docker build -t build-python .
docker run --rm -v /path_to_sample/layer/selenium:/var/task -w /var/task build-python pip install -t python/lib/python3.6/site-packages selenium==3.141.0
```
### Deploy Layer
```bash
cd /path_to_sample/layer/
sls deploy
```
### Environment variables
| 変数名 | 備考 |
----|----
| ENV_KEY | 任意の文字列 |
- [`.env.example`](function/.env.example) を `.env` にリネームして定義する
- もしくは、下記のようにコマンドで定義する
```bash
#e.g. Use export command
export ENV_KEY=xxxx
```
- Deploy後は[Lambdaコンソール](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html)で環境変数を変更できる
### Deploy Function
```bash
cd /path_to_sample/function/
npm install
sls deploy
```
## Setup Local
```bash
cd /path_to_sample/test-local/
pipenv install --dev
```
### Environment variables
- [`.env.example`](test-local/.env.example) を `.env` にリネームして定義する
- もしくは、コマンドで定義する

## How to run
```bash
#AWS
cd /path_to_sample/function/
sls invoke -f crawler 

#Local
cd /path_to_sample/test-local/
pipenv run getdriver
pipenv run start
```
