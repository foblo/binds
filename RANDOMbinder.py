import os

open('Script_.tmp', 'w').close()
f = open('Input.txt','r+')
nf = open('Script_.tmp','r+')

print('GET AN Input.txt IN THE FOLDER THIS IS RUN IN, OR IT WILL NOT WORK')
print('\n')
print('Old .cfg files will be deleted.')

bind = input('Bind to Key: ' )
filename = input('File Name: ')

prepre1 = 'alias '
prepre2 = input('Alias name? ')
prenum = 0
presuf = ' "say '
suffix = '"'

nf.write('bind '+bind+' '+'+'+prepre2+'_dice')
nf.write('\n')
nf.write('\n')

list = [[]]
setnum = 0
amount = 10
count = 0
listcnt = 0

result = prepre2+'_result'
cycle = prepre2+'_cycle'
prepre3 = prepre2+'_diceroll'

for i in f:
	if len(i) > 1:
		prefix = prepre1+prepre2+str(prenum)+presuf
		nf.write('%s%s%s\n' % (prefix, i.rstrip('\n').lstrip(' '), suffix))
		if len(list[setnum]) != amount:
			list[setnum].append(prepre2+str(prenum))
		elif len(list[setnum]) == amount:
			setnum += 1
			list.append([])
		prenum += 1
nf.write('\n\n')
nf.write('alias waitcheck_test2 "wait 10;alias waitcheck_result waitcheck_pass"''\n')
nf.write('alias waitcheck_test "waitcheck_test2;alias waitcheck_result waitcheck_fail;wait 15;waitcheck_result"''\n') 
nf.write('alias shittalk_waiton "alias diceroll '+prepre2+'_next; '+prepre2+'_next"''\n')
nf.write('alias shittalk_nowait "'+prepre2+'_cycle"''\n')

num2 = 0
for i in range(prenum-1):
        prefix = prepre1+prepre3+'_'+str(num2)+' '+'"alias '+result+' '+prepre2+str(num2)+";"+prepre1+cycle+' '+prepre3+'_'+str(num2+1)+'"'
        nf.write(prefix+'\n')
        num2 += 1
prefix = prepre1+prepre3+'_'+str(num2)+' '+'"alias '+result+' '+prepre2+str(num2)+";"+prepre1+cycle+' '+prepre3+'_'+str(0)+'"'
nf.write(prefix+'\n')

nf.write('\n')
                

nf.write('alias +'+prepre2+'_dice "alias waitcheck_pass shittalk_waiton;alias waitcheck_fail shittalk_nowait;waitcheck_test"''\n')
nf.write('alias -'+prepre2+'_dice "'+prepre2+'_result;alias diceroll"''\n')
nf.write('alias '+prepre2+'_next "'+prepre2+'_cycle;wait 5;diceroll"''\n')
nf.write('alias '+prepre2+'_cycle '+prepre2+'_diceroll_0''\n\n')

f.close()
nf.close()

for i in os.listdir("."):
	if i.endswith(".cfg"):
		os.remove(i)
	if i.startswith("Script_"):
		os.rename(i, filename+'.cfg')
