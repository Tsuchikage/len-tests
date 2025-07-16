import os
from uuid import uuid4

class WorkspaceData:
    def __init__(self, email: str = "test@test.com", code: str = "666555"):
        self.email = email
        self.code = code
        self.workspace_name = f"autotest_{str(uuid4())[:8]}"
        self.first_name = "Test"
        self.last_name = "Testov"

        current_file = os.path.abspath(__file__)
        project_root = current_file.split("tests")[0] + "tests"
        avatar_path = os.path.join(project_root, "autotests", "ui", "smoke", "workspace", "data", "avatar.png")

        self.data = {
            "email": self.email,
            "code": self.code,
            "workspace_name": self.workspace_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "avatar_path": avatar_path,
        }
