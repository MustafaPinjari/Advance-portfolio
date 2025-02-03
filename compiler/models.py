from django.db import models

class CodeHistory(models.Model):
    code = models.TextField()  # The Python code executed
    output = models.TextField()  # Output from the execution
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of execution

    def __str__(self):
        return f"Code executed at {self.timestamp}"
