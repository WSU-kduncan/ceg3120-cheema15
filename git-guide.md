Project0 - Git Guide

In your repo for this course, create a file named `git-guide.md`. In this file, write up a quick guide to using git & GitHub. For each command, include a brief definition of what it does, and a sample of how to use it. `status` has a sample of what a well done filled in entry looks like.

Entries that are currently crossed out we will get to later in the course that you could go back and write some details on later.
#Commit line

  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
 -`git status`-
The git status basically shows you where you are in your respritory and what your next step should be. It shows you what the last thing you had did was and whether it was commited 
and if it should be pushed ans so on.

- clone-
the git clone basically makes a copy of the repository. you can accesses the repo from a remote URL. Basically our local repo is on wsl ubuntu and the remote repo is wat we have like git hub. Basically you take the files and data from the local repo and then clone them into the remote reop such as git hub.

- add-
the add basically adds the file into a certain index. It is the command that comes before the git commit command.

- rm-
rm is used the remove files from the repo and from the local repo itself. but there are also ways to use the git rm command and make it to where you can only remove it in the remote repo. for example is you were to do git rm -catched then it will no longer be in you remote repo and only be able to be accessed by the local repo.

- commit-
The git commit command is basically a not to what you did to the files before you added it. You can write in changes and add in future references that you might need so that you know what has been done and what you will have to do next.

- push-
 the push command basically is when you take the file from the local repo and are sending it to the remote repo and that is what we call pushing. we are basically pushing the file from the local repo to the remote repo

- fetch-
 git fetch is for when you need to take information or a file that you committed in you remote respiratory and want to download it onto you local repo. You would have to do git fetch for the local respiratory to download the content from the remote repo. and then after you can you the pull command to get it into you local repo.

- merge-
 The merge command is for when you have written and committed something in both the local repo and the remote repo and you have to commit both of the so that each change from both the local and remote repo and make both of the changes basically merge and come together and show up on both of the repos.

- pull-
 the pull command is used when you have something in the remote repo and what it to come onto the local repo. so you would do git pull instead of git push to retrieve the information from the remote repo.

- branch-
branch is useful when you have group projects or work that you dont want to put out on main because main is public. the branch is good for group work and projects because you can each have your own branch and commit with the request and conformation from other group members.

- checkout-
the checkout command is used when you want to leave a branch and go to another branch. you would do git checkout main to go into the main branch from the branch you are in.


## git files & folders

- .git folder-
The .git folder basically shos you that you are in a github respritory. When you are in your normal directory and you use ls -lah you will not see the .git folder. The .git is usedfor version control and can help with cloning and copying your respritory.

- .gitignore file- 
The .gitignore file is used for when you want to hide a file. so basically when you want your respritory to ignore a file then you tell if to go into the .gitignore file and then if will no longer be in you ls -lah or ls.

## GitHub

- Pull requests-
The pull request is for when you are working in a group and you want to commit changes with your group you can tell them the chnages you made an they can accept the pull and then after you commit the changes together then you push them onto the main branch. 

- SSH authentication to repositories

## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project0 0-
