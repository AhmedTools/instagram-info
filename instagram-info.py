from requests import request
from base64 import urlsafe_b64encode
from json import dumps

def encID(sessionid: str):
	IGT = urlsafe_b64encode(dumps({"ds_user_id": sessionid.split('%')[0],"sessionid": sessionid}).encode("utf-8")).decode()
	return IGT

def info(id: str ,sessionid: str ,count=30) -> str:
	headers={'user-agent': 'Instagram 315.0.0.0.20 Android (34/14; 480dpi; 1080x2191; HONOR; LLY-LX1; HNLLY-Q; qcom; en_US; 555314045)'}
	if "%" in sessionid:
		JWT = encID(sessionid=sessionid)
		headers['authorization'] = f'Bearer IGT:2:{JWT}'
	response = request(method="GET",url=f"https://i.instagram.com/api/v1/users/{id}/info/",headers=headers).text
	return response

if __name__ == '__main__':
	print(
		info(id=input("– Enter instagram ID : ") ,sessionid=input("– Enter SessionID ( you can SKIP ) : "))
	)