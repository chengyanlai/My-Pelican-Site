Title: SSH login without password  
Date: 2013-10-15 16:05  
Author: Chen-Yen Lai
Category: OSX
Slug: ssh-tricks


## Create SSH key
Beforehand - You need to know where is the server (It's not helping!), and you need to create a new ssh-key like the following command at your home directory

    :::bash
    $ ssh-keygen -t rsa -C "{Your email}"

During the process, you will see

    :::bash
     Generating public/private rsa key pair.  
     Enter file in which to save the key (/home/a/.ssh/id_rsa): **{Name of the key}**  
     Created directory '${HOME}/.ssh'.  
     Enter passphrase (empty for no passphrase): **{You can choose to create or leave empty.}**  
     Enter same passphrase again: **{Do the same as above}**  
     Your identification has been saved in ${HOME}/.ssh/{Name of the key}.  
     Your public key has been saved in ${HOME}/.ssh/{Name of the key}.pub.  
     The key fingerprint is: 3e:4f:05:79:3a:9f:96:7c:3b:ad:e9:58:37:bc:37:e4 a@A  

After that you can see two files in the directory `${HOME}/.ssh/`, they are

    :::bash
	{Name of the key}
	{Name of the key}.pub

The first is your `Private Key`, and second is the `Public Key`. Remember ***NOT*** to share your `Private Key` to anyone.

## Protected Private Key {#prot}

If you chose to add the password during the key generation above, you need to do this to prevent the typing during every time you login (That's our goal!). Do the following command after the key is generated

    :::bash
	$ ssh-add -K ~/.ssh/{Name of the key}

It'll prompt for your passphrase if necessary, then add it to your Keychain[^2]. This only works for this local computer. If you move your private key to another, you need to type the passphrase.

## Config SSH Host
Next we need to edit the file located at ${HOME}/.ssh/config. If the file is not there, please create it. Add the following lines.

>     Host {You Name It!}
     	HostName {The url of the ssh server}
     	Port 22{unless the port is changed}
     	User {login username}
     	IdentityFile ${HOME}/.ssh/{Name of the key}

## Make Server Knows You
Here comes the most important part. You need to add the public key to the file on the server by using the following command

	cat ${HOME}/.ssh/{Name of the key}.pub | ssh {You Name It!} 'cat >> .ssh/authorized_keys'

It is basically all done. Now, we can try

    :::bash
	$ ssh {You Name It!}

to connect.

## SSH agent

You can check if your `Private Key` is loaded by `SSH agent`[^3]. Type this in terminal

    :::bash
	$ ssh-add -l

, and it will you which key is loaded. If the key you need is not shown, you need to add it by

    :::bash
	$ ssh-add /path/to/the/private key/{the private key}

. Then check again

    :::bash
	$ ssh-add -l

it should be there.

## Turn off passwd log-in on the server
For security reason, I choose to turn off the passwd login method on ssh server.
There is downside on this, you always need RSA key to login!!  
Open the file '/etc/ssh/sshd_config', and find the following

    # Change to yes to enable challenge-response passwords (beware issues with
    # some PAM modules and threads)
    ChallengeResponseAuthentication no

    # Change to no to disable tunnelled clear text passwords
    PasswordAuthentication no

    # If you just want the PAM account and session checks to run without
    # PAM authentication, then enable this but set PasswordAuthentication
    # and ChallengeResponseAuthentication to 'no'.
    UsePAM no


### Notes

You can also refer to [this page](http://www-uxsup.csx.cam.ac.uk/~aia21/osx/leopard-ssh.html).  
As of Leopard 10.5.1, the ssh agent will be launched during the start-up.
