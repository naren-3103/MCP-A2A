from pathlib import Path

class DocumentReaderTool:
    name = "read_document"
    description = "Reads a text document from disk"

    def run(self, input_data):
        path = Path(input_data["path"]).resolve()
        if not path.exists():
            raise FileNotFoundError(path)

        return path.read_text(encoding="utf-8")
