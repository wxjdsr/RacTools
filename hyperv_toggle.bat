@REM This file toggles the hypervisorlaunchtype between auto and off
@REM I use this to switch between Docker and simulator games like Ubuntu and Kirara Fantasia

@ECHO OFF

@REM Run as admin
pushd "%CD%"
CD /D "%~dp0"
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

FOR /F "tokens=2" %%a IN ('BCDEDIT /enum ^| FIND /i "hypervisorlaunchtype"') DO SET CURRENT_LAUNCHTYPE=%%a
ECHO Welcome! Hypervisor Launch Type is set to [%CURRENT_LAUNCHTYPE%] at the moment.

ECHO.
CHOICE /C 12 /M "Choose Hypervisor Launch Type: Auto[1](Docker) or Off[2](Kirara, Ubuntu)?" /N
IF ERRORLEVEL 1 SET LAUNCHTYPE=Auto
IF ERRORLEVEL 2 SET LAUNCHTYPE=Off
IF "%CURRENT_LAUNCHTYPE%" == "%LAUNCHTYPE%" GOTO unchanged

ECHO.
ECHO Setting Hypervisor Launch Type to [%LAUNCHTYPE%]
BCDEDIT /set hypervisorlaunchtype %LAUNCHTYPE%

ECHO.
ECHO Note: Changed Hypervisor Launch Type Settings only take effect after a restart!
CHOICE /C YN /M "Reboot the computer [Y/N]?" /N
IF ERRORLEVEL 2 GOTO end
IF ERRORLEVEL 1 GOTO reboot


:reboot
SHUTDOWN /r /t 0
GOTO end

:unchanged
ECHO Hypervisor Launch Type will remain unchanged [%LAUNCHTYPE%], no need to reboot.
GOTO end

:end
ECHO.
ECHO Have a nice day!
ECHO.
pause

SET LAUNCHTYPE=
SET CURRENT_LAUNCHTYPE=