# Zé lootinho

The project idea is to (try to) make a bot to keep track of prices on main hardware stores in Brazil.

It will search the pages, obtaining data such as names, prices and availability and thus build a database so that we can track price changes and keep up to date.

## Running the project

First download the chrome driver needed to selenium run. [Download page](https://chromedriver.chromium.org/downloads).

then extract the zip file and put the `chromedriver` file inside the `src/drivers` folder.

Next, insided the project root dir, create a virtual environment with

```
$ python3 -m venv env
```

and activate it with

```
$ source env/bin/activate
```

and install the dependencies with:
```
pip install -r requirements.txt
```
