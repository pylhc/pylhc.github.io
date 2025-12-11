# Git

How to's concerning  `git` in general,  [`gitlab`][cern_gitlab], [`GitHub`][github] and CI.

## Github Commandline Access Quickstart

This section explains the basic steps to get started with GitHub.
Since HTTP access via password only has been disabled by GitHub for security reasons, it is necessary to activate a secure method.

This aims to be as short and concise as possible, for more extensive information, [see the GitHub security documentation][github_security]{target=_blank}.

### Setup SSH Access

An easy way to access GitHub securely is to use SSH.
This guides you through the basic steps, but [details can be found in the GitHub documentation][github_ssh].

#### Create SSH Key

For this, create an SSH key pair locally using the email address associated with your GitHub account:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

When asked for a location, it makes sense to give it an easily identifiable name, to remember what the key is for.
The file should be placed in `~/.ssh/`, unless you are on `afs`, in which case the `~/private/` directory should be used.

```text
~/.ssh/github_authenticate
```

!!! tip "Passphrase"
    You can optionally provide a passphrase for the key, which will make it more secure.
    This way, even if someone else gets a hold of the private key file, they will not be able to access it.
    On the downside, you will be asked to enter the passphrase every time you want to use the key.
    **It is recommended, to use a passphrase** but as it is just an extra layer of security, you can keep it short and simple.

This will create two files: `github_authenticate` and `github_authenticate.pub`.
The `.pub` is your public key that you can share with others,
while the other file is your private key and **should never be shared with anyone!**

!!! quote "Keep it secret, keep it safe!"
    _Gandalf_, about private SSH keys (probably).

#### Add the Public SSH Key to GitHub

After creating the key, you need to add it to your GitHub account.
Log into your GitHub account, click on your avatar and go to `Settings` &rarr; `SSH and GPG keys`.
Then click on [++"New SSH key"++{.green-gui-button}][github_new_ssh_key]{target=_blank} and paste the contents of the `.pub` file into the `Key` field.

Give it a reasonable name in the `Title` field (which it will appear as in the GitHub interface) and leave the `Key type` as `Authentication key`.
Then click on `Add SSH key` and you are done.

#### Configure SSH to use the key

Next, you need to tell your local SSH client to use the key you created to connect to GitHub.
For that, add the following lines to your `ssh` configuration file (typically at `~/.ssh/config` on UNIX systems):

```bash
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/github_authenticate
```

or use for the `IdentityFile` field the path you chose earlier for the ssh key file.

!!! warning "Username"
    It is important that the `User` is `git` and **not your git-username**!
    GitHub will identify you automatically based on the email address you used to create the SSH key.

#### Test Access

Now you can test that everything works by running the following command:

```bash
ssh -T github.com
```

which should then display

```text
Hi <Username>! You've successfully authenticated, but GitHub does not provide shell access.
```

#### Clone Repository

When you clone a new repository, always use the SSH url

```text
git clone git@github.com:pylhc/omc3.git
```

which you can find from the ++"Clone"++{.green-gui-button} button of the repository page on GitHub.


!!! tip "Changing a Repository URL"
    In case you already have a repository cloned with the wrong URL, you can change it with `git remote set-url`, e.g.:

    ```bash
    git remote set-url origin git@github.com:pylhc/omc3.git
    ```

    If you are not sure which url is currently set, you can always check it with

    ```bash
    git remote -v
    ```

### Setup HTTPS Access

You can setup https access by creating and using a personal access token or a password manager.

!!! note "Not yet documented"
    As we use SSH access, this section not yet written.
    Refer to the [GitHub documentation][github_https] for more information and maybe write up a quick howto.


## Configuring Gitlab CI to Automatically Pull into AFS

If you are programming locally, but also want to have a copy on AFS, either because your colleges are not comfortable with Gitlab or you need the code for other scripts that you are running on lxplus or similar, here is how:

### Create Service Account

