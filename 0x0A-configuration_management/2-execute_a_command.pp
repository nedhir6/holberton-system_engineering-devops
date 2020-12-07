# kills a process named killmenow
exec { 'kill_a_process':
    command => 'pkill -f "killmenow"'
    path    => '/user/bin'
  }
