# Generated by Django 5.1.1 on 2024-10-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "assignments",
            "0004_alter_assignment_title_alter_assignmentdetails_title_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="assignmentteam",
            name="team_status",
            field=models.CharField(
                choices=[
                    ("submitted", "Submitted"),
                    ("not_submitted", "Not_Submitted"),
                    ("completed", "Completed"),
                ],
                default="not_submitted",
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="assignment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, default="2024-10-10T11:59:59Z"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="assignment",
            name="upload_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="assignmentsubtask",
            name="tag",
            field=models.CharField(
                choices=[
                    ("compulsory", "Compulsory"),
                    ("optional", "Optional"),
                    ("brownie_point", "Brownie_Points"),
                ],
                default="optional",
                max_length=50,
            ),
        ),
    ]
