Here is the content from the Word document "Lab 4: Working with Git" converted into Markdown format:

```markdown
# Lab 4: Working with Git

The aim of this lab is to give you a chance to work with Git and GitHub.

## Step 1: Git Client

In this first step, we will confirm that you have the Git command available.

To do this, open a Command Window on a Windows PC or a Terminal on a Mac or Linux machine. Once you have done this, enter the following command at the prompt:

```bash
git --version
```

If you have the Git client installed, you should see the version number of the Git client displayed. For example:

```
git version 2.2.5.0
```

In this case, the version of Git installed is version 2.2.5.0 for Windows but version 2.31.0 on the Mac.

If you do not have the Git client installed, you will be told that the command cannot be found. In this case, you need to install the Git client.

You can do this by going to the following website and downloading the correct version for your operating system:

[https://git-scm.com/downloads](https://git-scm.com/downloads)

## Step 2: Create a Directory to Work In

We will handle working with our labs using a specific directory. If you have not already done so, create a directory for coursework called something like `coursework`. On a Mac, you might put this under `/Users/<username>`, and on a Windows PC, this might be in `c:\Users\<username>`.

For example:

```bash
mkdir coursework
```

Now, change the directory into this newly created directory:

```bash
cd coursework
```

## Step 3: Git Clone a Repository

We will now clone an existing Git project from a GitHub hosted repository. Remember that to work with an existing repository in Git, you need to obtain a clone (copy) of that repository or project locally. This will copy the report project locally to your machine and allow you to make changes to that project.

To do this, issue the `git clone` command from within a Terminal or Command Window with an appropriate Git project web URL.

Return to your Terminal / Command Window and ensure that you have moved into the `coursework` directory:

```bash
pwd
```

This will tell you which directory you are currently in. If you are not inside `coursework`, then move into it:

```bash
cd coursework
```

Next, issue the `git clone` command as follows:

```bash
git clone https://github.com/johnehunt/playarea.git
```

This will clone a copy of the `playarea` project from the `johnehunt` GitHub repository to your machine.

If you now list the contents of the `coursework` directory, you will find that it now contains a subdirectory called `playarea`:

```bash
ls
```

You should now change the directory into the `playarea` directory:

```bash
cd playarea
```

If you list the contents of `playarea`, you will find it contains two files: a `README.md` file and a text file (`jjh-readme.txt`). Note that `.md` indicates that this is a Markdown format file and is used on the GitHub site to provide information about the repository.

## Step 4: Git History

We can now find out the commit history of one file in the `playarea`. To do this, return to your command window/terminal.

Now issue the following Git command:

```bash
git log jjh-readme.txt
```

For example:

```bash
git log jjh-readme.txt
```

Now try some of these commands to see the various types of log information available:

```bash
git show HEAD
```

This will show the current HEAD version of the file; the HEAD represents the current latest version.

And finally:

```bash
git blame jjh-readme.txt
```

In this last case, the output will be:

```
<output showing each line of the file with details of the last commit that modified it>
```

The `git blame` command is used to examine the contents of a file and see when each line was last modified and who the author of the modifications was.

## Step 5: Create a Branch

When working with Git, it is usual to work in a development branch. That is, all changes are made to a branch, and then this branch can be merged back into the main master branch via a Pull Request (or PR). This process is illustrated below:

<image-placeholder>

In the next few steps, we will work through this process.

The first thing we will do is create a new branch to work in. You can use the following commands to create a branch and switch into that branch:

```bash
git branch <new-branch-name>
git checkout <new-branch-name>
```

There is a shorthand form for this which is:

```bash
git checkout -b <new-branch-name>
```

This creates the new branch and switches to that branch.

Any changes you now make are applied to the branch you created.

We will now create a branch; name the branch after yourself. For example, if you are John Reginald Smith, then call your branch `jrsbranch`.

```bash
git checkout -b jrsbranch
```

The current branch is now the development branch you just created.

You can obtain a list of all branches using the command:

```bash
git branch
```

For example:

```bash
git branch
```

## Step 6: Adding a File

We will now create a file and add it to the current branch. The steps we will follow are illustrated below:

<image-placeholder>

First, create a file in your branch, again named after yourself, for example, `jrs-readme.txt`, within the `playarea` directory. You can do this in any way you wish.

Once you have created the file, use the Git command to see the status of your branch:

```bash
git status
```

For example:

```bash
git status
```

From this, you can see that there is one new file, but it is currently not being tracked by Git (i.e., Git knows nothing about it).

We will now add the file to the branch. To do this, use the `git add` command:

```bash
git add <filename>
```

For example:

```bash
git add jrs-readme.txt
```

Once you have done this, re-run the `git status` command. You should now see:

```bash
git status
```

Notice that Git now knows about the new file, but the changes have not yet been committed (added to the branch).

## Step 7: Commit Changes

Next, we will commit the changes we have just made to the branch. To do this, use the `git commit` command. This command needs a description for the commit you are making; we can provide this using the `-m` option. For example:

```bash
git commit -m "Added jrs-readme.txt"
```

Now use `git status` to see what the status is:

```bash
git status
```

## Step 8: Switching Branches

Next, we will see the effect of switching between the master branch and the branch you have been working in.

From the command window/Terminal, enter the command:

```bash
git checkout master
```

This will switch the current branch back to the master branch.

```bash
git checkout master
```

Now look at the contents of your directory. Can you see the file you created?

It’s not there; why not?

Because it is not part of the master branch.

Next, issue the `git status` command; what do you see?

```bash
git status
```

Finally, switch back to the branch you were working in. For example:

```bash
git checkout jrsbranch
```

(Remember to replace `jrsbranch` with whatever you called your own branch).

Now look at the contents of your directory; what is the difference?

Your file is back again because it is part of this branch.

## Step 9: Push Changes

All the changes we have made so far have been limited to your local machine. If you go to the online GitHub repository that is centrally hosting this project, you will see that none of your branches are available there.

For example:

Go to the URL [https://github.com/johnehunt/playarea](https://github.com/johnehunt/playarea).

Next, select the ‘Branch: master’ drop-down button to see the list of branches available. Initially, it looks something like this:

<image-placeholder>

Your own branch is not listed.

We will now push your branch to the GitHub repository. As this is the first time we have done this, and the remote Git repository does not know anything about our repository, we need to use an extended form of the `git push` command:

```bash
git push --set-upstream origin jrsbranch
```

To do this, you will need a GitHub account (if you do not have one, you will need to create one). You can create an account for free by going to:

[https://github.com/](https://github.com/)

Once you have done this, you can push a file to the `playarea` project within the `johnehunt` repository using the `git push` command:

```bash
git push --set-upstream origin jrsbranch
```

For example:

```bash
git push --set-upstream origin jrsbranch
```

To see any other changes made to this project, you can