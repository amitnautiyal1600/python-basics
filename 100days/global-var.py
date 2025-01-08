
g_var = 'This is Global'
g_var_2 = 'Global2'

def func () :
    global g_var
    g_var = 'This is Local'
    g_var_2 = 'Local2'
    print(g_var)


print(g_var)
print(g_var_2)
func()
print(g_var)
print(g_var_2)