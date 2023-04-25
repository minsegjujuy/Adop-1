from django.apps import AppConfig


class ServicioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Servicio'
    
    def ready(self):
        from Servicio.api.seeds.servicio_seeder import seed_data
        from django.db.models.signals import pre_migrate
        
        def migrate_callback(sender, **kwargs):
            # Verifica que es la primera migración
            if kwargs['using'] == 'default':
                seed_data()

            # Registra la señal
            pre_migrate.connect(migrate_callback, sender=self)