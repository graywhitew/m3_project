from m3_ext.context_processors import DesktopProcessor

# Определение функции-контекстного процессора
def desktop(request):
	# Вызов метода process() класса DesktopProcessor и передача объекта запроса
	return DesktopProcessor.process(request)
