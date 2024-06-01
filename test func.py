def test_functiom():
    def inner_function():
        print("Я в облости видимости функции test_function")

    inner_function()


test_functiom()

inner_function()

#  Вызвать inner_function вне функции test_funcyion
#try:
#    inner_function()
#except NameError:
#    print("Error: функция inner_function не определена в глобальной области видимости")