# Generated by Django 4.1.5 on 2023-01-09 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CDCs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=64, unique=True, verbose_name='ОКД')),
            ],
            options={
                'verbose_name': 'ОКД',
                'verbose_name_plural': 'ОКД',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ClueAttrs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Значащий атрибут',
                'verbose_name_plural': 'Значащие атрибуты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DataObjects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Объект данных')),
            ],
            options={
                'verbose_name': 'Объект данных логического узла',
                'verbose_name_plural': 'Объекты данных логического узла',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Datasets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Датасет')),
            ],
            options={
                'verbose_name': 'Датасет',
                'verbose_name_plural': 'Датасеты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LNobject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('func_group', models.IntegerField(default=-1, verbose_name='Функ. группа')),
                ('cus', models.CharField(choices=[('+', '+'), ('-', '-')], default='-', max_length=1, verbose_name='ЦУС')),
                ('rdu', models.CharField(choices=[('+', '+'), ('-', '-')], default='-', max_length=1, verbose_name='РДУ')),
                ('ras', models.CharField(choices=[('+', '+'), ('-', '-'), ('П', 'П')], default='-', max_length=1, verbose_name='РАС')),
                ('sgras_name', models.CharField(blank=True, max_length=256, verbose_name='Обозначение РАС/Уставка')),
                ('signal_type', models.CharField(choices=[('Внутр', 'Внутренний сигнал'), ('ВнутрШтрих', 'Внутренний штриховой'), ('-', 'Без прорисовки')], default='-', max_length=32, verbose_name='Тип сигнала (чертеж)')),
                ('signal_number', models.IntegerField(default=0, verbose_name='Номер выхода (чертеж)')),
                ('cdc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.cdcs', verbose_name='ОКД')),
                ('clue_attr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.clueattrs', verbose_name='Значащий атрибут')),
                ('data_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.dataobjects', verbose_name='Объект данных')),
                ('dataset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.datasets', verbose_name='Датасет')),
            ],
            options={
                'verbose_name': 'Объект логического узла',
                'verbose_name_plural': 'Объекты логических узлов',
                'ordering': ['data_object'],
            },
        ),
        migrations.CreateModel(
            name='LogicDevices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Обозначение логического устройства')),
                ('fb_name', models.CharField(max_length=128, unique=True, verbose_name='Обозначение функционального блока')),
                ('description', models.TextField(blank=True, max_length=1024, verbose_name='Назначение логического устройства (ФБ)')),
            ],
            options={
                'verbose_name': 'Логическое устройство',
                'verbose_name_plural': 'Логические устройства',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LogicNodeInstantiated',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=64, unique=True, verbose_name='Краткое имя (например: БУ или ДЗТ)')),
                ('full_name', models.CharField(blank=True, max_length=128, verbose_name='Полное имя')),
                ('ln_prefix', models.CharField(blank=True, max_length=32, verbose_name='Префикс ЛУ')),
                ('class_name', models.CharField(max_length=4, verbose_name='Класс (например: PDIF)')),
                ('instance', models.IntegerField(blank=True, null=True, verbose_name='Номер экземпляра')),
            ],
            options={
                'verbose_name': 'Экземпляр логического узла',
                'verbose_name_plural': 'Экземпляр логического узла',
                'ordering': ['short_name'],
            },
        ),
        migrations.CreateModel(
            name='LogicNodesTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Имя типа ЛУ')),
                ('description', models.TextField(blank=True, max_length=1024, verbose_name='Описание')),
                ('explanation', models.TextField(blank=True, max_length=2048, verbose_name='Пояснение')),
            ],
            options={
                'verbose_name': 'Тип логического узла',
                'verbose_name_plural': 'Типы логических узлов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SG_modes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Статусы програмного переключателя')),
            ],
            options={
                'verbose_name': 'Программный переключатель',
                'verbose_name_plural': 'Программные переключатели',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Signals',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Сигналы')),
            ],
            options={
                'verbose_name': 'Перечень сигналов',
                'verbose_name_plural': 'Перечни сигналов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Статусы сигнала')),
            ],
            options={
                'verbose_name': 'Статус сигнала',
                'verbose_name_plural': 'Статусы сигнала',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sw_type', models.CharField(choices=[('SW.2', 'SW.2'), ('SW.3', 'SW.3')], default='SW.2', max_length=4, verbose_name='Тип')),
                ('short_name', models.CharField(max_length=32, verbose_name='Краткое обозначение')),
                ('description', models.TextField(blank=True, max_length=1024, verbose_name='Назначение')),
            ],
            options={
                'verbose_name': 'Переключатель',
                'verbose_name_plural': 'Переключатели',
                'ordering': ['sw_type'],
            },
        ),
        migrations.CreateModel(
            name='Terminals',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Обозначение ИЭУ')),
                ('description', models.TextField(blank=True, max_length=1024, verbose_name='Назначение ИЭУ')),
            ],
            options={
                'verbose_name': 'ИЭУ',
                'verbose_name_plural': 'ИЭУ',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SwitchesAndLNs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ln', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.logicnodeinstantiated', verbose_name='Экземпляр лог. узла')),
                ('switch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.switch', verbose_name='Переключатель')),
            ],
            options={
                'verbose_name': 'Переключатель в составе ФБ',
                'verbose_name_plural': 'Переключатели в составе ФБ',
                'ordering': ['switch'],
            },
        ),
        migrations.CreateModel(
            name='PhDLDconnections',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ied', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.terminals', verbose_name='Физическое устройство')),
                ('ld', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.logicdevices', verbose_name='Логическое устройство')),
            ],
            options={
                'verbose_name': 'Связь между физическими и логическими устройствами',
                'verbose_name_plural': 'Связи между физическими и логическими устройствами',
                'ordering': ['ied'],
            },
        ),
        migrations.AddField(
            model_name='logicnodeinstantiated',
            name='ln_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.logicnodestypes', verbose_name='Тип ЛУ'),
        ),
        migrations.CreateModel(
            name='LNtypeObjConnections',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ln_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.lnobject', verbose_name='Объект лог. узла')),
                ('ln_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.logicnodestypes', verbose_name='Тип логического узла')),
            ],
            options={
                'verbose_name': 'Связь между типом логического узла и объектами',
                'verbose_name_plural': 'Связи между типами логических узлов и объектами',
                'ordering': ['ln_type'],
            },
        ),
        migrations.AddField(
            model_name='lnobject',
            name='sg_modes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.sg_modes', verbose_name='Состояние программного ключа'),
        ),
        migrations.AddField(
            model_name='lnobject',
            name='signal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.signals', verbose_name='Сигнал'),
        ),
        migrations.AddField(
            model_name='lnobject',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.statuses', verbose_name='Статус сигнала'),
        ),
        migrations.CreateModel(
            name='LDLNconnections',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ld', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.logicdevices', verbose_name='Логическое устройство')),
                ('ln', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.logicnodeinstantiated', verbose_name='Экземпляр лог. узла')),
            ],
            options={
                'verbose_name': 'Связь между логическими устройствами и экземплярами логических узлов',
                'verbose_name_plural': 'Связи между логическими устройствами и экземплярами логических узлов',
                'ordering': ['ld'],
            },
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4, verbose_name='Обозначение входа (напр.: С1, А4)')),
                ('number', models.IntegerField(default=0, verbose_name='Номер входа')),
                ('sw_type', models.CharField(choices=[('SW.2', 'SW.2'), ('SW.3', 'SW.3'), ('-', '-')], default='-', max_length=4, verbose_name='Тип переключателя')),
                ('sw_name', models.CharField(blank=True, max_length=32, verbose_name='Обозначение переключателя')),
                ('description', models.CharField(max_length=128, verbose_name='Описание входа (напр.: АСУ / Режим работы)')),
                ('ln_inst', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.logicnodeinstantiated', verbose_name='Экземпляр ЛУ к которому привязан вход')),
            ],
            options={
                'verbose_name': 'Вход',
                'verbose_name_plural': 'Входы',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Cabinets',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='Обозначение шкафа')),
                ('description', models.TextField(max_length=1024, verbose_name='Назначение шкафа')),
                ('terminal1', models.ForeignKey(max_length=64, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ied1_set', to='mainapp.terminals', verbose_name='ИЭУ1')),
                ('terminal2', models.ForeignKey(blank=True, max_length=64, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ied2_set', to='mainapp.terminals', verbose_name='ИЭУ2')),
                ('terminal3', models.ForeignKey(blank=True, max_length=64, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ied3_set', to='mainapp.terminals', verbose_name='ИЭУ3')),
            ],
            options={
                'verbose_name': 'Шкаф',
                'verbose_name_plural': 'Шкафы',
                'ordering': ['name'],
            },
        ),
    ]
