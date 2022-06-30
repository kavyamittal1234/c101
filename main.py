import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)  
        file = open(file_from, 'rb')
        dbx.files_upload(file.read(), file_to)

    

def main():
    access_token = 'sl.BKhLyvpQS9UfqRzyUchEun0u46PkViIiXS1RC83vVTm5-O-50SMQ6OQiqVhfH4hGqSRJg1LnAf7DhKpY8jjsFXzCUfSuMDIZwYkW_zxeLOeITdOmFr6NtKpkTJuzv3eHDxgB3HI'
    transfer_data = TransferData(access_token)
    
    file_from = "C:/Users/Swati/Desktop/101/Trial_text.txt"
    
    file_to = "/Class_Projects/Trial_text.txt"
    
    transfer_data.upload_file(file_from, file_to)
    print("Files has been moved")

main()