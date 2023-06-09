# javan-test-api



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/muhammadali07/javan-test-api.git
git branch -M main
git push -uf origin main
```

## How to running the Restful API 

```
- cd existing_repo
- running using command : docker compose up -d --build
- waiting until the build of application is done
- open the application client database like (dbeaver), and create a new connection and setup the configuration database using postgreSQL. the required of database hase seen in sample.env file.
```

## How to access 

```
- open the browser, and access in url : http://localhost:8888/api/docs
- and RestAPI ready to test
```

