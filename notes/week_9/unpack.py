def f(**kwargs):
  for arg in kwargs:
    print(arg)
    print(kwargs[arg])
  
f(galleons=100, sickles=50, knuts=25)