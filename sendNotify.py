#sendNotify
import requests as rs

class LineNotify:

    def lineNotifyMessage(self,token, msg, img):
        
        headers = {
            "Authorization": "Bearer " + token, 
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            'message': msg,             
            'imageThumbnail': img,
            'imageFullsize' : img
        }

        r = rs.post(
            "https://notify-api.line.me/api/notify",
            headers=headers, 
            params=payload)
        return r.status_code
