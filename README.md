instuctions for deploy:
-----------------------
git clone git@github.com:kkashicyn/parse.git
cd parse
rm -rf env
python3 -m venv env
source env/bin/activate
pip3 install -r req.txt
gunicorn -w=4 app:app -b 127.0.0.1:80