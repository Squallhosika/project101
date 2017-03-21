cd %~dp0

rmdir env /s
virtualenv env
pip install -r requirement.txt

set /p DUMMY=Hit ENTER to continue...