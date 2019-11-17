SET message=%2
IF %1==master (SET branch=heroku) ELSE (SET branch=dev)
IF [%message%] == [] (SET message=default) ELSE (SET message=%message%)

git add .
git commit --amend -m "%message%"
git push %branch% master -f
heroku logs --remote %branch% --tail