#kills killmeow
exec {'pkill killmenow':
	command		=> '/usr/bin/pkill killmenow',
	path		=> ['/bin', '/usr/bin'],
	refreshonly	=> true,
	subscribe	=> Notify['kill process killmenow'],
}

notify {'kill process killmenow':
	message		=> 'killing process killmenow'
}
``
