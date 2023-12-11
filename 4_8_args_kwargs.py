def anjayani(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(key)
        print(value)
    
anjayani("anjay", "dia", "saya", body="anjay", siy=1)

note = """
One important point to note is that the names args and kwargs are by convention,
and you can actually use any valid variable names, but using args and kwargs is a widely accepted
practice that makes the code more readable for other programmers."""

print(note)