import locale as __locale

if 'es' in __locale.getdefaultlocale()[0]:
    try:
        # Para python 2
        from spanish_messages import *
    except ImportError:
        # Para python 3
        from SeleniumFramework.constants import *
else:
    try:
        # Para python 2
        from english_message import *
    except ImportError:
        # Para python 3
        from SeleniumFramework.constants.english_message import *
    
# BROWSERS
CHROME = 'chrome'
CHROME_P = 'chrome_p'
CHROME_EO = 'chrome_eo'
FIREFOX = 'firefox'
FIREFOX_P = 'firefox_p'
    
# CHROME PROPERTIES
IGNORE_CERTIFICATE = '--ignore-certificate-errors'

# FIREFOX PROPERTIES
SAFEBROWSING = "browser.safebrowsing.malware.enabled"
AUTOLOGIN = "signon.autologin.proxy"
TRUSTED_URIS = 'trusted-uris'
NEGOTIATE = 'negotiate-auth'
N_TRUSTED_URIS = 'network.{}.{}'.format(NEGOTIATE, TRUSTED_URIS)
AUTOMATIC_NTLM = "network.automatic-ntlm-auth.{}".format(TRUSTED_URIS)
N_DELEGATION = "network.{}.delegation-uris".format(NEGOTIATE)
DOMAIN = ".sis.ad.bia.itau"
PROXY = "proxyserver.sis.ad.bia.itau:80"
BINARY = 'C:\\ITAU_Tools\\QA_Automation\Mozilla\\firefox.exe'
    
# # JS
# SCROLL = (
#     "arguments[0].scrollIntoView(true); "
#     "window.scrollBy(0, -window.innerHeight / 4);"
# )
SCROLL = "arguments[0].scrollIntoViewIfNeeded(true)"
SET_ATTRIBUTE = "arguments[0].setAttribute('style', arguments[1])"
CLICK = "arguments[0].click();"
NEW_TAB = 'window.open("{}")'
BACK = 'window.history.go(-1)'

BORDER = "border: 4px solid red"
STYLE = 'style'

# WEBELEMENT ATTRIBUTE
ARIA_OWNS = 'aria-owns'
TAG_LI = 'li'

# PATH
PNG = 'PNG'
LOG_PATH = '{}\{}.log'
PNG_FILE = '{}.png'

# ECXEL DATOS

CRM_DATA_PATH = 'C:\ITAU_Tools\QA_Automation\workspace\Fram27\src\proyectos\CRM\Data\Data_CRM.xlsx'
CRM_DATA_TEST_FUNC_SHEET = 'DataTestFunc'

HB_DATA_PATH = 'C:\ITAU_Tools\QA_Automation\workspace\Fram27\src\proyectos\hb\Data\Data_hb.xlsx'
HB_DATA_TEST_FUNC_SHEET = 'DataTestFunc'
HB_DATA_USER = 'Clientes'
HB_DATA_USER_BO = 'UsuariosBO'

# PATH

PATH_FOLDER_IMG = "C:/ITAU_Tools/QA_Automation/Workspace/Desktop_automation/src/proyectos/AS_400/img"
PNG = 'PNG'
LOG_PATH = '{}\{}.log'
PNG_FILE = '{}.png'
MSG_CREATE_LOG = "The log is in {}"

class MsgImage():
    # SCREEN SHOT
    MSG_SCREENSHOT = 'The screenshot is made. {}'
    MSG_SCREENSHOT_BUFFER = (
        "Taked a screenshot. Still in memory"
    )
    MSG_GET_IMAGE = (
        "The image element {0} is save in {1}"
    )
    MSG_GET_IMAGE_ERROR = "The element {} isn't an image"