
    'uid': user_info['uid'],
    'token': user_info['token'],
    'branchNo': user_info['branch_no'],
    'fundAccount': user_info['fund_account'],
    'version': version,
    'client': 'android',
    'deviceId': user_info['device_id'],
    'timestamp': timestamp(),
    'encrypt': '1',
    'amount': str(num),
    'erpCode': erp_code,
    "gpFundCode": erp_code,
    'payType': '-128',
    'score': '0',
    'paymentAmount': str(int(price) * num),
    'productAmount': str(int(price) * num),
    'usePlusPrice': '0',
    'shoppingScore': str(int(price) * num),
    'orderType': '11',
    'wineType': '0',
    'addressId': user_info['addr_id'],
    'insuranceCost': '0',
    'packCost': '0',
    'expressCost': '0',
    'appkey': appkey,
    'queueCode': queue_code

encoded = urllib.parse.urlencode(params)
params['__S__'] = js_context.call('get_signcode_with_s', encoded, user_info['code'])['__S__']
api = "/api/transaction/purchasePlaceOrder.decryption"
