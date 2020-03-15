git add .
git commit -m "%1%"
git push heroku_development dev:master
heroku logs --remote %branch% --tail