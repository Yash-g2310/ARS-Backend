# Generated by Django 5.1.1 on 2024-09-25 16:58

import attachments.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("assignments", "0002_remove_assignmentteam_submission_count_and_more"),
        (
            "submissions",
            "0002_assignmentsubmission_subtaskstatus_subtasksubmission_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Attachment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to=attachments.models.attachment_upload_path
                    ),
                ),
                (
                    "assignment",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="attachments",
                        to="assignments.assignment",
                    ),
                ),
                (
                    "assignment_submission",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="attachments",
                        to="submissions.assignmentsubmission",
                    ),
                ),
            ],
        ),
    ]
