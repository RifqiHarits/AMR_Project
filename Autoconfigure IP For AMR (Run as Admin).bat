@echo off
cls
:start
ECHO.
ECHO 1. Change IP to 192.168.1.200 and gateway to 192.168.1.254
ECHO 2. Change IP to 192.168.1.201 and gateway to 192.168.1.254
ECHO 3. Change IP to 192.168.1.202 and gateway to 192.168.1.254
ECHO 4. Change IP to 192.168.1.X and gateway to 192.168.1.254
ECHO 5. Change to default DHCP
ECHO 6. Exit
set choice=
set /p choice= Choice: 
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='1' goto con1
if '%choice%'=='2' goto con2
if '%choice%'=='3' goto con3
if '%choice%'=='4' goto con4
if '%choice%'=='5' goto autosearch
if '%choice%'=='6' goto end
ECHO "%choice%" is not valid, try again
ECHO.
goto start
:con1
ECHO Setting IP Address to 192.168.1.200 and Gateway to 192.168.1.254
netsh interface ip set address "Wi-Fi" static 192.168.1.200 255.255.255.0 192.168.1.254
netsh interface ip set dns "Wi-Fi" static 208.67.222.222
netsh interface ip add dns "Wi-Fi" 208.67.220.220
goto end

:con2
ECHO Setting IP Address to 192.168.1.201 and Gateway to 192.168.1.254
netsh interface ip set address "Wi-Fi" static 192.168.1.201 255.255.255.0 192.168.1.254
netsh interface ip set dns "Wi-Fi" static 208.67.222.222
netsh interface ip add dns "Wi-Fi" 208.67.220.220
goto end

:con3
ECHO Setting IP Address to 192.168.1.202 and Gateway to 192.168.1.254
netsh interface ip set address "Wi-Fi" static 192.168.1.202 255.255.255.0 192.168.1.254
netsh interface ip set dns "Wi-Fi" static 208.67.222.222
netsh interface ip add dns "Wi-Fi" 208.67.220.220
goto end

:con4
set /p hostbitval= Set host bit to:
SET customip=192.168.1.%hostbitval%
ECHO Setting IP Address to %customip% and Gateway to 192.168.1.254
netsh interface ip set address "Wi-Fi" static %customip% 255.255.255.0 192.168.1.254
netsh interface ip set dns "Wi-Fi" static 208.67.222.222
netsh interface ip add dns "Wi-Fi" 208.67.220.220
goto end

:autosearch
ECHO Change to DHCP Connection
netsh interface ip set address "Wi-Fi" dhcp
ECHO -- Renewing IP --
ipconfig /renew "Wi-Fi"
goto end

:bye
goto end

:end
pause