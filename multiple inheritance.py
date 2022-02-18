#Write a program multiple inheritance?
class a:
    x='python'
    print('hi...')
class b(a):
    print('hello')
class c(b):
    print('how are u')
class d(c,b,a):
    print('chandu')
e=d()
print(a.x)