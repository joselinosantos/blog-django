# Generated by Django 3.2.6 on 2021-08-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('programacao', 'Python'), ('raspberry', 'Raspberry Pi'), ('sql', 'SQL'), ('web', 'Web'), ('datascience', 'DataScience')], default=1, max_length=11),
            preserve_default=False,
        ),
    ]