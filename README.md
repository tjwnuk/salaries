# Salaries of Polish software developers
Salaries of Polish developers. Project aiming to process and analize salaries of Polish software engineers, based on their claims found on 4programmers.net forum thread.
The project is utilising Python, Docker, Scrapy, Pandas and Jupyter Notebook.

## Opis po polsku
Wynagrodzenia polskich deweloperów. Projekt mający na celu zebranie i przeanalizowanie danych dotyczących deklarowanych wynagrodzeń polskich programistów.
Dane zostały pozyskane z forum strony 4programmers.net:

[https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie?page=1](https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie?page=1)

Projekt wykorzystuje technologie Python, Docker, Scrapy, Pandas i Jupyter Notebook.

## Aim of the project
The project takes the data contained in the following thread:

[https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie?page=1](https://4programmers.net/Forum/Kariera/233131-ile_zarabiacie?page=1)

The devs were posting their earnings, stack and experience in the thread, the project aims to:
1. Scrape this data
2. Statistically analyze it, for example:
    1. Compute mean, dominant and median of it
    2. Make some graphs

## Notes

Remember to
```bash
chmod +x start.sh
chmod +x wait-for-it.sh
```
in host system

### Conda venv
Create conda venv and install required packages
```bash
conda init
conda create -p ./conda-venv

#this one prevents conda from activate on startup
conda config --set auto_activate_base false
conda activate conda-venv

pip install jupyter-notebook
pip install pandas
pip install matplotlib
```
conda-venv directory added to gitignore

when running
```bash
cd salaries
conda activate conda-venv
```

when stopping
```bash
conda deactivate
```

## Author and license

Copyright 2023 Tomasz Wnuk

This code is for educational purposes only. Please do not modify or redistribute it.

Contact: tjwnuk@proton.me

https://github.com/tjwnuk

https://www.linkedin.com/in/tjwnuk/