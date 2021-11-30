# Generated by Django 3.2.9 on 2021-11-30 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact_number', models.IntegerField(max_length=100, unique=True)),
                ('employee_id', models.IntegerField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventorymodel',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.CharField(max_length=100)),
                ('desigener', models.CharField(max_length=100)),
                ('manager', models.CharField(max_length=100)),
                ('lead', models.CharField(max_length=100)),
                ('architect', models.CharField(max_length=100)),
                ('sales_manager', models.CharField(max_length=100)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.employees')),
            ],
        ),
        migrations.CreateModel(
            name='Ordermodel',
            fields=[
                ('oid', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=40)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='mainapp.inventorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software', models.CharField(max_length=100)),
                ('Marketing', models.CharField(max_length=100)),
                ('sales', models.IntegerField(max_length=100)),
                ('Design', models.CharField(max_length=100)),
                ('production', models.CharField(max_length=100)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.employees')),
            ],
        ),
        migrations.CreateModel(
            name='customer_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('business', models.CharField(max_length=100)),
                ('contact_number', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('marketing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.departments')),
                ('sales_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.roles')),
            ],
        ),
    ]
