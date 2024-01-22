# Configure nginx to handel 2000+ requests.
# increase max number of file descriptors.
exec { 'file-descriptors':
  command  => 'sed -i "s/15/4096/g" /etc/default/nginx',
  provider => 'shell',
}
-> exec { 'restart-nginx':
  command  => 'service nginx restart',
  provider => 'shell',
}

