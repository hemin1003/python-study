# BeautifulSoup库的用法

from bs4 import BeautifulSoup

html_doc = """
<html class="no-js" >

  <head>
    <meta charset="utf-8">
    <title>
        原创 - CNU视觉联盟 

</title>
    <meta name="keywords" content=" CNU,视觉,摄影,视觉联盟,照片,摄影师,摄影作品集,在线摄影作品集,照片精选,网络摄影作品集,在线照片展廊,分享图片,专业摄影,社会摄影,上传照片,分享照片,出色的摄影作品集,摄影社区,最新摄影作品,快速创建作品集,模特和摄影师,商业摄影,建筑摄影,专业作品集管理,视觉中国图库,视觉中国,视觉联盟,摄影作品,摄影作品欣赏,时尚摄影,时尚摄影作品,艺术,艺术作品,艺术摄影作品,人体艺术,时尚杂志,品牌广告,视觉,视觉艺术,视觉作品,视觉作品欣赏,时尚,设计,当代艺术 " />
    <meta name="description" content=" 中国视觉联盟cnu.cc-是一家致力于传播优秀视觉文化,研究视觉艺术、交流视觉理念、开拓大众审美视野的专业性视觉网站。 ">

    <meta name="viewport" content="width=device-width">
      <link rel="icon" href="http://img.cnu.cc/assets/images/favicon.ico" type="image/x-icon" />
      <link rel="shortcut icon" href="http://img.cnu.cc/assets/images/favicon.ico" type="image/x-icon" />
    <link rel="stylesheet" href="http://www.cnu.cc/assets/font-awesome-4.4.0/css/font-awesome.css">


      <link rel="stylesheet" href="http://img.cnu.cc/assets/bootstrap/css/bootstrap.min.css">
      <link rel="stylesheet" href="http://img.cnu.cc/assets/styles/main.css">
      <!--[if lt IE 9]>
      <!--
      <script src="http://cdnjs.cloudflare.com/ajax/libs/respond.js/1.4.2/respond.min.js"></script>
      <script src="http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.2/html5shiv.min.js"></script>
      -->
      <script src="http://img.cnu.cc/assets/scripts/lib/respond.min.js"></script>
      <script src="http://img.cnu.cc/assets/scripts/lib/html5shiv.min.js"></script>
      <![endif]-->
    <script>
        
        Config = {
            'cdnDomain': 'http://img.cnu.cc',
            'user_id': 0,
            'routes': {
            },
            'token': 'FdU4eUAFGX6AeaxIpApGOJKpPxm5aNAjVC00Bi9Y'
        };
    </script>
      <script>
          var _hmt = _hmt || [];
          (function() {
              var hm = document.createElement("script");
              hm.src = "//hm.baidu.com/hm.js?debc91213222aae0abfdb6176ec8d28a";
              var s = document.getElementsByTagName("script")[0];
              s.parentNode.insertBefore(hm, s);
          })();
      </script>
    
    <link rel="stylesheet" href="http://img.cnu.cc/assets/styles/discovery.css">
    <link rel="stylesheet" href="http://img.cnu.cc/assets/styles/public.css">


  </head>

  <body>
        <nav class="navbar navbar-inverse navbar-fixed-top">

    <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" style="padding: 0px 20px;" href="http://www.cnu.cc"><div id="logo" ></div></a>
    </div>
    <div class="collapse navbar-collapse">
        <ul id="navbar" class="nav navbar-nav">
            <li>
                <a href="http://www.cnu.cc/selectedPage"><i class="myicon icon-home"></i> <span>首页</span></a>
            </li>
            <li>
                <a href="http://www.cnu.cc/inspirationPage/recent-0"><i class="myicon icon-inspiration"></i> <span>灵感</span></a>
            </li>

            <li>
                <a href="http://www.cnu.cc/discoveryPage/hot-0"><i class="myicon icon-discovery"></i> <span>原创</span></a>
            </li>
            
        </ul>


        <ul class="nav navbar-nav navbar-right" style="margin-right: 10px;">
<li><form method="GET" action="http://www.cnu.cc/search" accept-charset="UTF-8" id="searchForm" autocomplete="off" role="search" class="navbar-form navbar-left">

    <div class="search-group">
        <input type="text" id="keyword" value="" class="search-control" placeholder="登录后搜索">
    </div>
    </form>
</li>


                <li class="dropdown active publishBtn">
                    <a class="dropdown-toggle " id="dropdownMenu1" data-toggle="dropdown" href="#">
                         投稿
                        <span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">



                        <li><a href="http://www.cnu.cc/works/create"> 原创图集</a></li>
                        <li><a href="http://www.cnu.cc/work/createTutorial"> 原创教程</a></li>
                       
                                            </ul>
                </li>
                            <li ><a href="http://www.cnu.cc/signup">注册</a></li>
                <li ><a href="http://www.cnu.cc/login">登录</a></li>
            

        </ul>
    </div>

</nav>


        


      <div style ="display:none">
         
         </div>

    <div class="page-header second-nav" >

        <ul class="container nav nav-pills">
            <li class="select"><a href="http://www.cnu.cc/discoveryPage/hot-0">发现</a></li>
            <li ><a href="http://www.cnu.cc/activities">动态</a></li>
            <li ><a href="http://www.cnu.cc/following">我的关注</a></li>
        </ul>
    </div>

    <div class="container pc" >
        <form method="POST" action="http://www.cnu.cc/works/recommend" accept-charset="UTF-8" id="recommendForm" class="recommendForm"><input name="_token" type="hidden" value="FdU4eUAFGX6AeaxIpApGOJKpPxm5aNAjVC00Bi9Y">


    <div class="grid">
        <div class="grid-item">
            <div class="menu">
                <a href="http://www.cnu.cc/discoveryPage/hot-%E4%BA%BA%E5%83%8F" class='orderType selected'><h3>热门</h3></a>
                <a href="http://www.cnu.cc/discoveryPage/recommend-%E4%BA%BA%E5%83%8F" class='orderType '><h3>推荐</h3></a>
                <a href="http://www.cnu.cc/discoveryPage/recent-%E4%BA%BA%E5%83%8F" class='orderType '><h3>最新</h3></a>

                    <hr>
                    <div class="all">
                        <a  class="category" category_id="0" href="http://www.cnu.cc/discoveryPage/hot-0"><h4><span class="">全部</span></h4></a>
                    </div>
                    <div class="group row">
                        <a  class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E4%BA%BA%E5%83%8F"><span class="">人像</span></a>
                        <a  class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E8%83%B6%E7%89%87"><span class="">胶片</span></a>
                        <a  class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E8%87%AA%E7%84%B6"><span class="">自然</span></a>
                        <a  class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E8%89%BA%E6%9C%AF"><span class="">艺术</span></a>
                        <a  class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E8%A1%97%E9%81%93"><span class="">街道</span></a>
                        <a  class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E8%A1%A8%E6%BC%94"><span class="">表演</span></a>
                        <a  class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E9%9D%99%E7%89%A9"><span class="">静物</span></a>
                        <a  class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E9%A3%8E%E5%85%89"><span class="">风光</span></a>
                        <a  class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E9%BB%91%E7%99%BD"><span class="">黑白</span></a>
                        <a class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E6%97%B6%E5%B0%9A"><span class="">时尚</span></a>
                        <a class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E6%97%85%E8%A1%8C"><span class="">旅行</span></a>
                        <a class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E6%96%B0%E9%97%BB"><span class="">新闻</span></a>
                        <a class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E5%8A%A8%E7%89%A9"><span class="">动物</span></a>
                        <a class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E5%BB%BA%E7%AD%91"><span class="">建筑</span></a>
                        <a  class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E5%A9%9A%E7%A4%BC"><span class="">婚礼</span></a>
                        <a class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E5%AE%B6%E5%BA%AD"><span class="">家庭</span></a>
                        <a class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E5%B9%BF%E5%91%8A"><span class="">广告</span></a>
                        <a class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E5%BE%AE%E8%B7%9D"><span class="">微距</span></a>
                        <a class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E6%8A%BD%E8%B1%A1"><span class="">抽象</span></a>
                        <a  class="category col-xs-6" category_id="220" href="http://www.cnu.cc/discoveryPage/hot-%E4%BA%BA%E6%96%87"><span class="">人文</span></a>
                    </div>
                                </div>

            </div>
                                                <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/291520" class="thumbnail" target="_blank">
                        <div class="title">
                            Your Skin and Bones
                            </div>
                        <div class="author">
                            十识-Renta

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1807/22/11f86aa936903755bad79320c7c22788.jpg?width=2673&amp;height=4002" alt="Your Skin and Bones">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/291287" class="thumbnail" target="_blank">
                        <div class="title">
                            ”California Dreaming“
                            </div>
                        <div class="author">
                            darling安老师

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1807/19/ac67cbc0ec273f2c8360eee9cbb9b4c4.jpg?width=2076&amp;height=3124" alt="”California Dreaming“">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/291282" class="thumbnail" target="_blank">
                        <div class="title">
                            “我愿意”
                            </div>
                        <div class="author">
                            darling安老师

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1807/19/2e06bff1a68e3483800f10f441b1993f.jpg?width=3106&amp;height=2097" alt="“我愿意”">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/290746" class="thumbnail" target="_blank">
                        <div class="title">
                            花魁
                            </div>
                        <div class="author">
                            口肃

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1807/12/eaadd700552338c786f470af98487570.jpg?width=2448&amp;height=3264" alt="花魁">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/290244" class="thumbnail" target="_blank">
                        <div class="title">
                            "你不知道我的名字“
                            </div>
                        <div class="author">
                            darling安老师

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1807/08/60f9f10bf07a34068b2fc6bb59e18cfd.jpg?width=2875&amp;height=4336" alt=""你不知道我的名字“">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/287186" class="thumbnail" target="_blank">
                        <div class="title">
                            “鬼迷心窍”
                            </div>
                        <div class="author">
                            文艺青年安打

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1806/24/647c32ee779939f0af4facef5646caf1.jpg?width=1395&amp;height=2100" alt="“鬼迷心窍”">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/286315" class="thumbnail" target="_blank">
                        <div class="title">
                            草 绿 唇 红
                            </div>
                        <div class="author">
                            ClouinKim

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1806/20/123f451679623738883661fd26cddb32.jpg?width=3680&amp;height=5520" alt="草 绿 唇 红">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/286079" class="thumbnail" target="_blank">
                        <div class="title">
                            《云海之下》
                            </div>
                        <div class="author">
                            韩帅Ghost

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1806/19/3b1adcd5826539b6857e0f4e6bd0a8bb.jpg?width=1984&amp;height=1315" alt="《云海之下》">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/285165" class="thumbnail" target="_blank">
                        <div class="title">
                            五月，犹如梦中
                            </div>
                        <div class="author">
                            C的情绪

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1806/13/9705b63dc4ff3ddbb44051d21fbc6434.jpg?width=1000&amp;height=673" alt="五月，犹如梦中">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/283902" class="thumbnail" target="_blank">
                        <div class="title">
                            生活没有旁观者
                            </div>
                        <div class="author">
                            韩帅Ghost

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1806/07/9327d1ae3b9239ad81df9c959330322c.jpg?width=2362&amp;height=2362" alt="生活没有旁观者">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/281870" class="thumbnail" target="_blank">
                        <div class="title">
                            淡淡深圳湾
                            </div>
                        <div class="author">
                            物哀_

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1805/29/294d46d126753b07abcde2ea4d62993a.jpg?width=920&amp;height=920" alt="淡淡深圳湾">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/279243" class="thumbnail" target="_blank">
                        <div class="title">
                            古力果
                            </div>
                        <div class="author">
                            魚er人

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1805/16/ec3c725cf0223c27babf58574cb2b4a4.jpg?width=1449&amp;height=1995" alt="古力果">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/279005" class="thumbnail" target="_blank">
                        <div class="title">
                            情迷五月
                            </div>
                        <div class="author">
                            徐大力x

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1805/15/1197fdef2bf23945828eb27b1cef400a.jpg?width=1000&amp;height=674" alt="情迷五月">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/276850" class="thumbnail" target="_blank">
                        <div class="title">
                            梦田
                            </div>
                        <div class="author">
                            梦境记录册

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1805/04/84f658ef1a3536fbafa5a367cff8ee96.jpg?width=2000&amp;height=3000" alt="梦田">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/261036" class="thumbnail" target="_blank">
                        <div class="title">
                            舞
                            </div>
                        <div class="author">
                            张厚几

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1804/03/838da68faa143cb9925a0a028299da42.jpg?width=1406&amp;height=1875" alt="舞">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/260421" class="thumbnail" target="_blank">
                        <div class="title">
                            03/29 記錄
                            </div>
                        <div class="author">
                            蔡黎冰

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1803/31/8e40feecd1d330879c95c66b66cb64f7.jpg?width=5472&amp;height=3648" alt="03/29 記錄">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/258687" class="thumbnail" target="_blank">
                        <div class="title">
                            樱花三月
                            </div>
                        <div class="author">
                            C的情绪

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1803/24/6c26bd31ad56304389ae7a42085244f8.jpg?width=667&amp;height=1000" alt="樱花三月">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/257950" class="thumbnail" target="_blank">
                        <div class="title">
                            好久不见
                            </div>
                        <div class="author">
                            Gavin老C

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1805/18/7118a49f619f37f8b6947d0c9fd6c4c3.jpg?width=720&amp;height=1080" alt="好久不见">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/254986" class="thumbnail" target="_blank">
                        <div class="title">
                            London Underground Collection (ONE)
                            </div>
                        <div class="author">
                            找丝线

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1803/08/c937d36426d33914bcd8174d8075d309.jpg?width=1842&amp;height=1036" alt="London Underground Collection (ONE)">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/254649" class="thumbnail" target="_blank">
                        <div class="title">
                            Misery Is a Butterfly
                            </div>
                        <div class="author">
                            Stiizzii

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1803/06/763a534717ae3a1e91861c04aafcc432.jpg?width=3500&amp;height=2334" alt="Misery Is a Butterfly">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/254173" class="thumbnail" target="_blank">
                        <div class="title">
                            『季候风』
                            </div>
                        <div class="author">
                            小马哥

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1803/03/b1454f4ac2e03fb295a9c550e59c8d42.jpg?width=920&amp;height=1411" alt="『季候风』">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/253227" class="thumbnail" target="_blank">
                        <div class="title">
                            Pretend to be
                            </div>
                        <div class="author">
                            微醺十月

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1806/28/d48f9385e9a4397dbaede5648506ca05.jpg?width=3815&amp;height=2558" alt="Pretend to be">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/251912" class="thumbnail" target="_blank">
                        <div class="title">
                            未闻花名
                            </div>
                        <div class="author">
                            徐大力x

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1802/21/bf0a91fadf8e3efe93976d3d968472e0.jpg?width=1000&amp;height=1500" alt="未闻花名">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/249042" class="thumbnail" target="_blank">
                        <div class="title">
                            一个清晨的记忆
                            </div>
                        <div class="author">
                            鹅毛笔

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1801/30/9555912469743e5aa297d2d3da92ca37.jpg?width=2207&amp;height=3299" alt="一个清晨的记忆">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/249170" class="thumbnail" target="_blank">
                        <div class="title">
                            Season in the sun
                            </div>
                        <div class="author">
                            张厚几

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1801/31/871964cade233409b822723761d3deed.jpg?width=2409&amp;height=3212" alt="Season in the sun">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/246668" class="thumbnail" target="_blank">
                        <div class="title">
                            徐樱洛｜WINTER 胶片
                            </div>
                        <div class="author">
                            Amns阿梅

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1801/14/8147db87c80934e89fb3d8c6a0f03540.jpg?width=2433&amp;height=3637" alt="徐樱洛｜WINTER 胶片">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/245788" class="thumbnail" target="_blank">
                        <div class="title">
                            冬
                            </div>
                        <div class="author">
                            生先野

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1801/08/bace148c9fb538b49f849c4d901cbe44.jpg?width=5472&amp;height=3648" alt="冬">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/244938" class="thumbnail" target="_blank">
                        <div class="title">
                            Fashion kids | 复古童年
                            </div>
                        <div class="author">
                            LynnWei

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1801/04/aae0b68b2c583ea4889f561effbe9be1.jpg?width=1486&amp;height=2079" alt="Fashion kids | 复古童年">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/244654" class="thumbnail" target="_blank">
                        <div class="title">
                            电影少女 
                            </div>
                        <div class="author">
                            SATANn

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1801/02/63a38cb7f2223124b86063f297dceb76.jpg?width=4032&amp;height=3024" alt="电影少女 ">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/243743" class="thumbnail" target="_blank">
                        <div class="title">
                            SHANGYAN
                            </div>
                        <div class="author">
                            摄影师曹娜

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1712/27/20783d2d51bb35f1b52eefcc88b9ded6.jpg?width=2606&amp;height=1832" alt="SHANGYAN">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/243099" class="thumbnail" target="_blank">
                        <div class="title">
                            FOREVER
                            </div>
                        <div class="author">
                            BovieLee

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1807/23/6fbc3a67caab3899b82ad846a3965700.jpg?width=2728&amp;height=4199" alt="FOREVER">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/242628" class="thumbnail" target="_blank">
                        <div class="title">
                            为你
                            </div>
                        <div class="author">
                            jieyz

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1712/20/2e8c3f605cec3eeabb7d54475f1f6aca.jpg?width=947&amp;height=640" alt="为你">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/240108" class="thumbnail" target="_blank">
                        <div class="title">
                            ”舍不得“
                            </div>
                        <div class="author">
                            文艺青年安打

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1712/05/05c6e4c7a38537bf95609a44c5a78d3b.jpg?width=2000&amp;height=1333" alt="”舍不得“">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/239913" class="thumbnail" target="_blank">
                        <div class="title">
                            “请记住我！”
                            </div>
                        <div class="author">
                            文艺青年安打

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1712/04/98de4bb779a53fb9865aabd4d5fe86bc.jpg?width=3840&amp;height=5760" alt="“请记住我！”">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/239092" class="thumbnail" target="_blank">
                        <div class="title">
                            •11刀
                            </div>
                        <div class="author">
                            9946

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1711/30/31179365a73f3d84ba7995d90064f118.jpg?width=920&amp;height=1374" alt="•11刀">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/238499" class="thumbnail" target="_blank">
                        <div class="title">
                            原野
                            </div>
                        <div class="author">
                            微醺十月

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1711/27/189be1c6bd36331e980900b2147d54a6.jpg?width=3518&amp;height=2357" alt="原野">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/238316" class="thumbnail" target="_blank">
                        <div class="title">
                            这个女孩叫阿日
                            </div>
                        <div class="author">
                            loveAnchor

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1711/25/7ee205539de0340ab05424b806a54f1f.jpg?width=5185&amp;height=3472" alt="这个女孩叫阿日">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/238218" class="thumbnail" target="_blank">
                        <div class="title">
                            莉惠
                            </div>
                        <div class="author">
                            鳩月矢六

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1711/25/7559e55008a232ca84ba6e4bf0cc5378.jpg?width=5760&amp;height=3840" alt="莉惠">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/237625" class="thumbnail" target="_blank">
                        <div class="title">
                            My Crimson Dream
                            </div>
                        <div class="author">
                            居漫漫

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1711/21/c122968d566e386da9c9290302ba965e.jpg?width=1808&amp;height=1809" alt="My Crimson Dream">
                    </a>
                </div>

                            <div class="grid-item work-thumbnail">
                    <a href="http://www.cnu.cc/works/237413" class="thumbnail" target="_blank">
                        <div class="title">
                            醒着造梦
                            </div>
                        <div class="author">
                            微醺十月

                        </div>
                                                                        <img src="http://img.cnu.cc/uploads/images/flow/1711/20/4ee5ca748ab531d79a27bad23eb0275b.jpg?width=2251&amp;height=1500" alt="醒着造梦">
                    </a>
                </div>

                    
        </div>

            </form>

        <div class="pager_box">
            
                <ul class="pagination">
			<li class="disabled"><span>&laquo;</span></li><li class="active"><span>1</span></li><li><a href="http://www.cnu.cc/discoveryPage/hot-%E4%BA%BA%E5%83%8F?page=2">2</a></li><li><a href="http://www.cnu.cc/discoveryPage/hot-%E4%BA%BA%E5%83%8F?page=2" rel="next">&raquo;</a></li>	</ul>

                    </div>


    </div>
    <!--
        <div class="view-mask"></div>
        <div class="view">
            <div class="view-header">
                <span class="title">图片标题1</span>

                <div class="right">
                    <span class="icon-a share"></span>
                    <span class="vote"><span class="icon-a"></span><span>投一票</span></span>
                    <span class="icon-a tip-l"></span>
                    <span class="icon-a tip-r"></span>
                    <div class="float-l">
                        <span class="icon-b close"></span>
                        <span class="icon-b big"></span>
                    </div>
                </div>
            </div>
            <div class="view-box">

                <div class="multi" ></div>

            </div>

            <div  class="view-list">
                <ul></ul>
            </div>
        </div>-->
    
  
    <div class="pageFooter">
        <span>@ CNU视觉联盟（www.cnu.cc）</span><span><a target="_blank" href="http://www.miitbeian.gov.cn/" style="color:#666666">粤ICP备10023979号-3</a></span>

  </div>
  </body>

</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')

# 美化内容
print(soup.prettify())

# 获取title
print(soup.title)

# 获得title的内容
print(soup.title.string)

# 找到第一个img标签
print(soup.img)

# 找到所有img标签
print(soup.find_all('img'))

# 找到a标签
print(soup.a)

# 找到所有<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))

# 找到文档中所有的文本内容
print(soup.get_text())

# 找到id为link3的标签
print(soup.find(id='link3'))