!!! danger "Security Risk!"
    We will be creating a new account, so **you do not have to add the password of your main account to your Gitlab repository**: this would be a security risk!
    Admittedly, it is a low one if everything is done correctly, but just in case something goes wrong or leaks, you can just **delete this account**.
    Also, you can give this account **only the rights necessary** to write to AFS in the first place and do not risk that anyone can access other sensible information.

??? nodeco "1. Create a new service account, via the [CERN account management][new_account]{target=_blank .cern_login}, of length 8."
    You need at least 8 characters to mask that name in Gitlab (if you want to do so), but on the other hand, there is a warning, that AFS cannot handle names longer than 8.
    So exactly 8 seems to be the sweetspot.
    If you do not care about masking the name (it is not as important as masking the password, see below) you can go shorter.

??? nodeco "2. Set a password of length &GreaterEqual; 8 containing only `[a-zA-Z0-9+/@:]`."
    We want to hide the password later in gitlab, and this is only possible if its >= 8 characters long and only contains Base64 characters as well as `@:`.
    You can go as long as you want. Better make this 15 characters long at least.

3\. [Activate the AFS service][afs_services]{target=_blank .cern_login} for the newly created account.
{: style="margin: 0 0 0 0.1rem"}

### Setup AFS folder

_Steps to be done on AFS:_

