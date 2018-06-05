import ffilupa
lua = ffilupa.LuaRuntime()
lua_func = lua.eval('''
    function(a, b) -- a plus b
        return a + b
    end
''')
print(lua_func(22, 33))
lua.close()