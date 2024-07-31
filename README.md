Three types of files have been found whose execution does not block the WhatsApp client:

.PYZ (Python ZIP application),
.PYZW (PyInstaller program),
.EVTX (Windows event log file). 

BleepingComputer tests confirmed that WhatsApp does not block the execution of Python files and found that the same is true for PHP scripts.

https://www.bleepingcomputer.com/news/security/whatsapp-for-windows-lets-python-php-scripts-execute-with-no-warning/

1. Create file reverse_shell.py
2. Create file __main__.py
3. "Compile" them with "python -m zipapp -o reverse_shell.pyzw ."
   
