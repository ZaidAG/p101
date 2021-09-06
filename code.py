import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token='sl.A3f_tVkt-q1xl2WQ4WouKqWVGYAcXn7rwdHz5PxGgl7D_JgN1ZAtngmohU1qviNjPyIeyxia-4v6ACgXWXEhkkjYU7bm7vzv9qLfg84mmd3dOKVS-APZ_Rgt2bttySmJi5fy7Gs'
    transferData=TransferData(access_token)
    file_from=input("enter the file path to transfer:-")
    file_to=input("enter the full path transfer to dropbox:-")
    transferData.upload_file(file_from,file_to)
    print("file has been moved")
main()