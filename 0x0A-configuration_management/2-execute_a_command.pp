# manifest that kills a process named killmenow.

exec { 'kill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
