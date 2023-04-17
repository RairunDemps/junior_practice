global_var = "global_var"

def my_function(local_param_var="local_param_var"):
    global global_var
    local_scope_var = "local_scope_var"
    enclosing_scope_var = "enclosing_scope_var"
    
    print(f"accessing global variable global_var from my_function -> {global_var}")
    global_var = "global_var_changed"

    def inner_function():
        nonlocal enclosing_scope_var
        
        print(f"accessing enclosing scope var -> {enclosing_scope_var}")
        enclosing_scope_var = "enclosing_scope_var_inner_changed"
        print(f"accessing changed enclosing scope var in inner_function -> {enclosing_scope_var}")
    
    inner_function()
    print(f"accessing changed enclosing scope var my_function -> {enclosing_scope_var}")
    
my_function()
print(f"accessing global variable global_var from global scope -> {global_var}")