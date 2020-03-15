
IF %1==master (SET branch=heroku) ELSE (SET branch=dev)
SET message=%2
IF [%message%] == [] (SET message=default) ELSE (SET message=%message%)
IF %~3 == amend (SET key=-f)

git add .
git commit --amend -m "%message%"
git push %branch% master %3
heroku logs --remote %branch% --tail