??? nodeco "4. Clone your git into your AFS destination."
    It is important here to you use the right link to set this up, depending on whether you want your repository to be private or public.
    Go to your Gitlab repository page and click onto the <span style="color=#0033A0">blue clone button</span> on the right.
    If it is okay for your repo to be publicly accessible you can use the `HTTPS` url.
    If you want to set it up privately you will need to clone with the `KRB5` url, so Kerberos can be later used to authenticate your service account.
    ([See also below](#setup-git) for giving it rights to the repository.)

??? nodeco "5. Run: `find . -type d -exec fs sa {} ACCOUNTNAME rlidw \;`"
    Run **within** the repository or replace `.` with the repository name!<br>
    Replace `ACCOUNTNAME` with the name of your Service Account.
    This will give read/write access to this repository to the service account.
    Just giving these rights to the top-folder will not work, as it does not propagate to subfolders automatically.

    A possible other way would be to create an empty folder and give writing rights to that one to the service account and then login to lxplus with the service account and clone the repository directly with that account.
    The latter is a good test to see if everything worked correctly anyway.
    Do not forget, if you have set up the repository with Kerberos authentication, to adapt your `.ssh/config` to delegate the credentials.
    <br>Repeated for easy copying:
    ```bash
    find . -type d -exec fs sa {} ACCOUNTNAME rlidw \;
    ```

### Setup Git

_Steps to be done on your [Gitlab][cern_gitlab]{target=_blank} repository:_

??? nodeco "6. Give your service account access rights or set the repository to public."
    The former can be done under `Members`, the latter under `Settings` &rarr; `General` &rarr; `Visibility, project features, permissions`.
    If you set it up to be a private repository, you need to have cloned the repository with the `KRB5` url ([see above](#setup-afs-folder)).

??? nodeco "7. Add `SERVICE_ACCOUNT_USERNAME` and `SERVICE_ACCOUNT_PASSWORD` variables."
    This is done in `Settings` &rarr; `CI/CD` &rarr; `Variables`.
    Obviously the values of the variables will be the username and password of your [newly created service account](#create-service-account) respectively.
    These variables will be used in the next step in the YAML.
    For obvious reasons, **DO NOT WRITE THE PASSWORD IN CLEAR TEXT INTO THE YAML**.

!!! danger "Security Risk!"
    **MAKE SURE AT LEAST THE `SERVICE_ACCOUNT_PASSWORD` VARIABLE IS SET TO `Masked` !!!**

??? nodeco "8. Add a new stage to your `.gitlab-ci.yml` file, or create a new one."
    ```yaml
    stages:
    - afs_pull

    afs:
      stage: afs_pull
      image: gitlab-registry.cern.ch/linuxsupport/cc7-base
      before_script:
          - yum install -y openssh-clients
          - mkdir -p ~/.ssh
          - 'echo "lxplus ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDTA/5AzXgbkSapknIPDoEePTM1PzIBSiyDnpZihdDXKzm8UdXxCDJLUVjBwc1JfBjnaXPEeBKZDuozDss/m98m5qQu+s2Dks000V8cUFTU+BFotzRWX0jWSBpmzse0477b40X2XCPqX0Cqfx9yHdkuMlyF0kJRxXgsGTcwzwbmvqNHJdHHYJJz93hGpBhYMREcDN5VOxXz6Ack3X7xfF29xaC91oOAqq75O11LXF5Y4kAeN9kDG8o6Zsqk4c5at5aqWqzZfnnVtGjhkgU2Mt5aKwptaFMe0Z3ys/zZM4SnsE9NfompnnWsiKk2y09UvrbzuYPWLt43Fp3+IFqRJvBX" > ~/.ssh/known_hosts'
          - 'echo -e "Host *\n\tGSSAPIDelegateCredentials yes\n\tGSSAPITrustDNS yes\n\n" > ~/.ssh/config'
      script:
          - echo "${SERVICE_ACCOUNT_PASSWORD}" | kinit -f ${SERVICE_ACCOUNT_USERNAME}@CERN.CH
          - klist
          - ssh ${SERVICE_ACCOUNT_USERNAME}@lxplus "cd PATH_TO_YOUR_AFS && git checkout master && git pull"
      only:
          - master
    ```

    !!! info "Info"
        Replace `PATH_TO_YOUR_AFS` with the path to [your AFS folder](#setup-afs-folder).
        **Do NOT replace `SERVICE_ACCOUNT_USERNAME` and `SERVICE_ACCOUNT_PASSWORD`.**
        These will be inserted by gitlab's CI!.


    ??? note "More Info on the YAML"
        The `.yml` was copied and adapted from the [acc-models-lhc repository][acc_models_repo]{target=_blank} with some changes.
        In general, a Docker image is loaded, `openssh` is installed and a Kerberos token is created.
        With this token it is now possible to `ssh` to lxplus as the service account, go into the desired directory and checkout the repository.
        `git checkout master` is only performed in case someone changed the branch on AFS (which should not happen, do not touch).

        - **Image**: The image `gitlab-registry.cern.ch/linuxsupport/cc7-base` used is the default Cern Centos 7 docker image, provided by [Linux @ CERN][cern_linux]{target=_blank}.
        This is used, because it has Kerberos already set up and configured.
        The [acc-models yaml][acc_models_yml]{target=_blank} was using [their own docker image][acc_models_docker], of which the only additional functionality we need is `openssh`, hence it is installed manually instead.
        - **echo lxplus ssh-rsa** line: This line adds the public key of the lxplus server to the ssh `known_hosts` file, so it connects to lxplus without user interaction about this topic (do not touch).
        - **echo -e Host** line: Here the ssh `config` is adapted to use Kerberos as authentication method to any server (do not touch).
        - **only master**: Only the commits to `master` trigger the CI. Omit this part if you want the repo to be pulled on every commit, or change it to limit upon which commits this happens (as is done in the [acc-models yml][acc_models_yml]{target=_blank}).

### Done

Whenever you are pushing now any commits to the `master` branch, the CI/CD will automatically pull the latest commit into the AFS directory.

*[TN]: Technical Network
*[GPN]: General Purpose Network, the main CERN network
*[CBNG]: Common Build Next Generation
*[LSA]: LHC Software Architecture
*[AFS]: Andrew File System
*[CI]: Continuous Integration
*[CD]: Continuous Delivery
*[lxplus]: Linux Public Login User Service

[new_account]: https://account.cern.ch/account/Management/NewAccount.aspx
[afs_services]: https://resources.web.cern.ch/resources/Manage/AFS/Default.aspx
[github]: https://github.com/
[cern_gitlab]: https://gitlab.cern.ch/
[github_security]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure
[github_https]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github#https
[github_ssh]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh
[github_new_ssh_key]: https://github.com/settings/ssh/new