# About Bash projects

Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

## Concepts
*For this project, we expect you to look at this concept:*

- [Struggling with the sandbox? Try this: Using Docker & WSL on your local host](https://intranet.alxswe.com/concepts/100039)

# Resources

**Read or watch:**
- [Permissions](https://linuxcommand.org/lc3_lts0090.php)

## man or help:
- `chmod`
- `sudo`
- `su`
- `chown`
- `chgrp`
- `id`
- `groups`
- `whoami`
- `adduser`
- `useradd`
- `addgroup`

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), ***without the help of Google:**

## Permissions
- What do the commands `chmod`, `sudo`, `su`, `chown`, `chgrp` do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can’t a normal user `chown` a file
- How to run a command with root privileges
- How to change user ID or become superuser

## Other Man Pages
- How to create a user
- How to create a group
- How to print real and effective user and group IDs
- How to print the groups a user is in
- How to print the effective userid

# Requirements

## General
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
- All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
- The first line of all your files should be exactly `#!/bin/bash`
- A `README.md` file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use backticks, `&&`, `||` or `;`
- All your files must be executable

## Quiz questions

Question #0
Which command should I use for changing a file permission?


chgrp


su


chmod


chown

Question #1
What is the permission value for a file read only for the group owner?


070


040


050


060

Question #2
Which command should I use for changing a file owner?


chgrp


su


chmod


chown

Question #3
What is the permission value for a file without any restriction?


600


644


777

Question #4
What is the numerical value for the rwx------ permission?


700


600


621


704

Question #5
What is the numerical value for the ----w---x permission?


021


123


121


221

### Question #6

What is the numerical value for the r-xr--r-- permission?

- [ ] 411

- [ ] 522

- [ ] 544

- [ ] 644

## Tasks

### 0. My name is Betty

Create a script that switches the current user to the user betty.

- You should use exactly 8 characters for your command (+1 character for the new line)
- You can assume that the user `betty` will exist when we will run your script

```bash
julien@ubuntu:/tmp/h$ tail -1 0-iam_betty | wc -c
9
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `0-iam_betty`

### 1. Who am I

Write a script that prints the effective username of the current user.

```
julien@ubuntu:/tmp/h$ ./1-who_am_i
julien
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `1-who_am_i`

### 2. Groups

Write a script that prints all the groups the current user is part of.

```
julien@ubuntu:/tmp/h$ ./2-groups
julien adm cdrom sudo dip plugdev lpadmin sambashare
julien@ubuntu:/tmp/h$
```

Note: depending on the user, you will get a different output.

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `2-groups`

### 3. New owner

Write a script that changes the owner of the file `hello` to the user `betty`.

```
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 julien julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$ sudo ./3-new_owner
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 betty  julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `3-new_owner`

### 4. Empty!

Write a script that creates an empty file called `hello`.

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `4-empty`

### 5. Execute

Write a script that adds execute permission to the owner of the file `hello`.

The file `hello` will be in the working directory

```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./hello
bash: ./hello: Permission denied
julien@ubuntu:/tmp/h$ ./5-execute
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rwxrw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `5-execute`

### 6. Multiple permissions

Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.

- The file `hello` will be in the working directory

```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r--r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./6-multiple_permissions
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r-xr-xr-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `6-multiple_permissions`

### 7. Everybody!

Write a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`

- The file `hello` will be in the working directory
- You are not allowed to use commas for this script

```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rw-r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./7-everybody
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `7-everybody`

### 8. James Bond

Write a script that sets the permission to the file `hello` as follows:

- Owner: no permission at all
- Group: no permission at all
- Other users: all the permissions

The file `hello` will be in the working directory You are not allowed to use commas for this script

```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./8-James_Bond
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-------rwx 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `8-James_Bond`

### 9. John Doe

Write a script that sets the mode of the file `hello` to this:

```
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
```

- The file `hello` will be in the working directory
- You are not allowed to use commas for this script

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `9-John_Doe`

### 10. Look in the mirror

Write a script that sets the mode of the file `hello` the same as `olleh`’s mode.

- The file `hello` will be in the working directory
- The file `olleh` will be in the working directory

```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ ./10-mirror_permissions
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$
```

Note: the mode of `olleh` will not always be 664. Make sure your script works for any mode.

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `10-mirror_permissions`

### 11. Directories

Create a script that adds execute permission to all subdirectories of the **current directory** for the owner, the group owner and all other users.

Regular files should not be changed.

```
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx------ 2 julien julien 4096 Sep 20 14:49 dir0
drwx------ 2 julien julien 4096 Sep 20 14:49 dir1
drwx------ 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./11-directories_permissions
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `11-directories_permissions`

### 12. More directories

Create a script that creates a directory called `my_dir` with permissions 751 in the working directory.

```
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./12-directory_permission s
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `12-directory_permissions`

### 13. Change group

Write a script that changes the group owner to `school` for the file `hello`

- The file `hello` will be in the working directory

```
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   34 Sep 20 15:03 13-change_group
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./13-change_group
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      34 Sep 20 15:03 13-change_group
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien    4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien school   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `13-change_group`

### 14. Owner and group

Write a script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.

```
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   36 Sep 20 15:06 100-change_owner_and_group
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./100-change_owner_and_group
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 vincent staff   36 Sep 20 15:06 100-change_owner_and_group
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir0
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir1
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir2
drwxr-x--x 2 vincent staff 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 vincent staff   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `100-change_owner_and_group`

### 15. Symbolic links

Write a script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively.

- The file `_hello` is in the working directory
- The file `_hello` is a symbolic link

```
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
lrwxrwxrwx 1 julien julien    5 Sep 20 15:10 _hello -> hello
julien@ubuntu:/tmp/h$ sudo ./101-symbolic_link_permissions
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien      23 Sep 20 14:25 hello
lrwxrwxrwx 1 vincent  staff    5 Sep 20 15:10 _hello -> hello
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `101-symbolic_link_permissions`

### 16. If only

Write a script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.

- The file `hello` will be in the working directory

```
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien    julien      47 Sep 20 15:18 102-if_only
-rw-rw-r-- 1 guillaume julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./102-if_only
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      47 Sep 20 15:18 102-if_only
-rw-rw-r-- 1 betty  julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `102-if_only`

### 17. Star Wars

Write a script that will play the StarWars IV episode in the terminal.

**Repo:**
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: `103-Star_Wars`
