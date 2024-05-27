import os
import sys
import platform

# ############# Se define el path de las evidencias ###################
# El framwork esta creado dentro de la carpeta
# Fram27/src/proyectos/NombreProyecto, por ende, se toma el NombreProyecto para
# generar la evidencia. En caso que se ejecute fuera del framework, se crea
# una carpeta que se llame 'Sin proyecto'
try:
    # Si se ejecuta desde allure, se toma este path
    path = os.path.abspath(sys.argv[1])
except IndexError:
    # Si se ejecuta localmente, se usa este path
    path = os.path.abspath(sys.path[0])
splitpath = path.split('\\')
try:
    index = splitpath.index('proyectos')
    proyecto = splitpath[index+1]
except ValueError:
    proyecto = 'Sin proyecto'
# Una vez obtenido el nombre del proyecto, se crea la carpeta
if platform.system() == 'Windows':
    path_evidence = os.path.join('C:/ITAU_Tools/evidencias/homologacion',
                                 proyecto, 'screenshots')
else:
    print('Definir el path de la evidencia')
    
    
    


############################# Navegador que se utiliza #######################
# Hay que hacer que los test vengan aca a preguntar que navegador se va a
# utilizar
browser = 'Chrome'

# ############ Lectura del excel #######################################
# ########### Se define el path del excel que esta en la red #############
# Excel con los datos para hb y mb. Con sus correspondientes pestanas
hb_user_excel = '//ntaplic3/testing/Material Compartido/Automation/Data/Data_HBPF.xlsx'
# hb_user_excel = '//ntaplic3/Testing/apps/Data_hb.xlsx'
hb_user_sheet = 'Test'
hb_user_sheet_2 = 'Usuarios'
hb_user_login = 'Login'
mb_test_sheet = 'Mobile_test'

cca_user_excel = '//ntaplic3/testing/Material Compartido/Automation/Data/Data_cca.xlsx'
# cca_user_excel = '//ntaplic3/Testing/apps/Data_cca.xlsx'
cca_user_sheet = 'Test'

# Excel viejo de usuarios para hb
hb_old_excel = '//ntaplic3/testing/Material Compartido/Automation/Data/usuarios_hb.xlsx'
# hb_old_excel = '//ntaplic3/Testing/apps/usuarios_hb.xlsx'
hb_old_sheet = "DataTest"

# Excel viejo de los usuarios para mobile
mb_user_excel = '//ntaplic3/testing/Material Compartido/Automation/Data/Usuarios_Mobile.xlsx'
# mb_user_excel = '//ntaplic3/Testing/apps/Usuarios_Mobile.xlsx'
mb_user_sheet = "DataTest"


# Excel con los datos para Caja. Con sus correspondientes pestanas
caja_user_excel = '//ntaplic3/testing/Material Compartido/Automation/Data/Data_Caja.xlsx'
# caja_user_excel = '//ntaplic3/Testing/apps/Data_Caja.xlsx'
caja_user_sheet = 'TestINTE'
# caja_user_sheet_homo = os.getenv("CajaUserSheetHomo")
caja_user_sheet_homo = 'TestHOMO'
caja_user_sheet_desa = 'TestDESA'
caja_user_sheet_homo_suc_50 = 'TestHOMO_suc_50'


# Excel con los datos para MesaWeb. Con sus correspondientes pestanas
mesaWeb_user_excel = '//ntaplic3/testing/Material Compartido/Automation/Data/Data_MesaWeb.xlsx'

# mesaWeb_user_excel = '//ntaplic3/Testing/apps/Data_MesaWeb.xlsx'
mesaWeb_user_sheet_homo = 'TestHOMO'

# Excel con los datos para BPM. Con sus correspondientes pestanas
BPM_user_excel = '//ntaplic3/testing/Material Compartido/Automation/Data/Data_BPM.xlsx'

# BPM_user_excel = '//ntaplic3/Testing/apps/Data_BPM.xlsx'
BPM_user_sheet_homo = 'TestHOMO'
BPM_user_sheet_homo2 = 'Usuarios'

WhatsApp_user_excel = '//ntaplic3/testing/Material Compartido/Automation/Data/Data_WhatsApp.xlsx'
WhatsApp_user_sheet_homo = 'TestHOMO'

