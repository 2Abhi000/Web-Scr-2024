

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Alt-Used': 'alboraaq.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get('https://alboraaq.com/', headers=headers)

html = response.text

print(html)

#Output
'''
<script src="//archive.org/includes/analytics.js?v=cf34f82" type="383908f5585f83af7f5c5332-text/javascript"></script><script type="383908f5585f83af7f5c5332-text/javascript">window.addEventListener('DOMContentLoaded',function(){var v=archive_analytics.values;v.service='wb';v.server_name='wwwb-app201.us.archive.org';v.server_ms=381;archive_analytics.send_pageview({});});</script><script type="383908f5585f83af7f5c5332-text/javascript" src="/_static/js/bundle-playback.js?v=MzYkZ0TU" charset="utf-8"></script><script type="383908f5585f83af7f5c5332-text/javascript" src="/_static/js/wombat.js?v=UHAOicsW" charset="utf-8"></script><script type="383908f5585f83af7f5c5332-text/javascript">
  __wm.init("https://web.archive.org/web");
  __wm.wombat("https://altenen.pro/","20220702120207","https://web.archive.org/","web","/_static/",
              "1656763327");
</script>
<link href="/_static/css/banner-styles.css?v=S1zqJCYt" rel="stylesheet" type="text/css" />
<link href="/_static/css/iconochive.css?v=qtvMKcIJ" rel="stylesheet" type="text/css" /><!-- End Wayback Rewrite JS Include --><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><meta name="description" content=""><meta name="author" content="">
<link href="https://web.archive.org/web/20220702120207im_/https://i.postimg.cc/MKYnVYcH/favicon.gif" rel="icon" />
<title></title>
<link href="https://web.archive.org/web/20220702120207/https://getbootstrap.com/docs/4.0/examples/cover/" rel="canonical" />
<link href="https://web.archive.org/web/20220702120207cs_/https://getbootstrap.com/docs/4.0/dist/css/bootstrap.min.css" rel="stylesheet" />
<link href="https://web.archive.org/web/20220702120207cs_/https://getbootstrap.com/docs/4.0/examples/cover/cover.css" rel="stylesheet" /><!-- BEGIN WAYBACK TOOLBAR INSERT -->
<style type="text/css">body {
  margin-top:0 !important;
  padding-top:0 !important;
  /*min-width:800px !important;*/
}
</style>
<script type="383908f5585f83af7f5c5332-text/javascript">__wm.rw(0);</script>
<div id="wm-ipp-base" lang="en" style="display:none;direction:ltr;">
<div id="wm-ipp" style="position:fixed;left:0;top:0;right:0;">
<div id="donato" style="position:relative;width:100%;">
<div id="donato-base"><iframe frameborder="0" id="donato-if" scrolling="no" src="https://archive.org/includes/donate.php?as_page=1&amp;platform=wb&amp;referer=https%3A//web.archive.org/web/20220702120207/https%3A//altenen.pro/" style="width:100%; height:100%"></iframe></div>
</div>

<div id="wm-ipp-inside">
<div id="wm-toolbar" style="position:relative;display:flex;flex-flow:row nowrap;justify-content:space-between;">
<div id="wm-logo" style="/*width:110px;*/padding-top:12px;"><a href="/web/" title="Wayback Machine home page"><img alt="Wayback Machine" border="0" src="/_static/images/toolbar/wayback-toolbar-logo-200.png" srcset="/_static/images/toolbar/wayback-toolbar-logo-100.png, /_static/images/toolbar/wayback-toolbar-logo-150.png 1.5x, /_static/images/toolbar/wayback-toolbar-logo-200.png 2x" width="100" /></a></div>

<div class="c" style="display:flex;flex-flow:column nowrap;justify-content:space-between;flex:1;">
<form action="/web/submit" class="u" id="wmtb" method="get" name="wmtb" style="display:flex;flex-direction:row;flex-wrap:nowrap;" target="_top"><input id="wmtbURL" name="url" onfocus="if (!window.__cfRLUnblockHandlers) return false; this.focus();this.select();" style="flex:1;" type="text" value="https://altenen.pro/" data-cf-modified-383908f5585f83af7f5c5332-="" /><input name="type" type="hidden" value="replay" /><input name="date" type="hidden" value="20220702120207" /><input type="submit" value="Go" />&nbsp;</form>

<div style="display:flex;flex-flow:row nowrap;align-items:flex-end;">
<div class="s" id="wm-nav-captures" style="flex:1;"><a class="t" href="/web/20220702120207*/https://altenen.pro/" title="See a list of every capture for this URL">46 captures</a>

<div class="r" title="Timespan for captures of this URL">16 May 2018 - 08 Oct 2022</div>
</div>

<div class="k"><a href="" id="wm-graph-anchor"> </a>

<div id="wm-ipp-sparkline" style="position: relative" title="Explore captures for this URL"><a href="" id="wm-graph-anchor"><canvas border="0" height="27" id="wm-sparkline-canvas" width="675"></canvas> </a></div>
<a href="" id="wm-graph-anchor"> </a></div>
</div>
</div>

<div class="n">
<table>
        <tbody><!-- NEXT/PREV MONTH NAV AND MONTH INDICATOR -->
                <tr class="m">
                        <td class="b" nowrap="nowrap"><a href="https://web.archive.org/web/20220519060546/https://altenen.pro/" title="19 May 2022"><strong>May</strong></a></td>
                        <td class="c" id="displayMonthEl" title="You are here: 12:02:07 Jul 02, 2022">JUL</td>
                        <td class="f" nowrap="nowrap"><a href="https://web.archive.org/web/20220806061723/https://altenen.pro/" title="06 Aug 2022"><strong>Aug</strong></a></td>
                </tr>
                <!-- NEXT/PREV CAPTURE NAV AND DAY OF MONTH INDICATOR -->
                <tr class="d">
                        <td class="b" nowrap="nowrap"><a href="https://web.archive.org/web/20220617221146/https://www.altenen.pro/" title="22:11:46 Jun 17, 2022"><img alt="Previous capture" border="0" height="16" src="/_static/images/toolbar/wm_tb_prv_on.png" width="14" /></a></td>
                        <td class="c" id="displayDayEl" style="width:34px;font-size:22px;white-space:nowrap;" title="You are here: 12:02:07 Jul 02, 2022">02</td>
                        <td class="f" nowrap="nowrap"><a href="https://web.archive.org/web/20220706055522/http://altenen.pro/" title="05:55:22 Jul 06, 2022"><img alt="Next capture" border="0" height="16" src="/_static/images/toolbar/wm_tb_nxt_on.png" width="14" /></a></td>
                </tr>
                <!-- NEXT/PREV YEAR NAV AND YEAR INDICATOR -->
                <tr class="y">
                        <td class="b" nowrap="nowrap"><a href="https://web.archive.org/web/20201107193208/http://www.altenen.pro/" title="07 Nov 2020"><strong>2020</strong></a></td>
                        <td class="c" id="displayYearEl" title="You are here: 12:02:07 Jul 02, 2022">2022</td>
                        <td class="f" nowrap="nowrap">2023</td>
                </tr>
        </tbody>
</table>
</div>

<div class="r" style="display:flex;flex-flow:column nowrap;align-items:flex-end;justify-content:space-between;">
<div id="wm-btns" style="text-align:right;height:23px;">
<div id="wm-save-snapshot-success"><span class="xxs">success</span></div>

<div id="wm-save-snapshot-fail"><span class="xxs">fail</span></div>
</div>

<div class="xxs" id="wm-share">&nbsp;</div>

<div style="padding-right:2px;text-align:right;white-space:nowrap;"><a class="wm-btn wm-closed" href="#expand" id="wm-expand" onclick="if (!window.__cfRLUnblockHandlers) return false; __wm.ex(event);return false;" data-cf-modified-383908f5585f83af7f5c5332-=""><span class="xxs" style="font-size:80%">About this capture</span></a></div>
</div>
</div>

<div id="wm-capinfo" style="border-top:1px solid #777;display:none; overflow: hidden">
<div id="wm-capinfo-collected-by">
<div style="background-color:#666;color:#fff;font-weight:bold;text-align:center">COLLECTED BY</div>

<div id="wm-collected-by-content" style="padding:3px;position:relative">
<div style="display:inline-block;vertical-align:top;width:50%;">Organization: <a href="https://archive.org/details/archiveteam" style="color:#33f;" target="_new"><span class="wm-title">Archive Team</span></a>

<div style="max-height:75px;overflow:hidden;position:relative;">
<div style="position:absolute;top:0;left:0;width:100%;height:75px;background:linear-gradient(to bottom,rgba(255,255,255,0) 0%,rgba(255,255,255,0) 90%,rgba(255,255,255,255) 100%);">&nbsp;</div>
<img align="right" alt="" src="http://archiveteam.org/images/e/e6/Archiveteam.jpg" width="200" /> Formed in 2009, the Archive Team (not to be confused with the archive.org Archive-It Team) is a rogue archivist collective dedicated to saving copies of rapidly dying or deleted websites for the sake of history and digital heritage. The group is 100% composed of volunteers and interested parties, and has expanded into a large amount of related projects for saving online and digital history.
<p>History is littered with hundreds of conflicts over the future of a community, group, location or business that were &quot;resolved&quot; when one of the parties stepped ahead and destroyed what was there. With the original point of contention destroyed, the debates would fall to the wayside. Archive Team believes that by duplicated condemned data, the conversation and debate can continue, as well as the richness and insight gained by keeping the materials. Our projects have ranged in size from a single volunteer downloading the data to a small-but-critical site, to over 100 volunteers stepping forward to acquire terabytes of user-created data to save for future generations.</p>

<p>The main site for Archive Team is at <a href="http://www.archiveteam.org">archiveteam.org</a> and contains up to the date information on various projects, manifestos, plans and walkthroughs.</p>

<p>This collection contains the output of many Archive Team projects, both ongoing and completed. Thanks to the generous providing of disk space by the Internet Archive, multi-terabyte datasets can be made available, as well as in use by the <a href="http://archive.org/web/web.php">Wayback Machine</a>, providing a path back to lost websites and work.</p>

<p>Our collection has grown to the point of having sub-collections for the type of data we acquire. If you are seeking to browse the contents of these collections, the Wayback Machine is the best first stop. Otherwise, you are free to dig into the stacks to see what you may find.</p>

<p><strong>The Archive Team Panic Downloads</strong> are full pulldowns of currently extant websites, meant to serve as emergency backups for needed sites that are in danger of closing, or which will be missed dearly if suddenly lost due to hard drive crashes or server failures.</p>

<p>&nbsp;</p>
</div>
</div>

<div style="display:inline-block;vertical-align:top;width:49%;">
<div>Collection: <a href="https://archive.org/details/archiveteam_urls" style="color:#33f;" target="_new"><span class="wm-title">Archive Team: URLs</span></a></div>
</div>
</div>
</div>

<div id="wm-capinfo-timestamps">
<div style="background-color:#666;color:#fff;font-weight:bold;text-align:center" title="Timestamps for the elements of this page">TIMESTAMPS</div>

<div>
<div id="wm-capresources" style="margin:0 5px 5px 5px;max-height:250px;overflow-y:scroll !important">&nbsp;</div>

<div id="wm-capresources-loading" style="text-align:left;margin:0 20px 5px 5px;display:none"><img alt="loading" src="/_static/images/loading.gif" /></div>
</div>
</div>
</div>
</div>
</div>
</div>

<div id="wm-ipp-print">&nbsp;</div>
<script type="383908f5585f83af7f5c5332-text/javascript">//<![CDATA[
__wm.bt(675,27,25,2,"web","https://altenen.pro/","20220702120207",1996,"/_static/",["/_static/css/banner-styles.css?v=S1zqJCYt","/_static/css/iconochive.css?v=qtvMKcIJ"], false);
  __wm.rw(1);
//]]></script><!-- END WAYBACK TOOLBAR INSERT -->

<div class="cover-container d-flex h-100 p-3 mx-auto flex-column">
<header class="masthead mb-auto">
<div class="inner">
<h3 class="masthead-brand">Altenen</h3>

<nav class="nav nav-masthead justify-content-center"><a class="nav-link active" href="https://altenens.is">Current Link</a></nav>
</div>
</header>

<main class="inner cover" role="main">
<h1 class="cover-heading text-warning">Hello.</h1>


<p>Please Bookmark or Save these Domains:</p>

<p>► <a href="https://altenen.is">https://altenen.is</a></p>

<p>► <a href="http://altenen.st">Altenen.ST</a></p>

<p>► <a href="https://altenen.cm">https://altenen.cm</a></p>

<p>► <a href="https://altenen.io">https://altenen.io</a></p>

<p>► <a href="https://alboraaq.com">https://alboraaq.com</a></p>

<p class="lead"><a class="btn btn-lg btn-secondary" href="https://t.me/Altenen_nz" target="_blank">Join Our Telegram Group</a><br />
<span class="h6 text-muted">Join our Telegram group to stay up to date from all the news.</span></p>

<p><span style="background-color:#00ffff"><strong>Please join our Twitter for get updates</strong></span></p>

<p><span style="background-color:#00ffff"><a href="https://twitter.com/group_atn" style="background-color: #00ffff;"><strong>https://twitter.com/group_atn</strong></a></span></p>
&nbsp;

<p>Best Regards,<br />
<strong><span style="color:red">A</span>T<span style="color:red">N</span> Team</strong></p>

<h6 class="text-muted">altenen.com altenens.com altenen.is altenens.is altenen.io altenen.st altenen.cm alboraaq.com</h6>
</main>
&nbsp;

<footer class="mastfoot mt-auto">
<div class="inner">
<p>Altenen, <a href="#">Trust and Safety</a>!</p>
</div>
</footer>
</div>
<script data-cfasync="false" src="/web/20220702120207js_/https://altenen.pro/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script src="https://web.archive.org/web/20220702120207js_/https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="" crossorigin="anonymous" type="383908f5585f83af7f5c5332-text/javascript"></script><script type="383908f5585f83af7f5c5332-text/javascript">window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script><script src="https://web.archive.org/web/20220702120207js_/https://getbootstrap.com/docs/4.0/assets/js/vendor/popper.min.js" type="383908f5585f83af7f5c5332-text/javascript"></script><script src="https://web.archive.org/web/20220702120207js_/https://getbootstrap.com/docs/4.0/dist/js/bootstrap.min.js" type="383908f5585f83af7f5c5332-text/javascript"></script><!--
     FILE ARCHIVED ON 12:02:07 Jul 02, 2022 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 11:46:30 Dec 03, 2022.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
--><!--
playback timings (ms):
  captures_list: 204.722
  exclusion.robots: 0.334
  exclusion.robots.policy: 0.318
  cdx.remote: 0.148
  esindex: 0.014
  LoadShardBlock: 162.292 (3)
  PetaboxLoader3.datanode: 114.134 (5)
  CDXLines.iter: 18.731 (3)
  load_resource: 169.893
  PetaboxLoader3.resolve: 107.113
  loaddict: 21.687
<script src="/cdn-cgi/scripts/7d0fa10a/cloudflare-static/rocket-loader.min.js" data-cf-settings="383908f5585f83af7f5c5332-|49" defer></script>

'''
