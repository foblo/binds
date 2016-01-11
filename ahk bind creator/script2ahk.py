import os

open('Script_.tmp', 'w').close()
f = open('Input.txt','r+')
nf = open('Script_.tmp','r+')

print('\n')
print('OLD CFG FILES WILL BE DELETED')
print('\n')
print('if you do not have an input.txt in this folder, exit and do so.')
print('\n')      

bind = input('Bind to Key: ' )
delay = input('Delay Between Messages: ')
filename = input('File Name: ')

prenum = 0
presuf = ' Send, '
suffix = '{Enter}'

nf.write(bind+'::')
nf.write('\n')
nf.write('\n')

list = [[]]
setnum = 0
amount = 10
count = 0
listcnt = 0

for i in f:
	if len(i) > 1:
		prefix = presuf
		nf.write('%s%s%s%s\n' % (prefix, i.rstrip('\n').lstrip(' '), suffix, '\nsleep '+delay))
		
		if len(list[setnum]) == amount:
			setnum += 1
			list.append([])
		prenum += 1

for i in range(len(list)):
	nf.write('\nReturn')

f.close()
nf.close()

for i in os.listdir("."):
	if i.endswith(".ahk"):
		os.remove(i)
	if i.startswith("Script_"):
		os.rename(i, filename+'.ahk')
