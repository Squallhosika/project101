cd %~dp0

rmdir env /s
virtualenv env
env\Scripts\pip install -r requirement.txt

set /p DUMMY=Hit ENTER to continue...