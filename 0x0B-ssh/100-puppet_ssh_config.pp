# using puppet to make changes to an SSH config file
exec { 'echo "    IdentityFile ~/.ssh/holberton\n    PasswordAuthentication no" >> /etc/ssh/ssh_config':
  path    => '/bin/'
}
