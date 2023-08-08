from setuptools import setup

# Настройка проекта и его зависимостей
setup(
    name='m3_project',  # Имя проекта
    version='1.0.0',  # Версия проекта
    py_modules=['manage'],  # Главный модуль для управления проектом

    # Список пакетов, включая подпакеты и миграции
    packages=['app', 'app.migrations', 'm3_project'],

    # Список зависимостей, необходимых для работы проекта
    install_requires=[
        'django~=2.2.2',  # Версия Django
        'm3-django-compat~=1.9.2',  # Версия m3-django-compat
        'm3-objectpack~=2.2.47',  # Версия m3-objectpack
    ],

    # Дополнительная информация о проекте
    url='',  # URL проекта (None)
    license='',  # Лицензия проекта (None)
    author='graywhitew',  # Автор проекта
    author_email='lastofusfan@mail.ru',  # Электронная почта автора
    description='m3 project for interview',  # Описание проекта
)