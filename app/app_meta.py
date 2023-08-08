from django.conf.urls import url
from objectpack import desktop

from .controller import controller
from .actions import ContentTypeActionPack, UserActionPack, PermissionsActionPack, GroupsActionPack
# from .actions import content_type_action_pack, user_action_pack, permissions_action_pack, group_action_pack

def register_urlpatterns():
	"""
	Регистрация конфигурации урлов для приложения
	"""
	return [url(*controller.urlpattern)]


def register_actions():
	"""
	Регистрация экшен-паков
	"""
	return controller.packs.extend([
    	    ContentTypeActionPack(),
			UserActionPack(),
			PermissionsActionPack(),
			GroupsActionPack()
	])

def register_desktop_menu():
	"""
	регистрация элементов рабочего стола
	"""
	desktop.uificate_the_controller(
    	    controller,
    	    menu_root=desktop.MainMenu.SubMenu('Demo')
    )
	