Genesys_user_excel = '//ntaplic3/testing/Material Compartido/Automation/Data/Data_Genesys.xlsx'
Genesys_user_sheet_homo = 'TestHOMO'

# Excel con los datos para IBE. Con sus correspondientes pestanas
IBE_user_excel = '//ntaplic3/testing/Material Compartido/Automation/Data/Data_IBE.xlsx'

# mesaWeb_user_excel = '//ntaplic3/Testing/apps/Data_MesaWeb.xlsx'
IBE_user_sheet_homo = 'TestHOMO'


# Excel con los datos para NHBE. Con sus correspondientes pestanas
NHBE_user_excel = '//ntaplic3/testing/Material Compartido/Automation/Data/Data_NHBE.xlsx'

# mesaWeb_user_excel = '//ntaplic3/Testing/apps/Data_MesaWeb.xlsx'
NHBE_user_sheet_homo = 'TestHOMO'


# Para hacer otra ejecucion simultanea en homo con otros datos (se debe utilizar otro job (Caja_HOMOLOGACION_Pruebas_2)


# ########### URL de aplicaciones ########################################
url_hb = 'https://internethomo.sis.ad.bia.itau/internet/sso'
url_backoffice = "https://mcbohomo.sis.ad.bia.itau/backoffice/login/login.htm"
url_mobile = "https://mobilehomo.sis.ad.bia.itau/portal/www/index.html"
url_cca = "https://waslibhomorc.sis.ad.bia.itau/CCA/pages/login.xhtml"
url_crm = (
    "https://sapfiorihw11.sis.ad.bia.itau:8021/sap/bc/ui5_ui5/ui2/ushell/"
    "shells/abap/FioriLaunchpad.html#Shell-home"
)
url_visualizador = (
    "https://mcbohomo.sis.ad.bia.itau/visualizador-logs/login.jsp"
)


# ############ Path de los xml ################
# Desbloqueo de usuarios
path_xml = 'C:/ITAU_Tools/QA_Automation/workspace/Fram27/src/soap'
# Seteo de entornos para allure
allure_xml = 'C:/ITAU_Tools/QA_Automation/workspace/Fram27/src/utils'

if os.getenv("JOB_NAME"):
    
    if os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_50_UIC10020":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10020'
        
    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_50_UIC10021":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10021'

    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_50_UIC10022":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10022'
        
    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_46_UIC10009":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10009'

    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_46_UIC10008":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10008'
        
    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_46_UIC10007":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10007'
        
    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_46_UIC10003":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10003'
        
    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_46_UIC10002":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10002'
        
    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_46_UIC10001":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10001'        
        
    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_37_UIC10011":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10011'  
         
    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_37_UIC10012":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10012'
        
    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_37_UIC10013":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10013'
        
    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_37_UIC10018":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10018'
        
    elif os.environ['JOB_NAME'] == "Caja_ICaja_HOMOLOGACION_suc_37_UIC10019":
        caja_user_sheet_homo_suc_50 = 'TestHOMO_UIC10019'        
        
# caja_user_sheet_homo = os.getenv("CajaUserSheetHomo")
caja_user_sheet_2 = 'Usuarios'
# caja_homo_sheet = 'TestHOMO'
# ########### Definicion de usuarios y contrasenas locales #################
# Se obtiene el usuario y contrasena para el mail. Estos datos se tienen que
# crear en el archivo local_settings, ya que no estan subidos al repo
try:
    from utils.local_settings import usermail, mail_pass
except ImportError:
    usermail = ''
    mail_pass = ''

# Se obtiene el usuario y contrasena para CCA. Estos datos se tienen que
# crear en el archivo local_settings, ya que no estan subidos al repo
try:
    from utils.local_settings import cca_user, cca_pass
except ImportError:
    cca_user = ''
    cca_pass = ''

# Se obtiene el usuario y contrasena para CAJA. Estos datos se tienen que
# crear en el archivo local_settings, ya que no estan subidos al repo
try:
    from utils.local_settings import caja_user, caja_pass
except ImportError:
    caja_user = ''
    caja_pass = ''
