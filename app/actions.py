from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.hashers import make_password, identify_hasher
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .ui import ContentTypeUI, UserUI, PermissionsUI, PermissionAddUI, UserAddUI, GroupsUI


'''Каждый пакет (ActionPack) определяет, как взаимодействовать с моделью,
какие окна использовать для отображения и редактирования данных,
и реализует возможность добавления в меню и на рабочий стол'''

# Пакет действий для типов контента
class ContentTypeActionPack(ObjectPack):
    model = ContentType
    list_window = ContentTypeUI
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)
    add_to_menu = add_to_desktop = True

# Пакет действий для пользователей
class UserActionPack(ObjectPack):
    model = User
    list_window = UserUI
    add_window = edit_window = UserAddUI
    add_to_menu = add_to_desktop = True
    
    columns = [
        {'header': 'username', 'data_index': 'username','searchable': True, 'sortable': True},
        {'header': 'email', 'data_index': 'email'},
        {'header': 'first name', 'data_index': 'first_name'},
        {'header': 'last name', 'data_index': 'last_name'},
        {'header': 'active', 'data_index': 'is_active'},
        {'header': 'staff', 'data_index': 'is_staff'},
        {'header': 'superuser', 'data_index': 'is_superuser'},
        {'header': 'date joined', 'data_index': 'date_joined'},
        {'header': 'date last login', 'data_index': 'last_login'},
        {'header': 'password', 'data_index': 'password'},
    ]

    def save_row(self, obj, create_new, request, context, *args, **kwargs):
        """
        Обработка сохранения объекта. Выполняет хеширование нового пароля при необходимости.
        
        Аргументы:
            obj (Model): Сохраняемый объект модели.
            create_new (bool): Флаг, указывающий, создается ли новый объект.
            request (HttpRequest): Запрос от клиента.
            context (dict): Контекст выполнения.
            *args, **kwargs: Дополнительные аргументы и ключевые слова.

        """
        try:
            # Попытка идентификации используемого хеширования в Django
            identify_hasher(obj.password)
        except ValueError:
            # Если хешер не был найден, значит в поле password был введен новый пароль,
            # который следует захешировать
            obj.password = make_password(obj.password)

        # Вызов метода сохранения объекта в родительском классе
        super().save_row(obj, create_new, request, context, *args, **kwargs)

# Пакет действий для прав доступа
class PermissionsActionPack(ObjectPack):
    model = Permission
    list_window = PermissionsUI
    add_window = edit_window = PermissionAddUI
    add_to_menu = add_to_desktop = True

    columns = [
        {'header': 'name', 'data_index': 'name','sortable': True},
        {'header': 'codename', 'data_index': 'codename', 'sortable': True},
        {'header': 'content_type', 'data_index': 'content_type', 'sortable': True}
        ]

# Пакет действий для групп
class GroupsActionPack(ObjectPack):
    model = Group
    list_window = GroupsUI
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)
    add_to_menu = add_to_desktop =True

    columns = [
        {'header': 'name', 'data_index': 'name','sortable': True}
    ]