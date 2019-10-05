import webbrowser,sys,pyperclip

x = 0
x= x+1
if len(sys.argv)>1:
    address=''.join(sys.argv[1:])
else:
    address=pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)
