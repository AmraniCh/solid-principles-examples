
import logging
from abc import ABC

logging.basicConfig(level = logging.INFO)

class Document(ABC):

    def __init__(self, filename: str, data: str) -> None :
        self.filename = filename
        self.data = data

    def open(self) -> None:
        logging.info("opening the file {}...".format(self.filename))

    def save(self) -> None:
        logging.info("saving the file {}...".format(self.filename))

class ReadOnlyDocument(Document):

    def save(self) -> None:
        raise RuntimeError("Unable to save read only file")
    
class Project:

    def __init__(self, documents: list) -> None:
        self.documents = documents

    def openAll(self) -> None :
        doc: Document
        for doc in self.documents:
            doc.open()

    def saveAll(self) -> None :
        doc: Document
        for doc in self.documents:
            if not isinstance(doc, ReadOnlyDocument):
                doc.save()


planDoc = Document(filename="plan.docx", data="my project plan!!")
architectureDoc = ReadOnlyDocument(filename="architecture.docx", data="project architecture here!")

someProject = Project([
    planDoc,
    architectureDoc
])
someProject.openAll()
someProject.saveAll()