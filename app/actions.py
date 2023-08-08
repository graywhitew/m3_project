from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
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

# Пакет действий для прав доступа
class PermissionsActionPack(ObjectPack):
    model = Permission
    list_window = PermissionsUI
    add_window = edit_window = PermissionAddUI
    add_to_menu = add_to_desktop = True

# Пакет действий для групп
class GroupsActionPack(ObjectPack):
    model = Group
    list_window = GroupsUI
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)
    add_to_menu = add_to_desktop =True