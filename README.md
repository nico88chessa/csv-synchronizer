# csv-synchronizer

Si consiglia di usare un ambiente virtuale per python come venv.
Pacchetti da installare nell'ambiente virtuale:
<ol>
<li>pip install pyside2 (versione utilizzata: 5.13.1)</li>
<li>pip install paramiko (versione utilizzata: 2.6.0)</li>
<li>pip install watchdog (versione utilizzata: 0.9.0)</li>
<li>pip install PyInstaller (versione utilizzata: 3.5)</li>
</ol>

Comandi utili:
generazione .py da file .qrc
<tt>.\pyside2-rcc.exe C:\Users\nicola\workspace\csv-synchronizer\resources.qrc -o C:\Users\nicola\workspace\csv-synchronizer\resources.py</tt>

generazione eseguibile
1. andare nella cartella venv\Scripts
2. eseguire il comando:
<tt>.\pyinstaller.exe ..\..\main.py --distpath ..\..\dist</tt>
