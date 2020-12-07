# installs puppet-lint
exec { 'install_puppet-lint':
    command => 'gem install puppet-lint -v 2.1.1'
    path    => '/user/bin'
  }
