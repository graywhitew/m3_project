from objectpack.observer import (
    ObservableController,
    Observer,
)

observer = Observer()

controller = ObservableController(
    url='actions',  # URL-префикс для действий контроллера
    observer=observer,  # Подключение ранее созданного экземпляра Observer
)

