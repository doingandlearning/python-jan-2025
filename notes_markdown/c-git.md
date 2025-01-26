# Plan for Session
- Git Introduction
- Single Project Repository
- Git Source Code Control
- Git Change Flow
- File States in Git
- Git Tools
- Command Line Git
- Adding Files in Git
- Working with a Remote Repository
- GitHub
- Branching & Pull Requests

---

## Git Introduction
- Git is a Source Code Configuration Management system (SCCM or SCM system).
- A shared repository of code to allow teams to work on the codebase of a project.
- Tracks software changes so that those changes can be undone if necessary.
- Tags releases to know exactly what code made it into a release, useful when different versions are needed for different clients.

---

## Remote Server
- Develop code locally and store it centrally.

---

## Git Source Code Control
- **Remote Repository**: The central repository that holds the code.
- **Local Repository**: A copy of the repository on the local machine.
- **Working Directory**: The directory where you make changes.
- **Staging (index)**: The area where changes are staged before committing.
- **Git Commands**:
  - `git clone` to copy the remote repository.
  - `git add` to add changes to the index/staging area.
  - `git commit` to save changes in the local repository.
  - `git push` to update the remote repository.
  - `git pull` to retrieve changes from the remote repository.

---

## Git Change Flow
- The flow of changes in Git:
  1. **Working Directory**: Where changes are made.
  2. **Staging Area**: Changes are added to the staging area using `git add`.
  3. **Local Repository**: Changes are committed to the local repository using `git commit`.
  4. **Remote Repository**: Changes are pushed to the remote repository using `git push`.

---

## File States in Git
- Files can be in one of four states:
  1. **Untracked**: The file is not tracked by Git.
  2. **Staged**: The file is included in the list of changes to be committed.
  3. **Tracked**: The file has been staged and then committed, and Git tracks changes to this file.
  4. **Modified**: The file has changed but not yet been staged.

---

## Git Tools
- **Command Line Tools**: Basic command line interface for Git.
- **GitHub**: Web-based interface to Git repositories, supports Pull Requests (PRs) and other workflow options, reviews, diff tools, etc.
- **IDEs Git Plugins/Support**: Git support in PyCharm, Visual Studio Code, etc.

---

## Command Line Git
- Available for Mac, Windows, and Linux.
- Can be used to create a new project or clone an existing repository.
- Example commands:
  - `git init` to initialize a new Git project.
  - `git clone <repo-url>` to clone an existing repository.

---

## Adding Files in Git
- Need to stage changes using `git add`, which adds them to the list of changed files.
- Commit inserts the staged changes into the local repository using `git commit`.

### Example:
```bash
$ git add <filename>
$ git commit -m "Commit message"
```

---

## Working with a Remote Repository
- Use the `git push` command to update the remote repository.
- May need to specify the branch, e.g., `git push main`.

### Example:
```bash
$ git push
```

---

## GitHub Interface
- Can use the web interface to see comments, commits, and get clone URL information.

---

## Branching
- Typically do development in a branch, then merge your changes back into the master/main branch, typically via a Pull Request (PR).
- Another developer reviews and then pulls the changes into the main branch.
- Create a branch using `git checkout -b <branch-name>`.

### Example:
```bash
$ git branch
$ git checkout -b <branch-name>
```

---

## Branching & Pull Requests
- Creating a PR is used to request changes are merged from a branch to the main or dev branch.
- Another developer reviews and then pulls the changes into another branch.

---

## Git Terminology Quick Reference
- **HEAD**: Symbolic reference to the latest version of the current branch.
- **Branch**: Reference to a specific state of files in the working directory.
- **Staging Area**: Stores changes before they are committed (a change list), also called the index.
- **Add**: Add changes to the staging area.
- **Commit**: Apply changes to the local repository.
- **Origin**: The default upstream (remote) repository.
- **Push**: Send changes from the local to the remote repository.
- **Pull**: Retrieve changes from a remote repository and apply them to the local repository.
- **Pull Request**: Request to merge two branches following review and approval process.

---

## Useful References
- **Git Home Page**: [http://git-scm.com](http://git-scm.com)
- **Git Glossary**: [https://www.kernel.org/pub/software/scm/git/docs/gitglossary.html](https://www.kernel.org/pub/software/scm/git/docs/gitglossary.html)
- **10 Git Commands Every Developer Should Know**: [https://www.freecodecamp.org/news/10-important-git-commands-that-every-developer-should-know](https://www.freecodecamp.org/news/10-important-git-commands-that-every-developer-should-know)

---

## Questions?

?
