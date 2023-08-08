from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from objectpack.ui import BaseListWindow, BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext


# Окно для управления типами контента
class ContentTypeUI(BaseListWindow):
    model = ContentType

# Окно для управления пользователями
class UserUI(BaseListWindow):
    model = User

# Окно для добавления нового пользователя
class UserAddUI(BaseEditWindow):
    def _init_components(self):
        super(UserAddUI, self)._init_components()

        # Поля формы для ввода данных пользователя
        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%'
        )
        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%'
        )
        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            anchor='100%',
            format='d.m.Y'
        )
        self.field__is_superuser = ext.ExtCheckBox(
            label=u'superuser status',
            name='is_superuser',
            anchor='100%',
            checked=False
        )
        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            anchor='100%',
            allow_blank=True
        )
        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            anchor='100%',
            allow_blank=True
        )
        self.field__email = ext.ExtStringField(
            label=u'email address',
            name='email',
            anchor='100%',
            vtype='email',
            input_type='passwordfield',
            allow_blank=True
        )
        self.field__is_staff = ext.ExtCheckBox(
            label=u'staff status',
            name='is_staff',
            anchor='100%',
            checked=False
        )
        self.field__is_active = ext.ExtCheckBox(
            label=u'active',
            name='is_active',
            anchor='100%',
            checked=False
        )
        self.field__last_login = ext.ExtDateField(
            label=u'date last login',
            name='date_last_login',
            anchor='100%',
            format='d.m.Y'
        )
        self.field__date_joined = ext.ExtDateField(
            label=u'date joined',
            name='date_joined',
            anchor='100%',
            format='d.m.Y'
        )

    def _do_layout(self):
        super(UserAddUI, self)._do_layout()
        # Расположение полей на форме
        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_superuser,
            self.field__is_active,
            self.field__last_login,
            self.field__date_joined
        ))

    def set_params(self, params):
        super(UserAddUI, self).set_params(params)
        self.height = 'auto'
    
# Окно для управления группами
class GroupsUI(BaseListWindow):
    model = Group

# Окно для управления правами доступа
class PermissionsUI(BaseListWindow):
    model = Permission

# Окно для добавления нового права доступа
class PermissionAddUI(BaseEditWindow):
    def _init_components(self):
        super(PermissionAddUI, self)._init_components()

        # Поля формы для ввода данных прав доступа
        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%'
        )
        content_types = ContentType.objects.all()
        content_type_choices = [(ct.id, ct.name) for ct in content_types]
        self.field__content_types = make_combo_box(
            label=u'content type',
            name='content_type_id',
            allow_blank=False,
            anchor='100%',
            data=content_type_choices,
            display_field='name'
        )

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%'
        )

    def _do_layout(self):
        super(PermissionAddUI, self)._do_layout()
        # Расположение полей на форме
        self.form.items.extend((
            self.field__name,
            self.field__content_types,
            self.field__codename
        ))

    def set_params(self, params):
        super(PermissionAddUI, self).set_params(params)
        self.height = 'auto'
    
