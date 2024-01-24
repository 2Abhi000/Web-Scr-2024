import requests

cookies = {
    'PMBC': '9900e0795f3ff4e57230bf97b0c7e4d0',
    'xf_csrf': 'vgPsCgaDmn15i5F-',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'PMBC=9900e0795f3ff4e57230bf97b0c7e4d0; xf_csrf=vgPsCgaDmn15i5F-',
    'Referer': 'https://altenens.is/award-system/list?category=9',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://altenens.is/index.php?threads/atn-official-rules.594/', cookies=cookies, headers=headers)
print(response.text)

#Output - content file"
'''
<!DOCTYPE html>
<html id="XF" lang="en-US" dir="LTR"
	data-app="public"
	data-template="error"
	data-container-key=""
	data-content-key=""
	data-logged-in="false"
	data-cookie-prefix="xf_"
	data-csrf="1706114610,b25f1165ac59a70621741b355ae33adf"
	class="XenMake has-no-jstemplate-error "
	>
<head>
	
	<!-- 
		       db        88                                                       
		      d88b       88   ,d                                                  
		     d8'`8b      88   88                                                  
		    d8'  `8b     88 MM88MMM ,adPPYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,   
		   d8YaaaaY8b    88   88   a8P_____88 88P'   `"8a a8P_____88 88P'   `"8a  
		  d8""""""""8b   88   88   8PP""""""" 88       88 8PP""""""" 88       88  
		 d8'        `8b  88   88,  "8b,   ,aa 88       88 "8b,   ,aa 88       88  
		d8'          `8b 88   "Y888 `"Ybbd8"' 88       88  `"Ybbd8"' 88       88  
		+ ---------------------- Card The Fucking World  ---------------------- +                                                               
	-->
	
	<meta charset="utf-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=Edge" />
	<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">

	
	
	

	<title>Oops! We ran into some problems. | Altenen - Trust and Safety</title>

	

	
		
	
	
	<meta property="og:site_name" content="Altenen - Trust and Safety" />


	
	
		
	
	
	<meta property="og:type" content="website" />


	
	
		
	
	
	
		<meta property="og:title" content="Oops! We ran into some problems." />
		<meta property="twitter:title" content="Oops! We ran into some problems." />
	


	
	
	
		
	
	
	<meta property="og:url" content="https://altenens.is/index.php?threads/atn-official-rules.594/" />


	
	

	
		<meta name="theme-color" content="#313d46" />
	

	
	

	
	<link rel="preload" href="/styles/fonts/fa/fa-regular-400.woff2" as="font" type="font/woff2" crossorigin="anonymous" />


	<link rel="preload" href="/styles/fonts/fa/fa-solid-900.woff2" as="font" type="font/woff2" crossorigin="anonymous" />


<link rel="preload" href="/styles/fonts/fa/fa-brands-400.woff2" as="font" type="font/woff2" crossorigin="anonymous" />

	<link rel="stylesheet" href="/css.php?css=public%3Anormalize.css%2Cpublic%3Acore.less%2Cpublic%3Aapp.less&amp;s=2&amp;l=1&amp;d=1697996256&amp;k=77943d4df536047c4405eaf17c8bbfadb8e55db8" />

	<link rel="stylesheet" href="/css.php?css=public%3Ashare_controls.less%2Cpublic%3Ath_covers.less%2Cpublic%3Axenmake.less%2Cpublic%3Axm_advancedFooter.less%2Cpublic%3Axp_vb.less%2Cpublic%3Aextra.less&amp;s=2&amp;l=1&amp;d=1697996256&amp;k=78470e85edf9351c190a65e177daa632657e5b29" />

	
		<script src="/js/xf/preamble.min.js?_v=305eb201"></script>
	


	
		<link rel="icon" type="image/png" href="https://altenens.is/favicon.ico" sizes="32x32" />
	
	
	
	
	<!--XenForo_Require:CSS-->
	
	
	<script>
	window.onload = function () {
		$('span:contains("Z33 Verified")').closest('.contentRow').remove();
	}
	</script>
	

</head>
<body data-template="error">

<div class="p-pageWrapper" id="top">


<div class="p-staffBar">
	<div class="p-staffBar-inner">	
		<div class="p-staffBar-content">
			
				<div class="p-nav-opposite">
    <div class="p-navgroup p-account p-navgroup--guest">
        
	    	<a href="/login/" class="p-navgroup-link p-navgroup-link--textual p-navgroup-link--logIn"
			data-xf-click="overlay" data-follow-redirects="on">
			<span class="p-navgroup-linkText"><i class="fas fa-key" aria-hidden="true"></i> Log in</span>
		</a>
		
			<a href="/register/" class="p-navgroup-link p-navgroup-link--textual p-navgroup-link--register"
				data-xf-click="overlay" data-follow-redirects="on">
				<span class="p-navgroup-linkText"><i class="fas fa-user-plus" aria-hidden="true"></i> Register</span>
			</a>
		
        
    </div>

    <div class="p-navgroup p-discovery">
    <a href="/whats-new/"
		class="p-navgroup-link p-navgroup-link--iconic p-navgroup-link--whatsnew"
		aria-label="What&#039;s new"
		title="What&#039;s new">
		<i aria-hidden="true"></i>
		<span class="p-navgroup-linkText">What's new</span>
	</a>

        
		<a href="/search/"
			class="p-navgroup-link p-navgroup-link--iconic p-navgroup-link--search"
			data-xf-click="menu"
			data-xf-key="/"
			aria-label="Search"
			aria-expanded="false"
			aria-haspopup="true"
			title="Search">
			<i aria-hidden="true"></i>
			<span class="p-navgroup-linkText">Search</span>
		</a>
        <div class="menu menu--structural menu--wide" data-menu="menu" aria-hidden="true">
	    	<form action="/search/search" method="post"
			class="menu-content"
			data-xf-init="quick-search">

			<h3 class="menu-header">Search</h3>
			
			<div class="menu-row">
				
					<input type="text" class="input" name="keywords" placeholder="Search…" aria-label="Search" data-menu-autofocus="true" />
				
			</div>

				
				<div class="menu-row">
					<label class="iconic"><input type="checkbox"  name="c[title_only]" value="1" /><i aria-hidden="true"></i><span class="iconic-label">Search titles only</span></label>

				</div>
				
				<div class="menu-row">
					<div class="inputGroup">
						<span class="inputGroup-text" id="ctrl_search_menu_by_member">By:</span>
						<input type="text" class="input" name="c[users]" data-xf-init="auto-complete" placeholder="Member" aria-labelledby="ctrl_search_menu_by_member" />
					</div>
				</div>
				<div class="menu-footer">
					<span class="menu-footer-controls">
						<button type="submit" class="button--primary button button--icon button--icon--search"><span class="button-text">Search</span></button>
						<a href="/search/" class="button"><span class="button-text">Advanced search…</span></a>
					</span>
				</div>
				<input type="hidden" name="_xfToken" value="1706114610,b25f1165ac59a70621741b355ae33adf" />
			</form>
		</div>
	    
		
	</div>
</div>
					
			
		</div>	
	</div>
</div>


<header class="p-header  " id="header">

	<div class="p-header-inner">
		<div class="p-header-content">

			<div class="p-header-logo p-header-logo--image">
				<a href="https://altenens.is">
				
					<img src="/styles/xenmake/innovate-dark/_custom/card.png"
						alt="Altenen - Trust and Safety"
						 />
						
				</a>
			</div>
			
								
					
	
<div class="block">
	<div class="block-container">
		<h3><i class=""></i> Follow Us On Social Media</h3>			
		<div class="divider fw"></div>
		<div class="block-body block-row">	
			<div class="shareButtons shareButtons--iconic">
				

						

					
						<a class="shareButtons-button shareButtons-button--brand shareButtons-button--twitter" href="https://twitter.com/group_atn" target="_blank">
							<i aria-hidden="true"></i>
							<span>Twitter</span>
						</a>
					

					
					
					
					
					

					
					
					
					
					
					
					
					
					
					
					
						<a class="shareButtons-button shareButtons-button--brand shareButtons-button--instagram" href="https://www.instagram.com/altenen.official/" target="_blank">
							<i aria-hidden="true"></i>
							<span>Instagram</span>
						</a>
					
								
					
				
					
					
					
						<a class="shareButtons-button shareButtons-button--brand shareButtons-button--whatsApp" href="https://t.me/altenen_nz" target="_blank">
							<i aria-hidden="true"></i>
							<span>WhatsApp</span>
						</a>
					
					
					
					
					
					
			

			
				
			</div>
		</div>
	</div>
</div>

					
			
			

			
				
		</div>
	</div>
</header>






	
	<nav class="p-nav">
		<div class="p-nav-inner">
<div class="th_holiday__categoryStrip__left"></div>
<div class="th_holiday__categoryStrip__center"></div>
<div class="th_holiday__categoryStrip__right"></div>
				<a class="p-nav-menuTrigger" data-xf-click="off-canvas" data-menu=".js-headerOffCanvasMenu" role="button" tabindex="0">
					<i aria-hidden="true"></i>
					<span class="p-nav-menuText">Menu</span>
				</a>

				<div class="p-nav-smallLogo">
					<a href="https://altenens.is">
						<img src="/styles/xenmake/innovate-dark/_custom/card.png"
							alt="Altenen - Trust and Safety"
						 />
					</a>
				</div>

				<div class="p-nav-scroller hScroller" data-xf-init="h-scroller" data-auto-scroll=".p-navEl.is-selected">
					<div class="hScroller-scroll">
						<ul class="p-nav-list js-offCanvasNavSource">
						
							<li>
								
	<div class="p-navEl " >
		

			
	
	<a href="https://altenens.is"
		class="p-navEl-link "
		
		data-xf-key="1"
		data-nav-id="home">Home</a>


			

		
		
	</div>

							</li>
						
							<li>
								
	<div class="p-navEl is-selected" data-has-children="true">
		

			
	
	<a href="/"
		class="p-navEl-link p-navEl-link--splitMenu "
		
		
		data-nav-id="forums">Forums</a>


			<a data-xf-key="2"
				data-xf-click="menu"
				data-menu-pos-ref="< .p-navEl"
				class="p-navEl-splitTrigger"
				role="button"
				tabindex="0"
				aria-label="Toggle expanded"
				aria-expanded="false"
				aria-haspopup="true"></a>

		
		
			<div class="menu menu--structural" data-menu="menu" aria-hidden="true">
				<div class="menu-content">
					<!--<h4 class="menu-header">Forums</h4>-->
					
						
	
	
	<a href="/whats-new/posts/"
		class="menu-linkRow u-indentDepth0 js-offCanvasCopy "
		
		
		data-nav-id="newPosts">New posts</a>

	

					
						
	
	
	<a href="/search/?type=post"
		class="menu-linkRow u-indentDepth0 js-offCanvasCopy "
		
		
		data-nav-id="searchForums">Search forums</a>

	

					
				</div>
			</div>
		
	</div>

							</li>
						
							<li>
								
	<div class="p-navEl " data-has-children="true">
		

			
	
	<a href="/whats-new/"
		class="p-navEl-link p-navEl-link--splitMenu "
		
		
		data-nav-id="whatsNew">What's new</a>


			<a data-xf-key="3"
				data-xf-click="menu"
				data-menu-pos-ref="< .p-navEl"
				class="p-navEl-splitTrigger"
				role="button"
				tabindex="0"
				aria-label="Toggle expanded"
				aria-expanded="false"
				aria-haspopup="true"></a>

		
		
			<div class="menu menu--structural" data-menu="menu" aria-hidden="true">
				<div class="menu-content">
					<!--<h4 class="menu-header">What's new</h4>-->
					
						
	
	
	<a href="/whats-new/posts/"
		class="menu-linkRow u-indentDepth0 js-offCanvasCopy "
		 rel="nofollow"
		
		data-nav-id="whatsNewPosts">New posts</a>

	

					
						
	
	
	<a href="/whats-new/profile-posts/"
		class="menu-linkRow u-indentDepth0 js-offCanvasCopy "
		 rel="nofollow"
		
		data-nav-id="whatsNewProfilePosts">New profile posts</a>

	

					
						
	
	
	<a href="/whats-new/thread-ratings/"
		class="menu-linkRow u-indentDepth0 js-offCanvasCopy "
		 rel="nofollow"
		
		data-nav-id="BRATR_newThreadRatings">New Thread Ratings</a>

	

					
				</div>
			</div>
		
	</div>

							</li>
						
							<li>
								
	<div class="p-navEl " data-has-children="true">
		

			
	
	<a href="/members/"
		class="p-navEl-link p-navEl-link--splitMenu "
		
		
		data-nav-id="members">Members</a>


			<a data-xf-key="4"
				data-xf-click="menu"
				data-menu-pos-ref="< .p-navEl"
				class="p-navEl-splitTrigger"
				role="button"
				tabindex="0"
				aria-label="Toggle expanded"
				aria-expanded="false"
				aria-haspopup="true"></a>

		
		
			<div class="menu menu--structural" data-menu="menu" aria-hidden="true">
				<div class="menu-content">
					<!--<h4 class="menu-header">Members</h4>-->
					
						
	
	
	<a href="/members/list/"
		class="menu-linkRow u-indentDepth0 js-offCanvasCopy "
		
		
		data-nav-id="registeredMembers">Registered members</a>

	

					
						
	
	
	<a href="/online/"
		class="menu-linkRow u-indentDepth0 js-offCanvasCopy "
		
		
		data-nav-id="currentVisitors">Current visitors</a>

	

					
						
	
	
	<a href="/whats-new/profile-posts/"
		class="menu-linkRow u-indentDepth0 js-offCanvasCopy "
		 rel="nofollow"
		
		data-nav-id="newProfilePosts">New profile posts</a>

	

					
						
	
	
	<a href="/search/?type=profile_post"
		class="menu-linkRow u-indentDepth0 js-offCanvasCopy "
		
		
		data-nav-id="searchProfilePosts">Search profile posts</a>

	

					
				</div>
			</div>
		
	</div>

							</li>
						
							<li>
								
	<div class="p-navEl " >
		

			
	
	<a href="/award-system/list"
		class="p-navEl-link "
		
		data-xf-key="5"
		data-nav-id="addonFlarePubAwards">Awards</a>


			

		
		
	</div>

							</li>
						
							<li>
								
	<div class="p-navEl " >
		

			
	
	<a href="https://altenens.is/ads.html"
		class="p-navEl-link "
		
		data-xf-key="6"
		data-nav-id="10000">Advertising</a>


			

		
		
	</div>

							</li>
						
						</ul>
					</div>
				</div>

				
		</div>
	</nav>

	
	
		<div class="p-sectionLinks">
			<div class="p-sectionLinks-inner hScroller" data-xf-init="h-scroller">
				<div class="hScroller-scroll">
					<ul class="p-sectionLinks-list">
					
						<li>
							
	<div class="p-navEl " >
		

			
	
	<a href="/whats-new/posts/"
		class="p-navEl-link "
		
		data-xf-key="alt+1"
		data-nav-id="newPosts">New posts</a>


			

		
		
	</div>

						</li>
					
						<li>
							
	<div class="p-navEl " >
		

			
	
	<a href="/search/?type=post"
		class="p-navEl-link "
		
		data-xf-key="alt+2"
		data-nav-id="searchForums">Search forums</a>


			

		
		
	</div>

						</li>
					
					</ul>
				</div>
			</div>
		</div>
	



<div class="offCanvasMenu offCanvasMenu--nav js-headerOffCanvasMenu" data-menu="menu" aria-hidden="true" data-ocm-builder="navigation">
	<div class="offCanvasMenu-backdrop" data-menu-close="true"></div>
	<div class="offCanvasMenu-content">
		<div class="offCanvasMenu-header">
			Menu
			<a class="offCanvasMenu-closer" data-menu-close="true" role="button" tabindex="0" aria-label="Close"></a>
		</div>
		
			<div class="p-offCanvasRegisterLink">
				<div class="offCanvasMenu-linkHolder">
					<a href="/login/" class="offCanvasMenu-link" data-xf-click="overlay" data-menu-close="true">
						Log in
					</a>
				</div>
				<hr class="offCanvasMenu-separator" />
				
					<div class="offCanvasMenu-linkHolder">
						<a href="/register/" class="offCanvasMenu-link" data-xf-click="overlay" data-menu-close="true">
							Register
						</a>
					</div>
					<hr class="offCanvasMenu-separator" />
				
			</div>
		
		<div class="js-offCanvasNavTarget"></div>
	</div>
</div>


<!-- XENMAKE MESSAGE -->


<div class="p-body">
	<div class="p-body-inner">
		<div class="p-body-content">		
		
			<!--XF:EXTRA_OUTPUT-->
		

			

			

			 

			<div class='xenmake-breadcrumb'>
			
	
		<ul class="p-breadcrumbs "
			itemscope itemtype="https://schema.org/BreadcrumbList">
		
			

			
			
				
				
	<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<a href="https://altenens.is" itemprop="item">
			<span itemprop="name">Home</span>
		</a>
		<meta itemprop="position" content="1" />
	</li>

			

			
				
				
	<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<a href="/" itemprop="item">
			<span itemprop="name">Forums</span>
		</a>
		<meta itemprop="position" content="2" />
	</li>

			
			

		
		</ul>
		
			
	
	<div class="shareButtons shareButtons--iconic">
		

		

		
			<a class="shareButtons-button shareButtons-button--brand shareButtons-button--twitter" href="https://twitter.com/group_atn" target="_blank">
				<i aria-hidden="true"></i>
				<span>Twitter</span>
			</a>
		
		
			<a class="shareButtons-button shareButtons-button--brand shareButtons-button--youtube" href="https://www.youtube.com/watch?v=SKN2n1BM7ok" target="_blank">
				<i aria-hidden="true"></i>
				<span>youtube</span>
			</a>
		
					
		
					
		

		
					
		
					
		
					
		
					
		
					
		
			<a class="shareButtons-button shareButtons-button--brand shareButtons-button--instagram" href="https://www.instagram.com/altenen.official/" target="_blank">
				<i aria-hidden="true"></i>
				<span>Instagram</span>
			</a>
		
								
		
				
		
					
		
			<a class="shareButtons-button shareButtons-button--brand shareButtons-button--whatsApp" href="https://t.me/altenen_nz" target="_blank">
				<i aria-hidden="true"></i>
				<span>WhatsApp</span>
			</a>
		
					
		
					
		
					
		

		
	
	</div>

		
	

			</div>	
			

			
	<noscript><div class="blockMessage blockMessage--important blockMessage--iconic u-noJsOnly">JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.</div></noscript>

			
	<!--[if lt IE 9]><div class="blockMessage blockMessage&#45;&#45;important blockMessage&#45;&#45;iconic">You are using an out of date browser. It  may not display this or other websites correctly.<br />You should upgrade or use an <a href="https://www.google.com/chrome/browser/" target="_blank">alternative browser</a>.</div><![endif]-->


			
				
<div class="p-body-header "
style=" ">

				
					
						<div class="p-title ">
						
							
										
									<h1 class="p-title-value">Oops! We ran into some problems.</h1>
								
							
							
						
						</div>
					

					
				
				</div>
			

			<div class="p-body-main  ">
				

				<div class="p-body-content">
					
					<div class="p-body-pageContent">

<div class="blockMessage">
	
		The requested thread could not be found.
	
</div></div>
					
				</div>

				
			</div>

			
			<div class='xenmake-breadcrumb bottom'>
			
	
		<ul class="p-breadcrumbs p-breadcrumbs--bottom"
			itemscope itemtype="https://schema.org/BreadcrumbList">
		
			

			
			
				
				
	<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<a href="https://altenens.is" itemprop="item">
			<span itemprop="name">Home</span>
		</a>
		<meta itemprop="position" content="1" />
	</li>

			

			
				
				
	<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<a href="/" itemprop="item">
			<span itemprop="name">Forums</span>
		</a>
		<meta itemprop="position" content="2" />
	</li>

			
			

		
		</ul>
		
			
	
	<div class="shareButtons shareButtons--iconic">
		

		

		
			<a class="shareButtons-button shareButtons-button--brand shareButtons-button--twitter" href="https://twitter.com/group_atn" target="_blank">
				<i aria-hidden="true"></i>
				<span>Twitter</span>
			</a>
		
		
			<a class="shareButtons-button shareButtons-button--brand shareButtons-button--youtube" href="https://www.youtube.com/watch?v=SKN2n1BM7ok" target="_blank">
				<i aria-hidden="true"></i>
				<span>youtube</span>
			</a>
		
					
		
					
		

		
					
		
					
		
					
		
					
		
					
		
			<a class="shareButtons-button shareButtons-button--brand shareButtons-button--instagram" href="https://www.instagram.com/altenen.official/" target="_blank">
				<i aria-hidden="true"></i>
				<span>Instagram</span>
			</a>
		
								
		
				
		
					
		
			<a class="shareButtons-button shareButtons-button--brand shareButtons-button--whatsApp" href="https://t.me/altenen_nz" target="_blank">
				<i aria-hidden="true"></i>
				<span>WhatsApp</span>
			</a>
		
					
		
					
		
					
		

		
	
	</div>

		
	

			</div>	
			
		</div>
	</div>
</div>

<!-- XenMake Advanced Footer -->



<div class="p-footer-inner">
    <div class="xenMakeFooter">
        <ul class="footerColumnContainer">
            

            
				<li class="footerColumn footer_col2">
				
						
	
			
			<div class="block">
				<div class="block-container">
				<h3 class="block-minorHeader"><i class=""></i>About Us</h3>
					<div class="divider fw"></div>
					<strong>Altenen is a forum dedicated to making money on the Internet, various earning schemes, IT issues and much more. This is a forum about making money on the Internet, Also we share knowledge about earning fast,malware modification, hacking, security, programming, cracking, among many other things. Also of tools related to the above. If you have interest and desire to learn do not hesitate to register and start being part of our community, if you are new we will help you in everything we can.</strong>
				</div>
			</div>	
			

					
                </li>
            

            

            
				<li class="footerColumn footer_col4">
					
	
			
			<div class="block">
				<div class="block-container">
				<h3 class="block-minorHeader"><i class=""></i>A RESPONSIBILITY</h3>
					<div class="divider fw"></div>
					<strong>Administration does not bear any responsibility for publications on this forum. If you think that topics and messages may contain information prohibited for distribution, please immediately inform the Administration.</strong>
				</div>
			</div>	
			
		
                </li>
            
        </ul>
    </div>
</div>





	

<footer class="p-footer-inner" id="footer">
	<div class="p-footer">

		<div class="p-footer-row">
			
				<div class="p-footer-row-main">
					<ul class="p-footer-linkList">
					
						
							<li><a href="/misc/style" data-xf-click="overlay"
								data-xf-init="tooltip" title="Style chooser" rel="nofollow">
								<i class="fa--xf far fa-paint-brush" aria-hidden="true"></i> ATN - Main Style
							</a></li>
						
						
					
						
					</ul>
				</div>
				
			<div class="p-footer-row-opposite">
				<ul class="p-footer-linkList">
					

					
						<li><a href="https://altenens.is/index.php?threads/atn-official-rules.594/">Terms and rules</a></li>
					

					

					
						<li><a href="/help/">Help</a></li>
					

					
						<li><a href="https://altenens.is">Home</a></li>
					

					<li><a href="/forums/-/index.rss" target="_blank" class="p-footer-rssLink" title="RSS"><span aria-hidden="true"><i class="fa--xf far fa-rss" aria-hidden="true"></i><span class="u-srOnly">RSS</span></span></a></li>
				</ul>
			</div>
		</div>
	</div>
</footer>



<div class="p-footer-inner" id="footerLegalWrap">
    <div class="footerLegal">
		
			<div class="p-footer-copyright">
			
				<a href="https://xenforo.com" class="u-concealed" dir="ltr" target="_blank">Forum software by XenForo<sup>&reg;</sup> <span class="copyright">&copy; 2010-2019 XenForo Ltd.</span></a><div data-af-cp style="margin: 0 auto;"><a class="u-concealed" target="_blank" href="https://www.addonflare.com">Awards System by <span style="color:rgb(255, 255, 255);">AddonFlare - Premium XF2 Addons</span></a></div>
<div class="xp-copyright">
			Parts of this site powered by <a class="u-concealed" rel="nofollow noopener" href="https://xen-pro.com/store/?utm_source=altenens.is&utm_campaign=site&utm_medium=footer&utm_content=footer" target="_blank">XenForo add-ons by Dadparvar&#8482;</a>
			&copy;2011-2024 <a class="u-concealed" rel="nofollow noopener" href="https://xen-pro.com/?utm_source=altenens.is&utm_campaign=site&utm_medium=footer&utm_content=footer" target="_blank">Xen-Pro</a>
			(<a class="u-concealed" rel="nofollow noopener" href="https://xen-pro.com/store/details/?products=30&utm_source=altenens.is&utm_campaign=product&utm_medium=footer&utm_content=footer" target="_blank">Details</a>)
		</div>

				<center>
	<img src="styles/xenmake/innovate-dark/_custom/atn_team.png"><br>
	<span style="color: white">
		We are all like the bright moon, <br>we still have our darker side.
	</span>
</center><span class="thBranding"> | <a href="https://www.themehouse.com/?utm_source=altenens.is&utm_medium=xf2product&utm_campaign=product_branding" class="u-concealed" target="_BLANK" nofollow="nofollow">Add-ons by ThemeHouse</a></span>
			
			</div>
		
<center> <img src="https://i.imgur.com/j6iEpBY.png"></center>
<small><center><em>    We are all like the bright moon,</em></center></small>
<small><center><em> we still have our darker side.</em></center></small>
		
	</div>
</div>	

</div> <!-- closing p-pageWrapper -->

<div class="u-bottomFixer js-bottomFixTarget">
	
	
</div>


	<div class="u-scrollButtons js-scrollButtons" data-trigger-type="both">
		<a href="#top" class="button--scroll button" data-xf-click="scroll-to"><span class="button-text"><i class="fa--xf far fa-arrow-up" aria-hidden="true"></i><span class="u-srOnly">Top</span></span></a>
		
			<a href="#footer" class="button--scroll button" data-xf-click="scroll-to"><span class="button-text"><i class="fa--xf far fa-arrow-down" aria-hidden="true"></i><span class="u-srOnly">Bottom</span></span></a>
		
	</div>



	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script><script>window.jQuery || document.write('<script src="/js/vendor/jquery/jquery-3.3.1.min.js?_v=305eb201"><\/script>')</script>
	<script src="/js/vendor/vendor-compiled.js?_v=305eb201"></script>
	<script src="/js/xf/core-compiled.js?_v=305eb201"></script>
	<script src="/js/foroagency/coloredusername/index.js?_v=305eb201"></script>
<script>jQuery.extend(XF.phrases, {
		brms_category:       "Category",
		brms_download:       "Download",
		brms_update:         "Update",
		brms_review:         "Review",
		brms_rating: "Rating",
		brms_forum:          "Forum",
		brms_views:          "Views",
		brms_replies:        "Replies",
		brms_likes:          "Likes",
});
</script>
	<script>
		jQuery.extend(true, XF.config, {
			// 
			userId: 0,
			enablePush: false,
			pushAppServerKey: 'BIPdIO9FwcLYscgVbZCcpJ0vLeCaygRvfcCV2inMfsjTJflX4LlfZMumrzUIwUMcjPya3+igaop2Dn2e7Wo65NY=',
			url: {
				fullBase: 'https://altenens.is/',
				basePath: '/',
				css: '/css.php?css=__SENTINEL__&s=2&l=1&d=1697996256',
				keepAlive: '/login/keep-alive'
			},
			cookie: {
				path: '/',
				domain: '',
				prefix: 'xf_',
				secure: true
			},
			csrf: '1706114610,b25f1165ac59a70621741b355ae33adf',
			js: {"\/js\/foroagency\/coloredusername\/index.js?_v=305eb201":true},
			css: {"public:share_controls.less":true,"public:th_covers.less":true,"public:xenmake.less":true,"public:xm_advancedFooter.less":true,"public:xp_vb.less":true,"public:extra.less":true},
			time: {
				now: 1706114610,
				today: 1706054400,
				todayDow: 3
			},
			borderSizeFeature: '3px',
			fontAwesomeWeight: 'r',
			enableRtnProtect: true,
			enableFormSubmitSticky: true,
			uploadMaxFilesize: 2097152,
			allowedVideoExtensions: ["m4v","mov","mp4","mp4v","mpeg","mpg","ogv","webm"],
			shortcodeToEmoji: true,
			visitorCounts: {
				conversations_unread: '0',
				alerts_unread: '0',
				total_unread: '0',
				title_count: true,
				icon_indicator: true
			},
			jsState: {},
			publicMetadataLogoUrl: '',
			publicPushBadgeUrl: 'https://altenens.is/styles/xenmake/innovate-dark/xenforo/bell.png'
		});

		jQuery.extend(XF.phrases, {
			// 
			date_x_at_time_y: "{date} at {time}",
			day_x_at_time_y:  "{day} at {time}",
			yesterday_at_x:   "Yesterday at {time}",
			x_minutes_ago:    "{minutes} minutes ago",
			one_minute_ago:   "1 minute ago",
			a_moment_ago:     "A moment ago",
			today_at_x:       "Today at {time}",
			in_a_moment:      "In a moment",
			in_a_minute:      "In a minute",
			in_x_minutes:     "In {minutes} minutes",
			later_today_at_x: "Later today at {time}",
			tomorrow_at_x:    "Tomorrow at {time}",

			day0: "Sunday",
			day1: "Monday",
			day2: "Tuesday",
			day3: "Wednesday",
			day4: "Thursday",
			day5: "Friday",
			day6: "Saturday",

			dayShort0: "Sun",
			dayShort1: "Mon",
			dayShort2: "Tue",
			dayShort3: "Wed",
			dayShort4: "Thu",
			dayShort5: "Fri",
			dayShort6: "Sat",

			month0: "January",
			month1: "February",
			month2: "March",
			month3: "April",
			month4: "May",
			month5: "June",
			month6: "July",
			month7: "August",
			month8: "September",
			month9: "October",
			month10: "November",
			month11: "December",

			active_user_changed_reload_page: "The active user has changed. Reload the page for the latest version.",
			server_did_not_respond_in_time_try_again: "The server did not respond in time. Please try again.",
			oops_we_ran_into_some_problems: "Oops! We ran into some problems.",
			oops_we_ran_into_some_problems_more_details_console: "Oops! We ran into some problems. Please try again later. More error details may be in the browser console.",
			file_too_large_to_upload: "The file is too large to be uploaded.",
			uploaded_file_is_too_large_for_server_to_process: "The uploaded file is too large for the server to process.",
			files_being_uploaded_are_you_sure: "Files are still being uploaded. Are you sure you want to submit this form?",
			attach: "Attach files",
			rich_text_box: "Rich text box",
			close: "Close",
			link_copied_to_clipboard: "Link copied to clipboard.",
			text_copied_to_clipboard: "Text copied to clipboard.",
			loading: "Loading…",

			processing: "Processing",
			'processing...': "Processing…",

			showing_x_of_y_items: "Showing {count} of {total} items",
			showing_all_items: "Showing all items",
			no_items_to_display: "No items to display",

			push_enable_notification_title: "Push notifications enabled successfully at Altenen - Trust and Safety",
			push_enable_notification_body: "Thank you for enabling push notifications!"
		});
	</script>

	<form style="display:none" hidden="hidden">
		<input type="text" name="_xfClientLoadTime" value="" id="_xfClientLoadTime" title="_xfClientLoadTime" tabindex="-1" />
	</form>

	



	<script type="text/template" id="xfReactTooltipTemplate">
		<div class="tooltip-content-inner">
			<div class="reactTooltip">
				
					<a href="#" class="reaction reaction--1" data-reaction-id="1"><i aria-hidden="true"></i><img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" class="reaction-sprite js-reaction" alt="Like" title="Like" data-xf-init="tooltip" /></a>
				
					<a href="#" class="reaction reaction--2" data-reaction-id="2"><i aria-hidden="true"></i><img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" class="reaction-sprite js-reaction" alt="Love" title="Love" data-xf-init="tooltip" /></a>
				
					<a href="#" class="reaction reaction--3" data-reaction-id="3"><i aria-hidden="true"></i><img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" class="reaction-sprite js-reaction" alt="Haha" title="Haha" data-xf-init="tooltip" /></a>
				
					<a href="#" class="reaction reaction--4" data-reaction-id="4"><i aria-hidden="true"></i><img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" class="reaction-sprite js-reaction" alt="Wow" title="Wow" data-xf-init="tooltip" /></a>
				
					<a href="#" class="reaction reaction--5" data-reaction-id="5"><i aria-hidden="true"></i><img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" class="reaction-sprite js-reaction" alt="Sad" title="Sad" data-xf-init="tooltip" /></a>
				
					<a href="#" class="reaction reaction--6" data-reaction-id="6"><i aria-hidden="true"></i><img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" class="reaction-sprite js-reaction" alt="Angry" title="Angry" data-xf-init="tooltip" /></a>
				
					<a href="#" class="reaction reaction--9" data-reaction-id="9"><i aria-hidden="true"></i><img src="https://i.imgur.com/LhkkUkn.png"  class="reaction-image js-reaction" alt="Worked" title="Worked" data-xf-init="tooltip" /></a>
				
					<a href="#" class="reaction reaction--7" data-reaction-id="7"><i aria-hidden="true"></i><img src="https://i.imgur.com/whDbMrU.png"  class="reaction-image js-reaction" alt="Agree" title="Agree" data-xf-init="tooltip" /></a>
				
					<a href="#" class="reaction reaction--8" data-reaction-id="8"><i aria-hidden="true"></i><img src="https://i.imgur.com/VwN95Mk.png"  class="reaction-image js-reaction" alt="Disagree" title="Disagree" data-xf-init="tooltip" /></a>
				
			</div>
		</div>
	</script>


	<script type='text/javascript' src="/js/xenmake/headroom.min.js"></script>
	




<script type="text/javascript">
    var header = document.querySelector("#navigation");

    new Headroom(header, {
        tolerance: {
            down: 2,
            up: 5
        },
        offset: 100,
        classes: {
            initial: "slide",
            pinned: "slide--reset",
            unpinned: "slide--up"
        }
    }).init();
</script>







<!-- Style Version: 2.1.1.0 -->


</html>



'''