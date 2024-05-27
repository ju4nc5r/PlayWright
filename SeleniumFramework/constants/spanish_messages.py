# -*- coding: utf-8 -*-


class MsgBrowser():
    __SIZE = u'{0}X{1}px'
    # OPEN BROWSERS
    MSG_OPEN_CHROME = u'Se inicializa Chrome'
    MSG_OPEN_FIREFOX = u'Se inicializa Firefox'
    MSG_OPEN_IE = u'Se inicializa IE'
    MSG_CLOSE_BROWSER = u'Se cierra el navegador'
    # MAXIMIZE
    MSG_MAXIMIZE = u'Se maximiza la pantalla del navegador'
    # PAGE
    MSG_URL = u'Se abre la url: {}'
    MSG_CURRENT_URL = u'La actual URL es: {}'
    MSG_REFRESH = u'Se refresca la página'
    # WINDOW SIZE
    MSG_WINDOW_SIZE = (
        u'Se obtiene las medidas de la ventana. La medida es %s' % __SIZE
    )
    MSG_SET_WINDOW_SIZE = u'Se setea la medida de la ventana a %s' % __SIZE
    # TAB
    MSG_NEW_TAB = u'Se crea una nueva pestaña con la URL: {}'
    __TAB = u'Se cambia la pestaña activa por la que se esta en '
    MSG_CHANGE_TAB = u'%sla posicion {}' % __TAB
    MSG_CHANGE_TAB_ERROR = u'No existe la pestaña en la posicion {}'
    MSG_CLOSE_TAB = u'Se cierra la actual pestaña'
    MSG_BACK_PAGE = u'Se vuelve a la pagina anterior'
    MSG_FORWARD_PAGE = u'Se adelanta una pagina'
    # MOBILE
    __MOBILE = u'Se inicializa Chrome con la '
    MSG_MOBILE = u'%sinterfaz del dispositivo {}' % __MOBILE
    MSG_MOBILE_SIZE = u'%sresolucion %s, pixel_ratio {2}' % (__MOBILE, __SIZE)


class MsgLog():
    # CREATE LOG
    MSG_CREATE_LOG = u'El log se crea en {}'


class MsgSearch():
    # SEARCH ELEMENTS
    MSG_SEARCH_ELEM = u'Se encontró el elemento {}'
    MSG_SEARCH_ELEM_ERROR = u'No se muestra el elemento {}'
    MSG_SEARCH_ELEMS = u'Se encontró {0} elementos con el xpath {1}'
    MSG_SEARCH_ELEM_ID_ERROR = u'No se muestra el elemento con el id {}'
    MSG_DOUBLE_SEARCH = u'Se inicia la doble busqueda'
    MSG_DOUBLE_SEARCH_ERROR = u'No se encontraron los elementos buscados'
    # COMPARE TEXT
    MSG_COMPARE_TEXT = u'El texto {0}, se muestra en el elemento buscado {1}'
    MSG_COMPARE_TEXT_ERROR = (
        u'El texto {0} es diferente al elemento {1}'
    )
    DSC_COMPARE_TEXT = u'Valor esperado {0}, valor encontrado {1}'
    MSG_COMPARE_TEXT_FAIL = 'Los textos son diferentes'
    # VERIFY
    MSG_VERIFY = u'Se verificó: {}'
    MSG_VERIFY_ERROR = u'No se pudo verificar: {}'
    MSG_VERIFY_VALUES = u'Cantidad de elementos a buscar = {}'
    __SEARCH = u'Cantidad de elementos a buscar = {}'
    __FOUNDED = u'Cantidad de elementos no encontrados {}'
    MSG_VERIFY_VALUES_RESULT = u'%s\n%s\nElementos buscados {}' % (__SEARCH,
                                                                   __FOUNDED)
    # CHECK FIELDS
    __F_SEARCH = u'Cantidad de campos a buscar {0}'
    __F_FOUNDED = u'Contador campos encontrados = {1}'
    __NOT_FOUND = u'Contador caompos NO encontrados = {2}'
    MSG_RESULT_CHECK_FIELD = (
        u'%s\n%s\n%s' % (__F_SEARCH, __FOUNDED, __NOT_FOUND)
    )
    MSG_CHECK_FIELD_ERROR = u'Hay campos que no se están mostrando'
    MSG_SEARCH_ELEM_BY = u'Se busca elemento con parametro {0} y valor {1}'
    MSG_ARRAY_SEARCH = u'Se comineza la busqueda por lista'


