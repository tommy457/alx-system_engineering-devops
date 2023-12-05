# configuring a custom HTTP header with Puppet

exec { 'update':
  path    => '/usr/bin:/bin',
  command => 'sudo apt-get update',
}

-> exec { 'install nginx':
  path    => '/usr/bin:/bin',
  command => 'sudo apt-get install nginx -y',
}

-> package { 'nginx':
  ensure => 'installed',
}

-> file_line { 'add header':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => '        add_header X-Served-By $hostname;',
}

-> exec { 'restart nginx':
  path    => '/usr/bin:bin/',
  command => 'sudo service nginx restart',
}
