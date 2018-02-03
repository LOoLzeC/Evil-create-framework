import marshal
import __builtin__ as pp
def marshaller(file):
  f=open(file).read()
  s = f.replace("\r\n","\n")
  s = s.replace("\r","\n")
  if s and s[-1] != '\n':
    s = s + '\n'
  ff=pp.compile(s,'<s>','exec')
  hh=marshal.dumps(ff)
  awal="""
import marshal
exec(marshal.loads(''"""
  akhir="''))"
  open(file[:-3]+'_new.py', 'w').write(awal+repr(hh)+akhir)

q=raw_input('script.py > ')
try:marshaller(q)
except:print 'check nama file...'