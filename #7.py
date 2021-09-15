#dictionary is just map in cpp
#it has one key and a value
data = {1:'shashikant',10:'saurabh',3:'prashansa'}
print(data[3])

print(data.get(10))

#if data is present than it will display the data.
print(data.get(2,'Not found'))

keys = ['shashikant','yash','garv','naveen']
values = ['cpp','javascript','python','golang']
print(keys)
print(values)

data = dict(zip(keys,values))

print(data)

print(data['yash'])

data['saurabh'] = 'devops'

print(data)

#list & dictionary inside dictionaty
prog = {'JS':'Atom','CS':'VS','Python':['pycharm','sublime'],'java':{'JSE':'Netbeans','JEE':'Eclipse'}}

print(prog)

prog['java']

print(prog['java']['JSE'])