import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadFile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token) 
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = "sl.A8KlI6LXKyoe8tfy28GS5Hy_YvSJLD1i7UowN6Jm7MrErrHjccqTX8mjlllI_RTKPB2XQzbN469h-GKMjaO2VQDFoacc-zlsboVec8YP6s2BnMoZhrib8O9SOq-eW3Nmwc8ZMmLHT4oE"
    transferData = TransferData(access_token)
    file_from = input("enter the file")
    file_to = input("enter the path to upload")
    transferData.uploadFile(file_from,file_to)
    print("File has been moved")

main()