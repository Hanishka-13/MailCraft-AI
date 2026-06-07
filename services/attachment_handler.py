import mimetypes
def prepare_attachments(uploaded_files):
    attachments=[]
    for file in uploaded_files:
        mime_type,_=mimetypes.guess_type(file.name)
        if mime_type:
            maintype,subtype=mime_type.split("/")
        else:
            maintype="application"
            subtype="octet-stream"
        attachments.append(
            {
                "filename":file.name,
                "content":file.read(),
                "maintype":maintype,
                "subtype":subtype
            }
        )
    return attachments