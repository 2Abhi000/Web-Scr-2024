import requests

cookies = {
    'PMBC': '49dd932ee042c652474c551be57c903b',
    'xf_csrf': '1fulvyqudoWpJf-q',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'PMBC=49dd932ee042c652474c551be57c903b; xf_csrf=1fulvyqudoWpJf-q',
    'DNT': '1',
    'Origin': 'https://altenens.is',
    'Referer': 'https://altenens.is/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'tab_id': '0',
    'modern_statistic_id': '1',
    'hard_reload': 'false',
    '_xfRequestUri': '/',
    '_xfWithData': '1',
    '_xfToken': '1706114120,8ed610fa70c83658c78587461dda9c98',
    '_xfResponseType': 'json',
}

response = requests.post('https://altenens.is/index.php?brms-statistics/load-tab', cookies=cookies, headers=headers, data=data)
print(response.text)
#output
'''{
    "tabContentHtml": "\n\t<ol class=\"brmsContentList u-clearFix\">\n\t\t\n\t\t\t\n\t\t\t\n\t<li class=\"itemStast BRMSToolTip itemThread first\">\n\t\t<div class=\"itemContent\">\n\t\t\t\n\t<div class=\"listBlock counter counter_1\">\n\t\t<span class=\"countNumber\">1</span>\n\t\t<span class=\"arrow\"><span></span></span>\n\t</div>\n\t<div class=\"listBlock itemTitle\">\n\t\t\n\t\t<a href=\"/threads/%E2%AD%90-make-money-reselling-fortnite-accounts-%E2%AD%90-easy-method-%E2%9C%85-january-2024.2198585/\" class=\"\"\n\t\t\tdata-tp-primary=\"on\" data-xf-init=\"brms-tooltip\"\n\t\t\t\n\t\t\tdata-kind=\"thread\"\n\t\t\tdata-box=\"Earnings schemes\"\n\t\t\tdata-view=\"250\"\n\t\t\tdata-rep=\"13\"\n\t\t\tdata-like=\"13\"\n\t\t\t\n\t\t\tdata-preview-url=\"\"><span class=\"label label--silver\" dir=\"auto\">Tutorial</span><span class=\"label-append\">&nbsp;</span> \u2b50 MAKE MONEY RESELLING FORTNITE ACCOUNTS \u2b50 EASY METHOD \u2705 JANUARY 2024</a>\n\t</div>\n\n\t\t\t\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailDate\">\n\t\t\t\t\t<a class=\"paint\" href=\"/threads/%E2%AD%90-make-money-reselling-fortnite-accounts-%E2%AD%90-easy-method-%E2%9C%85-january-2024.2198585/\" title=\"\"><time  class=\"u-dt\" dir=\"auto\" datetime=\"2024-01-24T16:43:54+0000\" data-time=\"1706114634\" data-date-string=\"Jan 24, 2024\" data-time-string=\"4:43 PM\" title=\"Jan 24, 2024 at 4:43 PM\">A moment ago</time></a>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailName\">\n\t\t\t\t\t<a href=\"/members/ghostlygamer.1352519/\" class=\"username \" dir=\"auto\" data-user-id=\"1352519\" data-xf-init=\"member-tooltip\"><span class=\"username--style29\">GhostlyGamer</span></a>\n\t\t\t\t</div>\n\t\t\t\n\t\t</div>\n\t</li>\n\n\t\t\n\t\t\t\n\t\t\t\n\t<li class=\"itemStast BRMSToolTip itemThread\">\n\t\t<div class=\"itemContent\">\n\t\t\t\n\t<div class=\"listBlock counter counter_2\">\n\t\t<span class=\"countNumber\">2</span>\n\t\t<span class=\"arrow\"><span></span></span>\n\t</div>\n\t<div class=\"listBlock itemTitle\">\n\t\t\n\t\t<a href=\"/threads/10gb-porn-turkish.2130669/\" class=\"\"\n\t\t\tdata-tp-primary=\"on\" data-xf-init=\"brms-tooltip\"\n\t\t\t\n\t\t\tdata-kind=\"thread\"\n\t\t\tdata-box=\"Images &amp;  Videos &amp; Porn Accounts\ud83d\udd1e\"\n\t\t\tdata-view=\"1082\"\n\t\t\tdata-rep=\"138\"\n\t\t\tdata-like=\"135\"\n\t\t\t\n\t\t\tdata-preview-url=\"\"> 10GB PORN TURKISH</a>\n\t</div>\n\n\t\t\t\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailDate\">\n\t\t\t\t\t<a class=\"paint\" href=\"/threads/10gb-porn-turkish.2130669/\" title=\"\"><time  class=\"u-dt\" dir=\"auto\" datetime=\"2024-01-24T16:43:07+0000\" data-time=\"1706114587\" data-date-string=\"Jan 24, 2024\" data-time-string=\"4:43 PM\" title=\"Jan 24, 2024 at 4:43 PM\">A moment ago</time></a>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailName\">\n\t\t\t\t\t<a href=\"/members/marbos.1391437/\" class=\"username \" dir=\"auto\" data-user-id=\"1391437\" data-xf-init=\"member-tooltip\">marbos</a>\n\t\t\t\t</div>\n\t\t\t\n\t\t</div>\n\t</li>\n\n\t\t\n\t\t\t\n\t\t\t\n\t<li class=\"itemStast BRMSToolTip itemThread\">\n\t\t<div class=\"itemContent\">\n\t\t\t\n\t<div class=\"listBlock counter counter_3\">\n\t\t<span class=\"countNumber\">3</span>\n\t\t<span class=\"arrow\"><span></span></span>\n\t</div>\n\t<div class=\"listBlock itemTitle\">\n\t\t\n\t\t<a href=\"/threads/%E2%9C%A8-method-%E2%9C%A8-rdp-vps-1month-free-work-%F0%9F%92%AF.2119915/\" class=\"\"\n\t\t\tdata-tp-primary=\"on\" data-xf-init=\"brms-tooltip\"\n\t\t\t\n\t\t\tdata-kind=\"thread\"\n\t\t\tdata-box=\"VPS/RDP\"\n\t\t\tdata-view=\"4422\"\n\t\t\tdata-rep=\"310\"\n\t\t\tdata-like=\"252\"\n\t\t\t\n\t\t\tdata-preview-url=\"\"><span class=\"label label--blue\" dir=\"auto\">RDP</span><span class=\"label-append\">&nbsp;</span> \u2728 METHOD \u2728 RDP/VPS 1MONTH FREE WORK \ud83d\udcaf</a>\n\t</div>\n\n\t\t\t\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailDate\">\n\t\t\t\t\t<a class=\"paint\" href=\"/threads/%E2%9C%A8-method-%E2%9C%A8-rdp-vps-1month-free-work-%F0%9F%92%AF.2119915/\" title=\"\"><time  class=\"u-dt\" dir=\"auto\" datetime=\"2024-01-24T16:42:49+0000\" data-time=\"1706114569\" data-date-string=\"Jan 24, 2024\" data-time-string=\"4:42 PM\" title=\"Jan 24, 2024 at 4:42 PM\">1 minute ago</time></a>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailName\">\n\t\t\t\t\t<a href=\"/members/idedro1120.764769/\" class=\"username \" dir=\"auto\" data-user-id=\"764769\" data-xf-init=\"member-tooltip\">idedro1120</a>\n\t\t\t\t</div>\n\t\t\t\n\t\t</div>\n\t</li>\n\n\t\t\n\t\t\t\n\t\t\t\n\t<li class=\"itemStast BRMSToolTip itemThread\">\n\t\t<div class=\"itemContent\">\n\t\t\t\n\t<div class=\"listBlock counter counter_4\">\n\t\t<span class=\"countNumber\">4</span>\n\t\t<span class=\"arrow\"><span></span></span>\n\t</div>\n\t<div class=\"listBlock itemTitle\">\n\t\t\n\t\t<a href=\"/threads/%E2%9A%A0%EF%B8%8F-very-private-sexy-%E2%9B%94%E2%9B%94-girls-nudes-%E2%9B%94%E2%9B%94-mega-link-18-%E2%9A%A0%EF%B8%8F.2198029/\" class=\"\"\n\t\t\tdata-tp-primary=\"on\" data-xf-init=\"brms-tooltip\"\n\t\t\t\n\t\t\tdata-kind=\"thread\"\n\t\t\tdata-box=\"Images &amp;  Videos &amp; Porn Accounts\ud83d\udd1e\"\n\t\t\tdata-view=\"428\"\n\t\t\tdata-rep=\"44\"\n\t\t\tdata-like=\"39\"\n\t\t\t\n\t\t\tdata-preview-url=\"\"> \u26a0\ufe0f Very Private - Sexy \u26d4\u26d4 Girls Nudes \u26d4\u26d4 [MEGA LINK] 18+ \u26a0\ufe0f</a>\n\t</div>\n\n\t\t\t\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailDate\">\n\t\t\t\t\t<a class=\"paint\" href=\"/threads/%E2%9A%A0%EF%B8%8F-very-private-sexy-%E2%9B%94%E2%9B%94-girls-nudes-%E2%9B%94%E2%9B%94-mega-link-18-%E2%9A%A0%EF%B8%8F.2198029/\" title=\"\"><time  class=\"u-dt\" dir=\"auto\" datetime=\"2024-01-24T16:42:44+0000\" data-time=\"1706114564\" data-date-string=\"Jan 24, 2024\" data-time-string=\"4:42 PM\" title=\"Jan 24, 2024 at 4:42 PM\">1 minute ago</time></a>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailName\">\n\t\t\t\t\t<a href=\"/members/zengoxx97.151417/\" class=\"username \" dir=\"auto\" data-user-id=\"151417\" data-xf-init=\"member-tooltip\"><span class=\"username--style8\">zengoxx97</span></a>\n\t\t\t\t</div>\n\t\t\t\n\t\t</div>\n\t</li>\n\n\t\t\n\t\t\t\n\t\t\t\n\t<li class=\"itemStast BRMSToolTip itemThread\">\n\t\t<div class=\"itemContent\">\n\t\t\t\n\t<div class=\"listBlock counter counter_5\">\n\t\t<span class=\"countNumber\">5</span>\n\t\t<span class=\"arrow\"><span></span></span>\n\t</div>\n\t<div class=\"listBlock itemTitle\">\n\t\t\n\t\t<a href=\"/threads/%F0%9F%94%9E%F0%9F%94%A5%E2%80%A2turk%C4%B0sh-beaut%C4%B0ful-g%C4%B0rl%E2%80%A2%F0%9F%94%A5%F0%9F%94%9E.2087554/\" class=\"\"\n\t\t\tdata-tp-primary=\"on\" data-xf-init=\"brms-tooltip\"\n\t\t\t\n\t\t\tdata-kind=\"thread\"\n\t\t\tdata-box=\"Images &amp;  Videos &amp; Porn Accounts\ud83d\udd1e\"\n\t\t\tdata-view=\"1594\"\n\t\t\tdata-rep=\"149\"\n\t\t\tdata-like=\"64\"\n\t\t\t\n\t\t\tdata-preview-url=\"\"> \ud83d\udd1e\ud83d\udd25\u2022TURK\u0130SH BEAUT\u0130FUL G\u0130RL\u2022\ud83d\udd25\ud83d\udd1e</a>\n\t</div>\n\n\t\t\t\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailDate\">\n\t\t\t\t\t<a class=\"paint\" href=\"/threads/%F0%9F%94%9E%F0%9F%94%A5%E2%80%A2turk%C4%B0sh-beaut%C4%B0ful-g%C4%B0rl%E2%80%A2%F0%9F%94%A5%F0%9F%94%9E.2087554/\" title=\"\"><time  class=\"u-dt\" dir=\"auto\" datetime=\"2024-01-24T16:42:15+0000\" data-time=\"1706114535\" data-date-string=\"Jan 24, 2024\" data-time-string=\"4:42 PM\" title=\"Jan 24, 2024 at 4:42 PM\">1 minute ago</time></a>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailName\">\n\t\t\t\t\t<a href=\"/members/azizd.1191663/\" class=\"username \" dir=\"auto\" data-user-id=\"1191663\" data-xf-init=\"member-tooltip\">azizd</a>\n\t\t\t\t</div>\n\t\t\t\n\t\t</div>\n\t</li>\n\n\t\t\n\t\t\t\n\t\t\t\n\t<li class=\"itemStast BRMSToolTip itemThread\">\n\t\t<div class=\"itemContent\">\n\t\t\t\n\t<div class=\"listBlock counter counter_6\">\n\t\t<span class=\"countNumber\">6</span>\n\t\t<span class=\"arrow\"><span></span></span>\n\t</div>\n\t<div class=\"listBlock itemTitle\">\n\t\t\n\t\t<a href=\"/threads/nude-video-sara-paxton-rape-scene-in-forest-the-last-house-on-the-left.2057692/\" class=\"\"\n\t\t\tdata-tp-primary=\"on\" data-xf-init=\"brms-tooltip\"\n\t\t\t\n\t\t\tdata-kind=\"thread\"\n\t\t\tdata-box=\"Images &amp;  Videos &amp; Porn Accounts\ud83d\udd1e\"\n\t\t\tdata-view=\"1606\"\n\t\t\tdata-rep=\"160\"\n\t\t\tdata-like=\"161\"\n\t\t\t\n\t\t\tdata-preview-url=\"\"> [NUDE VIDEO] Sara Paxton Rape Scene in Forest - The Last House On The Left</a>\n\t</div>\n\n\t\t\t\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailDate\">\n\t\t\t\t\t<a class=\"paint\" href=\"/threads/nude-video-sara-paxton-rape-scene-in-forest-the-last-house-on-the-left.2057692/\" title=\"\"><time  class=\"u-dt\" dir=\"auto\" datetime=\"2024-01-24T16:41:46+0000\" data-time=\"1706114506\" data-date-string=\"Jan 24, 2024\" data-time-string=\"4:41 PM\" title=\"Jan 24, 2024 at 4:41 PM\">2 minutes ago</time></a>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailName\">\n\t\t\t\t\t<a href=\"/members/newgodness.786300/\" class=\"username \" dir=\"auto\" data-user-id=\"786300\" data-xf-init=\"member-tooltip\"><span class=\"username--style8\">newgodness</span></a>\n\t\t\t\t</div>\n\t\t\t\n\t\t</div>\n\t</li>\n\n\t\t\n\t\t\t\n\t\t\t\n\t<li class=\"itemStast BRMSToolTip itemThread\">\n\t\t<div class=\"itemContent\">\n\t\t\t\n\t<div class=\"listBlock counter counter_7\">\n\t\t<span class=\"countNumber\">7</span>\n\t\t<span class=\"arrow\"><span></span></span>\n\t</div>\n\t<div class=\"listBlock itemTitle\">\n\t\t\n\t\t<a href=\"/threads/mega-%E2%AD%90%E2%9D%A3%EF%B8%8Fnew-homemade-porn-pack-08%E2%AD%90%E2%9D%A3%EF%B8%8F10-in-1%E2%AD%90%E2%9D%A3%EF%B8%8Fgrab-asap%E2%9D%A3%EF%B8%8F%E2%AD%90link-working-rn%E2%9C%94%EF%B8%8F.2198205/\" class=\"\"\n\t\t\tdata-tp-primary=\"on\" data-xf-init=\"brms-tooltip\"\n\t\t\t\n\t\t\tdata-kind=\"thread\"\n\t\t\tdata-box=\"Images &amp;  Videos &amp; Porn Accounts\ud83d\udd1e\"\n\t\t\tdata-view=\"356\"\n\t\t\tdata-rep=\"32\"\n\t\t\tdata-like=\"32\"\n\t\t\t\n\t\t\tdata-preview-url=\"\"> [MEGA] \u2b50\u2763\ufe0fNEW HOMEMADE PORN PACK 08\u2b50\u2763\ufe0f10 IN 1\u2b50\u2763\ufe0fGRAB ASAP\u2763\ufe0f\u2b50LINK WORKING RN\u2714\ufe0f</a>\n\t</div>\n\n\t\t\t\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailDate\">\n\t\t\t\t\t<a class=\"paint\" href=\"/threads/mega-%E2%AD%90%E2%9D%A3%EF%B8%8Fnew-homemade-porn-pack-08%E2%AD%90%E2%9D%A3%EF%B8%8F10-in-1%E2%AD%90%E2%9D%A3%EF%B8%8Fgrab-asap%E2%9D%A3%EF%B8%8F%E2%AD%90link-working-rn%E2%9C%94%EF%B8%8F.2198205/\" title=\"\"><time  class=\"u-dt\" dir=\"auto\" datetime=\"2024-01-24T16:41:22+0000\" data-time=\"1706114482\" data-date-string=\"Jan 24, 2024\" data-time-string=\"4:41 PM\" title=\"Jan 24, 2024 at 4:41 PM\">2 minutes ago</time></a>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailName\">\n\t\t\t\t\t<a href=\"/members/ghostlygamer.1352519/\" class=\"username \" dir=\"auto\" data-user-id=\"1352519\" data-xf-init=\"member-tooltip\"><span class=\"username--style29\">GhostlyGamer</span></a>\n\t\t\t\t</div>\n\t\t\t\n\t\t</div>\n\t</li>\n\n\t\t\n\t\t\t\n\t\t\t\n\t<li class=\"itemStast BRMSToolTip itemThread\">\n\t\t<div class=\"itemContent\">\n\t\t\t\n\t<div class=\"listBlock counter counter_8\">\n\t\t<span class=\"countNumber\">8</span>\n\t\t<span class=\"arrow\"><span></span></span>\n\t</div>\n\t<div class=\"listBlock itemTitle\">\n\t\t\n\t\t<a href=\"/threads/x-1-brazzers-premium-access.1538067/\" class=\"\"\n\t\t\tdata-tp-primary=\"on\" data-xf-init=\"brms-tooltip\"\n\t\t\t\n\t\t\tdata-kind=\"thread\"\n\t\t\tdata-box=\"Brazzers Accounts\"\n\t\t\tdata-view=\"2845\"\n\t\t\tdata-rep=\"249\"\n\t\t\tdata-like=\"243\"\n\t\t\t\n\t\t\tdata-preview-url=\"\"><span class=\"label label--green\" dir=\"auto\">Account</span><span class=\"label-append\">&nbsp;</span> X 1 BRAZZERS PREMIUM ACCESS</a>\n\t</div>\n\n\t\t\t\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailDate\">\n\t\t\t\t\t<a class=\"paint\" href=\"/threads/x-1-brazzers-premium-access.1538067/\" title=\"\"><time  class=\"u-dt\" dir=\"auto\" datetime=\"2024-01-24T16:40:46+0000\" data-time=\"1706114446\" data-date-string=\"Jan 24, 2024\" data-time-string=\"4:40 PM\" title=\"Jan 24, 2024 at 4:40 PM\">3 minutes ago</time></a>\n\t\t\t\t</div>\n\t\t\t\t<div class=\"listBlock itemDetail itemDetailName\">\n\t\t\t\t\t<a href=\"/members/cybercaliphate.893715/\" class=\"username \" dir=\"auto\" data-user-id=\"893715\" data-xf-init=\"member-tooltip\"><span class=\"username--style23 username--color-17\">CyberCaliphate</span></a><i data-xf-init=\"tooltip\" data-original-title=\"A verification badge confirms that this is an authentic Page/Profile for this business, organization or person.\" class=\"fa--xf far fa-check-circle fa-lg fa-fw xpvb\" aria-hidden=\"true\"></i>\n\t\t\t\t</div>\n\t\t\t\n\t\t</div>\n\t</li>\n\n\t\t\n\t</ol>\n",
    "limit": 15,
    "tabId": 0
}'''