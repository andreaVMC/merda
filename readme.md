# Merda.
Se avete bisogno di supporto chiedete a Matte (Kev non sa neanche da che parte è girato).

### Come eseguire
1. Clonare repo - comando: ```git clone https://github.com/kev1nl1u/merda/new/main```
2. Attivare virtual environment (venv) - comando ```. bin/activate```
3. Installare i pacchetti richiesti - comando: ```pip install -r requirements.txt``` (Att.ne: eseguire questo comando solo nel venv)
4. Configurare database PSQL: utilizzare ```db.sql``` per creare e configurare il database ed ```example_data.sql``` per inserire dei dati di test (vi è anche un accont di test ___stalin@urss.it___)
5. Modificare la classe Config nel file config.py in modo che sia possibile collegarsi al db che avete in locale
6. Eseguire il server - comando: ```flask run``` (Att.ne: eseguire questo comando solo nel venv)







