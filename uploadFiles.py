import dropbox

class TransferData:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken

    def fileUpload(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.accesstoken)

        f = open(fileFrom,'rb')
        dbx.files_upload(f.read(),fileTo)

def main():
    myAT = 'm0XQGrupZv4AAAAAAAAAAW23BTzCXtRyf65kOPbAKd4EuXRuiRsXaWGb9WFSYPwY'
    transferData1 = TransferData(myAT)

    source = input('Enter the path of the filr which is to be transferred: ')
    destination = input('Enter the path of the dropbox folder: ')

    transferData1.fileUpload(source,destination)

main()