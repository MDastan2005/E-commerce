from django.db import models

# Create your models here.
class Cart(models.Model):
	cart_total = models.SmallIntegerField()
	items: list[int] = []

	def add_item(self, item_id: int):
		self.items.append(item_id)