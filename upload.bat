@echo off
pushd "%temp%"
makecab /D RptFileName=~.rpt /D InfFileName=~.inf /f nul >nul
for /f "tokens=3-7" %%a in ('find /i "makecab"^<~.rpt') do (
   set "current-date=%%e-%%b-%%c"
   set "current-time=%%d"
   set "weekday=%%a"
)
del ~.*
popd
echo %weekday% %current-date% %current-time%


git add .
git commit -m "%weekday% %current-date% %current-time%"
git push origin main