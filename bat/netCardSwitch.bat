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
title ���û���ñ�������
CLS
color 0a
GOTO MENU
:MENU
ECHO.
ECHO. ==============���ý��ñ�������==============
ECHO.
ECHO. 1 ������̫��
ECHO. 2 ������̫��
ECHO. 3 ���������
ECHO. 4 ���������
ECHO. 5 ����WLAN
ECHO. 6 ����WLAN
ECHO. 10 �� ��
ECHO. ==========================================
ECHO.
ECHO.
echo. ������ѡ����Ŀ����ţ�
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
echo ������̫��
netsh interface set interface name="��̫��" admin=DISABLED
goto MENU
:startEth
echo ������̫��
netsh interface set interface name="��̫��" admin=ENABLED
GOTO MENU
:stopVM
echo ���������
netsh interface set interface name="VMware Network Adapter VMnet1" admin=DISABLED
netsh interface set interface name="VMware Network Adapter VMnet8" admin=DISABLED
goto MENU
:startVM
echo ���������
netsh interface set interface name="VMware Network Adapter VMnet1" admin=ENABLED
netsh interface set interface name="VMware Network Adapter VMnet8" admin=ENABLED
GOTO MENU
:stopWlan
echo ����WLAN
netsh interface set interface name="WLAN" admin=DISABLED
goto MENU
:startWlan
echo ����WLAN
netsh interface set interface name="WLAN" admin=ENABLED
GOTO MENU