class MsgImage():
    # SCREEN SHOT
    MSG_SCREENSHOT = u'Se realiza la captura de pantalla. {}'
    MSG_SCREENSHOT_BUFFER = (
        u'Se realiza una captura de pantalla, se deja en memoria'
    )
    MSG_GET_IMAGE = (
        u'Se pudo obtener la imagen del elemento {0}, se guardo en {1}'
    )
    MSG_GET_IMAGE_ERROR = u'El elemento {} no es una imagen'


class MsgMouse():
    # CLICK
    MSG_CLICK_ELEM = u'Se selecciona el elemento {}'
    MSG_CLICK_ELEM_ERROR = u'No se pudo seleccionar el elemento {}'
    MSG_DOUBLE_CLICK = u'Se realiza doble click sobre el elemento {}'
    MSG_DRAG_DROP = u'Se arrastra el elemento {0} al elemento {1}'


class MsgSelect():
    # SELECT
    MSG_SELECT_OPTION = u'Se selecciona la opción {0} del elemento {1}'
    __OPTION = u'La opción {} no se encuentra dentro de'
    __ERROR = u'las opciones disponibles'
    MSG_SELECT_OPTION_ERROR = u'%s %s' % (__OPTION, __ERROR)
    MSG_SELECT_OPTION_REVIEW = u'Revisar la opción ingresada'
    MSG_SELECT_OPTION_INDEX_ERROR = u'El índice ingresado, no existe'
    MSG_SELECT_INDEX = (
        u'Se selecciona la opción del índice {0} del elemento {1}'
    )
    MSG_SELECT_VALUE = (
        u'Se selecciona la opción con valor {0} del elemento {1}'
    )
    MSG_SELECT_TEXT = u'Se selecciona la opción con texto {0} del elemento {1}'
    __SEL_ERROR = u"No se encontró la opción con el "
    MSG_SELECT_INDEX_ERROR = u'%síndice {0} en el elemento {1}' % __SEL_ERROR
    MSG_SELECT_VALUE_ERROR = u'%svalor {0} en el elemento {1}' % __SEL_ERROR
    MSG_SELECT_TEXT_ERROR = u'%stexto {0}  en el elemento {1}' % __SEL_ERROR
    MSG_SELECT_ELEMENT_ERROR = (
        u'El elemento buscado {}, no es un elemento select'
    )
    MSG_SELECT_RANDOM = u'Se selecciona, aleatoriamente, una opción'


class MsgKeyboard():
    # WRITE
    MSG_INPUT = u'Se va a tipear "{1}" en {0}'
    MSG_INPUT_KEY = u'Se ingresa la tecla {0} en el elemento {1}'
    MSG_INPUT_KEY_ERROR = u'La tecla {}, no existe'
    # CLEAR
    MSG_CLEAR = u'Se borra el contenido del elemento {}'
    MSG_CLEAR_ERROR = u'{0}\nNo se puede borrar el contenido del elemento {1}'


class MsgJS():
    # SCROLL
    MSG_SCROLL = u'Se desplaza hasta el elemento {}'
    MSG_HIGHLIGHT = u'Se resalta el elemento {}'
    MSG_CREATE_TAB = u'Se crea pestaña nueva con la url: {}'
    MSG_BACK = u'Se regresa a la anterior pagina'


class MsgWebelement():
    # GET TEXT
    MSG_GET_TEXT = u'Se obtine el texto {1}, del elemento {0}'
    # ATTRIBUTE
    MSG_ATTRIBUTE = u'Se obtubo el atributo {2} del elemento {1}: {0}'
    MSG_ATTRIBUTE_ERROR = (
        u'No se pudo obtener el atributo {0} del elemento {1}'
    )
    MSG_GET_LOCATION = u'La ubicacion del elemento {0}, es {1}'
    MSG_GET_SIZE = u'El tamaño del elemento {0}, es {1}'
    MSG_DISPLAYED = u'El elemento {} se encuentra visible'
    MSG_DISPLAYED_ERROR = u'El elemento {} no se encuentra visible'
    MSG_ENABLED = u'El elemento {} se encuentra disponible'
    MSG_ENABLED_ERROR = u'El elemento {} no se encuentra disponible'
    MSG_SELECTED = u'El elemento {} se encuentra seleccionado'
    MSG_SELECTED_ERROR = u'El elemento{} no se encuentra seleccionado'


class MsgAllure():
    MSG_ATTACH_IMAGE = u'Se adjuntó la imagen {} en allure'
    MSG_STEP = u'PASO {0}: {1}'


# RETRY
MSG_RETRY = u'reintentar Seleccion: {}'

# WAITING
MSG_WAITING = u'Se pausa el test por {} segundos'

# UPLOADFILE
MSG_UPLOAD = u'Se inicia el proceso para subir un archivo'
MSG_UPLOAD_DONE = u'Se logró subir el archivo {}'
MSG_UPLOAD_FAIL = u'Archivo inválido {}'
