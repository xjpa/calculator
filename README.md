compile c code to a shared library

```
$ gcc -shared -o libcalculator_operations.so -fPIC calculator.c
```

start the flask web server

```
$ python app.py
```

to access app, go to

http://127.0.0.1:5000/
