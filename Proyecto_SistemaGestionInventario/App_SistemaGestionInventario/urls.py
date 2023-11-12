from django.urls import path
from App_SistemaGestionInventario import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="index_principal"),

    #Plantillas generales
    path('index_info/', views.index_info, name="index_info"),
    path('in_se/', views.login_cuenta, name="login_cuenta"),
    path('veri_usu', views.verificar_usuario, name="verificar_usuario"),
    path('veri_contra', views.verificar_contrasena, name="verificar_contrasena"),
    
    
    #Plantillas instructor de planta
    path('fun_ins_planta/', views.funciones_instructor_planta, name="funciones_instructor_planta"),
    path('lis_usu_planta', views.lista_usuarios_planta, name="lista_usuarios"),
    path('regis_mate_ins_planta/', views.registrar_material_instructor_planta, name="registrar_material_instructor_planta"),
    path('lis_mate_consu_planta/', views.listar_materiales_consumibles_planta, name="listar_materiales_consumibles_planta"),
    path('lis_mate_devo_planta/', views.listar_materiales_devolutivos_planta, name="listar_materiales_devolutivos_planta"),
    path('calen_planta/', views.calendario_planta, name="calendario_planta"),
    path('lis_mate_garan_planta/', views.listar_material_garantia_planta, name="listar_material_garantia_planta"),
    path('lis_mate_baja_planta/', views.listar_material_baja_planta, name="listar_material_baja_planta"),
    path('lis_mate_sopor_planta/', views.listar_material_soporte_planta, name="listar_material_soporte_planta"),
    path('entre_consu_planta/', views.entregable_consumible_planta, name="entregable_consumible_planta"),
    path('entre_devo_planta/', views.entregable_devolutivo_planta, name="entregable_devolutivo_planta"),
    path('ver_cuenta_planta/', views.visualizar_cuenta_planta, name="visualizar_cuenta_planta"),
    path('generar_reportes/', views.generar_reporte, name="generar_reporte"),
    path('generar-reporte-pdf/', views.generar_reporte_pdf_materiales, name='generar_reporte_pdf'),
    path('generar_excel/', views.generar_excel_materiales, name='generar_excel'),
    path('generar_excel_prestamo/', views.generar_excel_prestamo, name='generar_excel_prestamo'),
    path('generar_excel_consumible/', views.generar_excel_consumible, name='generar_excel_consumible'),
    path('generar_excel_clientes/', views.generar_excel_clientes, name='generar_excel_clientes'),
    path('generar_excel_usuario/', views.generar_excel_usuario, name='generar_excel_usuario'),



    #Plantillas instructor de contrato
    path('fun_ins_contra/', views.funciones_instructor_contrato, name="funciones_instructor_contrato"),
    path('lis_usu_contra', views.listar_usuarios_contrato, name="lista_usuarios_contra"),
    path('regis_mate_ins_contra/', views.registrar_materiales_instructor_contrato, name="registrar_materiales_instructor_contrato"),
    path('calen_contra/', views.calendario_contrato, name="calendario_contrato"),
    path('lis_mate_baja_contra/', views.listar_material_baja_contrato, name="listar_material_baja_contrato"),
    path('lis_mate_consu_contra/', views.listar_material_consumible_contrato, name="listar_material_consumible_contrato"),
    path('lis_mate_devo_contra/', views.listar_material_devolutivo_contrato, name="listar_material_devolutivo_contrato"),
    path('lis_mate_garan_contra/', views.listar_material_garantia_contrato ,name="listar_material_garantia_contrato"),
    path('lis_mate_sup_contra/', views.listar_material_soporte_contrato, name="listar_material_soporte_contrato"),
    path('entre_consu_contra/', views.entregable_consumible_contrato, name="entregable_consumible_contrato"),
    path('entre_devo_contra/', views.entregable_devolutivo_contrato, name="entregable_devolutivo_contrato"),


    #Plantillas monitor
    path('fun_moni/', views.funciones_monitor, name="funciones_monitor"),
    path('lis_usu_moni/', views.listar_usuarios_monitor, name="listar_usuarios_monitor"),
    path('lis_mate_devo_moni/', views.listar_material_devolutivo_monitor, name="listar_material_devolutivo_monitor"),
    path('lis_mate_consu_moni/', views.listar_material_consumible_monitor, name="listar_material_consumible_monitor"),
    path('entre_consu_moni/', views.entregable_consumible_monitor, name="entregable_consumible_monitor"),
    path('entre_devo_moni/', views.entregable_devolutivo_monitor, name="entregable_devolutivo_monitor"),
    path('calen_moni/', views.calendario_monitor, name="calendario_monitor"),
    path('regis_mate_moni/', views.registrar_material_monitor, name="registrar_material_monitor"),

]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)