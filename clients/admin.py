from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from account_managers.models import AccountManager
from client_managers.models import ClientManager

from .models import Client


class ClientResource(resources.ModelResource):

    account_manager = fields.Field(
        column_name="account_manager",
        attribute="account_manager",
        widget=ForeignKeyWidget(AccountManager, field="account_manager__email"),
    )

    client_manager = fields.Field(
        column_name="client_manager",
        attribute="client_manager",
        widget=ForeignKeyWidget(ClientManager, field="client_manager__email"),
    )

    class Meta:
        model = Client
        skip_unchanged = True
        report_skipped = True
        fields = [
            "id",
            "client",
            "account_manager",
            "client_manager",
        ]
        import_id_fields = ["id"]

        export_order = [
            "client",
            "account_manager",
            "client_manager",
        ]


class ClientAdmin(ImportExportModelAdmin):
    show_full_result_count = False
    resource_class = ClientResource
    list_display = ("client", "account_manager", "client_manager", "id")
    autocomplete_fields = ("account_manager", "client_manager")
    search_fields = ("client",)
    list_per_page = 25
    search_help_text = "Search by Client Name"


admin.site.register(Client, ClientAdmin)
