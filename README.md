# Smartbot

Using tensorflow and ntlk create a bot which answers to the users.
I trained the ML algorithm over intents iot achieve it.

## Install dependencies

If you don't want to use the [virtualenv](https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) or if you need
to install the dependencies
of the project, use the following command

```bash
pip install -r requirements.txt
```


## Start app

If you used a virtualenv just run the following command (make sure the virtualenv is at the root of the project and named *venv*)

```bash
# activate the virtual env
source venv/bin/activate
python src/main.py
```

You can also run 
```bash
chmod a+x run.sh
./run.sh
```

Otherwise you can just run if you don't want to use a virtualenv
```bash
python src/main.py
```