from unittest.mock import Mock, MagicMock

plain_mock = Mock()
magic_mock = MagicMock()

# print(len(plain_mock)) # there's no __len__
print(len(magic_mock))

print(magic_mock[3])
print(magic_mock['hola'])
# __getitem__

magic_mock.__len__.return_value = 30
print(len(magic_mock))

if magic_mock:
    print("animo josa yo se que vas a lograr ser un programador")

magic_mock.__bool__.return_value = False

if not magic_mock:
    print("\nen efecto bro es un booleano falso")

magic_mock.__getitem__.return_value = 31
print(magic_mock[3])
print(magic_mock['hola'])