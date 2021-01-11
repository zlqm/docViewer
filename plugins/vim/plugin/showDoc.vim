function! LivePreview()
	let filename =expand('%:p')
	let port = 9000
	call system('previewDoc '.filename.' --port='.port.' 2>&1 >> /tmp/docViewerVim.log &')
	let url = 'http://localhost:'.port.'/lite-preview?filename='.filename
	call system('xdg-open '.url)
	echo 'live preview is ready at '.url
endfunction

command! -nargs=0 LivePreview call LivePreview()
