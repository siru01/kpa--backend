# Generated by Django 5.2 on 2025-07-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WheelSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('axleBoxHousingBoreDia', models.CharField(max_length=100)),
                ('bearingSeatDiameter', models.CharField(max_length=100)),
                ('condemningDia', models.CharField(max_length=100)),
                ('intermediateWP', models.CharField(max_length=100)),
                ('lastShopIssueSize', models.CharField(max_length=100)),
                ('rollerBearingBoreDia', models.CharField(max_length=100)),
                ('rollerBearingOuterDia', models.CharField(max_length=100)),
                ('rollerBearingWidth', models.CharField(max_length=100)),
                ('treadDiameterNew', models.CharField(max_length=100)),
                ('variationSameAxle', models.CharField(max_length=100)),
                ('variationSameBogie', models.CharField(max_length=100)),
                ('variationSameCoach', models.CharField(max_length=100)),
                ('wheelDiscWidth', models.CharField(max_length=100)),
                ('wheelGauge', models.CharField(max_length=100)),
                ('wheelProfile', models.CharField(max_length=100)),
                ('formNumber', models.CharField(max_length=50, unique=True)),
                ('submittedBy', models.CharField(max_length=100)),
                ('submittedDate', models.DateField()),
            ],
        ),
    ]
