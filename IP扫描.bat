@echo off
set a=1
:start
echo %a%
@echo off
ping 192.168.65.%a% -w 1 -n 1 >nul
if %errorlevel%==0 (echo 192.168.65.0%a%>>IP.txt ) else (echo 192.168.65.%a% fail)
rem:if %c%==0 (echo 192.168.73.%a% >>IP.txt)
set /a a=%a%+1
if %a%==48 exit
goto :start 