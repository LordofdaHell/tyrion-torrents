from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1277114958:AAEYuYGAx6v43bdL0BnKPu9Ws-u6V3w44vg"
    APP_ID = 1406403
    API_HASH = "f2481f41eeaa0bd6b939c30b690fa42f"
    OWNER_ID = 619947188
    AUTH_CHANNEL = [-499982235]
    INDEX_LINK = "https://mrwhite.yobitch.workers.dev/0:/Bot%20Upload"
    DESTINATION_FOLDER = "Lucifer Morningstar" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[tyrion]
type = drive
scope = drive
token = {"access_token":"ya29.A0AfH6SMDEGnYEksNskpjbmkXkhVPaCVH5wBwGQ7Cat5eb4F_H8uQRMLMzZIEBLDgDRDgJKWyN7e63-zLOh70NxnluDzxjBfD4u9BGGfy9jm-ROPxX01gzKNfr9ZLqfWMLwzr09HY5JKvzgmtzx6UVKhF3zphN","token_type":"Bearer","refresh_token":"1//0gnn8qjw0Kx9hCgYIARAAGBASNwF-L9IrrtQgZrpekiPT8ZO92QXVZ7VtSzj49jZAQapaIg39Fafo9Uh3tJ_nf0wfC98qiWwU7go","expiry":"2021-02-25T20:09:03.457983412Z"}
team_drive = 0AFjjOocY2Jp2Uk9PVA
root_folder_id =
"""
