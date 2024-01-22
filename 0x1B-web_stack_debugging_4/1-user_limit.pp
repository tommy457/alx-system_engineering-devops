# increase max number of file descriptors for holberton user
exec { 'har-file-descriptors':
  command  => 'sed -i "/holberton hard nofile/s/5/50/g" /etc/security/limits.conf',
  provider => 'shell',
}
exec { 'soft-file-descriptors':
  command  => 'sed -i "/holberton soft nofile/s/4/40/g" /etc/security/limits.conf',
  provider => 'shell',
}
