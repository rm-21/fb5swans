call cd /d %1
call fb-py\Scripts\activate.bat
call python binary_reader.py %2
pause