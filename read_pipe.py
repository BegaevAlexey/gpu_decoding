import pipes

t = pipes.Template()
t.append('tr a-z A-Z', '--')
f = t.open('pipe_3', 'r')
data = f.read()
print(data)