from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.blocks import (
    CharBlock,
    StreamBlock,
    StructBlock,
    URLBlock,
)

##Blocks
class PublicationsItemBlock(StructBlock):
    title = CharBlock(label="titre")
    link = URLBlock(label="Lien du document")


class DocumentBlock(StreamBlock): 
    document_external = PublicationsItemBlock(
        label="Document externe"
    )
    document = DocumentChooserBlock(
        label="Document à télécharger",
    )


##Two types of streamblock 

class OldStreamFieldClass(StreamBlock):
    document = DocumentChooserBlock(
        label="Document (ancien bloc)",
        template="blocks/document_internal.html",
    )



class NewStreamFieldClass(StreamBlock): 
    document_list = DocumentBlock(label="Document")

    document = DocumentChooserBlock(
        label="Document (ancien bloc)",
        template="blocks/document_internal.html",
    )

    
