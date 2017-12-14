-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 2017-12-14 08:03:45
-- 服务器版本： 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `news`
--

-- --------------------------------------------------------

--
-- 表的结构 `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `public_id` varchar(50) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `release_time` datetime DEFAULT NULL,
  `update_by` varchar(50) NOT NULL,
  `summary` varchar(150) NOT NULL,
  `body` text NOT NULL,
  `views` int(11) DEFAULT '0',
  `is_hot` tinyint(1) DEFAULT NULL,
  `is_del` tinyint(1) DEFAULT NULL,
  `news_type` varchar(20) DEFAULT NULL,
  `news_keys` varchar(80) DEFAULT NULL,
  `thumb` varchar(80) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `news`
--

INSERT INTO `news` (`id`, `title`, `public_id`, `create_time`, `update_time`, `release_time`, `update_by`, `summary`, `body`, `views`, `is_hot`, `is_del`, `news_type`, `news_keys`, `thumb`) VALUES
(2, '泸州—停天下寻觅已久的历史文化名城', '709326dc-97ab-4ccc-9ef3-ba05da935757', '2017-11-29 03:30:53', '2017-11-29 03:30:53', NULL, '2487f1ce-a903-4d97-bfa8-3d6b00e2d8d7', '', '<p class=\'pre\'>11月28日，位于泸州市龙马潭区南光路1号的科维商城，作为停天下首个泸州项目已全部安装完成。</p>\r\n<img style=\'width:100%\' src=\'../../assets/images/news/8/26656ec484e6.gif\'>\r\n<p class=\'pre\'>泸州作为中国历史文化名城，历史悠久，旅游资源丰富，加之气候温和，四季分明，吸引了无数本地及外地游客的踏足，人、车流量较大，一直是停天下一个重点关注的目标。</p>\r\n<img style=\'width:100%\' src=\'../../assets/images/news/8/75a6e232f3aa.jpg\'>\r\n<img style=\'width:100%\' src=\'../../assets/images/news/8/546615fd2370.jpg\'>\r\n<img style=\'width:100%\' src=\'../../assets/images/news/8/67c8655d5f3d.jpg\'>\r\n<p>科维商城施工现场图</p><p class=\'pre\'>项目确定后，技术团队迅速完成项目六进四出的设备安装和调试。干劲十足！完成了停天下响应“智慧交通，畅通城市”号召的一个实质性飞跃。截止目前，泸州多个项目也正在洽谈中。</p>\r\n<p class=\'pre\'>现在：泸州不只有老窖，还有停天下！</p>', 5, 0, 1, '公司新闻', 'demo', '/images/201711/201700001.png'),
(3, '无人收费停车场，做好用户体验才是王道', 'f0585c63-adcb-42ce-90d1-53c6de1a54b3', '2017-11-29 07:51:36', '2017-11-30 01:48:10', NULL, '2487f1ce-a903-4d97-bfa8-3d6b00e2d8d7', '', '<p class="pre">以前，说到无人化、智能化，总联想到军用的无人机、智能机器人、未来战士。总感觉离普通人很远。如今，无人收费停车场、无人机送外卖、无人机送快递、无人驾驶、无人超市、无人餐厅已经走入了我们的生活。2017年，可谓是无人化最火爆的一年。</p><p class="pre">值得一提的是自去年停天下率先开启了无人收费停车场这一模式后，给其他还在苦苦寻找发展模式的智能停车企业指明了发展方向。相继有企业进入这一领域。</p><p class="pre">同时，停天下CEO陈跃强表示：“无人收费停车场这一领域不同于其他行业，我们的客户包括B端（停车场管理方）和C端（车主）。得让两方面都满意才行。但目前进入智能停车领域企业的产品及服务质量是良莠不齐。他们还不能快速的打开市场。为了智能停车行业的健康、快速发展，我们只有不断的做好用户体验才是王道，彻底取得用户的信任与支持才是行业发展的基石。”。</p><h4 class="text-center ck_font_weight">一切为了客户满意！”</h4><p class="pre">据了解，停天下之所以能在无人收费停车场这一领域领先其他企业，因为他们始终坚持贯彻“一切为了客户满意”这一目标。包括对员工的考核，也是以此为标准。</p><p class="pre">为了达到这一目标，停天下始终坚持：</p><p class="pre"></p><h5 class="ck_font_weight">一、对硬件产品的不断更新迭代。</h5>技术、工艺永远在不断的向前发展。今年领先的产品也许明年就已经跟不上用户的需求了。所以停天下智能产品中心的研发团队，不断的在对产品进行改进、升级。目前，停天下的智能产品从1.0产品、2.0产品到现在推出的3.0产品。以及正在研发的智能停车4.0解决方案。不久后也将会与客户见面。<p></p><img src="../../assets/images/news/4/image002.jpg"><p class="pre"></p><h5 class="ck_font_weight">二、AI系统的不断完善。</h5>在停车场的管理中。每个停车场的实际情况都不一样，客户的需求也是不同的。但要做到无人化，智能化的管理。必须要去迎合这些需求。否则无人收费停车场是不可能被市场接受的。<p></p><img src="../../assets/images/news/4/image004.jpg"><p class="pre"></p><h5 class="ck_font_weight">三、场内指示、告示系统的准确、直观。</h5>由于无人收费停车场目前还属于新鲜事物，很多车主还停留在传统的人工收费的模式中。<br>所以在停车场出入口、场内设置完善各种指示、提示信息就非常有必要。停天下对此制定了非常详细的视觉标准。<p></p><img src="../../assets/images/news/4/image006.jpg"><p class="pre"></p><h5 class="ck_font_weight">四、后台客服系统的服务水平</h5>车主在使用过程中肯定会遇到一些特殊的情况，导致不能正常出场。尤其是在一些单出口的停车场，就可能造成整个停车场的拥堵。这时候就需要后台客服人员的快速处理了。这时候停天下后台云收费中心的优势就凸显出来了。<br>后台客服系统采用7*24小时模式人工值守。为停车场的的稳定运行提供安全保障。同时具有强大的应急处理能力：远程核对车辆信息、远程开闸放行、视频语音实时对讲、自动故障诊断、远程升级系统、及时修复漏洞、自动派单维修等。快速处理各种特殊情况。确保停车场的稳定运行。<p></p><img src="../../assets/images/news/4/image008.jpg"><p class="pre"></p><h5 class="ck_font_weight">五、应急响应团队的及时处理</h5>在停车场的运行中，难免会出现各种特殊情况，断电、断网、机械故障等。停天下的应急响应团队做了充分的灾备预案：双重网络/电源备份、三重数据备份、四重灾备预案。从系统自动报警，通知地面维护人员。到工作人员到达现场处理必须控制在合理的时间内。否则将会对客户满意度造成恶劣影响。<p></p><img src="../../assets/images/news/4/image010.jpg"><p class="pre">正是因为停天下始终坚持“一切为了客户满意”的服务宗旨，努力把用户体验做到极致。才能领先于行业、赢得越来越多的客户的信任。</p>', 4, 0, 0, '公司新闻', '泸州,古城,历史', '/images/201711/201700001.png'),
(4, '停天下已支持新能源车牌识别', 'e9028f68-adf3-4b5f-85d7-382474c6beee', '2017-11-29 07:52:00', '2017-11-29 07:52:00', NULL, '2487f1ce-a903-4d97-bfa8-3d6b00e2d8d7', '', '停天下已支持新能源车牌识别', 0, 0, 0, '公司新闻', 'demo', '/images/201711/201700001.png'),
(5, '又搞大事了，首家微信停车场上线！', 'abaf8e5c-29f9-441b-b50a-8e711eb6f0a0', '2017-11-29 07:52:12', '2017-11-29 07:52:12', NULL, '2487f1ce-a903-4d97-bfa8-3d6b00e2d8d7', '', '又搞大事了，首家微信停车场上线！', 0, 0, 0, '公司新闻', 'demo', '/images/201711/201700001.png'),
(6, '无人收费停车场，做好用户体验才是王道', '76d99177f29340ee95e76cda0e7ed8b3', '2017-11-30 03:08:08', '2017-11-30 03:08:08', NULL, '2487f1ce-a903-4d97-bfa8-3d6b00e2d8d7', '', '<p class=\'pre\'>以前，说到无人化、智能化，总联想到军用的无人机、智能机器人、未来战士。总感觉离普通人很远。如今，无人收费停车场、无人机送外卖、无人机送快递、无人驾驶、无人超市、无人餐厅已经走入了我们的生活。2017年，可谓是无人化最火爆的一年。</p>', 0, 0, 0, '公司新闻', '泸州,古城,历史', '/images/201711/201700001.png'),
(14, '这是一条测试新闻', '2413a6b2cba74882abd5738a8254538f', '2017-12-07 16:38:29', '2017-12-07 16:38:29', '2017-12-07 16:38:29', '8205db503b6045ec8956c9b718662931', '测试', '公司新闻', 0, 0, 0, '公司新闻', '测试', '../2017.jpg'),
(13, '这是一条测试新闻', '1275128a64d94b26962d436be05271a5', '2017-12-07 16:36:55', '2017-12-07 16:36:55', '2017-12-07 16:36:55', '8205db503b6045ec8956c9b718662931', '测试', '公司新闻', 0, 0, 0, '公司新闻', '测试', '../2017.jpg'),
(15, '这是一条测试新闻', 'ba3fc8979ba44dceac30413204b4ee65', '2017-12-07 16:40:01', '2017-12-07 16:40:01', '2017-12-07 16:40:01', '8205db503b6045ec8956c9b718662931', '测试', '公司新闻', 0, 0, 0, '公司新闻', '测试', '../2017.jpg'),
(16, '这是一条测试新闻', 'eb39246deff545daa922e81f7818e4fb', '2017-12-07 16:40:41', '2017-12-07 16:40:41', '2017-12-07 16:40:41', '8205db503b6045ec8956c9b718662931', '测试', '<p class="pre">这是一条测试新闻</p>', 1, 0, 0, '公司新闻', '测试', '../2017.jpg'),
(17, 'this is a test title', 'd46c244ffa01415581bdc81caf90e60f', '2017-12-07 17:37:19', '2017-12-07 17:37:19', '2017-12-07 17:37:19', '8205db503b6045ec8956c9b718662931', 'test', 'this is a test content', 0, 0, 0, '公司新闻', 'test', '../20171207.jpg'),
(18, '厉害！山东连续上线3个云收费停车场', '3e374edb89194601a93932391257a5d4', '2017-12-08 10:31:31', '2017-12-08 10:31:31', '2017-12-08 10:31:31', '8205db503b6045ec8956c9b718662931', '山东,云收费,停车场', '厉害！山东连续上线3个云收费停车场', 0, 0, 0, '公司新闻', '山东,云收费,停车场', 'http://127.0.0.1:5000/static/image/201712/5544c40868b5480cac8d15993310cc7b.gif'),
(19, '停天下已支持新能源车牌识别', '339d18bc767842d1996bf9a89acd81af', '2017-12-08 10:32:20', '2017-12-08 10:32:20', '2017-12-08 10:32:06', '8205db503b6045ec8956c9b718662931', '停天下已支持新能源车牌识别', '停天下已支持新能源车牌识别', 0, 0, 0, '公司新闻', '停天下,新能源车牌', 'http://127.0.0.1:5000/static/image/201712/e4b7af6caf254b84a54e4e851d29dfa6.gif'),
(20, '又搞大事了，首家微信停车场上线！', 'dbb2180b38be4e4b9ca0060cec141522', '2017-12-08 16:21:00', '2017-12-08 16:21:00', '2017-12-08 16:20:25', '8205db503b6045ec8956c9b718662931', '近日，有细心的成都车主发现在武侯区富顿中心 B座地面停车场上出现了一个全新的无人收费停车场', '近日，有细心的成都车主发现在武侯区富顿中心 B座地面停车场上出现了一个全新的无人收费停车场。没错，小编很嗨森的告诉大家，这是中国无人收费停车场的引领者——停天下专为微型停车场量身设计开发的“微信停车场”。上线后受收到物业及车主的一致好评。', 0, 0, 0, '公司新闻', '微信停车场', 'http://127.0.0.1:5000/static/image/201712/3995c8b9dfff45238389a82c7968ee0a.gif'),
(21, 'test add news api', '4a8ecb3612744c259be846bfb6ee56b8', '2017-12-14 11:46:13', '2017-12-14 11:46:13', '2017-12-14 16:20:25', 'e36e4cbcb0a94c7e831baa4497e805e7', 'test add news api', 'test add news api', 0, 0, 0, '行业新闻', 'test,api', '201712/2017.jpg'),
(22, 'test add news api', '08e1606126014b2b8e987080fe82dcb1', '2017-12-14 11:46:48', '2017-12-14 07:34:02', '2017-12-14 16:20:25', '42ca449dd1a84e02a69320fddecebb5d', 'test add news api', 'test add news api', 4, 0, 0, '公司新闻', 'test,api', '201712/2017.jpg');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `public_id` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `password` varchar(80) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT NULL,
  `weixin` varchar(50) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`id`, `public_id`, `name`, `password`, `admin`, `weixin`, `create_time`, `update_time`) VALUES
(7, '42ca449dd1a84e02a69320fddecebb5d', 'iamk', 'sha256$0ySD2ks5$ff96d9ca17dc93ed8bcc383a834cd2c05e6ba7419d00d02aa5df7832d5e97141', 1, 'oCJfqvgk_O60fQ9GIWSp-rrVTiDA', '2017-12-14 11:31:32', '2017-12-14 11:31:32'),
(4, '8205db503b6045ec8956c9b718662931', 'wujun', 'sha256$1kG8G4ni$7bca4341139db6e681602326bc94c1277e384fffa537c70158ae96e82feff725', 0, '2313', '2017-12-07 16:34:05', '2017-12-07 16:34:05'),
(5, 'e36e4cbcb0a94c7e831baa4497e805e7', 'test', 'sha256$Czy8J8Vl$c6005b18e8451674923cd5a02c20ace5871335626910e02ef905008723ecb860', 1, 'test', '2017-12-14 11:13:18', '2017-12-14 11:13:18');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `public_id` (`public_id`),
  ADD KEY `发布时间` (`release_time`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `weixin` (`weixin`) USING BTREE,
  ADD UNIQUE KEY `public_id` (`public_id`),
  ADD UNIQUE KEY `name` (`name`) USING BTREE;

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
--
-- 使用表AUTO_INCREMENT `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
