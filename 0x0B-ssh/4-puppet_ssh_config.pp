#  to set up client SSH configuration file
exec { 'PasswordAuthentication no':
    command     => 'echo -e "\tPasswordAuthentication no \n \tIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
    provider    => 'shell',
  }
