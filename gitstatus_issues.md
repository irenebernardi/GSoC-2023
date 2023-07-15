**Problem:** `git status` shows random untracked files from random locations on computer. This occurs even in a freshly cloned repo. 

**Solution:** I had accidentally created a `.git` folder in a root directory. To find it: 

- 1. From /Users/ directory, I ran `find . -type d -name ".git"` 
- 2. found wrong path (`.git` folder on root directory) and ran `rm -rf /path/to/.git`



