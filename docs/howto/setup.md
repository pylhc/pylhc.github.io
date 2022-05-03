# Useful Setup How-To's

## Mounting TN Resources on GPN and Other Machines

To be able to run the GUI or CBNG seamlessly from computers which are not in the technical network, it might be useful to mount `/user`, `/nfs` and `/eos` via `sshfs` using the following recipe:

1. Create mountpoints and symbolic links (only once)

```bash
mkdir -p ~/mnt/user && ln -nfs ~/mnt/user /user
mkdir ~/mnt/nfs && ln -nfs ~/mnt/nfs /nfs
mkdir ~/mnt/eos && ln -nfs ~/mnt/eos /eos
```

2. Mount network resources (repeat after timeouts and restarts)

```bash
sshfs username@cs-ccr-dev3.cern.ch:/user/ ~/mnt/user
sshfs username@cs-ccr-dev3.cern.ch:/nfs/ ~/mnt/nfs
sshfs username@lxplus.cern.ch:/eos/ ~/mnt/eos
```

3. If outside of the GPN, jump through `lxplus` to mount `dev3`-folders:

```bash
sshfs username@cs-ccr-dev3.cern.ch:/user/ ~/mnt/user -o ssh_command='ssh -t username@lxplus.cern.ch ssh'
sshfs username@cs-ccr-dev3.cern.ch:/nfs/ ~/mnt/nfs -o ssh_command='ssh -t username@lxplus.cern.ch ssh'
```

!!! info ""
    To avoid getting asked for your password all the time, you should have your `ssh` properly configured with Kerberos.

??? tip "In case you need to unmount these"

    ```
    sudo fusermount -u ~/mnt/user
    sudo fusermount -u ~/mnt/nfs
    sudo fusermount -u ~/mnt/eos
    ```

## Running GUIs Locally

To use the [KMod GUI][kmod_gui] or the `KnobPanel` in the [Beta-Beat GUI][bb_gui], it is required to be on the TN, as they need to connect to LSA.
If you are in the GPN but not on the TN, you will need to tunnel through some machines.

First, install the program [sshuttle][sshuttle]{target=_blank}, which should be available in your package manager.
Then, run this command in a terminal and leave it open:

```bash
sshuttle -vr <username>@cs-ccr-dev2 172.18.0.0/16
```

All traffic related to the technical network will be redirected through the `cs-ccr-dev2` machine which has access to both networks. In case it isn't available, the other `cs-ccr-devX` machines can be used.

## Configuring Gitlab CI to Automatically Pull into AFS

If you are programming locally, but also want to have a copy on AFS, either because your colleges are not comfortable with Gitlab or you need the code for other scripts that you are running on `lxplus` or similar, here is how:

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
    Do not forget, if you have set up the repository with Kerberos authentification, to adapt your `.ssh/config` to delegate the credentials.
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
    **MAKE SURE AT LEAST THE `SERVICE_ACCOUNT_PASSWORD ` VARIABLE IS SET TO `Masked` !!!**

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
        - **echo -e Host** line: Here the ssh `config` is adapted to use Kerberos as authetication method to any server (do not touch). 
        - **only master**: Only the commits to `master` trigger the CI. Omit this part if you want the repo to be pulled on every commit, or change it to limit upon which commits this happens (as is done in the [acc-models yml][acc_models_yml]{target=_blank}).  

### Done!

Whenever you are pushing now any commits to the `master` branch, the CI/CD will automatically pull the latest commit into the AFS directory.

*[TN]: Technical Network
*[GPN]: General Purpose Network, the main CERN network
*[CBNG]: Common Build Next Generation
*[LSA]: LHC Software Architecture
*[AFS]: Andrew File System
*[CI]: Continuous Integration
*[CD]: Continuous Delivery
*[lxplus]: Linux Public Login User Service

[sshuttle]: https://sshuttle.readthedocs.io/en/stable/

[kmod_gui]: ../guis/kmod/gui.md
[bb_gui]: ../guis/betabeat/gui.md

[new_account]: https://account.cern.ch/account/Management/NewAccount.aspx
[afs_services]: https://resources.web.cern.ch/resources/Manage/AFS/Default.aspx
[cern_gitlab]: https://gitlab.cern.ch/
[cern_linux]: https://linux.web.cern.ch/dockerimages/
[acc_models_repo]: https://gitlab.cern.ch/acc-models/acc-models-lhc/
[acc_models_yml]: https://gitlab.cern.ch/acc-models/acc-models-lhc/-/blob/2018/.gitlab-ci.yml
[acc_models_docker]: https://gitlab.cern.ch/acc-models/acc-models-www/-/blob/master/_docker/Dockerfile_cern_cc7_base