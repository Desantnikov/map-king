git add .
git commit -m "%1%"
git push heroku_development development:master
heroku logs --remote %branch% --tail