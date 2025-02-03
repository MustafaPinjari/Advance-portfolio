from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import subprocess
from .models import CodeHistory
from .serializers import CodeHistorySerializer

class ExecuteCodeView(APIView):
    """
    Handles execution of Python code sent from the frontend.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        code = request.data.get("code", "")
        if not code.strip():
            return Response({"output": "Error: No code provided."}, status=400)

        try:
            # Execute Python code
            result = subprocess.run(
                ["python", "-c", code],
                capture_output=True,
                text=True,
                timeout=5,
            )
            output = result.stdout if result.returncode == 0 else result.stderr
        except subprocess.TimeoutExpired:
            output = "Error: Code execution timed out."
        except Exception as e:
            output = f"Error: {str(e)}"

        # Save the execution result to history
        CodeHistory.objects.create(code=code, output=output)

        return Response({"output": output})


class CodeHistoryView(APIView):
    """
    Returns a history of all executed code.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        history = CodeHistory.objects.all().order_by('-timestamp')
        serializer = CodeHistorySerializer(history, many=True)
        return Response(serializer.data)


def editor_view(request):
    """
    Renders the editor page.
    """
    return render(request, "compiler/editor.html")
