@echo off 
 
:: BatchGotAdmin 
:------------------------------------- 
REM --> Check for permissions 
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system" 
 
REM --> If error flag set, we do not have admin. 
if '%errorlevel%' NEQ '0' ( 
 echo Requesting administrative privileges... 
 goto UACPrompt 
) else ( goto gotAdmin ) 
 
:UACPrompt 
 echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs" 
 echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs" 
 
 "%temp%\getadmin.vbs" 
 exit /B 
 
:gotAdmin 
 if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" ) 
 pushd "%CD%" 
 CD /D "%~dp0" 
:-------------------------------------- 
 
cls
@ECHO OFF
title 启用或禁用本地连接
CLS
color 0a
GOTO MENU
:MENU
ECHO.
ECHO. ==============启用禁用本地连接==============
ECHO.
ECHO. 1 禁用以太网
ECHO. 2 启用以太网
ECHO. 3 禁用虚拟机
ECHO. 4 启用虚拟机
ECHO. 5 禁用WLAN
ECHO. 6 启用WLAN
ECHO. 10 退 出
ECHO. ==========================================
ECHO.
ECHO.
echo. 请输入选择项目的序号：
set /p ID=
if "%id%"=="1" goto stopEth
if "%id%"=="2" goto startEth
if "%id%"=="3" goto stopVM
if "%id%"=="4" goto startVM
if "%id%"=="5" goto stopWlan
if "%id%"=="6" goto startWlan
if "%id%"=="10" exit
PAUSE
:stopEth
echo 禁用以太网
netsh interface set interface name="以太网" admin=DISABLED
goto MENU
:startEth
echo 启用以太网
netsh interface set interface name="以太网" admin=ENABLED
GOTO MENU
:stopVM
echo 禁用虚拟机
netsh interface set interface name="VMware Network Adapter VMnet1" admin=DISABLED
netsh interface set interface name="VMware Network Adapter VMnet8" admin=DISABLED
goto MENU
:startVM
echo 启用虚拟机
netsh interface set interface name="VMware Network Adapter VMnet1" admin=ENABLED
netsh interface set interface name="VMware Network Adapter VMnet8" admin=ENABLED
GOTO MENU
:stopWlan
echo 禁用WLAN
netsh interface set interface name="WLAN" admin=DISABLED
goto MENU
:startWlan
echo 启用WLAN
netsh interface set interface name="WLAN" admin=ENABLED
GOTO MENU