
import logging
from abc import ABC

logging.basicConfig(level = logging.INFO)

class Document(ABC):

    def __init__(self, filename: str, data: str) -> None :
        self.filename = filename
        self.data = data

    def open(self) -> None:
        logging.info("opening the file {}...".format(self.filename))
    
class WritableDocument(Document):

    def save(self) -> None:
        logging.info("saving the file {}...".format(self.filename))


class Project:

    def __init__(self, documents: list, writableDocuments: list) -> None:
        self.documents = documents
        self.writableDocuments = writableDocuments

    def openAll(self) -> None :
        doc: Document
        for doc in self.documents + self.writableDocuments:
            doc.open()

    def saveAll(self) -> None :
        doc: Document
        for doc in self.writableDocuments:
            doc.save()


planDoc = WritableDocument(filename="plan.docx", data="not completed project plan, needs to be updated soon!")
architectureDoc = Document(filename="architecture(READ ONLY).docx", data="project architecture here!")

someProject = Project(documents=[architectureDoc], writableDocuments=[planDoc])
someProject.openAll()
someProject.saveAll()