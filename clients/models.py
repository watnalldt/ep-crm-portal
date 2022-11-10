from django.db import models
from django.urls import reverse

from account_managers.models import AccountManager
from client_managers.models import ClientManager
from core.models import TimeStampedModel


class ClientsManager(models.Manager):
    def get_queryset(self):
        return (
            super(ClientsManager, self)
            .get_queryset()
            .prefetch_related("account_manager", "client_manager")
        )


class Client(TimeStampedModel):
    client = models.CharField(max_length=255, unique=True)
    account_manager = models.ForeignKey(
        AccountManager,
        on_delete=models.CASCADE,
        related_name="account_manager_clients",
    )
    client_manager = models.ForeignKey(
        ClientManager,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="client_manager_clients",
    )

    objects = ClientsManager()

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.client

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this client."""
        return reverse("clients:client_contracts", args=[str(self.id)])
