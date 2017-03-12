def func(s, x, obracket_len, cbracket_len):
	if len(s) == 2*x:
		print s
		return
	if obracket_len < x:
		func(s+'(', x, obracket_len+1, cbracket_len)
	if cbracket_len < x and obracket_len > cbracket_len:
		func(s+')', x, obracket_len, cbracket_len+1)